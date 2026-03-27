from dataclasses import dataclass
from pathlib import Path


@dataclass
class RecordingUploadBundle:
    instructions: Path
    soundcloud_audio: Path
    soundcloud_artwork: Path
    soundcloud_track_title: str
    soundcloud_description: str
    soundcloud_release_date: str
    youtube_video: Path
    youtube_thumbnail: Path
    youtube_title: str
    youtube_description: str
    youtube_recording_date: str
