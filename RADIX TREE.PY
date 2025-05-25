class RadixNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class RadixTree:
    def __init__(self):
        self.root = RadixNode()

    def insert(self, word):
        node = self.root
        while word:
            for key in node.children:
                common = self._common_prefix(key, word)
                if common:
                    if common == key:
                        word = word[len(common):]
                        node = node.children[key]
                        break
                    elif common == word:
                        # Split the existing node
                        old_child = node.children.pop(key)
                        node.children[common] = RadixNode()
                        node.children[common].children[key[len(common):]] = old_child
                        node.children[common].is_end = True
                        return
                    else:
                        # Need to split into common, rest of key and rest of word
                        old_child = node.children.pop(key)
                        node.children[common] = RadixNode()
                        node.children[common].children[key[len(common):]] = old_child
                        node.children[common].children[word[len(common):]] = RadixNode()
                        node.children[common].children[word[len(common):]].is_end = True
                        return
            else:
                # No common prefix found, add the word directly
                node.children[word] = RadixNode()
                node.children[word].is_end = True
                return

    def search(self, word):
        node = self.root
        while word:
            found = False
            for key in node.children:
                if word.startswith(key):
                    word = word[len(key):]
                    node = node.children[key]
                    found = True
                    break
            if not found:
                return False
        return node.is_end

    def _common_prefix(self, s1, s2):
        min_len = min(len(s1), len(s2))
        i = 0
        while i < min_len and s1[i] == s2[i]:
            i += 1
        return s1[:i]

# Example Usage
tree = RadixTree()
tree.insert("rom")
tree.insert("rope")
tree.insert("rose")
tree.insert("road")

print(tree.search("rom"))   # True
print(tree.search("rope"))  # True
print(tree.search("rose"))  # True
print(tree.search("ro"))    # False
print(tree.search("roar"))  # False
