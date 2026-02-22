import os
from pathlib import Path
import shutil
import subprocess
import sys

from recording_metadata import RecordingMetadata

class RecordingUploadArtifactsWriter:
    def write(self, metadata: RecordingMetadata):
        if shutil.which("ffmpeg") is None and sys.platform == "win32":
            subprocess.run([
                "winget", "install",
                "-e", "--id", "Gyan.FFmpeg",
                "--accept-package-agreements",
                "--accept-source-agreements",
            ], check=True)

        soundcloud_artwork_path=Path(__file__).parent / "soundcloud-artwork.jpg"
        youtube_thumbnail_path=Path(__file__).parent / "youtube-thumbnail.jpg"

        destination_directory = Path(str(metadata.audio_file_path).removesuffix('.mp3'))
        if not os.path.isdir(destination_directory):
            os.makedirs(destination_directory)

        shutil.copy(soundcloud_artwork_path, destination_directory)
        shutil.copy(metadata.audio_file_path, destination_directory / "soundcloud-audio.mp3")
        shutil.copy(youtube_thumbnail_path, destination_directory)
        subprocess.run([
            "ffmpeg",
            "-i", youtube_thumbnail_path,
            "-i", metadata.audio_file_path,
            "-c:v", "libx264",
            "-tune", "stillimage",
            "-c:a", "copy",
            destination_directory / "youtube-video.mp4"
        ])

        file_path = destination_directory / "upload-instructions.txt"
        file_contents = """Upload Instructions

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
""".format(
            soundcloud_track_title=f"{metadata.title} // {metadata.date}",
            soundcloud_description=f"{metadata.title} // {metadata.speaker_name}\nFind out more about River City Church at rivercitydbq.org",
            soundcloud_release_date=metadata.date,
            youtube_title=metadata.title,
            youtube_description=f"{metadata.speaker_name} // {metadata.date}\nFind out more about River City Church at rivercitydbq.org",
            youtube_recording_date=metadata.date
        )
        file_path.write_text(file_contents)

        return destination_directory