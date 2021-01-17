"""
Write a program that prints the numbers from 1 to 100.

But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".

For numbers which are multiples of both three and five print "FizzBuzz".
Instead of only printing "fizz", "buzz", and "fizzbuzz", add a fourth print statement: "prime". You should print this whenever you encounter a number that is prime (divisible only by itself and one). As you implement this, don't worry about the efficiency of the algorithm you use to check for primes. It's okay for it to be slow.

"""

number=1

def GenerateFizBuzz(number):
    while (number<=100):
        if number%3==0 and number%5==0:
            print("FizzBuzz")
            #continue
        elif number%3==0:
            print("Fizz")
            #continue
        elif number%5==0:
            print("Buzz")
            #continue
        elif number%number==0 and number%1==0:
            print("prime")
        else:
            print(number)
            #continue
        number=number+1
        
        

GenerateFizBuzz(number)
    


