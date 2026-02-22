from datetime import date, timedelta

from pathlib import Path
import tkinter as tk
from tkinter import ttk, filedialog

from recording_metadata import RecordingMetadata
from recording_metadata_validator import RecordingMetadataValidator

class RecordingMetadataForm:
    def __init__(self):
        self.validator = RecordingMetadataValidator()

    def get_metadata(self) -> RecordingMetadata | None:
        # Set up frame
        self.root = tk.Tk()
        self.root.title("Sermon Upload Assistant")
        self.root.geometry("500x325")
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky="nsew")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)

        # Audio File Path
        ttk.Label(main_frame, text="Audio File:").grid(row=0, column=0, sticky="w", pady=5)
        self.get_recording_audio_file_path_var = tk.StringVar()
        self.file_path_entry = ttk.Entry(main_frame, textvariable=self.get_recording_audio_file_path_var)
        self.file_path_entry.grid(row=0, column=1, sticky="ew", pady=5, padx=(5, 5))
        self.browse_button = ttk.Button(main_frame, text="Browse", command=self.__browse_file)
        self.browse_button.grid(row=0, column=2, pady=5)

        # Passage / Title
        ttk.Label(main_frame, text="Passage / Title:").grid(row=1, column=0, sticky="w", pady=5)
        self.get_recording_title_var = tk.StringVar()
        self.title_entry = ttk.Entry(main_frame, textvariable=self.get_recording_title_var)
        self.title_entry.grid(row=1, column=1, columnspan=2, sticky="ew", pady=5, padx=(5, 0))

        # Recording Date (Default to most recent sunday)
        today = date.today()
        most_recent_sunday = (today - timedelta(days=(today.weekday() + 1) % 7))

        ttk.Label(main_frame, text="Recording Date:").grid(row=2, column=0, sticky="w", pady=5)
        self.get_recording_date_var = tk.StringVar(value=most_recent_sunday.strftime("%Y.%m.%d"))
        self.date_entry = ttk.Entry(main_frame, textvariable=self.get_recording_date_var)
        self.date_entry.grid(row=2, column=1, columnspan=2, sticky="ew", pady=5, padx=(5, 0))

        # Speaker (Default to Aaron)
        ttk.Label(main_frame, text="Speaker:").grid(row=3, column=0, sticky="w", pady=5)
        self.get_recording_speaker_var = tk.StringVar(value="Aaron Morrow")
        self.speaker_entry = ttk.Entry(main_frame, textvariable=self.get_recording_speaker_var)
        self.speaker_entry.grid(row=3, column=1, columnspan=2, sticky="ew", pady=5, padx=(5, 0))

        # Submit Button
        self.submit_button = ttk.Button(main_frame, text="Submit", command=self.__on_submit)
        self.submit_button.grid(row=4, column=0, columnspan=3, pady=20)

        # Validation Messages
        self.validation_label = tk.Label(main_frame, text="", fg="red", anchor="w", justify="left")
        self.validation_label.grid(row=5, column=0, columnspan=3, sticky="w")

        # Initialize Form
        self.data = None
        self.root.mainloop()
        return self.data

    def __browse_file(self):
        file_path = filedialog.askopenfilename(
            title="Select a file",
            filetypes=[("mp3 Files", "*.mp3")]
        )
        if file_path:
            self.get_recording_audio_file_path_var.set(file_path)

    def __on_submit(self):
        recording_metadata = RecordingMetadata(
            audio_file_path=Path(self.get_recording_audio_file_path_var.get()),
            title=self.get_recording_title_var.get(),
            date=self.get_recording_date_var.get(),
            speaker_name=self.get_recording_speaker_var.get(),
        )
        errors = self.validator.get_errors(recording_metadata)
        if len(errors) == 0:
            self.data = recording_metadata
            self.root.destroy()
        else:
            self.validation_label.config(text="\n".join(errors))

class FakeRecordingMetadataForm:
    def get_metadata(self) -> RecordingMetadata | None:
        return RecordingMetadata(
            audio_file_path=Path('/home/nathanblaubach/Development/sermons/data/A - WARM - CHURCHFRONT PADS.mp3'),
            title='Mark 8:16',
            date='2026.02.21',
            speaker_name='Aaron Morrow',
        )
