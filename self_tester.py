'''
    In order to run the tester:
    1.  Make sure your AVLTree.py file and this file
        are both in the same directory.
    2.  Run: python3 student_tester.py  
    3.  Your grade will be printed at the end.
        Only failed tests will be printed.
'''

import unittest
from AVLTree import AVLTree

GRADE = 0
MAX_GRADE = 10
TEST_COUNT = 1
POINTS_PER_TEST = MAX_GRADE / TEST_COUNT


class BasicStudentTester(unittest.TestCase):

    def setUp(self):
        self.T = AVLTree()

    def add_points(self):
        global GRADE
        GRADE += POINTS_PER_TEST

    def test_join(self):
        self.T.insert(10, "10")
        self.T.insert(5, "5")
        self.T.insert(15, "15")

        tree2 = AVLTree()
        tree2.insert(40, "40")
        tree2.insert(50, "50")
        tree2.insert(60, "60")
        tree2.insert(80, "80")
        tree2.insert(90, "90")

        self.T.join(tree2, 30, "30")

        self.assertEqual(self.T.size(), 9)
        self.assertIsNotNone(self.T.search(50)[0])
        self.assertIsNotNone(self.T.search(5)[0])
        self.assertIsNotNone(self.T.search(15)[0])

        self.assertIsNotNone(self.T.max_node())
        self.assertEqual(self.T.max_node().key, 90)

        self.add_points()

# ------------------------
#   Custom Test Runner
# ------------------------

if __name__ == "__main__":
    print("Running Self Tester...\n")

    suite = unittest.defaultTestLoader.loadTestsFromTestCase(BasicStudentTester)
    result = unittest.TextTestRunner(verbosity=0).run(suite)

    print("\n==============================")
    print("       TESTER SUMMARY")
    print("==============================")

    if result.failures or result.errors:
        print("\n❌ Failed Tests:")
        for test, err in result.failures + result.errors:
            test_name = test.id().split(".")[-1]
            print(f"  - {test_name}")
            print(f"    {err.splitlines()[-1]}")
    else:
        print("\n✅ All tests passed!")

    print("\nGrade:", GRADE, "/", MAX_GRADE)
    print("==============================")
