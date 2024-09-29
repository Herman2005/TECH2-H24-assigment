import math as mt
import numpy as np



"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""

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




test = [1,2,3]
std = np.std(test)

#print(std_builtin(test) == std_loops(test) == std)


