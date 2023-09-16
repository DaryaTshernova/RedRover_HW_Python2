# codewars_test can be installed from https://github.com/codewars/python-test-framework
# run "pip install git+https://github.com/codewars/python-test-framework.git#egg=codewars_test"


import codewars_test as test
from solution import pillars

@test.describe("Basic Tests")
def basic_tests():
    
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(pillars(1, 10, 10), 0)
        test.assert_equals(pillars(2, 20, 25), 2000)
        test.assert_equals(pillars(11, 15, 30), 15270)