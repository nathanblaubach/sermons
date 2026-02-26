from instructions_generator import InstructionsGenerator
from recording_editor import RecordingEditor
from recording_metadata_form import RecordingMetadataForm
from recording_upload_artifacts_writer import RecordingUploadArtifactsWriter
from video_generator import VideoGenerator


def main():
    recording = RecordingEditor(
        RecordingMetadataForm(),
        RecordingUploadArtifactsWriter(VideoGenerator(), InstructionsGenerator()),
    )
    recording.prepare_for_upload()


if __name__ == "__main__":
    main()
