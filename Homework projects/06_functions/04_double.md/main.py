def double(num):
    doubling=num*2
    print(f'Double that is {doubling}')
    
def main():
    user_num:int=int(input('Enter a num: '))
    double(user_num)
    
if __name__=='__main__':
    main()