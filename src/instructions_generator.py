from pathlib import Path

from recording_metadata import RecordingMetadata

FILE_TEMPLATE = """Upload Instructions

Soundcloud: https://soundcloud.com/upload

Choose files: soundcloud-audio.mp3
Add new artwork: soundcloud-artwork.jpg
Track title: {soundcloud_track_title}
Genre: Religion & Spirituality
Description:
{soundcloud_description}
Advanced Details > Release date: {soundcloud_release_date}
Permissions > Engagement privacy: Uncheck all

Add to Playlists

- River City Church Sermons
- Current Sermon Series (If Applicable)

YouTube: https://studio.youtube.com/channel/UCKmv_adKiFPQCbwQW2qaONw

Select files: youtube-video.mp4
Title: {youtube_title}
Description:
{youtube_description}
Thumbnail: youtube-thumbnail.jpg
Playlists:
- Sermons
- Current Sermon Series (If Applicable)
Audience: No, it's not made for kids
Show more > Recording date and location > Recording date: {youtube_recording_date}
"""


class InstructionsGenerator:
    def generate(self, destination_directory: Path, metadata: RecordingMetadata):
        file_path = destination_directory / "upload-instructions.txt"
        file_contents = FILE_TEMPLATE.format(
            soundcloud_track_title=f"{metadata.title} // {metadata.date}",
            soundcloud_description=f"{metadata.title} // {metadata.speaker_name}\nFind out more about River City Church at rivercitydbq.org",
            soundcloud_release_date=metadata.date,
            youtube_title=metadata.title,
            youtube_description=f"{metadata.speaker_name} // {metadata.date}\nFind out more about River City Church at rivercitydbq.org",
            youtube_recording_date=metadata.date,
        )
        file_path.write_text(file_contents)
