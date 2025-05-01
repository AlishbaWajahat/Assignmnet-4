def print_ones(digit):
    ones=digit%10
    print(f'The ones digit is {ones}')
    
def main():
    num = int(input("Enter a number: "))
    print_ones(num)
    
if __name__ == '__main__': main()
    