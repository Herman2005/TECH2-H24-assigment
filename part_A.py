import math as mt
import numpy as np



"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""

# -------------------------------------------- Functions -----------------------------------

def std_loops(numbers):
    """
    Compute standard deviation of x using loops.

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    
    
    sum = 0
    i = 0
    
    for num in numbers:
        sum += num
        i += 1 
        
    mean = sum/i
    
    sumOfSquares = 0
    for num in numbers: 
        sumOfSquares += num**2
        
    S = sumOfSquares/i
    variencesquared = S - mean**2
    
    return mt.sqrt(variencesquared)


    
    
      
        

def std_builtin(numbers):
    """
    Compute standard deviation of x using the built-in functions sum()
    and len().

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    
    mean = sum(numbers)/len(numbers)
    S = sum([num**2 for num in numbers])/len(numbers)
    variance = S - mean**2
    return mt.sqrt(variance)


# method 3
def std_numpy(numbers):
    return np.std(numbers) 



def main(): 
    #showingthe result is the same
    num_lst = [i for i in range(1,5)]
    print(std_builtin(num_lst) == std_loops(num_lst) == std_numpy(num_lst))
    
    
# ----------------------------------- Main ---------------------------------

main()
    


