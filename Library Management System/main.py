return_days = 7 
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
        # ### ERROR: 'id' is not defined in this function's scope. It will try to use the global 'id' from the initialization loop at the bottom, which is not safe.
        default_books[id] = { 
        "title": self, 
        # ### ERROR: The 'book' class does not have a 'self.id' attribute initialized in __init__ (you used self.s_no).
        "author": self.id, 
        "genre": self.genre,
        "copies": self.copies,
        "available": self.available_copies
    }, # ### SYNTAX: This trailing comma makes this dictionary a 'tuple'. Remove the comma.
    
#seperate book functions
def get_book(userbook):
        for id,info in default_books.items():
            infotitle = info["title"]
            bookfound = False 
            userbook_str = str(userbook)
            if userbook_str.lower() == infotitle.name.lower():
                bookfound = True
                return infotitle
                # ### LOGIC: 'break' is unreachable here because 'return' exits the function immediately.
                break 
            # ### LOGIC: This check is INSIDE the loop. It will print "Book Not found" for every single book that doesn't match until it finds the right one. This should be outside the loop.
            if bookfound == False :
                print("Book Not found")
                
def get_student(student_entry):
        for id,name in default_students.items():
            student_name = name["name"]
            studentfound = False 
            student_entry_str = str(student_entry)
            # ### ERROR: You are checking 'student_name.name'. In your dictionary setup, 'name["name"]' IS the student object. So 'student_name.name' works, but the variable naming is confusing.
            if student_entry_str.lower() == student_name.name.lower() or student_entry_str == id:
                studentfound = True
                return student_name
                break
            # ### LOGIC: Same issue as above. This will print "Wrong Student" multiple times while looping.
            if studentfound == False :
                print("Wrong Student Entry Please Enter Correct Name or ID")

def borrow_book(book_,student_entry):
        get_student(student_entry)
        # ### CRITICAL: If get_book returns None (book not found), accessing .available_copies will crash the program.
        if get_book(book_).available_copies > 0 :
            bklist = get_student(student_entry).bk
            # ### LOGIC: You are setting the value to integer 10. Later you treat this as a date. You should probably store the actual date string here.
            bklist[book_] = 10 
            # ### ERROR: 'user_book' is not defined in this function. You named the argument 'book_'. 'user_book' only works because it exists globally in the main loop (bad practice).
            print(f"You have borrowed {get_book(user_book).name} written by {get_book(user_book).author}")
        else:
            print("Book Unavailable")
        
def return_book(book,student_entry):
    error = None
    # ### CRITICAL: If get_student returns None, .bk will crash.
    bklist = get_student(student_entry).bk
    try:
        # ### CRITICAL: 'bklist' is a Dictionary. Dictionaries do not have a .remove() method (that is for lists). You need 'del bklist[book]' or 'bklist.pop(book)'.
        bklist.remove(book) 
    except ValueError as e:
        print("You dont have that book you want to return")
        error = e
    if error == None:
        get_book(book).available_copies += 1
        # ### ERROR: Again, 'user_book' is not defined here. Use the argument 'book'.
        print(f"You have returned {get_book(user_book).name} written by {get_book(user_book).author}")

def display_all_books():
    print("ALL books are listed below ::\n")
    for id,info in default_books.items():
        # ### SYNTAX ERROR: You cannot use double quotes (") inside an f-string that is already wrapped in double quotes. Use single quotes for the keys: info['title'].name
        print(f"Name : {info["title"].name}  ::  ID :: {id}  ::  Available : {info["available"]}\n")

def reserve_a_book(book_,student_entry):
        get_student(student_entry)
        if get_book(book_).available_copies > 0 :
            bklist = get_student(student_entry).bk
            # ### CRITICAL: 'bklist' is a Dictionary. .append() is a List method. This will crash.
            bklist.append(book_) 
            # ### ERROR: 'user_book' is not defined here. Use 'book_'.
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
        # ### SYNTAX: 'ValueError and KeyError' evaluates to just 'KeyError'. To catch both, use a tuple: (ValueError, KeyError).
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
        # ### ERROR: 'id' is not defined in this scope.
        default_students[id] ={ 
        "name": self, 
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
        # ### CRITICAL: If get_book returns None (not found), this throws 'AttributeError: 'NoneType' object has no attribute 'about''.
        get_book(user_book).about()
        
    elif choice == 4:
        user_student = str(input("Enter the name of the student you want to know about  ::  "))
        # ### CRITICAL: Same here. If get_student returns None, this crashes.
        get_student(user_student).about()
        
    elif choice == 5:
        name = input("Enter the name of the book  ::  ")
        id = input("Enter the id of the book  ::  ")
        author = input("Enter the author of the book  ::  ")
        genre = input("Enter the genre of the book  ::  ")
        copies = input("Enter the copies of the book  ::  ")
        available_copies = input("Enter the available copies of the book  ::  ")
        name = book(name,id,author,genre,copies,available_copies)
        # ### LOGIC: The add_a_book method will fail because it relies on the global 'id' variable which is currently set to the last student ID from the loop above, not the new 'id' you just input.
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
        # ### LOGIC: Same logic error as choice 5. 'add_a_student' uses a stale global 'id'.
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
        # ### CRITICAL: 'get_student(...).bookdate(...)' might return an error object (e) or a number. If it returns the error object, int() will crash.
        date_due = int(get_student(enter_name).bookdate(book_enter.lower())) - return_days
        print("\n\t::")
        if date_due > 0 :
            print(f"You have {date_due} days to return the book")
        elif date_due == 0:
            print("You have to return the book today")
        else:
            print(f"You have {(0-date_due)} days of overdue and your fine is ruppes {0-(date_due)*fine_per_day}")
            
    elif choice == 10:
        # ### BUG: 'print' returns None. 'student_enter' will be None. You must use 'input()' here.
        student_enter = print("Enter your name  ::  ")
        # ### BUG: Same as above. 'book_enter' will be None.
        book_enter = print("Enter the name of the book you want to reserve  ::  ")
        reserve_a_book(book_enter,student_enter)
        
    elif choice == 0:
        print("Exiting Programme .........")
        break
    else:
        print("Wrong Choice Please Try again")
    
    print("\n\n\n\n")