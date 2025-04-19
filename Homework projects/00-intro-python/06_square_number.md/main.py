def main():
    number : float =float(input('Type a number to see its square: '))
    squared:float=number ** 2
    print(f'{number} squared is {squared}')
    
if __name__ == '__main__':
    main()