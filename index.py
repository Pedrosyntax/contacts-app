from contact import Contact
from trie import Trie

class ContactsIndex:
    def __init__(self):  
        self.contacts_by_id = {} #dictionaries are unordered, they only store data for fast access.
        self.contacts_by_phone = {} #store contasts in a dictionary using their phone
        self.trie = Trie() #make name search must faster doesnt need to check every contact
        self.next_id = 1
    
    def add_contact(self, contact):
        if contact.phone in self.contacts_by_phone:
            print("Warning: phone already exists") #print a warning
        contact_id = self.next_id # give unique ID
        self.next_id += 1
        self.contacts_by_id[contact_id] = contact
        self.contacts_by_phone[contact.phone] = contact #looking up for or deleting a contact by phone is instant.
        self.trie.insert(contact.full_name, contact) #add contact into the trie so I can search it later
        return contact_id
    
    def remove_contact(self, contact_id):
        if contact_id in self.contacts_by_id:
            contact = self.contacts_by_id.pop(contact_id)
            self.contacts_by_phone.pop(contact.phone, None) # remove from the phone dictionary
    
    def find_by_phone(self, phone):
        return self.contacts_by_phone.get(phone)
    
    def find_by_name(self, name):
        matches = self.trie.search_prefix(name)
        exact = [c for c in matches if c.full_name.lower() == name.lower()] # filter to get exact name matches
        return exact
    
    def search_by_prefix(self, prefix): #return all contacts whose names start with the prefix
        return self.trie.search_prefix(prefix)
    
    def all_sorted_by_name(self): #sort contacts alphabetically 
        return sorted(self.contacts_by_id.values(), key=lambda c: c.full_name.lower()) #sprt all contacts by name