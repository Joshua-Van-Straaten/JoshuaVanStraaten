#Calculates the sum of any parsed factorial's digits

#import libraries
import numpy as np                                            #Numpy library for math operations
import argparse                                               

parser = argparse.ArgumentParser(description='Calculate sum of factorial digits')
parser.add_argument('number', type=int, help='Number to find factorial of')
args = parser.parse_args()

def sum_func(number):                                         

    sum_of_digits = 0                                         #initialise variable to store sum of factorial digits
    fact = np.math.factorial(number)                          #finding factorial of parsed input

    while fact > 0:                                           #sum each digit of factorial
        sum_of_digits += fact % 10                             #adds the last digit of the factorial to sum_of_digits
        fact //= 10                                            #Rounds the factorial down to the nearest int after dividing by 10
    
    return sum_of_digits

if __name__ == '__main__':                                   
    print (sum_func(args.number))                             #output
