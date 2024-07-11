# -*- coding: utf-8 -*-
"""CarterQ Math215 Lab12.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UHy_OaR0tLu8I1Y95oxlMpV8RbzRq9-1

#**Lab 12 - Gram-Schmidt and QR decompositions**

Enter your code in the spaces provided. Do not change any of the variable names or function names that are already provided for you. In places where we specify the name of the return value, make sure that your code produces the a value with the correct name.
"""

# Do not edit this cell.

LabID="Lab12"

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

#This function reads in two vectors and outputs a boolean variable describing whether the two vectors are orthogonal.

def orthogonal_check(a,b):
  cutoff = 1e-12
  if np.dot(a,b)<cutoff and np.dot(a,b) >= 0:
    return True
  else:
    return False

"""Check your function:"""

a = np.array([1,2,-1,4])
b = np.array([2,-2,-6,-1])

orthogonal_check(a,b)

"""**Problem 2**"""

# This function reads in a list of vectors and checks whether they form an orthogonal set. Orthcheck should be a Boolean value (True or False).

def orth_set_check(A):
  for i in range(1, len(A)):
   for j in range(0, len(A)):
    if (i != j and orthogonal_check(A[i], A[j]) == False):
        return False
  return True

"""Check your function:"""

p = [np.array([1,-1,0]),np.array([1,1,1]),np.array([0,1,-1])]
q = [np.array([1,0,0]),np.array([0,1,0]),np.array([0,0,1])]

orth_set_check(p)

"""**Problem 3**"""

# This function accepts a vector and returns a unit vector in the same direction.

def normalize(v):
  m = np.linalg.norm(v)
  return v/m

"""Check your function:"""

normalize(np.array([1,1,1,1]))

"""**Problem 4**"""

# This function accepts two vectors a and b and returns the projection of a onto b.

def proj(a,b):
  p = (np.dot(a,b) / np.dot(b,b))*b
  return p

"""Check your function:"""

a = np.array([1,4,1])
b = np.array([1,1,1])
proj(a,b)

"""**Problem 5**"""

# This function accepts a list of linearly independent vectors V, and produces a new list X of orthonormal vectors which span the same space as a the vector of V.

def gram_schmidt(V):
  X = V.copy()
  n = len(V)
  for i in range(1, n):
    for j in range(0, i):
      X[i] = X[i] - proj(V[i], X[j])
  for i in range(n):
    X[i] = normalize(X[i])
  return X

"""Check your function:"""

L=[np.array([1,3,2,4,0]),np.array([-1,0,4,5,0]),np.array([0,2,2,2,2]),np.array([3,2,3,2,0])]
A=gram_schmidt(L)
print(orth_set_check(A))
A

"""**Problem 6**"""

# This function accepts a matrix A as a 2D NumPy Array, and returns two new matrices Q and R.

def QR_decomposition(A):
  B = np.transpose(A)
  Q = np.transpose(gram_schmidt(B))
  R = np.dot(np.transpose(Q), A)
  return Q, R

"""Check your function:"""

A=np.transpose(np.array([[1,3,2,4,0],[-1,0,4,5,0],[0,2,2,2,2],[3,2,3,2,0]]))
np.shape(A)[1]
Q,R=QR_decomposition(A)

print(Q)
print(R)

"""We can check to see if QR=A, after rounding with the following command:"""

np.round(np.matmul(Q,R))

"""**Problem 7**"""

# This Function was created in Lab 5.  It accepts an upper triangular square matrix U and a vector b, solves Ux=b for x.  You may use it in the function QR_solver.

def back_substitution(U,b): 
  n = len(b)
  x = np.array([0.0 for i in range(n)])
  for i in range(n - 1,-1, -1):
    r=(b[i]-sum([x[j]*U[i][j] for j in range(i + 1,n)]))/U[i][i]
    x[i] = r
  return x

# This function accepts an invertible matrix A and a vector b, solves Ax=b for x.

def QR_solver(A,b):
  Q,R = QR_decomposition(A)
  Z = np.transpose(Q)@b
  return back_substitution(R,Z)

A=np.array([[3,1,-2],[1.5,2,-5],[2,-4,1]])
b=np.array([1.1,3,-2])
QR_solver(A,b)

"""**STOP!  BEFORE YOU SUBMIT THIS LAB:**  Go to the "Runtime" menu at the top of this page, and select "Restart and run all".  If any of the cells produce error messages, you will either need to fix the error(s) or delete the code that is causing the error(s).  Then use "Restart and run all" again to see if there are any new errors.  Repeat this until no new error messages show up.

**You are not ready to submit until you are able to select "Restart and run all" without any new error messages showing up.  Your code will not be able to be graded if there are any error messages.**

To submit your lab for grading you must first download it to your compute as .py file. In the "File" menu select "Download .py". The resulting file can then be uploaded to http://www.math.byu.edu:30000 for grading.
"""