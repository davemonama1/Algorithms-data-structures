'''
my notes
python built in data structures

# Indexing strings - accessing any element in strings
x = 'frog'
#print(x[2]) >> o


#slicing Strings
r = 'computer'
#print(r[1:6:2]) >> opt

x = 'dave'
'u' in x

#iterating
t = [1,2,3,4]
for item in x:
    pass

#finding the address of items (indexing)
t = [13,2,4,5]
for index,item in enumerate(t):
    #print(index, item)
    pass

#sorting items
#1strings
x = 'bug'
print(sorted(x))
it will return 
'b' 'g' 'u'

#2 list
y = ['mike', 'dave', 'glen']
print(sorted(y))
it will return 'dave','glen','mike'

#3 tuple
u = ('ronny', 'kevin', 'emily')
print(sorted(u))



#unpacking of items (the amount of variables must match the number of the list)

i = 'dave', 'lorrein'
n, m = i

# print(m,n)


constructores for lists - how to create lists

1 empty lists
x = lists()

y = ['a', 2,3,'lon', 1.00] # you can have multiple datatypes

2. create a tuple and pass it in a list constructor
tupplee = (10,20)
z = list(tupple)

3. list comprehension
a = [m for m in range(8)]
print(a)
b = [i**2] for i in range(10) if i>4]
print(b)


#3. list comprehension
a = [m for m in range(8)]
#print(a)
b = [i**2 for i in range(10) if i>4]
#print(b)

#deleting an item from a list
q = [1,1,2,3]
del[q[1]]


Dictionaries - they are key value pairs some call them hashmaps

how to create dictionaries
x = {'dave', 'lord', 'changable', 'lord' }
print(x)


Python List Comprehension
basic format: new_list = [transform sequence[filter]]

we will use the random module in these examples so we will need to import random


import random

#get values withi range
under_10 = [x for x in range(10)]
#print('under_10: ' + str(under_10))

#2. get squared values
squares = [x**2 for x in under_10]
#print(squares)

#get odd numbers using mod 
ten_x = [x * 10 for x in range(10)]
# print('multiples of ten:' + str(ten_x))

#4. get numbers from string

s = 'i love 2 go to the 4club 6'
nums = [ x for x in s if x.isnumeric()]
print('nums: ' + ''.join(nums))

#4. delete an item from a list
letters = [x for x in 'abcdefg']
random.shuffle(letters)
ltrs = [a for a in letters if a != 'c']
print(letters, ltrs)

DATASTRUCTURES
1.Stacks
  In computer science, a stack is an abstract data type that serves
  as a collection of elements, with two main principal operations: 
  Push, which adds an element to the collection, and Pop, which 
  removes the most recently added element that was not yet removed.

stack is a LIFO data structure -- last-in, first-out
use append() to push an item onto the stack
use pop() to remove an item

#1. STACK - append 

stack1 = list() #you use this to create a new list and use append to push values in that stack 
stack1.append(46) 
stack1.append(2)
stack1.append(42)
stack1.append(3)
stack1.append(7)
print(stack1)
'''
# STACK - pop

#print(stac k.pop())

#STACK - using list with a wrapper class
#we create a stack class and a full set of stack methods.
#but the underlying data structure is reallly a python list
#for pop and peak methods we first check whether the stack is empty, to avoid exceptions

class Stack(): #instead of creating a regular stack class (-  Class Stack:  - ) we create a wrapper class (-  Class stack():  -)
    def __init__(self):
        self.stack = list()
    def push(self, item): #we create a constructor with a new list called item
        self.stack.append(item) # first you choose the function/ constructor (self.stack) then you choose the method which is append()

    def pop(self): #pop is when you remove the most recent added value
        if len(self.stack) > 0: #create an if statement that iterates when the top value is greater or equal to 1 (>0)
            return self.stack.pop()
        else:
            return None
    def peek(self):
        if len(self.stack) >0: # if the lenth of the stack is zero
            return self.stack.pop()#return thr latest node
        else:
            return None
    def __str__(self):
        return str(self.stack)

#test Code for stack wrapper class

# Queues CLASS Wrapping


class queues(): #this is a queues wrapper class
    def __init__(self):
        self.queues = list() #create a list
    def dequeue(self, item): 
        self.queues.dequeue(item)
    def enqueue(self):
        if len(self.queues()):
            return self.queues.enqueue()
        else:
            return None
    def __str__(self):
        return str(self.queues)

'''
QUEUES
  In computer science, a queue is a collection of entities that are maintained
  in a sequence and can be modified by the addition of entities at one end of 
  the sequence and the removal of entities from the other end of the sequence.

1. Enqueue - add an item to the end of the line
2. dequeue - remove an item from the frontt of the line

it is also known as a first-in, first-out

first you need to import a liabrary called deque
#QUEUES

 
queue = deque()
queue.append(1)
deque.append(4)
print(queue)
print(queue.pop())

#MAX HEAPS - they are fast.
they are implemented in lists
*insert in 0(log n)
*Get Max in 0(1)
*Remove Max in 0(log n)


*they are easy to implement using a list (index)

'''
max_heaps = [25,26,24,5,11,19,1,2,3,5]

# how to find a left children node in a max heap
i = max_heaps[3] * 2 + 1
'''
'''

#Python MaxHeap

class MaxHeap:
    def __init__(self, items=[]): # creating a constructor with a new LIST called items
        super().__init__()
        self.heap = [0] # this zero is the first element (index 0) in the heap called items/list
        for item in items: #iterate through the list
            self.heap.append(item) #this will add values one at a time to the end of the list
            self.__floatUp(len(self.heap) - 1) #floadUp will re-arange them to their proper positions as parents and nodes

    #Push Method
    def push(self, data): # create a list/array called data
        self.heap.append(data) # add the heap to data whenever the function push is used
        self.__floatUp(len(self.heap) - 1) #push or move the added element to its proper position


    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False
        
    def pop(self):
        if len(self.heap) > 2: # if the length of the list is greather than 2
            self.__swap(1, len(self.heap) - 1) #swap the heap
            max = self.heap.pop() #remove the element at the specify position
            self.__bubbleDown(1) # move the item in index 1 (thats the max heap) own to its proper position

        elif len(self.heap) == 2:
            max = self.heap.pop() #remove / reposition the element at the max (index 1)
        else:
            max = False
        return max

    def __swap(self, i, j): #we pass in 2 indices
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i] #and then we swap those two items in the list

    def __floatUp(self, index): #reposition the element to be the max/parent
        parent = index//2 #declare a parent variable then define it
        if index <= 1: #our first index is 0 so the 1 is our new first
            return #if the value (heap/item) is less than or greater than the current max, return the current maxheap
        elif self.heap[index] > self.heap[parent]: #if the (new element/heap) is greater then the current parrent
            self.__swap(index, parent) #swap the new index with the parent
            self.__floatUp(parent) #then because the old nax value might be bigger than other elements, re-position it using floatUp


    def __bubbleDown(self, index): #bubbledown is when you move the max item down the list  
        left = index * 2 #left child
        right = index * 2 + 1 #Right child
        largest = index #we only use bubbleDown when our index is bigger than our maxheap 
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:#if the item is greater than the left child and less than the right child
            largest = left # we are going to swap positions with the left child
        if len(self.heap) > right and self.heap[largest] < self.heap[right]: #if the item is greater than the right child and less than the left child
                largest = right #we swap positions with the right child
        if largest != index: #if the largest/max is not greater than the new item 
            self.__swap(index, largest) #we will swap the two items
            self.__bubbleDown(largest) #and we will recursively bubbledown the item untiil it reaches its proper position

    def __str__(self):
        return str(self.heap)

#MaxHeap Test code
'''
m = MaxHeap([95, 3,21]) #call the class using MaxHeap() - now assign the class to m then add values to the class
m.push(94) 
print(m)
print(m.pop())
print(m.peek())
'''

'''
LINKED LIST - every linked list will be composed of NODES
* every Node has 2 parts. - Data and a Pointer to the next Node
*You can store whatever data you want in a linked list

root - pointer to the beginning of the list
size - number of nodes in a list:
    add() - this will add a new root node to the list
    remove() - this will remove the root node.
'''

#LINKED LIST CLASS

#find operation - iterates through the nodest until it finds data passed in. if it finds the data it will return it otherwise returns NOne
#Print_list - iterates the list and prints each node

class Node:
    def __init__(self, d, n = None, p = None): #this are the value in a node D = data, N = next_node, P = previous Node. (this __INIT__ is the base class method)
        #every node has 2 parts DATA and a Pointer (there are 2 pointer types NEXT NODE pointer and there is the PREVIOURS NODE pointer).
        self.data = d #we assign the variable data to the list D or vice versa
        self.next_node = n #this is the NEXT NODE pointer
        self.prev_node = p #PREVIOUS NODE pointer

    def __str__(self): #this is a string representation - it gives us back the data in parenthesis ()
        return('(' + str(self.data) + ')')


class LinkedList:
    def __init__(self, r = None):
        #our constructor has 2 attributes root and size
        self.root = r #the first node
        self.size = 0 

    def add(self, d): #this function adds a new node * remember d = data
        new_node = Node(d, self.root) #we create a new node passing in the data and the next node as the root node.
        #the current root node is going to be the secont node hence (d, self.root)

        self.root = new_node #we change the root node to the new node
        self.size += 1 #we increment our size by 1

    def find(self, d): #to find a piece of data or a node (we pass in the data) = (self, d)
        this_node = self.root #we are gonna iterate throgh the nodes 1 node at a time .. we will start at the root node which we will call this_node (index 1) hence we write * this_node = self.root
        
        while this_node is not None: #as long as this_note (root node) is a valid node we are going to iterate through the list 
            if this_node.data == d: #when we find the valid node we are searching for we will then return it
                return d 
            else: #else if the node is not in the linked list
                this_node = this_node.next_node # return the nextnode
        return None #if this_node is not a valid node we will return None

    def remove(self, d): #this function Removes a node, remember we always remove the first node(root node) in the linked list
        this_node = self.root #we remove the first node
        prev_node = None #removing the root node means that there will not be any previous node

        while this_node is not None: #while we have a valid root node we are going to iterate through the linked list
            if this_node.data == d: # if the passed node that we are looking for is in the linked list itarate throgh
                if prev_node is not None: #if its not in the root (the passed node)
                    prev_node.next_node = this_node.next_node #we delete iit by changing the prev node (NEXT NODE pointer) to the passed node (NEXT NODE pointer)
                else: # if it is a root node with no prev node
                    self.root = this_node.next_node #swap it with the next node and remove it
                self.size -= 1 #
                return True #if we successfully remove it we return true

            else: #we dont find the node we are looking for make the prev node this node and then point this node to the next_node pointer
                prev_node = this_node 
                this_node = this_node.next_node

        return False # if we iterate through the list and we dont find the node the we return false
    
    def print_list(self): 
        this_node = self.root #print the list starting from the root node hence >> this_node = self.root
        while this_node is not None: #this while loop is going to check when we reach the end of the list
            print(this_node, end='->') #print the string representation of that list then show the next node by (_>)
            this_node = this_node.next_node

        print('None') #print none at the end of the list


#LINKED LIST TEST CODE >>>>

myList = LinkedList() #call the class linked list then assign the list (myList) to the class

#now we want to add nodes to the linked List
myList.add(5)
myList.add(8)
myList.add(12)


class CircularLinkedList: # a circular linked list is like a loop, you cannot add the new node  on the root position
    def __init__(self, r = None):
        self.root = r
        self.size = 0

    def add (self, d):
        if self.size == 0:
            self.root = Node(d)
            self.root.next_node = self.root
        else:
            new_node = Node(d, self.root.next_node)
            self.root.next_node = new_node

        self.size +=1 

    def find(self, d): #to find a piece of data or a node (we pass in the data) = (self, d)
        this_node = self.root #we are gonna iterate throgh the nodes 1 node at a time .. we will start at the root node which we will call this_node (index 1) hence we write * this_node = self.root

        while True:
            if this_node.data == d:
                return d
            elif this_node.next_node == self.root:
                return False
            this_node = this_node.next_node
        

    def remove(self, d): #this function Removes a node, remember we always remove the first node(root node) in the linked list
        this_node = self.root #we remove the first node
        prev_node = None #removing the root node means that there will not be any previous node

        while True: #while we have a valid root node we are going to iterate through the linked list
            if this_node.data == d: # if the passed node that we are looking for is in the linked list itarate throgh
                if prev_node is not None: #if its not in the root (the passed node)
                    prev_node.next_node = this_node.next_node #we delete iit by changing the prev node (NEXT NODE pointer) to the passed node (NEXT NODE pointer)
                else: # if it is a root node with no prev node
                    while this_node.next_node != self.root:
                        this_node = this_node.next_node
                    this_node.next_node = self.root.next_node
                    self.root = self.root.next_node
                self.size -=1
                return True
            elif this_node.next_node == self.root:
                return False
            prev_node = this_node
            this_node = this_node.next_node

'''
Doubly LINKED LIST
*every node has 3 parts : data and pointers to previous and next node

ADVANTAGES - over regular (single) linked List
*it can iterate the list in either direction
it can delete a node without iterating through the list (if given a pointer to the node)

'''
#Doubl LINKed LIst

class DoublyLinkedList:
    def __init__(self, r = None): # this will hold 2 attributes SIZE and Root which is the first node then becase it is a doubly linked list it will also contain a last pointer (it points to the prev node)
        self.root = r
        self.last = r # this means we can always access the last / prev node
        self.size = 0

    def add (self, d):
        if self.size == 0: # if the size of the node is 0 (<1)
            self.root = Node(d)
            self.last = self.root
        else: #if there are values to the list / (size >= 1)
            new_node = Node(d, self.root) #declare a new variable to the root node
            self.root.prev_node = new_node #point the root nodes prev pointer to the newly made root node 
            self.root = new_node #now make the newly added node the root node 
        self.size += 1 #add that node to the list

    def find(self, d):
        this_node = self.root #this_node is the value or data you entered
        while this_node is not None: #iterate through the list if the node is valid    
            if this_node.data == d:
                return d
            elif this_node.next_node == None:
                return False
            else:
                this_node = this_node.next_node

    def remove(self, d):
        this_node = self.root
        while this_node is not None: # if this_node(root node) is valid iterate through the list
            if this_node.data == d: # if there is a node that looks the same as the passed value
                if this_node.prev_node is not None: #because it is a doubly linked list check the prev node... even from the root node
                    if this_node.next_node is not None:
                        this_node.prev_node.next_node = this_node.next_node
                        this_node.prev_node.next_node = this_node.prev_node

                    else:
                        this_node.prev_node.next = None 
                        self.last = this_node.prev_node

                else:
                    self.root = this_node.next_node
                    this_node.next_node.prev_node = self.root
                self.size -= 1
                return True
            else:
                this_node = this_node.next_node
        return False

    def print_list(self): #this will output all the values n the linked list
        if self.root is None: # if the first node is valid 
            return
        this_node = self.root
        print(this_node, end='-->>') #this will create a little aspiring error (---->>>)
        while this_node.next_node is not None:
            this_node = this_node.next_node
            print(this_node, end='-->>')
        print()




