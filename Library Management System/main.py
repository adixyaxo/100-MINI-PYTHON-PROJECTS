class book:
    def __init__(self,name,s_no,author,genre,copies,available_copies):
        self.name=name
        self.s_no=s_no
        self.author=author
        self.genre = genre
        self.copies=copies
        self.available_copies=available_copies
    
    def about(self):
            print("\n" + "="*30)
            print(f" BOOK DETAILS")
            print("="*30)
            print(f" NAME      :: {self.name}")
            print(f" AUTHOR    :: {self.author}")
            print(f" GENRE     :: {self.genre}")
            print(f" ISBN/ID   :: {self.s_no}")
            print("-" * 30)
            print(f" TOTAL COPIES     :: {self.copies}")
            print(f" AVAILABLE COPIES :: {self.available_copies}")
            print("="*30 + "\n")
    
    def add_a_book(self):
        default_books[id] = {
        "title": self.name,
        "author": self.id,
        "genre": self.genre,
        "copies": self.copies,
        "available": self.available_copies
    },
    
#seperate book functions
def get_book(userbook):
        for id,info in default_books.items():
            infotitle = info["title"]
            bookfound = False 
            if userbook.lower() == infotitle.name.lower():
                bookfound = True
                return infotitle
                break
            elif bookfound == False :
                print("Book Not found")
                
def get_student(student_entry):
        for id,name in default_students.items():
            student_name = name["name"]
            studentfound = False 
            if student_entry.lower() == student_name.name.lower() or student_entry.lower()== id:
                studentfound = True
                return student_name
                break
            elif studentfound == False :
                print("Wrong Student Entry Please Enter Correct Name or ID")

def borrow_book(book,student_entry):
        get_student(student_entry)
        if get_book(book).available_copies > 0 :
            bklist = get_student(student_entry).bk
            bklist.append(book)
            print(f"You have borrowed {get_book(user_book).name} written by {get_book(user_book).author}")
        else:
            print("Book Unavailable")
        
def return_book(book,student_entry):
        bklist = get_student(student_entry).bk
        try:
            bklist.remove(book)
        except ValueError as e:
            print("You dont have that book you want to return")
        get_book(book).available_copies += 1
        print(f"You have returned {get_book(user_book).name} written by {get_book(user_book).author}")


class student:
    def __init__(self,name,id,course,year,bk=[]):
        self.name=name
        self.id = id
        self.course = course
        self.year = year
        self.bk = bk
        

#default books and students
# --- Random Default Data ---

# Key = ISBN (Unique ID)
# Value = Dictionary with book details
default_books = {
    "978-0132350884": {
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "genre": "Computer Science",
        "copies": 3,
        "available": 3
    },
    "978-0201616224": {
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt",
        "genre": "Computer Science",
        "copies": 2,
        "available": 1  # One is currently borrowed
    },
    "978-0451524935": {
        "title": "1984",
        "author": "George Orwell",
        "genre": "Fiction",
        "copies": 5,
        "available": 5
    },
    "978-0743273565": {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Fiction",
        "copies": 2,
        "available": 2
    },
    "978-0061120084": {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Classic",
        "copies": 4,
        "available": 0  # All borrowed
    }
}

for id,key in default_books.items():
    key["title"] = book(key["title"],id,key["author"],key["genre"],key["copies"],key["available"])

# Key = Student ID (Roll Number)
# Value = Dictionary with student details
default_students = {
    "STU-001": {
        "name": "Aditya Dagar",
        "course": "B.Tech CSE",
        "year": 1,
        "borrowed_books": []  # Currently has nothing
    },
    "STU-002": {
        "name": "Rahul Sharma",
        "course": "B.Tech Mechanical",
        "year": 2,
        "borrowed_books": ["The Pragmatic Programmer"]  # Has 'The Pragmatic Programmer'
    },
    "STU-003": {
        "name": "Priya Singh",
        "course": "B.Tech CSE",
        "year": 1,
        "borrowed_books": []
    },
    "STU-004": {
        "name": "Vikram Malhotra",
        "course": "BBA",
        "year": 3,
        "borrowed_books": ["To Kill a Mockingbird"] # Has 'To Kill a Mockingbird'
    }
}

for id,name in default_students.items():
    name["name"] = student(name["name"],id,name["course"],name["year"],name["borrowed_books"])
    
    
    
    
    
    
    
    
    
    
    
while True:
    print("""--Welcome To The Library Management System--

    What would you like to do ?
    01-Borrow a book
    02-Return a book
    03-Know about a book
    04-Know about a student
    05-Add a new book
    06-Register a new student
    07-Display all books
    08-Search for a book
    09-Check overdue books / Fines
    10-View lending history
    11-Reserve a book
    12-Save & Exit""")
    choice = int(input("Please enter your choice -- :: "))

    if choice == 1:
        user_book = str(input("Enter the name of the book you want to borrow  ::  "))
        student_entry = input("Enter you name  :: ")
        borrow_book(user_book,student_entry)
    elif choice == 2:
        user_book = str(input("Enter the name of the book you want to return  ::  "))
        student_entry = input("Enter you name  :: ")
        return_book(user_book,student_entry)
    elif choice == 3:
        user_book = str(input("Enter the name of the book you want to know about  ::  "))
        get_book(user_book).about()
    elif choice == 4:
        pass
    elif choice == 5:
        name = input("Enter the name of the book  ::  ")
        id = input("Enter the id of the book  ::  ")
        author = input("Enter the author of the book  ::  ")
        genre = input("Enter the genre of the book  ::  ")
        copies = input("Enter the copies of the book  ::  ")
        available_copies = input("Enter the available copies of the book  ::  ")
        name = book(name,id,author,genre,copies,available_copies)
        name.add_a_book()
    elif choice == 6:
        pass
    elif choice == 7:
        pass
    elif choice == 8:
        pass
    elif choice == 9:
        pass
    elif choice == 10:
        pass
    elif choice == 11:
        pass
    elif choice == 12:
        pass
    
    print("\n\n\n\n")