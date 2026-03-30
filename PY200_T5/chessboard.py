''' Print an N x N grid: • If (row+col) is even → print 1 • else → print 0 But if row == col → print X instead.'''

#Taking input in a integer format
N = int(input("Enter value of N: "))

#loop for rows 
for row in range(N):
    #loop for columns

    for col in range(N):
    #check if row and column are equal, if yes print X
        if row == col:
            print("X", end=" ")    
        elif (row + col) % 2 == 0:      
            print(1, end=" ")           
        else:                        
            print(0, end=" ")         
    print()      #for new line after each row