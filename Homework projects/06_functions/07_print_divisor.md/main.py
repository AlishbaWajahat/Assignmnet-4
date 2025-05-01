def divisors(num):
    print(f'The divisors of {num} are:')
    for i in range(1,num+1):
        if num % i == 0:
           print(i)
           
           
def main():
    user_input:int=int(input('Enter a num: '))
    divisors(user_input)
        
        
if __name__ == '__main__':
    main()