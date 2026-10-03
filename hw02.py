# Name: Sophia Bernal 
# Task 1.1:
#  Complete the function "read_two_ints" below:
def read_two_ints():
    """
    take two numbers and return the given numbers
    
        Returns:
            x (int): An integer
            y (int): Another integer
    """
    # the return shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    # collect user input for x 
    x = int(input("give me x: "))
    # collect user inpute for y
    y = int(input("give me y: "))
    return x,y


    

# Task 2.1:
#  Complete the function "compute_multadd" below:
def compute_multadd(a, b):
    """Find the product and sum of two numbers, return the result of the product divided by the sum
        
            Args:
                a (int): An integer
                b (int): Another integer
            
            Returns:
                mult_result/add_result: The result of the product of a and b divided by the sum of a and b
    """
    # ADD a Docstring for this function
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    # Save the product of a*b in the variable mult_result 
    mult_result= a*b
    # print the result of a*b 
    print("mult result:",mult_result)
    # Save the sum of a+b in the variable add_result
    add_result= a+b
    # print the result of a+b
    print("add result:",add_result)
    # return the result of (a*b)/(a+b)
    return mult_result/add_result
  
# Task 3.1:
#  Complete the function "print_fancy" below:
def print_fancy(a, b, ab_multadd):
    """Creates a series of print statements using the given variables"""
    # ADD a Docstring for this function
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    print("****************")
    # print the user input for x and y and the result of (a*b)/(a+b) 
    print("RESULTS:")
    print("first number:",a)
    print("second number:",b)
    print("multadd result:",ab_multadd)
    print("================")

def main ():
    """Calls the read_two_ints function then the compute_multadd function and finally print_fancy function"""
    # ADD a Docstring for this function
    # Task 1.2:
    #  Add one line below to call read_two_ints (note that it returns two values)
    #  the call should provide no arguments
    #  store the returned values into two variables: x and y
    
    
    
# Call the read_two_ints function and assigns the outputs to x and y
    x, y= read_two_ints()

    # Task 2.2:
    #  Add one line below to call multadd (note that it returns one value)
    #  the call should provide the arguments x, and y you obtained above;
    #  store the returned value in a variable called xy_multadd
# Call the compute_multadd function with the arguments x and y
    xy_multadd= compute_multadd(x, y)

    # Task 3.2:
    #  Complete The line below to call print_fancy
    #  the call should provide the arguments x, y, and xy_multadd you obtained above;
# Call the print_fancy with the arguments x, y, and xy_multadd 
    print_fancy(x, y, xy_multadd)


    # Do not modify this final print statement
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
