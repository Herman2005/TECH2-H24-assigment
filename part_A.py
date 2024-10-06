import numpy as np


"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""

# A progrom to calcutlte the standar deviation of a list of numbers using different approaches, and then demonstrate that they give similar answers

# ------------------------------------------- Functions -----------------------------------------------


# ------------- Method 1 ---------------

def std_loops(numbers):
    """
    Compute standard deviation of numbers using loops.

    Parameters
    ----------
    numbers: list
        A list of the numbers we want to evaluate 

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    
    # --- Code block to find sum of the sequence and sum of squares in the same sequence ---
    sum = 0  # Variable to store all the "part" sums 
    sumOfSquares = 0 # variable to contain the sum of sqares of the number in the sequence numbers 
    i = 0    # variable to count numbers
    
    # itterate through every number in numbers and add it to the sum  
    for num in numbers:
        sum += num  #updating sum
        sumOfSquares += num**2  #update the sum of squares
        i += 1    # updation numbers itterated through
        
    # --- Caluclate the mean and mean of squares for the sequence ---
    mean = sum/i
    S = sumOfSquares/i  # calcucate the mean of sqares
    
    # Variance define as:
    variance = S - mean**2

    
    # calculate the standard deviation
    sd = np.sqrt(variance)
    
    return sd


    
# ------------- Metod 2 -------------
        

def std_builtin(numbers):
    """
    Compute standard deviation of numbers using the built-in functions sum()
    and len().

    Parameters
    ----------
    numbers: List
       A list containing the numbers we want to evaluate

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
    
    # calucualte stardard deviation
    sd = np.sqrt(variance)
    
    return sd


# -------------- Method 3 -------------

# A function using numpy's std function to find the standard deviation
def std_numpy(numbers):
    """_summary_

    Parameters:
        numbers: List
           a list of the numbers we want to evaluate

    Returns:
        sd: Float 
          the standar deviation of Numbers
    """
    
    sd = np.std(numbers) 
    return sd



def main(): 
    
    """A functini for executing the main program
    """

    # Demonstrating that the fuctions provide the same result for all the functions
    num_lst = [i for i in range(1,5)]
    print(std_builtin(num_lst) == std_loops(num_lst) == std_numpy(num_lst))
    
    
    

# ------------------------------------------ Main program ----------------------------------------------

main()
    


