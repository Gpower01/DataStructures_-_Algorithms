#Linked List & Big O Complexity Analysis
"""
Topics covered:
: Issues with arrays that linked list solves
: Doubly linked list 
: Big O analysis (array vs linked list)

#Issues with Array Example
stock_prices = [298, 305, 320, 301, 292]

stock_prices in memory:
    |
0x00500 -> 298
0x00504 -> 305
0x00508 -> 320
0x0050A -> 301
0x0050F -> 292

: When we try to insert another stock price - for example at index loction 1, it will copy all other stock price to another location 

stock_prices.insert(1, 284)
0x00500 -> 298
xxxxxxx -> 284
0x0050x -> 305
0x0050x -> 320
0x0050x -> 301
0x0050x -> 292

                    Big O notation of Array insertion = O(n)

Python List is a Dynamic Array

stock_prices = []

stock_prices.append(298)
stock_prices.append(305)
stock_prices.append(320)

stock_prices.insert(1, 284)

So - in this case, the overhead is not only copying/swaping values but also allocating new memory location and copying over all the elements to this new memory location
: So we can see that this is not very efficient 

LINKED LIST

:Imagine we have a data structure like this
: Arrays store values in contiguous memory location whereas the values below are stored in a random memory location which are linked by the pointer 
: The first element have a reference to the address of the next element. So we are creating a link here and through  this link we can access the elements 

stock_prices
    |
0x00500         0x00A1       0x00C5        0x00D7        0x00C0
| 298|0xC702|->|305|0x00C5|->|320|0x00D7|->|301|0x00C0|->|292|null|
             |
            0xC702
         |284|0x00A1|

: So now when we want to insert new element (284) with  the linked list reference, it becomes very easy

                    Insertion Element (LinkedList) at the Begining = O(1)
                    Delete Element (LinkedList) at the Begining    = O(1)
                    Insert/Delete Element (LinkedList) at the End  = O(n) 


: This Data Structure is called: Linked List
: It has two main benefits over array:

a) You don't need to pre-allocate space
b) Insertion is easier 

Big O notation: 
                    Linked List Traversal = O(n)
                    Accessing Element By Value = O(n)

DOUBLE LINKED LIST 
: Here you not only have reference to your next element - but you also have reference to the previous element

stock_prices
    |
0x00500             0x00A1                0x00C5                  0x00D7                0x00C0
|null|298|0x00A1|<->|0x00500|305|0x00C5|<->|0x00A1|320|0x00D7|<->|0x00C5|301|0x00C0|<->|0x00D7|292|null|

Now Let's try and implement Linked List in PYTHON 
: Two classes - 
: Node class, which represents individual element in the linked list (it accepts data and next(pointer) attributes)
" LinkedList class, which contains the head variable that point to the head of the next list 

"""

class Node:
    def __init__(self, data=None, next=None) -> None:
        """ 
        Data contain integer numbers, text strings or complex numbers
        : The node class represents the individual element in the Linked list 
        : It has two variables which are `data` element in the list and `next` which is the pointer to the next element in the list 
        """
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        """This is the Linked List class which contains the `head` variable that points to the next `head` in the list"""
        self.head = None

    def insert_at_begining(self, data):
        """ Takes the data and the head with the pointer to the next """
        node  = Node(data, self.head)
        self.head =  node 
    
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return 

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next 
        
        print(llstr)

    def insert_at_end(self, data):
        """
        First we need to check if the head is None, then we will insert that data and since we are inserting to the end, the `next` will be null

        : However, in a case where the linked list is not blank, we want to iterate all the way to the end and insert the data 
        : So we will iterate `itr.next` all the way to the end until `itr.next` becomes None - which means that we are at the end, at that point then we will point the node to the new node data
        """
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)
    
    def insert_values(self, data_list):
        """
        This method will take a list of value as an input value and it will create a new fresh linked list 
        : So in this method, because we are wiping out all the values and starting from scratch and we are creating a new Linked List 
        : We can simply iterate through each of the data in the list and insert the each data at the end calling the insert_at_end method
        """
        self.head  =  None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        """This method counts the number of element in our Linked List and return the total count"""
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next

        return count 


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining(5)
    ll.insert_at_begining(89)
    ll.insert_at_end(79)
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    print("length of Linked List is:", ll.get_length())