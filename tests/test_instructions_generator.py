from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from instructions_generator import InstructionsGenerator
from recording_upload_bundle import RecordingUploadBundle


class TestGenerate:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.generator = InstructionsGenerator()

    @patch("pathlib.Path.write_text")
    @patch("instructions_generator.FILE_TEMPLATE")
    def test_generates_upload_instructions(
        self, mock_template: MagicMock, mock_write: MagicMock
    ):
        bundle = RecordingUploadBundle(
            instructions=Path("instructions.txt"),
            soundcloud_audio=Path("sermon.mp3"),
            soundcloud_artwork=Path("artwork.png"),
            soundcloud_track_title="Sunday Sermon // 2026.02.16",
            soundcloud_description="Sunday Sermon // John Smith\nFind out more about River City Church at rivercitydbq.org",
            soundcloud_release_date="2026.02.16",
            youtube_video=Path("sermon.mp4"),
            youtube_thumbnail=Path("thumbnail.png"),
            youtube_title="Sunday Sermon",
            youtube_description="John Smith // 2026.02.16\nFind out more about River City Church at rivercitydbq.org",
            youtube_recording_date="2026.02.16",
        )

        mock_template.format.return_value = "fake generated file contents"

        self.generator.generate(bundle)

        mock_template.format.assert_called_once_with(
            soundcloud_audio=Path("sermon.mp3"),
            soundcloud_artwork=Path("artwork.png"),
            soundcloud_track_title="Sunday Sermon // 2026.02.16",
            soundcloud_description="Sunday Sermon // John Smith\nFind out more about River City Church at rivercitydbq.org",
            soundcloud_release_date="2026.02.16",
            youtube_video=Path("sermon.mp4"),
            youtube_thumbnail=Path("thumbnail.png"),
            youtube_title="Sunday Sermon",
            youtube_description="John Smith // 2026.02.16\nFind out more about River City Church at rivercitydbq.org",
            youtube_recording_date="2026.02.16",
        )

        mock_write.assert_called_once_with("fake generated file contents")
