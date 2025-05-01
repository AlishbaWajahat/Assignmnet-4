def get_list_of_ints():
    """
    Reads in integers until the user presses enter and returns the resulting list.
    """
    lst = []  # Make an empty list to store integers
    user_input = input("Enter an integer or press enter to stop: ")  # Get user input for an integer
    while user_input != "":  # While the user doesn't enter nothing...
        lst.append(int(user_input))  # Cast the user input into an integer and add it to our list
        user_input = input("Enter an integer or press enter to stop: ")  # Get the next user input

    return lst

def get_count(lst):
    count=0
    for num in lst:
        if num %2==0:
            count+=1
            
    print(f'Even numbers are {count}')


def main():
    lst=get_list_of_ints()
    count=get_count(lst)
    
if __name__ == '__main__':
    main()
    