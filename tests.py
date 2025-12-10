from contact import Contact
from index import ContactsIndex

def run_tests():
    print("Starting ContactsIndex tests..")
    contacts_index = ContactsIndex() #main contact manager to hold and search contacts

    contact1 = Contact("Pedro", "12345")
    contact2 = Contact("Maria", "56789")
    contact3 = Contact("Belle", "54321")
    contact4 = Contact("Mylo", "676767")
    contacts_index.add_contact(contact1) 
    contacts_index.add_contact(contact2)
    contacts_index.add_contact(contact3)
    contacts_index.add_contact(contact4)

    print("Find by phone 12345:", contacts_index.find_by_phone("12345").full_name)

    print("Exact search 'Pedro:'", [c.full_name for c in contacts_index.find_by_name("Pedro")])

    print("Prefix search 'Pe':", [c.full_name for c in contacts_index.search_by_prefix("Pe")])

    print("All contacts sorted by name:", [c.full_name for c in contacts_index.all_sorted_by_name()])

    contact_dup = Contact("Fred", "12345")
    contacts_index.add_contact(contact_dup)

    empty_search = contacts_index.find_by_name("NonExistent")
    print("Empty search result:", empty_search)

    contact_id = contacts_index.add_contact(Contact("Josh", "55555"))
    contacts_index.remove_contact(contact_id)
    print("After removal, search Josh", contacts_index.find_by_name("Josh"))

if __name__ == "__main__":
    run_tests()