# codewars_test can be installed from https://github.com/codewars/python-test-framework
# run "pip install git+https://github.com/codewars/python-test-framework.git#egg=codewars_test"


import codewars_test as test
    
@test.describe("longest")
def tests():
    @test.it("basic tests")
    def basics():
        test.assert_equals(longest("aretheyhere", "yestheyarehere"), "aehrsty")
        test.assert_equals(longest("loopingisfunbutdangerous", "lessdangerousthancoding"), "abcdefghilnoprstu")
        test.assert_equals(longest("inmanylanguages", "theresapairoffunctions"), "acefghilmnoprstuy")
        