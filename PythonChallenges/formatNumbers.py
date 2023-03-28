# Write a function named 'formatNumber' that takes a non-negative number as its only parameter. Your function should convert the
# number to a string and add commas as a thousand separators. For example, calling format_number(1000000) should return "1,000,000".
import unittest


def formatNumber(num):
    if int(num) < 0:
        return "Error: Number Must Be Non-Negative"
    num = str(num)
    formattedNum = ''
    for i in range(len(num) - 1, 0, -1):
        formattedNum += num[i]
        if (len(num) - i) % 3 == 0 and i != len(num) - 1:
            formattedNum += ','
    return num[0] + formattedNum[::-1]


class TestFormatNumber(unittest.TestCase):

    def test_no_change(self):
        self.assertEqual(formatNumber(1), '1', 'Should be 1')
        self.assertEqual(formatNumber(10), '10', 'Should be 10')
        self.assertEqual(formatNumber(100), '100', 'Should be 100')

    def test_change(self):
        self.assertEqual(formatNumber(1000), '1,000', 'Should be 1,000')
        self.assertEqual(formatNumber(10000), '10,000', 'Should be 10,000')
        self.assertEqual(formatNumber(100000), '100,000', 'Should be 100,000')
        self.assertEqual(formatNumber(1000000),
                         '1,000,000', 'Should be 1,000,000')
        self.assertEqual(formatNumber(10000000),
                         '10,000,000', 'Should be 10,000,000')

    def test_invalid(self):
        self.assertEqual(formatNumber(-1), 'Error: Number Must Be Non-Negative',
                         'Should be "Error: Number Must Be Non-Negative"')


if __name__ == '__main__':
    unittest.main()
