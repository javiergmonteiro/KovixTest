from nose.tools import istest, eq_
from formatters import format_string


@istest
def string_should_return_2_iterations():
    test_string = "AAAAAFFFFOOOA"
    eq_("AAFFOOA", format_string(test_string, 2))


@istest
def number_string_should_return_1_iterations():
    test_string = "111223333344"
    eq_("1234", format_string(test_string, 1))


@istest
def string_should_return_1_iterations():
    test_string = "AABB"
    eq_("AB", format_string(test_string, 1))
