import unittest
import pyperclip
from bulleter import exporter_clipboarder, bulleter_function


class TestBulleter(unittest.TestCase):
    def test_clipboard(self):
        """
        Tests the exporter_clipboarder function
        tests creaio of a file and if it has the right documents
        """
        exporter_clipboarder("zzzzzzzzz", 'testfile')
        with open('testfile.txt', 'w') as text:
            print("zzzzzzzzz", file=text)
        with open('testfile.txt', 'r') as text:
            new = text.read()
            self.assertEqual('zzzzzzzzz\n', new)
        copied = pyperclip.paste()
        self.assertEqual('zzzzzzzzz', copied)

    def test_bulleter(self):
        """
        Tests the bulleter functionality if the entered text is formatted correctly
        """
        mylist = ["apple"]
        result = bulleter_function(mylist)
        self.assertEqual(result, '*Apple \n')


if __name__ == "__main__":
    unittest.main()
