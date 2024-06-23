#Here's a trivial example: Suppose you're iterating over a list. You need to iterate over 20 numbers, 
#but the list is made from user input, and might not have 20 numbers in it. After you reach the end of the list, 
#you just want the rest of the numbers to be interpreted as a 0. Here's how you could do that:
def do_stuff_with_number(n):
    print(n)

def catch_this():
    the_list = (1, 2, 3, 4, 5)

    for i in range(20):
        try:
            do_stuff_with_number(the_list[i])
        except IndexError: # Raised when accessing a non-existing index of a list
            do_stuff_with_number(0)

catch_this()


----


# Setup
actor = {"name": "John Cleese", "rank": "awesome"}

# Function to modify!!!
def get_last_name(): 
    return actor["name"].split()[1]
    

# Test code
get_last_name()
print("All exceptions caught! Good job!")
print("The actor's last name is %s" % get_last_name())
