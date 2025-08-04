import os
NOTES_DIR = "notes"

#ensures the notes directory exists
os.makedirs(NOTES_DIR, exist_ok=True)

#function to create notes
def create_note():
    title = input("enter note title: ")
    content = input("enter note content: ")

    filepath = os.path.join(NOTES_DIR, f"{title}.txt")
    with open(filepath, "w") as f:
        f.write(content)

    print(f"Note '{title}' saved!")

#function to view notes
def view_notes():
    files = os.listdir(NOTES_DIR)
    if not files:
        print("No notes found!")
        return
    print("\n notes: ")
    for filename in files:
        print(f"- {filename[:-4]}") #remove .txt extension

#funtion to search notes
def search_notes():
    keyword = input("Enter keyword to search: ").lower()
    found = False

    for filename in os.listdir(NOTES_DIR):
        filepath = os.path.join(NOTES_DIR, filename)
        with open(filepath, "r") as f:
            content = f.read().lower()
            if keyword in content:
                print(f"Found in '{filename[:-4]}':")
                print(content)
                print("-"*30)
                found = True

    if not found:
        print("no matching file found.")

#function to define the menu for managment
def menu():
    while True:
        print("\n----Notes Manager----")
        print("1. Create Note")
        print("2. View Notes")
        print("3. Search Notes")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")
        if choice == "1":
            create_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            search_notes()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
if __name__ == "__main__":
    menu()
            
