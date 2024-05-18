def find_first_pe(prices, eps, index):
    """
    Time complexity Order of One Exmple

    O(1)
    """
    pe = prices[index]/eps[index]
    return pe 

##This is a classic example of O(1) time complexity. 
#Let's take for example, we want to find the pricess of stocks in a list with `eps` and `index`
#When we supply an index, it will perform a constant operations - so it doesn't matter whether we have a millionn stocks in the list 

