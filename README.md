# DataStructures_-_Algorithms
* Data Structure and Algorithms - Time &amp; Space Complexity Analysis 

* Programming is Art as well as Science 

- Data Structures are building blocks or raw materials for any software programs. 
- One cannot become a good programmer without sound understanding of data structures.

* Data Structures are containers for storing data in a specific memory layout 

## PROBLEM EXAMPLE 1  
- For example we want to ask queston about the Apple stock price for 5 days and answer:
1) What was the price on day 1
2) What was the price on day 3

* In this case, we only care about sequence. We are caring about day 1 vs day 3

- So we can write a simple python programme which looks like this:
- So we can compile the stock prices in a list and access the stock pricess using the index operator 

```
stock_price  = [298, 305, 320, 301, 292]

stock_price[0] <- stock price on day 1

stock_price[2] <- stock price on day 3
```

## PROBLEM EXAMPLE 2
- Let's say your problem is that you want to get the stock prices along with the date from March 4th to March 17th 

1) What was the stock price on March 17th 
2) What was the stock price on March 4th 

* In this case, it makes sense to write a python programme where you can access the stock price on a given date using the dictionary key - for example 

```
stock_price = {
    'march 4': 298, 
    'march 5': 305,
    'ls
    smarch 6': 320,
    'march 7': 301,
    }
```


stock_price[march 7] <- march 7 stock price
stock_price[march 4] <- march 4 stock price 

## You can see that in this two scenarios, I used two different data structures which are LIST and DICTIONARY, which have a hashmap behind the scene

* we used this two different data structure to solve two different problems - so it depends on what kind of problem that you are solving - will determine what kind of data structure that will be best suited for the particular problem. 

## Memory Layout for both of these data structure
1) List: where the stock prices are stored in a contiguous memory (RAM) location

stock_price = [298, 305, 320, 301, 292]
```
| 298 | 305 | 320 | 301 | 292 |  --> Array or List 
```

2) Dictionary: Where it uses a hashmap behind the scene. And the way that hasmap work is that we have a key on which you apply a hash function, which will give you an address of a bucket - and using that address now you access a given element. 

* This way, you get an O(n) - order of one complexity for your search and your search is really fast
```
stock_price = {
    'march 4': 298, 
    'march 5': 305,
    'march 6': 320,
    'march 7': 301,
    }
```

## Different Data Structures & Programming Languages  
| Data Structure  | Python        | Java                     | C++     |
| ---             | ---           | ---                      | ---
| Array           | List          | Native array / Array list| Native array /std::vector|
| Hash Table      | dictionary    | HashMap / LinkedHashMap  | std::map |
| Linked List     | Not available | LinkedList               | std::list  |

## Big O notation:
* Big O notation is used to measure how running time or space requirements for your program grows as input size grows.

## O(n) Time Complexity 
- **Runtime Analysis:** 
* for example, let's assume below array function:
```
def foo(arr):

size(arr) --> 100 --> 0.22 milliseconds
size(arr) --> 1000 --> 2.30 milliseconds

time = a*n + b

--Is a linear progression
```

* simplified:
`time = a*n + b` 
* time = a*n  : keep faster growing term
* time = O(n) : drop constants 

>> Now we say that the Big O notation time complexity for this program is order of n --> O(n)

## O(1) Time Complexity :
* time = a

1) Keep faster growing term 
2) Drop constants 

`time = O(1)`

## O(n^2) Time Complexity 
- A classic exmple is where we trying to find a duplicate number in a list 

* time = a * n^2 + b

`time = O(n^2)`

* Another O(n^2) scenario is
`time = a*n^2 + b*n + c`

- For this two scenarios, always remember, 
1) keep the fastest growing term
2) Drop contants 

- **Big O** refers to large value of `n`. Hence if you have a function like:

`time = 5*n^2 + 3*n + 20`

- When value of `n` is very large `b*n + c` becomes irrelevant: For example:

* time = 5*1000^2 + 3*1000 + 20
* time = 5000000 + 3020

- So as we can see `5*n^2` - is 5million compared to `3*n + c` which is 3020

 

