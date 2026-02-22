from recording_metadata_form import RecordingMetadataForm
from recording_upload_artifacts_writer import RecordingUploadArtifactsWriter


class RecordingEditor:
    def __init__(
        self, form: RecordingMetadataForm, writer: RecordingUploadArtifactsWriter
    ):
        self.form = form
        self.writer = writer

    def prepare_for_upload(self):
        metadata = self.form.get_metadata()
        if metadata is not None:
            upload_artifacts_directory = self.writer.write(metadata)
            print(f"Upload artifacts written to {upload_artifacts_directory}")
