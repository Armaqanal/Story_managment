import os.path

from validators import validate_date
from author import Author  # alt+shift+entr
from uploader_context_manager import UploaderContextManager


class Story:
    all_stories = []

    def __init__(self, title, author: Author, file_name, upload_date):
        self.title = title
        self.author = author
        self.file_name = file_name
        self.file_path = os.path.join(UploaderContextManager.directory_path, file_name)
        self.upload_date = validate_date(upload_date)
        self.story_checked = False
        Story.all_stories.append(self)

    def check_story(self):
        pass

    @staticmethod
    def display_checked_stories():
        return [story for story in Story.all_stories if story.story_checked]
