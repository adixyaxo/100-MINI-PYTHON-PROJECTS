
return_days = 7 # enter the no of days a student can keep a book borrowed
fine_per_day = 100
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
        "title": self, # critical fix we are using self (the object) instead of self.name as self is an object and self.name is a string
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
            userbook_str = str(userbook)
            if userbook_str.lower() == infotitle.name.lower():
                bookfound = True
                return infotitle
                break
            if bookfound == False :
                print("Book Not found")
                
def get_student(student_entry):
        for id,name in default_students.items():
            student_name = name["name"]
            studentfound = False 
            student_entry_str = str(student_entry)
            if student_entry_str.lower() == student_name.name.lower() or student_entry_str == id:
                studentfound = True
                return student_name
                break
            if studentfound == False :
                print("Wrong Student Entry Please Enter Correct Name or ID")

def borrow_book(book_,student_entry):
        get_student(student_entry)
        if get_book(book_).available_copies > 0 :
            bklist = get_student(student_entry).bk
            bklist[book_] = 10
            print(f"You have borrowed {get_book(user_book).name} written by {get_book(user_book).author}")
        else:
            print("Book Unavailable")
        
def return_book(book,student_entry):
    error = None
    bklist = get_student(student_entry).bk
    try:
        bklist.remove(book)
    except ValueError as e:
        print("You dont have that book you want to return")
        error = e
    if error == None:
        get_book(book).available_copies += 1
        print(f"You have returned {get_book(user_book).name} written by {get_book(user_book).author}")

def display_all_books():
    print("ALL books are listed below ::\n")
    for id,info in default_books.items():
        print(f"Name : {info["title"].name}  ::  ID :: {id}  ::  Available : {info["available"]}\n")

def reserve_a_book(book_,student_entry):
        get_student(student_entry)
        if get_book(book_).available_copies > 0 :
            bklist = get_student(student_entry).bk
            bklist.append(book_)
            print(f"You have reserved {get_book(user_book).name} written by {get_book(user_book).author}")
        else:
            print("Book Unavailable")



class student:
    def __init__(self,name,id,course,year,bk={}):
        self.name=name
        self.id = id
        self.course = course
        self.year = year
        self.bk = bk
    
    def bookdate(self,b_k):
        try:
            return self.bk[b_k] or self.bk[b_k.lower()]
        except ValueError and KeyError as e:
            return e
        
    def about(self):
        print("--- Student Details ---")
        print(f"Name:   {self.name}")
        print(f"ID:     {self.id}")
        print(f"Course: {self.course}")
        print(f"Year:   {self.year}")
        print(f"Books:  {self.bk}")
        print("-----------------------")
    
    def add_a_student(self):
        default_students[id] ={
        "name": self, # critical fix we are using self (the object) instead of self.name as self is an object and self.name is a string
        "course": self.course,
        "year": self.year,
        "borrowed_books": self.bk
    }
        

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
        "borrowed_books": {"halwa chalwa" : 8}  # Currently has nothing
    },
    "STU-002": {
        "name": "Rahul Sharma",
        "course": "B.Tech Mechanical",
        "year": 2,
        "borrowed_books": {"The Pragmatic Programmer" : 1}  # Has 'The Pragmatic Programmer'
    },
    "STU-003": {
        "name": "Priya Singh",
        "course": "B.Tech CSE",
        "year": 1,
        "borrowed_books": {}
    },
    "STU-004": {
        "name": "Vikram Malhotra",
        "course": "BBA",
        "year": 3,
        "borrowed_books": {"To Kill a Mockingbird" : 1} # Has 'To Kill a Mockingbird'
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
    10-Reserve a book
    0-Exit""")
    
    try :
        choice = int(input("Please enter your choice -- :: "))
    except ValueError as e:
        print("Please only enter numbers")
        continue
    
    print("\n\n")
    
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
        user_student = str(input("Enter the name of the student you want to know about  ::  "))
        get_student(user_student).about()
        
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
        name = input("Enter the name of the student  ::  ")
        id = input("Enter the id of the student  ::  ")
        course = input("Enter the course of the student  ::  ")
        year = int(input("Enter the year of the student  ::  "))
        books = int(input("Enter the no of books borrowed by student  ::  "))
        books_br={}
        for i in range (1,books+1):
            books_br[input(f"Enter the name of the book {i}  ::  ")] = input("Enter the date book was taken  ::  ")
        student_regestration = student(name,id,course,year,books_br)
        student_regestration.add_a_student()
        
    elif choice == 7:
        display_all_books()
        
    elif choice == 8:
        user_search = input("Enter the name of the book you want to search for  ::  ")
        x = get_book(user_search)
        if x != None:
            x.about()   
            
    elif choice == 9:
        enter_name = input("Enter you name  ::  ")
        book_enter = input("Enter the name of the book you want to find  ::  ")
        date_due = int(get_student(enter_name).bookdate(book_enter.lower())) - return_days
        print("\n\t::")
        if date_due > 0 :
            print(f"You have {date_due} days to return the book")
        elif date_due == 0:
            print("You have to return the book today")
        else:
            print(f"You have {(0-date_due)} days of overdue and your fine is ruppes {0-(date_due)*fine_per_day}")
            
    elif choice == 10:
        student_enter = print("Enter your name  ::  ")
        book_enter = print("Enter the name of the book you want to reserve  ::  ")
        reserve_a_book(book_enter,student_enter)
        
    elif choice == 0:
        print("Exiting Programme .........")
        break
    else:
        print("Wrong Choice Please Try again")
    
    print("\n\n\n\n")