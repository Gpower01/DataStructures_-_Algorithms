#Arrays: Let's assume we are writing a program to find Apple stock prices for 5 days - specifically for 1st and 3rd day
#Numbers stored in RAM are converted to binary number: for example 298 = 100101010
#When you have an integer number, we use 4bytes 

#PYTHON

"""
298 = 00000000 00000000 00000001 00101010 } 4bytes

: 1byte is 8bits

:So for the Apple stock price example: 4bytes for every number 
stock_prices = [298, 305, 320, 301, 292]

: For Example - to calculate, what was the price on day 3?
stock_prices:
 |
0x00500 -> 298         stock_prices[2] -> 320 (price on day 3)
0x00504 -> 305         stock_prices[0] -> 0x00500
0x00508 -> 320         stock_prices[2] -> 0x00500 + 2 * sizeof(integer)
0x0050A -> 301         stock_prices[2] -> 0x00500 + 2 * 4
0x0050F -> 292         stock_prices[2] -> 0x00508
                      
                       Lookup by index = O(1) --> constant time operations


: Another Example - On what day was the stock price 301?
: for this eample:

for i in range(len(stock_prices)):
    if stock_prices[i] == 301:
        return i
                        Lookup by value = O(n)  --> Big O notation 

: Another Example - Print all the prices

for prive in stock_prices:
    print(prices)
                        Array traversal = O(n)  --> Big O notation 

: Another Example Operations - Insert new stock price 284 at index 1
Because the insert operation will shift all the elements by 1 step 

stock_prices.insert(1, 284)
                        Array insertion = O(n)  --> Big O notation 

: Another Example Operation - Delete element 305 from stock_prices array which is at index 1
Again, because all the elements needs to be adjusted 

stock_prices.remove(1)
                        Array deletion = O(n)  --> Big O notation 

: In Python, list is implemented as Dynamic array

: In other languages like JAVA, C++ - we have both Static and Dynamic arrays
"""

#JAVA
"""
Assuming we are writing the program in JAVA to store the stock price array 

: In JAVA - we have both Static and Dynamic arrays

: STATIC ARRAY
int[] stockPrices = new int[5]; //Static integer array of fixed size 5

stockPrices[0] = 298;
stockPrices[1] = 305;
stockPrices[2] = 320;
stockPrices[3] = 301;
stockPrices[4] = 292;

: Attempting to insert another array - for example at 7th position - we get an error 

stockPrices[6] = 400;   // Not allowed. Throws ArrayIndexOutOfBounds exception

: DYNAMIC ARRAY 
: When Dynamic array grows, there is an overhead of allocating new memory and copying over all the elements plus the new addition - using a mathematical opertion known as GEOMETRIC PROGRESSION
ArrayList<Integer> stockPrices = new ArrayList<Integer>();

stockPrices.add(298);
stockPrices.add(305);
stockPrices.add(320);
stockPrices.add(301);
stockPrices.add(292);

stockPrices.add(400);
"""

#ARRAYS DATA TYPE
"""
Arrays can store
: numbers
: text 
: complex objects 

For example

stock_prices = [2, 3, 5, 6]

stock_names = ["Apple", "IBM", "TATA"]

stock_data = [
{"ticker": "AAPL", "price": 302},
{"ticker": "TSLA", "price": 902},
{"ticker": "TATA", "price": 278},
]

:PYTHON
In python array can store different data types - integers, strings, complex data etc

:JAVA & C++
Cannot store different data types, the type is fixed -once you set integer, you cannot insert string for example

: In C++ --> Dynamic arrays are called vectors

:ARRAY DIMENSIONS
We can different dimensions of array - 1D, 2D, 3D etc

: An example of 2D Array --> 2 Dimensional Array
stock_prices = [
[2, 3, 5, 6],
[40, 42, 38, 44],
[78, 89, 71, 66]
]

: To retrive for example stock_price of 42:
stock_prices[1][1]
"""