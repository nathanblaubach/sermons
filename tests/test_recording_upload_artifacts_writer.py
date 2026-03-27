from pathlib import Path
from unittest.mock import ANY, MagicMock, patch

import pytest

from recording_metadata import RecordingMetadata
from recording_upload_bundle import RecordingUploadBundle
from recording_upload_bundle_writer import RecordingUploadBundleWriter


class TestWrite:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.video_generator = MagicMock()
        self.instructions_generator = MagicMock()
        self.writer = RecordingUploadBundleWriter(
            self.video_generator, self.instructions_generator
        )

    @patch("recording_upload_bundle_writer.shutil.copy")
    def test_writes_upload_bundle_for_the_given_metadata(self, mock_copy: MagicMock):

        root_directory = Path(__file__).parent

        given_metadata = RecordingMetadata(
            audio_file_path=root_directory / "fake-test-recording.mp3",
            title="Sunday Sermon",
            date="2026.02.16",
            speaker_name="John Smith",
        )

        expected_upload_bundle = RecordingUploadBundle(
            instructions=root_directory / "fake-test-recording.txt",
            soundcloud_audio=root_directory / "fake-test-recording.mp3",
            soundcloud_artwork=root_directory / "soundcloud-artwork.jpg",
            soundcloud_track_title="Sunday Sermon // 2026.02.16",
            soundcloud_description="Sunday Sermon // John Smith\nFind out more about River City Church at rivercitydbq.org",
            soundcloud_release_date="2026.02.16",
            youtube_video=root_directory / "fake-test-recording.mp4",
            youtube_thumbnail=root_directory / "youtube-thumbnail.jpg",
            youtube_title="Sunday Sermon",
            youtube_description="John Smith // 2026.02.16\nFind out more about River City Church at rivercitydbq.org",
            youtube_recording_date="2026.02.16",
        )

        result = self.writer.write(given_metadata)

        assert root_directory.is_dir()

        mock_copy.assert_any_call(ANY, expected_upload_bundle.soundcloud_artwork)
        mock_copy.assert_any_call(ANY, expected_upload_bundle.youtube_thumbnail)

        self.video_generator.generate.assert_called_once_with(expected_upload_bundle)

        self.instructions_generator.generate.assert_called_once_with(
            expected_upload_bundle
        )

        assert result == root_directory
