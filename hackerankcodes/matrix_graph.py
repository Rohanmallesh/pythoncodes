# this program to implement the graph using matrix representation
import numpy as np

def graph(no_verteces):
   mat = np.zeros(no_verteces,no_verteces)
   return mat

def add_edge(mat,v1,v2,directed=True):
    mat = mat[[v1,v2]]=1
    
    
class roh:
   def __init__(yes,fname,lname,age):
      yes.fname = fname
      yes.lname = lname
      yes.age = age
      
r = roh('rohan','mallesh',20)
o = roh('pruthvi','thiru',40)