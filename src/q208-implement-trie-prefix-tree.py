#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start


class Trie:

    def __init__(self):
        self._data = [True, {}]

    def insert(self, word: str) -> None:
        _, cur = self._data
        for c in word:
            try:
                pre = cur
                _, cur = cur[c]
            except KeyError:
                pre = cur
                cur[c] = [False, {}]
                cur = cur[c][1]
        pre[word[-1]][0] = True

    def search(self, word: str) -> bool:
        exist, cur = self._data
        for c in word:
            try:
                exist, cur = cur[c]
            except KeyError:
                return False
        return exist

    def startsWith(self, prefix: str) -> bool:
        _, cur = self._data
        for c in prefix:
            try:
                _, cur = cur[c]
            except KeyError:
                return False
        return True

# @lc code=end


def test_default():
    trie = Trie()
    assert not trie.startsWith('a')
    assert not trie.search('apple')
    trie.insert('apple')
    assert trie.search('apple')
    assert not trie.search('app')
    assert trie.startsWith('app')
    trie.insert('app')
    assert trie.search('app')
