import unittest
from unittest.suite import TestSuite
import demoqa, saucedemo

if __name__ == '__main__':
    #create test suite from class
    suite = TestSuite() 
    #panggil test
    tests = unittest.TestLoader()
    #add test ke test suite 
    suite.addTests(tests.loadTestsFromModule(saucedemo)) 
    suite.addTests(tests.loadTestsFromModule(demoqa)) 

    #run test suite
    runner = unittest.TextTestRunner()
    runner.run(suite)