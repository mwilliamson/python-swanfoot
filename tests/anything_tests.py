from nose.tools import istest, assert_equal

from swanfoot import anything
from swanfoot.results import matched


@istest
def matches_anything():
    assert_equal(matched(), anything.match(4))
    assert_equal(matched(), anything.match(None))
    assert_equal(matched(), anything.match("Hello"))


@istest
def description_is_anything():
    assert_equal("anything", anything.describe())

