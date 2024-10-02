import numpy as np


"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""

# ------------------------------------ Functions -----------------------------------


# ------------- Method 1 ---------------
def std_loops(numbers):
    """
    Compute standard deviation of x using loops.

    Parameters
    ----------
    numbers: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    
    # --- Code block to add find the mean of the sequece of numbers ---
    sum = 0  # Variable to store all the "part" sum 
    i = 0    # variable to count numbers
    
    # itterate through every number in numbers and add it to the sum  
    for num in numbers:
        sum += num  #updating sum
        i += 1    # updation numbers itterated through
        
    #calculating the mean 
    mean = sum/i

    # --- Code block to calculate the mean of squares
    
    sumOfSquares = 0 #variable to contain the sum of sqares of the number in the sequence numbers 
    
    # itterate through every number in numbers
    for num in numbers: 
        sumOfSquares += num**2  #update the sum of squares
        
    S = sumOfSquares/i  # calcucate the mean of sqares
    
    variencesquared = S - mean**2  # calcualte the variance
    
    # Returning the standard deviation using the sqrt(function) form numpy
    return np.sqrt(variencesquared)


    
# ------------- Metod 2 -------------
        

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
    
    # calcualte the mean as the sum devided by the number of items in the list using inbuilt python functions
    mean = sum(numbers)/len(numbers)
    
    # calcualte the mean of squares as the sum of squared devided by number of numbers in the list
    S = sum([num**2 for num in numbers])/len(numbers)
    
    # Calcualte variance
    variance = S - mean**2
    # Returning the stander deviation
    return np.sqrt(variance)


# -------------- Method 3 -------------

# A function using numpy's std function to find the standard deviation
def std_numpy(numbers):
    return np.std(numbers) 



def main(): 
    # Demonstrating that the fuctions provide the same result for all the functions
    num_lst = [i for i in range(1,5)]
    print(std_builtin(num_lst) == std_loops(num_lst) == std_numpy(num_lst))
    
    
    

# --------------------------------------------- Main program -------------------------------------------

main()
    


