#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
from collections import defaultdict

# @lc code=start


class TrieNode:
    def __init__(self) -> None:
        self.leaves = defaultdict(TrieNode)
        self.exist = False

    def __getitem__(self, key):
        return self.leaves[key]

    def __bool__(self):
        return bool(self.leaves) or self.exist

    def __str__(self) -> str:
        return f'{self.exist}\n{str(self.leaves)}'

    def __repr__(self) -> str:
        return str(self)


class Trie:

    def __init__(self):
        self._data = TrieNode()

    def insert(self, word: str) -> None:
        cur = self._data
        for c in word:
            cur = cur[c]
        cur.exist = True

    def search(self, word: str) -> bool:
        cur = self._data
        for c in word:
            cur = cur[c]
            if not cur:
                return False
        return cur.exist

    def startsWith(self, prefix: str) -> bool:
        cur = self._data
        for c in prefix:
            cur = cur[c]
            if not cur:
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
