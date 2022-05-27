from multiprocessing.sharedctypes import Value
import unittest
import client2

class TestClient(unittest.TestCase):

    def test_one_minute_averages(self):
        self.assertRaises(ValueError, client2.one_minute_averages)


if __name__ == '__main__':
    unittest.main()