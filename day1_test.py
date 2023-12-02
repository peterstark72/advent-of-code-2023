import unittest
import day1
import os

input = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet'''.splitlines()

class TestDay1(unittest.TestCase):
    
        def test_part1(self):
            self.assertEqual(day1.part_one(input), 142)
    


if __name__ == '__main__':
    unittest.main()