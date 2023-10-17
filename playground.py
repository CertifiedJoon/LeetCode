class Node:
    def __init__(self, letter):
        self._letter = letter
        self._children = dict()

    def add_child(self, c):
        node = Node(c)
        self._children[c] = node
        return node

    def get_letter(self):
        return self._letter

    def iter_children(self):
        for child in self._children:
            yield child

    def is_parent(self, letter):
        return letter in self._children

    def get_child(self, letter):
        return self._children[letter]


class Trie:
    def __init__(self, words):
        self._root = Node("_")

        for word in words:
            curr = self._root
            for c in word:
                if curr.is_parent(c):
                    curr = curr.get_child(c)
                else:
                    curr = curr.add_child(c)

    def search(self, word):
        curr = self._root
        matched_chars = []

        for c in word:
            if curr.is_parent(c):
                matched_chars.append(c)
                curr = curr.get_child(c)

        return "".join(matched_chars)


if __name__ == "__main__":
    trie = Trie(["mobile", "mouse", "moneypot", "monitor", "mousepad"])
    print(trie.search("mouse"))
