#step 1: Declare two variables for number input and max int
#step 2: While number innput is positive 
#step 3: Ask for new input number 
#step 4: If input number is bigger than max int then that number input becomes max int
#step 5: When input number becomes negative, print out max-int

num_int=0
max_int = 0
while num_int >= 0:
    num_int = int(input("Input a number: ")) 

    if num_int > max_int:
        max_int = num_int

print("The maximum is", max_int)    # Do not change this line