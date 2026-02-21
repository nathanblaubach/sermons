from pathlib import Path
import shutil
import subprocess
import sys

class RecordingMediaWriter:
    def write(self, audio_file_path: str):
        if shutil.which("ffmpeg") is None and sys.platform == "win32":
            subprocess.run([
                "winget", "install",
                "-e", "--id", "Gyan.FFmpeg",
                "--accept-package-agreements",
                "--accept-source-agreements",
            ], check=True)

        executable_directory = Path(__file__).parent
        destination_directory = Path(audio_file_path).parent

        subprocess.run([
            "ffmpeg",
            "-i", executable_directory / "logo-youtube.jpg",
            "-i", audio_file_path,
            "-c:v", "libx264",
            "-tune", "stillimage",
            "-c:a", "copy",
            destination_directory / f"{Path(audio_file_path).stem}.mp4"
        ])

        shutil.copy(
            executable_directory / "logo-youtube.jpg",
            destination_directory / "youtube-thumbnail.jpg"
        )

        shutil.copy(
            executable_directory / "logo-soundcloud.jpg",
            destination_directory / "soundcloud-artwork.jpg"
        )
