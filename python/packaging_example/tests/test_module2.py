import unittest


from my_library.module2 import multiply


class TestModule2(unittest.TestCase):


    def test_multiply(self):


        self.assertEqual(multiply(2, 3), 6)


if __name__ == '__main__':


    unittest.main()