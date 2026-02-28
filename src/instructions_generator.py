from pathlib import Path

from recording_metadata import RecordingMetadata

FILE_TEMPLATE = """Upload Instructions

Soundcloud: https://soundcloud.com/upload

Upload the recording

Select "Upload" > "Choose File"
Choose files: soundcloud-audio.mp3
Add new artwork: soundcloud-artwork.jpg
Track title: {soundcloud_track_title}
Genre: Religion & Spirituality
Description:
{soundcloud_description}
Advanced Details > Release date: {soundcloud_release_date}
Permissions > Engagement privacy: Uncheck all
Select "Upload"

Add to playlists

Select "View track"
Select "More" ... icon
Select "Add to Playlist"
Select "Add to Playlist" next to the current sermon series
- Skip this if the recording is not a part of a sermon series
- Create the sermon series playlist if it doesn't exist (Instructions below)
Select "Add to Playlist" next to "River City Church Sermons"
Select the "River City Church Sermons" playlist
Select the "Edit" pencil icon
Select the "Tracks" tab
Drag the new sermon to the top of the playlist
Select "Save changes"

How to create a sermon series playlist if needed

Go to the "Create a playlist" tab
Playlist title: Sermon series name
Select "Save"
Go back to the "Add to Playlist" and continue above

YouTube: https://studio.youtube.com/channel/UCKmv_adKiFPQCbwQW2qaONw

Select "Create" > "Upload Videos"
Select files: youtube-video.mp4
Title: {youtube_title}
Description:
{youtube_description}
Thumbnail: youtube-thumbnail.jpg
Playlists:
- Sermons
- Current Sermon Series (If Applicable)
Show more > Recording date and location > Recording date: {youtube_recording_date}
Select "Next" 3 times
Select "Publish"

How to create a sermon series playlist if needed

Click "Create" > "New Playlist"
Title: Sermon series name
Description: Leave Blank
Visibility: Public
Default video order: Date published (newest)
Select "Create"
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
