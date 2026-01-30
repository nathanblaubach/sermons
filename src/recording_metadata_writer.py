from pathlib import Path
from recording_metadata import RecordingMetadata

class RecordingMetadataWriter:

    def write(self, metadata: RecordingMetadata):
        file_path = Path(metadata.audio_file_path).parent / f"{Path(metadata.audio_file_path).stem}.txt"
        file_contents = f"""Recording Upload Information

Soundcloud: https://soundcloud.com/upload

Add new artwork: logo-soundcloud.jpg
Track title: {metadata.title} // {metadata.date}
Genre: Religion & Spirituality
Description:
{metadata.title} // {metadata.speaker_name}
Find out more about River City Church at rivercitydbq.org
Advanced Details > Release date: {metadata.date}
Permissions > Engagement privacy: Uncheck all

Add to Playlists

- River City Church Sermons
- Current Sermon Series (If Applicable)

YouTube: https://studio.youtube.com/channel/UCKmv_adKiFPQCbwQW2qaONw

Title: {metadata.title}
Description:
{metadata.speaker_name} // {metadata.date}
Find out more about River City Church at rivercitydbq.org
Thumbnail: logo-youtube.jpg
Playlists:
- Sermons
- Current Sermon Series (If Applicable)
Audience: No, it's not made for kids
Show more > Recording date and location > Recording date: {metadata.date}
"""
        file_path.write_text(file_contents)
