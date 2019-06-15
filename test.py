from flask import Flask, jsonify
from flask import request
import unittest
import mainf

class Testmainf(unittest.TestCase):
    def test_comb1(self):
        result =[c for c in mainf.combs1(2,[1,2,3],[])]
        self.assertEqual(result,[[1, 2], [1, 3], [2, 3]])






if __name__ == '__main__':
    unittest.main()