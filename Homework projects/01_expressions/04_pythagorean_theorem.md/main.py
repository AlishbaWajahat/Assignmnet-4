import math
def main():
    base : float =float(input('Enter the length of AC: '))
    perpendicular :float = float(input('Enter the length of BC: '))
    hypotenuse:float=math.sqrt(base**2 + perpendicular**2)
    print(f'The length of AB (the hypotenuse) is: {hypotenuse:.2f}')
    
if __name__ == '__main__':
    main()
    