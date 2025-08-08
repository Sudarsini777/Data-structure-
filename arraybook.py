class Stack:
 def __init__(self):
    self.stack = []
 def push(self, book_title):
   self.stack.append(book_title)
   print(f"Book '{book_title}' added to the stack.")
 def pop(self):
     if self.is_empty():
       print("Stack is empty. No book to pop.")
     return None
     return self.stack.pop()
 def peek(self):
     if self.is_empty():
        print("Stack is empty. No book to peek.")
     return None
     return self.stack[-1]
 def is_empty(self):
     return len(self.stack) == 0
 def display_stack(self):
     if self.is_empty():
      print("Stack is empty.")
     return
     print("Current Stack of Books:")
     for title in reversed(self.stack):
       print(f"- {title}")

if __name__ == "__main__":
 book_stack = Stack()

 book_stack.push("money")
 book_stack.push("pink shoe")
 book_stack.push("the world")
 
 book_stack.display_stack()

 top_book = book_stack.peek()
 if top_book:
      print(f"Top book on the stack: '{top_book}'")
 
      print(f"Popped book: '{book_stack.pop()}'")
      print(f"Popped book: '{book_stack.pop()}'")

 book_stack.display_stack()

 book_stack.pop()
 book_stack.pop() 
