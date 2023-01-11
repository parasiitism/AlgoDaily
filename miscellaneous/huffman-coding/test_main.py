import unittest
# import the is_prime function
from main import Huffman


class TestHuffman(unittest.TestCase):
    def test0(self):
        s = "AABCBAD"
        encoding_map, encoding_str = Huffman.encode(s)
        t = Huffman.decode(encoding_map, encoding_str)
        self.assertEqual(s, t)

    def test1(self):
        s = "I am Calvin, from Hong Kong. Now I work at Facebook in London."
        encoding_map, encoding_str = Huffman.encode(s)
        t = Huffman.decode(encoding_map, encoding_str)
        self.assertEqual(s, t)

    def test2(self):
        s = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
        encoding_map, encoding_str = Huffman.encode(s)
        t = Huffman.decode(encoding_map, encoding_str)
        self.assertEqual(s, t)


"""
    Command input: python3 test_main.py
    
    Command output:
    ...
    ----------------------------------------------------------------------
    Ran 3 tests in 0.001s

    OK
"""
if __name__ == '__main__':
    unittest.main()
