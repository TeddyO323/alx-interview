import unittest
from lockboxes import canUnlockAll

class TestCanUnlockAll(unittest.TestCase):
    def test_all_boxes_openable(self):
        boxes = [[1], [2], [3], [4], []]
        self.assertTrue(canUnlockAll(boxes))

        boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
        self.assertTrue(canUnlockAll(boxes))

    def test_not_all_boxes_openable(self):
        boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
        self.assertFalse(canUnlockAll(boxes))

if __name__ == "__main__":
    unittest.main()
