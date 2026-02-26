import os
from pathlib import Path
import shutil

from instructions_generator import InstructionsGenerator
from recording_metadata import RecordingMetadata
from video_generator import VideoGenerator


class RecordingUploadArtifactsWriter:
    def __init__(
        self,
        video_generator: VideoGenerator,
        instructions_generator: InstructionsGenerator,
    ):
        self.video_generator = video_generator
        self.instructions_generator = instructions_generator

    def write(self, metadata: RecordingMetadata):
        soundcloud_artwork_path = Path(__file__).parent / "soundcloud-artwork.jpg"
        youtube_thumbnail_path = Path(__file__).parent / "youtube-thumbnail.jpg"

        destination_directory = Path(str(metadata.audio_file_path).removesuffix(".mp3"))
        if not os.path.isdir(destination_directory):
            os.makedirs(destination_directory)

        shutil.copy(
            soundcloud_artwork_path, destination_directory / "soundcloud-artwork.jpg"
        )
        shutil.copy(
            metadata.audio_file_path, destination_directory / "soundcloud-audio.mp3"
        )
        shutil.copy(
            youtube_thumbnail_path, destination_directory / "youtube-thumbnail.jpg"
        )

        self.video_generator.generate(
            destination_directory, soundcloud_artwork_path, metadata.audio_file_path
        )

        self.instructions_generator.generate(destination_directory, metadata)

        return destination_directory
