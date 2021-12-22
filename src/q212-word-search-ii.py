#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
from typing import List
from collections import defaultdict


# @lc code=start

class TrieNode:
    def __init__(self, exist=False) -> None:
        self.leaves = defaultdict(TrieNode)
        self.exist = exist

    def __getitem__(self, key):
        return self.leaves[key]

    def __setitem__(self, key, value):
        self.leaves[key] = value

    def search(self, word):
        cur = self
        for c in word:
            cur = cur[c]
            if not cur.exist:
                return False
        return True


class Solution:
    adjs = ((-1, 0), (1, 0), (0, -1), (0, 1))

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie_tree = self.construct_trie_tree(board, len(max(words, key=len)))
        result = []
        for word in words:
            if trie_tree.search(word):
                result.append(word)
        return result

    def construct_trie_tree(self, matrix, length):
        tree = TrieNode()
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                self.dfs(tree, matrix, i, j, length-1)
        return tree

    def dfs(self, tree, matrix, start_i, start_j, remain):
        c, matrix[start_i][start_j] = matrix[start_i][start_j], False
        tree[c].exist = True
        if not remain:
            matrix[start_i][start_j] = c
            return
        m, n = len(matrix), len(matrix[0])
        for x, y in self.adjs:
            next_i, next_j = start_i + x, start_j + y
            if 0 <= next_i < m and 0 <= next_j < n and matrix[next_i][next_j]:
                self.dfs(tree[c], matrix, next_i, next_j, remain - 1)
        matrix[start_i][start_j] = c
        return


# @lc code=end
solve = Solution().findWords


def test_default():
    assert solve([['o', 'a', 'a', 'n'], ['e', 't', 'a', 'e'], ['i', 'h', 'k', 'r'], [
                 'i', 'f', 'l', 'v']], ['oath', 'pea', 'eat', 'rain']) == ['oath', 'eat']
    assert solve([['a', 'b'], ['c', 'd']], ['abcb']) == []
    assert solve([['a', 'b', 'c'], ['a', 'e', 'd'], ['a', 'f', 'g']], ['abcdefg', 'gfedcbaaa',
                 'eaabcdgfa', 'befa', 'dgc', 'ade']) == ['abcdefg', 'gfedcbaaa', 'eaabcdgfa', 'befa', ]


def test_corner_cases():
    assert solve([['a']], ['a']) == ['a']
    assert solve([['a']], ['b']) == []
    assert solve([['a'], ['b']], ['ab', 'ba']) == ['ab', 'ba']
