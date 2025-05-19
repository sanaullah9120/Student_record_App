# step-0 import datetime module
from datetime import datetime
# Step 1: Function – Add New Note
def add_new_note():
    
    name = input("Enter name of student:")
    subject = input("Enter subject name:")
    note = input("Enter note content:")

    timestamp = datetime.now().strftime("%y-%m-%d %H:%M:%S")

    # Yahan hum ek proper formatted entry bana rahe hain jo file mein likhni hai. '-'*40 ka matlab 40 dash lines.

    entry = f"Datetime:{timestamp}\nName:{name}\nSubject:{subject}\nNote:{note}\n{"-"*40}\n"

    # File ko "w" mode mein open kiya — yani overwrite karegi ,entry file mein likh di
    with open("student_notes.txt","w")as file:
        file.write(entry)

    print("New note saved successfully") #User ko confirm message dikhaya


# Step 2:Creat Function – View Notes (read a file)
def view_notes():
    try:
        with open("student_notes.txt","r")as file:  # File ko read mode mein khola
            content = file.read()     # Uska poora content read() karke ek string mein store kiya
            if content.strip() == "":  # gar file empty hai (strip karke check kiya) to message dikhaya
                print("NO notes find")
            else:
                print("\n===All Notes===")
                print(content)
    except FileNotFoundError:   # Agar file hi nahi bani ab tak to yeh error handle karega
        print("file not found")
        
# Step 3:Creat Function –that Append More Notes of user
def append_note():   # User se naya note ka input le rahe hain
    name = input("Enter student name:")
    subject = input("Enter subject:")
    note = input("Enter note content:") 
    timestamp = datetime.now().strftime("%y-%m-%d %H:%M:%S")

    entry = f"Time:{timestamp}\nName:{name}\nSubject:{subject}\nNote:{note}\n{"-"*40}\n"
    with open("student_notes.txt","a")as file:  # "a" mode ka use kiya — yani append karega


        file.write(entry)  # Entry file mein likh di without deleting old notes
        print(" Note added successfully!")

# Step 4: Function – Search by Student Name
def search_name():
    search_name = input("Enter name to search:").lower()
    found = False  #User se naam poocha jisko dhoondhna hai, aur found ko False set kiya
    try:
        with open("student_notes.txt","r")as file:
            lines = file.readlines()  # File ko read kiya line-by-line
            entry = "" # entry naam ka empty string banaya har ek full note collect karne ke liye
            for line in lines:
                entry += line  # Har line entry mein jor rahe hain
                if line.strip() =="-"*40:  # Jab 40 dashes milein, matlab ek entry complete hai


                    if search_name in entry.lower(): # Check kar rahe hain kya us entry mein search_name hai?
                        print("\nfound entry:",entry)  #Agar haan, to us entry ko print karo
                        found = True
                    entry = ""
                    
            if not found:
                print("NO note found for that name:")
    except FileNotFoundError:
        print("Note file not found. Please add a note first.")
                        
#  Step 5: Create a Function – Clear All Notes of file
def clear_notes():
    with open("student_notes.txt","w")as file:
        file.write("")                    # File ko "w" mode mein open karke blank likh diya — yani file clear ho gayi.
        print("All notes cleared") 
		
# Step 6: Main Menu Loop
while True:
    print("\n===Student Notes Manager===")
    print("1- Add new note(overwrite)")
    print("2- View all notes")
    print("3- Append more notes")
    print("4- Search note by name")
    print("5- Clear all notes")
    print("6- Exist")

    choice = input("choose an option from (1 to 6):")

    if choice == "1":
        add_new_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        append_note()
    elif choice == "4":
        search_name()
    elif choice == "5":
        clear_notes()
    elif choice == "6":
        print("Goodbay")
        break
    else:
        print("Invalid choice,please choose from 1 to 6.")
        
        
