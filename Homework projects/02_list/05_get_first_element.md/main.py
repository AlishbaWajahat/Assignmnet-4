def get_first_element(lst):
    print(lst[0]) 

def main():
    lst=[]
    user_input:str=input('Please enter an element of the list or press enter to stop. ')
    while user_input != "":
        lst.append(user_input)
        user_input:str=input('Please enter an element of the list or press enter to stop. ')
        
    get_first_element(lst)

if __name__ == '__main__':
    main()


    