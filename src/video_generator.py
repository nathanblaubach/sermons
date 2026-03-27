import shutil
import subprocess
import sys

from recording_upload_bundle import RecordingUploadBundle


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

    def generate(self, upload_bundle: RecordingUploadBundle):
        subprocess.run(
            [
                "ffmpeg",
                "-i",
                upload_bundle.youtube_thumbnail,
                "-i",
                upload_bundle.soundcloud_audio,
                "-c:v",
                "libx264",
                "-tune",
                "stillimage",
                "-c:a",
                "copy",
                upload_bundle.youtube_video,
            ]
        )
