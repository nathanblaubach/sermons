from pathlib import Path

from instructions_generator import InstructionsGenerator
from recording_editor import RecordingEditor
from recording_metadata import RecordingMetadata
from recording_metadata_form import RecordingMetadataForm
from recording_upload_artifacts_writer import RecordingUploadArtifactsWriter
from video_generator import VideoGenerator


class FakeRecordingMetadataForm(RecordingMetadataForm):
    def get_metadata(self) -> RecordingMetadata | None:
        return RecordingMetadata(
            audio_file_path=Path(__file__).parent / "test-recording.mp3",
            title="Test Recording",
            date="2026.02.25",
            speaker_name="Nathan Blaubach",
        )


def main():
    recording = RecordingEditor(
        FakeRecordingMetadataForm(),
        RecordingUploadArtifactsWriter(VideoGenerator(), InstructionsGenerator()),
    )
    recording.prepare_for_upload()


if __name__ == "__main__":
    main()
