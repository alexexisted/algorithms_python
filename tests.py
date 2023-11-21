from factorial import factorial
from bin_search import binary_search
from bubble_sort import bubble_sort
from ins_sort import insertion_sort
from merge_sort import merge_sort


def test_factorial():
    assert factorial(1) == 1
    assert factorial(0) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6


def test_binary_search():
    assert binary_search([1, 5, 6, 11, 12, 16, 35, 78, 444], 16) == True
    assert binary_search([1, 5, 6, 11, 12, 16, 35, 78, 444], 17) == False


def test_buble_sort():
    assert bubble_sort([1, 5, 6, 11, 12, 16, 35, 78, 444]) == [1, 5, 6, 11, 12, 16, 35, 78, 444]
    assert bubble_sort([98, 2, 12, 43, 5, 11]) == [2, 5, 11, 12, 43, 98]
    assert bubble_sort([]) == []
    assert bubble_sort([9, 88, 77, 6, 5, 234, 1, 12]) == [1, 5, 6, 9, 12, 77, 88, 234]


def test_insertion_sort():
    assert insertion_sort([67, 34, 1, 45, 17, 3]) == [1, 3, 17, 34, 45, 67]


def test_merge_sort():
    assert merge_sort([5, 3, 65, 2, 11, 4]) == [2, 3, 4, 5, 11, 65]
