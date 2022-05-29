contact={}

def display_contact():
    print("Contact_Name\t\tPhone_number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))


while True:
    choice = int(input(" 1.Add new contact \n 2.Search contact \n 3.display contact \n 4.Edit contact \n 5.Delete conatct \n 6.Exit \n Enter your choice:"))
    if choice==1:
        name=input("Enter contact name:")
        phone_no= input("enter the contact number:")
        if len(phone_no)<=12:
            print("Valid phone number")
            contact[name] = phone_no
        else:
            print("Invalid phone number")

    elif choice==2:
        search_contact=input("enter contact name:")
        if search_contact in contact:
            print((search_contact,"'s contact phone is ",contact[search_contact]))
        else:
            print("contact name is not found in the contact book.")
    elif choice==3:
        if not contact:
            print("contact book is empty")
        else:
            display_contact()
    elif choice==4:
        edit_contact=input("enter the contact name:")
        if edit_contact in contact:
            phone_no = input("enter the contact number:")
            if len(phone_no) <= 12:
                print("Valid phone number")
                contact[edit_contact] = phone_no
            else:
                print("Invalid phone number")
                print("contact updated")
            display_contact()
        else:
            print("Name is not found in contact book")
    elif choice==5:
        del_contact= input("enter the contact to be deleted ")
        if del_contact in contact:
            confrim=input("do you want to delete the contact permanently y/n?")
            if confrim=="y" or confrim=="Y":
                contact.pop(del_contact)
                print("Contact has been deleted ")
                display_contact()
            else:
                print("Contact has not found in the contact book ")
    else:
        break



