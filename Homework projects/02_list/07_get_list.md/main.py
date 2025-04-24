def main():
    lst=[]
    user_input:str=input('Enter a value or press enter to print your list. ')
    while user_input != "":
        lst.append(user_input)
        user_input:str=input('Enter a value or press enter to print your list. ')
    print(lst)
    
if __name__ == '__main__':
    main()
    