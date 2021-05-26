def reverse(string):
    def rev(string, index):

        if index == -1:
            return ""
        return string[index] + rev(string, index - 1)
    result = ""
    n = len(string) - 1
    result += rev(string, n)
    return result
    
# Test Cases
from nose.tools import assert_equal
class TestReverse(object):

    def test_rev(self, solution):
        assert_equal(solution('hello'), 'olleh')
        assert_equal(solution('hello world'), 'dlrow olleh')
        assert_equal(solution('123456789'), '987654321')

        print('PASSED ALL TEST CASES')

test = TestReverse()
test.test_rev(reverse)
