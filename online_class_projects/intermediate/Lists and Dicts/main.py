# Problem #1: List Practice

fruits:list[str]=['apple','banana', 'orange', 'grape', 'pineapple']
print(len(fruits))

fruits.append('mango')
print(fruits)

# Problem #2: Index Game

numbers:list[int|str]=[1,2,3,4,'A']

# Accessing Elements:
def accessing(lst,indx):
    try:
        return lst[indx]
    except IndexError:
        return 'index is out of range'
     
# Modifying Elements:

def modifying(lst,indx,newValue):
    try: 
        lst[indx]=newValue
        return lst
    except IndexError:
        return 'index is out of range'


# Slicing the List:

def slicing(lst,indx,endIndx):
    try: 
        return lst[indx:endIndx]
    except IndexError:
        return 'index is out of range'


def index_game():
    lst = [1, 2, 3, 4, 5]  # Example list
    print("Current list:", lst)
    print("Choose an operation: access, modify, slice")
    operation = input("Enter operation: ")

    if operation == "access":
        index = int(input("Enter index to access: "))
        print(accessing(lst, index))
    elif operation == "modify":
        index = int(input("Enter index to modify: "))
        new_value = int(input("Enter new value: "))
        print(modifying(lst, index, new_value))
    elif operation == "slice":
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print(slicing(lst, start, end))
    else:
        print("Invalid operation.")

index_game()


