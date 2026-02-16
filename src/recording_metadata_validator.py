from os.path import isfile

from recording_metadata import RecordingMetadata


class RecordingMetadataValidator:
    def is_valid(self, metadata: RecordingMetadata):
        if metadata.audio_file_path == '' or not isfile(metadata.audio_file_path):
            return False
        if metadata.title == '':
            return False
        if metadata.date == '':
            return False
        if metadata.speaker_name == '':
            return False
        return True
