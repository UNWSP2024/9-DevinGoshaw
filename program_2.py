# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).

#programmer: Devin Goshaw
#Date:10/30/25
#program: random number program
import random

def main():
    numOfNumbers=int(input("how many random numbers do you want to generate (1000 number max): "))

    if numOfNumbers<1 or numOfNumbers>1000:
        print('enter a number between 1-1000')
        return
    with open("randomNumbers.txt",  "w") as file:
        for _ in range(numOfNumbers):
            number=random.randint(1,500)
            file.write(str(number) + "/n")
    
    print(numOfNumbers,'random numbers have been added to the file' )

if __name__=="__main__":
    main()



























