from solution import Solution

solve = Solution().findSubstring


def test_default():
    assert set(solve('barfoothefoobarman', ['foo', 'bar'])) == {0, 9}
    assert set(solve('barfoofoobarthefoobarman', [
               'bar', 'foo', 'the'])) == {6, 9, 12}
    assert set(solve('bcabbcaabbccacacbabccacaababcbb', [
               'c', 'b', 'a', 'c', 'a', 'a', 'a', 'b', 'c'])) == {6, 16, 17, 18, 19, 20}


def test_corner_cases():
    assert set(solve('', ['foo', 'bar'])) == set()
    assert set(solve('barfoothefoobarman', [])) == set()


def test_failure_cases():
    assert set(solve('wordgoodgoodgoodbestword', [
               'word', 'good', 'best', 'word'])) == set()
