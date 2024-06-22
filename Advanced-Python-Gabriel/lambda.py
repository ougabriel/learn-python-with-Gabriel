# normal function

def sum(a,b):
    return a + b

a = 1
b = 2
c = sum(a,b)
print(c)

# using a LAMBDA function

a = 1
b = 2
sum = lambda x,y : x + y
c = sum(a,b)
print(c)

# They don't need to have a name, so they also called anonymous functions. just define the lambda function using the keyword lambda.


#Write a program using lambda functions to check if a number in the given list is odd. Print "True" if the number is odd or "False" if not for each element.

l = [2,4,7,3,14,19]
for i in l:
    # your code here
    my_lambda = lambda x : (x % 2) == 1
    print(my_lambda(i))
