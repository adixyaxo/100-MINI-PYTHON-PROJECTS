class book:
    def __init__(self,name,s_no,author,std,status):
        self.name=name
        self.s_no=s_no
        self.author=author
        self.std=std
        self.status=status
    
    def book_borrowed(self):
        pass
        
class student:
    def __init__(self,name,id,bk={None}):
        self.name=name
        self.id = id
        self.bk = bk
        

book1 = book()
