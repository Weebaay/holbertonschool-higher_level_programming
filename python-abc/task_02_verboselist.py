#!/usr/bin/python3
"""Module task_02_verboselist: Define Extending the Python list with Notifications"""


class VerboseList(list):
    """A list that prints a message when items are added or removed."""

    def append(self, item):
        print(f"Added {item} to the list.")
        super().append(item)

    def extend(self, items):
        print(f"Extended the list with {len(items)} items.")
        super().extend(items)

    def remove(self, item):
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]
        print(f"Popped {item} from the list.")
        return super().pop(index)
