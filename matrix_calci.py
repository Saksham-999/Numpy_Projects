import numpy as np
#user input for matrix
def get_matrix():
    rows=int(input("enter no of rows"))
    columns=int(input("enter no of column"))
    lmatrix=[]
    for i in range(rows):
        
        row=list(map(int,input(f"enter row {i+1} elements seperated by space").split()))
        #check
        while (len(row) != columns):
            print("column size and number of row elements donot match")
            row=list(map(int,input(f"enter row {i+1} elements seperated by space").split()))
        lmatrix.append(row)
    matrix=np.matrix(lmatrix,dtype=int)
    return matrix

def deter(A):
      if(A.shape[0]==A.shape[1]):
         return(np.linalg.det(A))
      else:
          print("matrix must be square matrix for further calculation")
      
   
def menu():
    print("\nMatrix Calculator")
    print("1. Add Matrices")
    print("2. Subtract Matrices")
    print("3. Multiply Matrices")
    print("4. Transpose Matrix")
    print("5. Inverse Matrix")
    print("6. Determinant of Matrix")
    print("7. Exit")
    choice = input("Choose an operation (1-7): ")
    return choice

while True:
    choice=menu()

    if choice == '1':
      #add
      A=get_matrix()
      B=get_matrix()
      if(A.shape==B.shape):
          print("sum is:")
          print(A+B)
      else:
          print("matrix must have same shape to add")

    elif choice == '2':
      #subtract
      A=get_matrix()
      B=get_matrix()
      if(A.shape==B.shape):
          print("difference is:")
          print(A-B)
      else:
          print("matrix must have same shape to subtract")

    elif choice == '3':
      #multiply
      A=get_matrix()
      B=get_matrix()
      if(A.shape[1]==B.shape[0]):
          print("sum is:")
          print(A*B)
      else:
          print("number of column of 1st matrix must be equal to no of row of 2nd matrix to multiply")

    elif choice == '4':
      #transpose
      A=get_matrix()
      print("Transpose : ")
      print(np.transpose(A))

    elif choice == '5': 
      #inverse 
      A=get_matrix()
      if(deter(A)!=0):
         print("Inverse : ")
         print(np.linalg.inv(A))
      else:
           print("determinant of matrix shouldnot be equal to 0 for inverse to exists")   

    elif choice == '6': 
      #determinant 
      A=get_matrix()
      print("Determinant :",deter(A))

     
    elif choice == '7':
       print("-------Exiting----------")
       break

    else:
       print("Invalid option")

