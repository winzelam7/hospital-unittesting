import unittest
import argparse
import sys
import send

#These aren't working right now, need to figure this out!
def parse_args():
    parser = argparse.ArgumentParser(description='Unit testing for hospital website')
    
    parser.add_argument("--test",action="store_true",help="Include to run tests")
    parser.add_argument("--dryrun",action="store_true",help="Include to perform dry run of tests (but do not actually run them)")

    args = parser.parse_args()

    return args

# Here are all my tests! - actual code located in send.py
class Testing(unittest.TestCase):
    # test some stuff
    def test_string(self):
        a = 'some'
        b = 'some'
        self.assertEqual(a, b)

    # test some other stuff
    def test_boolean(self):
        a = True
        b = True
        self.assertEqual(a, b)
    
    # test if you can connect to website
    def test_connectivity(self):
        connected = send.test_connection()
        self.assertEqual(connected, 200)

    # test for login to fail
    def test_loginfailure(self):
        response = send.test_failure()
        self.assertEqual(response, 301)
    
    # test for login to work
    def test_loginpass(self):
        response = send.test_login()
        self.assertEqual(response, 201)
    
    # test a PUT request
    def test_put(self):
        response = send.test_put()
        self.assertEqual(response, 200)

if __name__ == '__main__':
    #args = parse_args()

    if len(sys.argv) > 1:
        unittest.mock()
    else:
        unittest.main()