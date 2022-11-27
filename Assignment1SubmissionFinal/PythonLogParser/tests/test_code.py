import unittest 
import my_library
from my_library  import get_manufacturer

class TestFormatter(unittest.TestCase): 
    def test_1(self): 
        test_text =  "C8:4B:D6:AA:BB:CC" 
        result = my_library.get_manufacturer(test_text) 
        self.assertEqual(result, "Dell") 
        
if __name__ =="__main": 
	unittest.main()