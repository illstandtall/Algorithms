class Node:
    def __init__(self):
        self.children = {}
        self.subN = 0

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, string):
        curr = self.root

        for char in string:
            if char not in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]
            curr.subN += 1

def solution(words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    cnt = 0
    for word in words:
        curr = trie.root
        for char in word:
            if char in curr.children:
                if curr.subN == 1:
                    break
                curr = curr.children[char]
                cnt += 1
    return cnt