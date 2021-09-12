import princess_creator
from princess_collection import Princess_collection


def read_princess_file(filepath):
    with open(filepath) as f:
        for line in f:
            data = line.replace('|', '')
            princess = creator.create_princess(data)
            if not princess is None:
                princesses.add(princess)


creator = princess_creator.Princess_creator()
princesses = Princess_collection()
read_princess_file('disney.txt')
princesses.list()
