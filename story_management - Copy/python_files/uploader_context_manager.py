import os
import pathlib


class UploaderContextManager:
    directory_path = "../story_files/temp_stories"

    def __init__(self, file_path: str):
        self.src_file_path = pathlib.Path(file_path)
        self.dst_file_path = pathlib.Path(os.path.join(UploaderContextManager.directory_path, self.src_file_path.name))
        self.src_file_obj = None
        self.dst_file_obj = None

    def __enter__(self):
        self.src_file_obj = self.src_file_path.open('r', encoding="utf-8")
        self.dst_file_path.parent.mkdir(parents=True, exist_ok=True)
        self.dst_file_obj = self.dst_file_path.open('a', encoding="utf-8")
        for line in self.src_file_obj:
            self.dst_file_obj.write(line)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.src_file_obj.close()
        self.dst_file_obj.close()
