# -*- coding: utf-8 -*-
"""CarterQ Math215 Lab4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y31ZvBH_ybI2ssBXEj4SKeWmMT-YeWGY

#**Lab 4 - Iterative methods for solving systems of linear equations**

Enter your code in the spaces provided. Do not change any of the variable names or function names that are already provided for you. In places where we specify the name of the return value, make sure that your code produces the a value with the correct name.
"""

# Do not edit this cell.

LabID="Lab4"

try:
  from graderHelp import ISGRADEPLOT
except ImportError:
  ISGRADEPLOT = True

"""**Enter your name, section number, and BYU NetID**"""

# Enter your first and last names in between the quotation marks.

first_name="Carter"

last_name="Quesenberry"

# Enter your Math 215 section number in between the quotation marks. 

section_number="001"  

# Enter your BYU NetID in between the quotation marks.  NOT YOUR BYU ID NUMBER!

BYUNetID="carterqb"

"""**Problem 1**"""

# Replace the values of 0 with the values you solved for in Problem 1.

x_val=1   

y_val=1

"""**Problem 2**"""

# Performs one iteration of the Jacobi method for system (1) applied to the point (x,y).

def jacobi1_iteration(x,y): 
    new_x = 1/7*(6+y)
    new_y = 1/5*(x+4)
    
    list1=[new_x, new_y]
    return list1

jacobi1_iteration(3,5)

"""**Problem 3**"""

# Performs n iterations of the Jacobi method on system (1) with starting estimate (0,0).

def jacobi1_method(n):
    x_n=0
    y_n=0
    list2 = [x_n,y_n]
    for i in range(n): 
      list2 = jacobi1_iteration(x_n,y_n)
      x_n = list2[0]
      y_n = list2[1]
    return list2

jacobi1_method(2)

"""**Problem 4**"""

# Replace the values of 0 with the values you solved for in Problem 4.

n_var1=1    #FIXME might be 0

n_var2=2

"""**Problem 5**"""

# Performs one iteration of the Gauss-Seidel method for system (1) applied to the point (x,y).

def gs1_iteration(x,y): 
    new_x = 1/7*(6+y)
    new_y = 1/5*(new_x+4)
    
    list3=[new_x, new_y]
    return list3

gs1_iteration(3,5)

"""**Problem 6**"""

# Performs n iterations of the Gauss-Seidel method on system (1) with starting estimate (0,0).

def gs1_method(n): 
    x_n=0
    y_n=0
    list4 = [x_n,y_n]
    for i in range(n): 
      list4 = gs1_iteration(x_n,y_n)
      x_n = list4[0]
      y_n = list4[1]
    return list4

gs1_method(4)

"""**Problem 7**"""

# Replace the values of 0 with the values you solved for in Problem 7.

n_var3=2    

n_var4=4

"""**Problem 8**"""

import numpy as np

# Finds the error of the nth approximation of the solution to system (1) using the Gauss-Seidel method.

def gs1_error(n): 
    list5 = gs1_method(n)
    list6 = [x_val,y_val]
    error = np.linalg.norm(np.array(list6)-np.array(list5))
    return error

gs1_error(3)

# The following code will construct your plot of gs1_error for you.  You don't need to change anything in this cell, simply execute it. Consider this one a freebie.

# Note that you must have a function defined called gs1_error from the previous problem in order for the plot to be created.  We first import matplotlib.pyplot:

import matplotlib.pyplot as plt



# This command uses the function gs1_error to create a new function vect_gs1_error which will accept NumPy arrays of various sizes as input, instead of just a single number.

vect_gs1_error=np.vectorize(gs1_error)  



# This creates a NumPy array of values of the form [0,1,2,...,48,49], similar to the np.linspace command.  The 1 in the function tells NumPy to count up by ones.

n_vals=np.arange(0,50,1)



# This creates the plot, and labels the axes.  See if you can determine what each command is doing.

plt.title('Error of the Gauss-Seidel Method Applied to System 1')
plt.xlabel('Number of iterations')
plt.ylabel('Error')
plt.plot(n_vals,vect_gs1_error(n_vals),'ro')
plt.show()

"""**Problem 9**"""

# Gives one iteration of the Gauss-Seidel method for system (4) applied to the point (x,y).

def gs2_iteration(x,y): 
    new_x = y + 1
    new_y = (-2*new_x) +5
    
    list7=[new_x, new_y]
    return list7
  
# Performs n iterations of the Gauss-Seidel method on system (4) with starting estimate (0,0).

def gs2_method(n): 
    x_n=0
    y_n=0
    list8 = [x_n,y_n]
    for i in range(n): 
      list8 = gs2_iteration(x_n,y_n)
      x_n = list8[0]
      y_n = list8[1]
    return list8
  
# Finds the error of the nth approximation of the solution to system (4) using the Gauss-Seidel method.

def gs2_error(n): 
    list9 = gs2_method(n)
    list10 = [x_val,y_val]
    error = np.linalg.norm(np.array(list10)-np.array(list9))
    return error

gs2_method(5)

# The following code will construct your plot of gs2_error for you.  You don't need to change anything in this cell, simply execute it. Consider this one another freebie.

# Note again that you must have a function defined called gs2_error from the previous problem in order for the plot to be created.

vect_gs2_error=np.vectorize(gs2_error)  

n_vals=np.arange(0,50,1)

plt.title('Error of the Gauss-Seidel Method Applied to System 4')
plt.xlabel('Number of iterations')
plt.ylabel('Error')
plt.plot(n_vals,vect_gs2_error(n_vals),'ro')
plt.show()

gs2_error(3)

"""**Problem 10**"""

# Gives one iteration of the Gauss-Seidel method for the final system, applied to the point (x,y,z).

def gs3_iteration(x,y,z): 
    new_x = -1/5*(-2*y + 3*z +8)
    new_y = -1/4*(new_x - 4*z - 102)
    new_z = -1/4*(-2*new_x - 2*new_y +90)
    
    list11=[new_x, new_y, new_z]
    return list11

  
# Performs n iterations of the Gauss-Seidel method on the final system with starting estimate (0,0,0).

def gs3_method(n): 
    x_n=0
    y_n=0
    z_n=0
    list12 = [x_n,y_n,z_n]
    for i in range(n): 
      list12 = gs3_iteration(x_n,y_n,z_n)
      x_n = list12[0]
      y_n = list12[1]
      z_n = list12[2]
    return list12

gs3_method(4)

"""**STOP!  BEFORE YOU SUBMIT THIS LAB:**  Go to the "Runtime" menu at the top of this page, and select "Restart and run all".  If any of the cells produce error messages, you will either need to fix the error(s) or delete the code that is causing the error(s).  Then use "Restart and run all" again to see if there are any new errors.  Repeat this until no new error messages show up.

**You are not ready to submit until you are able to select "Restart and run all" without any new error messages showing up.  Your code will not be able to be graded if there are any error messages.**

To submit your lab for grading you must first download it to your compute as .py file. In the "File" menu select "Download .py". The resulting file can then be uploaded to http://www.math.byu.edu:30000 for grading.
"""