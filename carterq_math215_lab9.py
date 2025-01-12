# -*- coding: utf-8 -*-
"""CarterQ Math215 Lab9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RPmnEq8kR-PBelHWeKxvuX2oxWv6E6DD

#**Lab 9 - Iterative eigenvalues and Markov chains**

Enter your code in the spaces provided. Do not change any of the variable names or function names that are already provided for you. In places where we specify the name of the return value, make sure that your code produces the a value with the correct name.
"""

# Do not edit this cell.

LabID="Lab9"

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

"""**Import NumPy**"""

import numpy as np

"""**Problem 1**"""

def evect_approx1(x_0,k):
  A = np.array([[1,1],[2,0]])
  for i in range(k):
    x_0 = A@x_0
  return x_0

evect_approx1([1,9],10)

"""**Problem 2**"""

def eval_approx1(x_0,k):
  x_j = x_0
  x_0 = evect_approx1(x_0,k)
  x_j = evect_approx1(x_j,k + 1)
  de = x_j[0] / x_0[0]
  return de

eval_approx1(np.array([1,9]),10)

"""**Problem 3**"""

def norm_evect_approx1(x_0,k):
  A = np.array([[1,1],[2,0]])
  for i in range(k):
    w_j = A@x_0
    x_j = x_0
    x_0 = w_j / np.linalg.norm(w_j)
  val = w_j[0] / x_j[0]
  return x_0, val

norm_evect_approx1(np.array([1,9]),10)

"""**Problem 4**"""

def norm_approx_gen(M,x_0,k):
  A = np.array([[1,1],[2,0]])
  for i in range(k):
    w_j = M@x_0
    x_j = x_0
    x_0 = w_j / np.max(np.abs(w_j))
  val = w_j[0] / x_j[0]
  return x_0, val

norm_approx_gen(np.array([[2,4,6],[4,8,0],[1,2,9]]), np.array([1,5,-1]), 10)

"""**Problem 5**"""

def ray_quotient(M,x_0,k):
  x = norm_approx_gen(M,x_0,k)[0]
  rq = ((M@x)@x) / (x@x)
  return rq

ray_quotient(np.array([[2,4,6],[4,8,0],[1,2,9]]), np.array([1,5,-1]), 10)

"""**Problem 6**"""

y = np.array([[3,2,-2],[-1,1,4],[3,2,-5]])
y1 = np.array([1,1,1])

x_vect_3 = norm_approx_gen(y, y1, 3)[0]

x_vect_4 = norm_approx_gen(y, y1, 4)[0]

"""**Problem 7**"""

def subscriber_vals(x_0,k):
  P = np.array([[0.7, 0.2],[0.3, 0.8]])
  for i in range(k):
    x_0 = P@x_0
  return x_0

subscriber_vals(np.array([95,102]),10)

"""**Problem 8**"""

netflix_subs6 = subscriber_vals(np.array([0.6, 0.4]), 6)[1]

"""**Problem 9**"""

trans_matrix = np.array([[0.8, 0.5, 0.3, 0.2], [0.05, 0.2, 0.1, 0.1], [0.1, 0.1, 0.3, 0.1], [0.05, 0.2, 0.3, 0.6]])

"""**STOP!  BEFORE YOU SUBMIT THIS LAB:**  Go to the "Runtime" menu at the top of this page, and select "Restart and run all".  If any of the cells produce error messages, you will either need to fix the error(s) or delete the code that is causing the error(s).  Then use "Restart and run all" again to see if there are any new errors.  Repeat this until no new error messages show up.

**You are not ready to submit until you are able to select "Restart and run all" without any new error messages showing up.  Your code will not be able to be graded if there are any error messages.**

To submit your lab for grading you must first download it to your compute as .py file. In the "File" menu select "Download .py". The resulting file can then be uploaded to http://www.math.byu.edu:30000 for grading.
"""