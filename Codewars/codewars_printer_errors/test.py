# codewars_test can be installed from https://github.com/codewars/python-test-framework
# run "pip install git+https://github.com/codewars/python-test-framework.git#egg=codewars_test"


import codewars_test as test
from solution import printer_error

@test.describe("printer_error")
def basic_tests():
    @test.it('Example Test Cases')
    def example_test_cases():
        s="aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
        test.assert_equals(printer_error(s), "3/56")
        s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
        test.assert_equals(printer_error(s), "6/60")
        s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu"
        test.assert_equals(printer_error(s) , "11/65")