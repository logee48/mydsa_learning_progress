//linked list

//how to create a linked list
//structure of linked list:  head.1stnode -> 2ndnode -> 3rdnode -> 4thnode -> None
  
class node:
  def __init__(self, data):
    self.data = data
    self.next = None
    
class linkedlist(self):
  def __init__(self):
    self.head = None
    
  //display function
  def traverse(self):
    temp = self.head
    while(temp):
      print(temp.data, end=" ")
      temp = temp.data
      
list = linkedlist()
list.head = node(10)  //1st_node
sec = node(20)        //2nd_node
third = node(30)      //3rd_node
  
//making link to each nodes
list.head.next = sec
sec.next = third      //third.next will be none by default
list.traverse()       // displaying output
//output
//10 20 30 


// inserting node to linkedlist
// write function inside linkedlist class

def insertbeg(self, data):
  newnode = node(data)
  temp = self.head
  newnode.next = temp.next
  temp.next = newnode
  
def insert_last(self, data):
  newnode = node(data)
  temp = self.head
  if(temp == None):
    insertbeg(newnode)
  else:
    while(temp.next):
      temp.next = newnode
      
      
def insert_with_index(self, data, index):
  newnode = node(data)
  count = 0
  temp = self.head
  while(count<index):
    temp = temp.next
    count+=1
  newnode.next = temp.next
  temp.next = newnode
  
def insert_with_key(self, data, key):
  newnode = node(data)
  temp = self.head
  while(temp.data != key):
    temp = temp.next
  newnode.next = temp.next
  temp.next = newnode
  
  
  
// deleting node in linkedlist
// write functions inside linkedlist class

def delete_beg(self):
  temp = self.head
  self.head = temp.next
  temp = None
  
def delete_end(self):
  
  
  
  
  
// finding mid node
// 2 methods old skl one find no.of nodes and div it by 2 and find mid node
// with traverse find no.of node
// rewrite insert_with_key to find the node

// rabbit and turtle methode i named it.
// rabbit and turle are pointers when turtle move through 1 node, rabbit will move through 2 node. At end rabbit will be at end and turtle will be in middle

def find_mid(self):
  rabbit = self.head
  turtle = self.head
  while(rabbit and rabbit.next):
    turtle = turtle.next
    rabbit = rabbit.next.next
  print(turtle.data)
  
  
// reversing linkedlist using 2 pointer methode
// simple logic but little bit confusing

def reverse(self):
  prev = None
  current = self.head
  while(current):
    nextnode = current.next
    current.next = prev
    prev = current
    current = nextnode
  // now all linkes are reversed prev is new head in last node
  while(prev):
    print(prev.data)
    prev = prev.next
  
  
  
  
    
    
    
    
    
    
    
    
    
    
  
  
  
  
  
  
  
