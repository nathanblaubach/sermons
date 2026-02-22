from recording_editor import RecordingEditor
from recording_metadata_form import RecordingMetadataForm
from recording_upload_artifacts_writer import RecordingUploadArtifactsWriter


def main():
    recording = RecordingEditor(
        RecordingMetadataForm(), RecordingUploadArtifactsWriter()
    )
    recording.prepare_for_upload()


if __name__ == "__main__":
    main()
