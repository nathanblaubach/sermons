from pathlib import Path
from recording_metadata import RecordingMetadata

class RecordingMetadataWriter:

    def save_metadata_file(self, metadata: RecordingMetadata):
        file_path = Path(metadata.audio_file_path).parent / "sermon_metadata.txt"
        file_contents = f"""Recording Upload Information

Soundcloud

Title:
{metadata.title} // {metadata.date}
Description:
{metadata.title} // {metadata.speaker_name}
Find out more about River City Church at rivercitydbq.org

Youtube

Title:
{metadata.title}
Description:
{metadata.speaker_name} // {metadata.date}
Find out more about River City Church at rivercitydbq.org
"""
        file_path.write_text(file_contents)
