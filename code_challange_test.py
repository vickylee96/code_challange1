import unittest
import code_challange1


class MyTestCase(unittest.TestCase):

    def test_find_x(self):
        """This test checks the if the find x function is finding 
        the missing x from the array list
        """

        arry = [3,7,1,2,8,4,5]
        self.assertEqual(6, code_challange1.find_x(arry))

if __name__ == "__main__":
    unittest.main()
        

