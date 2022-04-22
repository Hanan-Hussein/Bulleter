import unittest
import bulleter

class TestBulleter(unittest.TestCase):
    def test_clipboard(self):
        bulleter.exporter_clipboarder("zzzzzzzzz",'testfile');
        with open('testfile.txt', 'r') as text:
            self.assertEqual('zzzzzzzzz\n', text.read());
            
    def test_bulleter(self):
        mylist = ["apple"];
        result = bulleter.bulleter_function(mylist);
        self.assertEqual(result,'*Apple \n');   
        
if __name__=="__main__":
    unittest.main()