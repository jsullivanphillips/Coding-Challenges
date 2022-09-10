#AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
input = "AAAABBBCCDAA"
output = "4A3B2C1D2A"


def encode(input):
    cur_char = input[0]
    counter = 1
    output = ""
    for i in range(1, len(input)):
        if input[i] == cur_char:
            counter += 1
        else:
            output += str(counter) + cur_char
            cur_char = input[i]
            counter = 1

    output += str(counter) + cur_char
    return output






#testing
import unittest

class TestEncode(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(encode("AAAABBBCCDAA"), "4A3B2C1D2A", "Should be 4A3B2C1D2A")
    def test1_encode(self):
        self.assertEqual(encode("BBCVVLLPPPPPPX"), "2B1C2V2L6P1X", "Should be 2B1C2V2L6P1X")

if __name__ == '__main__':
    unittest.main()
