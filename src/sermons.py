from recording_metadata_form import RecordingMetadataForm
from recording_media_writer import RecordingMediaWriter
from recording_metadata_writer import RecordingMetadataWriter

def main():
    metadata_form = RecordingMetadataForm()
    metadata_writer = RecordingMetadataWriter()
    media_writer = RecordingMediaWriter()

    metadata = metadata_form.get_recording_metadata()
    metadata_writer.write(metadata)
    media_writer.write(metadata.audio_file_path)

if __name__ == "__main__":
    main()
