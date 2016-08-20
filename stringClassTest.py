import unittest

class TestBuildInStringClass(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("emmanuel".upper(),"EMMANUEL")
    def test_lower(self):
        self.assertEqual("Emmanuel".lower(),"emmanuel")
    def test_isdigit(self):
        self.assertTrue("56".isdigit())
        self.assertFalse("Muthui".isdigit())
    def test_strip(self):
        self.assertEqual("    manuh  ".strip(),'manuh')
    def test_startswith(self):
        self.assertTrue("musyoka".startswith('m'))
        self.assertFalse("musyoka".startswith('e'))
    def test_split(self):
        self.assertEqual("emmanuel muthui".split(), ['emmanuel', 'muthui'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            "emmanuel muthui".split(2)
    def test_join(self):
        self.assertEqual(" ".join(['emmanuel', 'muthui'],'emmanuel muthui'))
    def test_index(self):
        self.assertEqual("emmanuel".index('m'),1)
        with self.assertRaises(ValueError):
            "emmanuel".index('q')
    def test_count(self):
        self.assertEquals("emmanuel".count('m'),2)
        
    def test_replace(self):
        self.assertEqual("emmanuel".replace('m','k'),'ekkanuel')
        self.assertEqual("emmanuel".replace('m','k'),'emmanuel')