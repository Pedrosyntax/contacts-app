class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False # mark if a name ends here
        self.contacts = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, contact):
        node = self.root
        for char in word.lower():
            if char not in node.children:
                node.children[char] = TrieNode() #move to next letter
            node = node.children[char]
        node.is_end_of_word = True
        node.contacts.append(contact) #save contact

    def search_prefix(self, prefix):
        node = self.root
        for char in prefix.lower():
            if char not in node.children:
                return []
            node = node.children[char]
        return self._collect_contacts(node)
    
    def _collect_contacts(self, node):
        found = [] #if a full name end here, add those contacts
        if node.is_end_of_word:
            found.extend(node.contacts)
        for child_node in node.children.values(): #keep checking all the children letters
            found.extend(self._collect_contacts(child_node))
        return found