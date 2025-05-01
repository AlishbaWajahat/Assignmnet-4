def average(num1,num2):
    sum=num1+num2
    average=sum/2
    return sum
def main():
    num1:int=int(input('Enter first number: '))
    num2:int=int(input('Enter second number: '))
    print(f'The average is {average(num1,num2)}')
    
if __name__ == '__main__':
    main()
    
    