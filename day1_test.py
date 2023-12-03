import unittest
import day1
import os


class TestDay1(unittest.TestCase):
    
        def test_part1(self):
            input = '''1abc2
            pqr3stu8vwx
            a1b2c3d4e5f
            treb7uchet'''.splitlines()
            self.assertEqual(day1.part_one(input), 142)
    
        def test_part2(self):
            input = '''two1nine
            eightwothree
            abcone2threexyz
            xtwone3four
            4nineeightseven2
            zoneight234
            7pqrstsixteen'''.splitlines()
            self.assertEqual(day1.part_two(input), 281)



if __name__ == '__main__':
    unittest.main()