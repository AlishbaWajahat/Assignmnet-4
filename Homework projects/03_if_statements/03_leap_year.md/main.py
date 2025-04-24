def main():
    user_input:int=int(input('Enter a year'))
    if (user_input%4==0) and (user_input% 100!=0 or user_input % 400==0 ):
        print('It\'s a leap year')
    else:
        print('It\'s  not a leap year')
        
      
if __name__ == '__main__':
    main()     