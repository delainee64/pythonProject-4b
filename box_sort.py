# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 01/31/2023
# Description: Write a Box class whose init method takes three parameters
# and uses them to initialize the private length, width and height data members of a Box.
# It should also have a method named volume that returns the volume of the Box. It should
# have get methods named get_length, get_width, and get_height. Write a separate function
# named box_sort (not part of the Box class) that uses insertion sort to sort a list of
# Boxes from greatest volume to least volume.

class Box:
    """Represents the measurements of a box."""

    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height

    def volume(self):
        """Returns the volume of a box."""
        return self._length * self._width * self._height

    def get_length(self):
        """Returns the length of a box."""
        return self._length

    def get_width(self):
        """Returns the width of a box."""
        return self._width

    def get_height(self):
        """Returns the height of a box."""
        return self._height


def box_sort(box_list):
    """Sorts box_list in descending order."""
    for index in range(1, len(box_list)):
        box = box_list[index]
        pos = index - 1
        while (pos >= 0 and
               box_list[pos].volume() < box.volume()):
            box_list[pos + 1] = box_list[pos]
            pos -= 1
            box_list[pos + 1] = box


# b1 = Box(3.4, 19.8, 2.1)
# b2 = Box(1.0, 1.0, 1.0)
# b3 = Box(8.2, 8.2, 4.5)
# box_list = [b1, b2, b3]
# box_sort(box_list)
# for box in box_list:
    # print(box.volume())
