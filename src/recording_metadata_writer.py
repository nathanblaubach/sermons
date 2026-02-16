from pathlib import Path
from recording_metadata import RecordingMetadata

TEMPLATE_PATH = Path(__file__).parent / "recording_metadata.template"

class RecordingMetadataWriter:

    def write(self, metadata: RecordingMetadata):
        file_path = Path(metadata.audio_file_path).parent / f"{Path(metadata.audio_file_path).stem}.txt"
        template = TEMPLATE_PATH.read_text()
        file_contents = template.format(
            title=metadata.title,
            date=metadata.date,
            speaker_name=metadata.speaker_name,
        )
        file_path.write_text(file_contents)
