#step 1: Declare innput value for lenght of sequence
#step 2: print out first three numbers in sequence(1,2,3)
#step 4: Get the next sequence number with the sum of the previous 3 numbers. 
#step 5: Print that number out and continue to the lenght of the sequence. 

n = int(input("Enter the length of the sequence: ")) # Do not change this line
n1=1                                       
n2=2    
n3=3                                    
print(n1, n2, n3, sep='\n')
for i in range(3,n):
    next=n1+n2+n3                      
    print(next)
    n1=n2
    n2=n3
    n3=next