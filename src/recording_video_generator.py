from pathlib import Path
import subprocess
import sys

class RecordingVideoGenerator:
    def generate(self, audio_file_path: str):
        if sys.platform == "win32":
            subprocess.run([
                "winget",
                "install",
                "ffmpeg"
            ])

        root_directory = Path(audio_file_path).parent
        subprocess.run([
            "ffmpeg",
            "-i", root_directory / "logo-youtube.jpg",
            "-i", audio_file_path,
            "-c:v", "libx264",
            "-tune", "stillimage",
            "-c:a", "copy",
            root_directory / f"{Path(audio_file_path).stem}.mp4"
        ])
