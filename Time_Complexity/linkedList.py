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
: Here you not only have reference to your next element - but you also have reference to your previous element as well

stock_prices
    |
0x00500             0x00A1                0x00C5                  0x00D7                0x00C0
|null|298|0x00A1|<->|0x00500|305|0x00C5|<->|0x00A1|320|0x00D7|<->|0x00C5|301|0x00C0|<->|0x00D7|292|null|

"""