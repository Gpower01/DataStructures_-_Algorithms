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
    'march 6': 320,
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
| Data Structure  | Python | Java                    | C++ |
| ---             | ---    | ---                     | ---
| Array           | List   |Native array / Array list| Native array /std::vector |

