from recording_metadata_form import RecordingMetadataForm
from recording_video_generator import RecordingVideoGenerator
from recording_metadata_writer import RecordingMetadataWriter

def main():
    metadata_form = RecordingMetadataForm()
    metadata = metadata_form.get_recording_metadata()

    metadata_writer = RecordingMetadataWriter()
    metadata_writer.save_metadata_file(metadata)

    video_generator = RecordingVideoGenerator()
    video_generator.generate(metadata.audio_file_path)

if __name__ == "__main__":
    main()
