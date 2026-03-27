from recording_upload_bundle import RecordingUploadBundle

FILE_TEMPLATE = """Upload Instructions

Soundcloud: https://soundcloud.com/upload

Upload the recording

Select "Upload" > "Choose File"
Choose files: file://{soundcloud_audio}
Add new artwork: file://{soundcloud_artwork}
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
Select files: file://{youtube_video}
Title: {youtube_title}
Description:
{youtube_description}
Thumbnail: file://{youtube_thumbnail}
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
    def generate(self, upload_bundle: RecordingUploadBundle):
        upload_bundle.instructions.write_text(
            FILE_TEMPLATE.format(
                soundcloud_audio=upload_bundle.soundcloud_audio,
                soundcloud_artwork=upload_bundle.soundcloud_artwork,
                soundcloud_track_title=upload_bundle.soundcloud_track_title,
                soundcloud_description=upload_bundle.soundcloud_description,
                soundcloud_release_date=upload_bundle.soundcloud_release_date,
                youtube_video=upload_bundle.youtube_video,
                youtube_thumbnail=upload_bundle.youtube_thumbnail,
                youtube_title=upload_bundle.youtube_title,
                youtube_description=upload_bundle.youtube_description,
                youtube_recording_date=upload_bundle.youtube_recording_date,
            )
        )
