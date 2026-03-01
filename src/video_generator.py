import shutil
import subprocess
import sys
from pathlib import Path


class VideoGenerator:
    def __init__(self):
        if shutil.which("ffmpeg") is None and sys.platform == "win32":
            subprocess.run(
                [
                    "winget",
                    "install",
                    "-e",
                    "--id",
                    "Gyan.FFmpeg",
                    "--accept-package-agreements",
                    "--accept-source-agreements",
                ],
                check=True,
            )

    def generate(self, destination_directory: Path, image_path: Path, audio_path: Path):
        subprocess.run(
            [
                "ffmpeg",
                "-i",
                image_path,
                "-i",
                audio_path,
                "-c:v",
                "libx264",
                "-tune",
                "stillimage",
                "-c:a",
                "copy",
                destination_directory / "youtube-video.mp4",
            ]
        )
