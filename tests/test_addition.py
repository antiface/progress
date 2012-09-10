import unittest
import yaml

import sys
sys.path.insert(0,"..")

from progress.progress import add

def load_items():
    return [i for i in yaml.load_all(open('progress.yaml'))]


class TestAddition(unittest.TestCase):

    def test_addition(self):
        add('test')
        items = load_items()
        is_added = False
        for i in items:
            print i
            if i['step']['title'] == 'test':
                is_added = True
                break
        self.assertTrue(is_added)


if __name__ == '__main__':
    unittest.main()