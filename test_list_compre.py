from unittest import TestCase

class Test(TestCase):
    def testListCompre(self):
        item = [1,1,2,2,4,4]
        new_item = [n * n for n in item]

        a = new_item[0]
        b = new_item[1]
        self.assertEqual(a, b)