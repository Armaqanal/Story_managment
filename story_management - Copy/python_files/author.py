import validators as v
from uploader_context_manager import UploaderContextManager


class Author:
    def __init__(self, name, email):
        self.name = v.validate_name(name)
        self.email = v.validate_email(email)

    @staticmethod
    def add_story(file_path: str):
        try:
            with UploaderContextManager(file_path):
                return "The story successfully uploaded."
        except FileNotFoundError:
            return "ERROR..."


if __name__ == '__main__':
    sara = Author("sara", "sara@gmail.com")
    sara.add_story(file_path="../story_files/sample_stories/story1.txt")
