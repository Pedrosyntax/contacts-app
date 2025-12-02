from contact import Contact
from trie import Trie
class ContactsIndex:
    def __init__(self):
        self.contacts_by_id = {}
        self.contacts_by_phone = {}
        self.trie = Trie()
        self.next_id = 1
    def add_contact(self, contact):
        if contact.phone in self.contacts_by_phone:
            print("Warning: phone already exists")
        contact_id = self.next_id
        self.next_id += 1
        self.contacts_by_id[contact_id] = contact
        self.contacts_by_phone[contact.phone] = contact
        self.trie.insert(contact.full_name, contact)
        return contact_id
    def remove_contact(self, contact_id):
        if contact_id in self.contacts_by_id:
            contact = self.contacts_by_id.pop(contact_id)
            self.contacts_by_phone.pop(contact.phone, None)
    def find_by_phone(self, phone):
        return self.contacts_by_phone.get(phone)
    def find_by_name(self, name):
        matches = self.trie.search_prefix(name)
        exact = [c for c in matches if c.full_name.lower() == name.lower()]
        return exact
    def search_by_prefix(self, prefix):
        return self.trie.search_prefix(prefix)
    def all_sorted_by_name(self):
        return sorted(self.contacts_by_id.values(), key=lambda c: c.full_name.lower())
    