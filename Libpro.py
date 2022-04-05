class Libr:
    def __init__(self,blist,lname):
        self.blist=blist
        self.lname=lname
        self.lendr={}
    def displayb(self):
        print(self.blist)
    def addb(self):
        book=input("Please Enter the name of the book: ")
        self.blist.append(book)
    def lendb(self):
        bname=input("Please Enter the name of the book: ").capitalize()
        if bname not in self.blist:
            print("Please enter the correct name of the book")
        if bname in self.blist:
            name=input("Please enter your name: ")        
            self.blist.remove(bname)
            self.lendr[bname]=name
        else:
            if self.blist.get(bname):
                print(f"Book is not available as {self.lendr[bname]} as already has it")
    def retb(self):
        book=input("Enter the name of the book you want to return: ").capitalize()
        if book in self.lendr:
            self.blist.append(book)
            del self.lendr[book]
        else:
            print("Please enter a valid name")

if __name__ == "__main__":
    bookl=[]
    s=int(input("Please enter the size of the Library and the names of the books: "))
    for i in range(s):
        name=str(input())
        bookl.append(name)
    arlib=Libr(bookl,'arlib')
    while True:
        op=input("Please enter what you want to do Display, Add, Lend, Return, or Quit (D,A,L,R,Q): ")
        if op=='Q' or op=='q':
            break
        if op=='D' or op=='d':
            arlib.displayb()
        elif op=='A' or op=='a':
            arlib.addb()
        elif op=='L' or op=='l':
            arlib.lendb()
        elif op=='R' or op=='r':
            arlib.retb()