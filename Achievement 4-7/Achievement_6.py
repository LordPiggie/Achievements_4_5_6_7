#This program takes a list of numbers from the user and seperates them into prime and non prime numbers. 

def primeNumber(): #This funtion checks to see if a number is larger than 1, and if it is divisible by more than itself and one.

    for input in inputList:
    
        if input > 1:
            
            for i in range(2, input):

                if (input % i) == 0:

                    nonPrimeList.append(input)

                    break

            else:

                primeList.append(input)

        else:

            nonPrimeList.append(input)

sep = ',' #This is for the future lists, so that they can be sperated by a comma

primeList = [] #An empty list which is filled with the prime numbers by the function

nonPrimeList = [] #An empty list which is filled with non Prime numbers by the function

input = input('Hello\n\nThis program takes a series of numbers seperated by a comma and gives a seperate output for prime and non prime numbers\n\nPlease input a string of numbers seperated only by a comma\ni.e. [1,2,3,4,5]: ')

inputList = input.split(',') #This splits the input and creates a list from the user input so that the program can interperet the information

inputList = list(map(int, inputList)) #This changes the lists type to int

primeNumber() #calling the function

print('The prime numbers are ', sep.join(map(str, primeList))) #This is where we print the lists and add modifyers so it prints in the desired format

print('The non prime numbers are ', sep.join(map(str, nonPrimeList)))