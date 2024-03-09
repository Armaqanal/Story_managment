from python_files.author import Author
from python_files.story import Story


def main():
    sara = Author("sara", "sara@gmail.com")
    javad = Author("javad", "javad@gmail.com")
    result = Author.add_story(file_path="../story_files/sample_stories/story1.txt")
    print(result)
    story1 = Story("story1", sara, "story1.txt", '3-8-2024')
    story2 = Story("story2", javad, "story2.txt", '13-10-2024')

    print(Story.display_checked_stories())
    story1.check_story()






if __name__ == '__main__':
    main()