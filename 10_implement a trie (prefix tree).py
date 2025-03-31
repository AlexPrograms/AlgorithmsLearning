# class Stack:
#     def __init__(self):
#         self.stack = []
#
#     def push(self, data):
#         self.stack.append(data)
#
#     def pop(self):
#         if not self.stack:
#             return "Stack is empty"
#         return self.stack.pop()
#
#     def peek(self):
#         if not self.stack:
#             return "Stack is empty"
#         return self.stack[-1]
#
#
# stack = Stack()
# stack.push(10)
# stack.push(20)
#
# print(stack.pop())
# print(stack.peek())
# print(stack.pop())


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            node = node.children.get(char)
            if not node: return False
        return node.is_end_of_word


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
trie.insert("app")
print(trie.search("app"))
