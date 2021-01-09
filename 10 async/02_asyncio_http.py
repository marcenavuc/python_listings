import asyncio


class Photo:
    def __init__(self, url):
        self.url = url

    @classmethod
    def from_json(cls, obj):
        return Photo(obj['url'])


def print_photo_titles(photos):
    for photo in photos:
        print(f"photo.url")


async def photos_by_aldum(task_name, album, session):
    print(task_name)
