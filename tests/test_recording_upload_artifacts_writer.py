from pathlib import Path
from unittest.mock import ANY, MagicMock, patch

import pytest

from recording_metadata import RecordingMetadata
from recording_upload_artifacts_writer import RecordingUploadArtifactsWriter


class TestWrite:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.video_generator = MagicMock()
        self.instructions_generator = MagicMock()
        self.writer = RecordingUploadArtifactsWriter(
            self.video_generator, self.instructions_generator
        )

    @patch("recording_upload_artifacts_writer.shutil.copy")
    def test_writes_upload_artifacts_for_the_given_metadata(self, mock_copy: MagicMock):

        audio_file_path: Path = (
            Path(__file__).parent / "data" / "fake-test-recording.mp3"
        )
        title = "Sunday Sermon"
        date = "2026.02.16"
        speaker_name = "John Smith"
        expected_destination_directory = (
            Path(__file__).parent / "data" / "fake-test-recording"
        )

        metadata = RecordingMetadata(
            audio_file_path=audio_file_path,
            title=title,
            date=date,
            speaker_name=speaker_name,
        )

        result = self.writer.write(metadata)

        assert expected_destination_directory.is_dir()

        mock_copy.assert_any_call(
            ANY, expected_destination_directory / "soundcloud-artwork.jpg"
        )
        mock_copy.assert_any_call(
            ANY, expected_destination_directory / "soundcloud-audio.mp3"
        )
        mock_copy.assert_any_call(
            ANY, expected_destination_directory / "youtube-thumbnail.jpg"
        )

        self.video_generator.generate.assert_called_once_with(
            expected_destination_directory, ANY, metadata.audio_file_path
        )

        self.instructions_generator.generate.assert_called_once_with(
            expected_destination_directory, metadata
        )

        assert result == expected_destination_directory
