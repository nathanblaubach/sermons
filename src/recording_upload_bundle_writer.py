import shutil
from pathlib import Path

from instructions_generator import InstructionsGenerator
from recording_metadata import RecordingMetadata
from recording_upload_bundle import RecordingUploadBundle
from video_generator import VideoGenerator


class RecordingUploadBundleWriter:
    def __init__(
        self,
        video_generator: VideoGenerator,
        instructions_generator: InstructionsGenerator,
    ):
        self.video_generator = video_generator
        self.instructions_generator = instructions_generator

    def write(self, metadata: RecordingMetadata):
        destination_directory = metadata.audio_file_path.parent

        upload_bundle = RecordingUploadBundle(
            instructions=Path(
                str(metadata.audio_file_path).removesuffix(".mp3") + ".txt"
            ),
            soundcloud_audio=metadata.audio_file_path,
            soundcloud_artwork=destination_directory / "soundcloud-artwork.jpg",
            soundcloud_track_title=f"{metadata.title} // {metadata.date}",
            soundcloud_description=f"{metadata.title} // {metadata.speaker_name}\nFind out more about River City Church at rivercitydbq.org",
            soundcloud_release_date=metadata.date,
            youtube_video=Path(
                str(metadata.audio_file_path).removesuffix(".mp3") + ".mp4"
            ),
            youtube_thumbnail=destination_directory / "youtube-thumbnail.jpg",
            youtube_title=metadata.title,
            youtube_description=f"{metadata.speaker_name} // {metadata.date}\nFind out more about River City Church at rivercitydbq.org",
            youtube_recording_date=metadata.date,
        )

        shutil.copy(
            Path(__file__).parent / "soundcloud-artwork.jpg",
            upload_bundle.soundcloud_artwork,
        )
        shutil.copy(
            Path(__file__).parent / "youtube-thumbnail.jpg",
            upload_bundle.youtube_thumbnail,
        )

        self.video_generator.generate(upload_bundle)

        self.instructions_generator.generate(upload_bundle)

        return destination_directory
