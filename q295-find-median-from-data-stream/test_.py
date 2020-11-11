from solution import MedianFinder

solve = MedianFinder()


def test_default():
    finder = MedianFinder()
    finder.addNum(1)
    finder.addNum(2)
    assert finder.findMedian() == 1.5
    finder.addNum(3)
    assert finder.findMedian() == 2
    finder.addNum(3)
    assert finder.findMedian() == 2.5
    finder.addNum(1)
    assert finder.findMedian() == 2


def test_corner_cases():
    finder = MedianFinder()
    assert finder.findMedian() == 0
    finder.addNum(1)
    assert finder.findMedian() == 1

def test_nonegative_input():
    finder = MedianFinder()
    finder.addNum(-1)
    assert finder.findMedian() == -1
    finder.addNum(-3)
    assert finder.findMedian() == -2
    finder.addNum(1)
    finder.addNum(2)
    assert finder.findMedian() == 0
