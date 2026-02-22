from recording_metadata_form import RecordingMetadataForm
from recording_upload_artifacts_writer import RecordingUploadArtifactsWriter

def main():
    metadata = RecordingMetadataForm().get_metadata()
    if metadata != None:
        upload_artifacts_directory = RecordingUploadArtifactsWriter().write(metadata)
        print(f"Upload files written to {upload_artifacts_directory}")

if __name__ == "__main__":
    main()
