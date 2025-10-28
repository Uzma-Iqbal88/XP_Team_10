import unittest
from add_task import add_task

class TestAddTask(unittest.TestCase):
    def test_add_task(self):
        tasks = []
        result = add_task(tasks, "Buy milk")
        self.assertEqual(result, ["Buy milk"])
        self.assertEqual(len(result), 1)

if __name__ == '__main__':
    unittest.main()
