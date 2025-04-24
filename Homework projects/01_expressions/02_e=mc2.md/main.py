def main():
    C : float =  299792458
    mass : float = float(input('Enter kilos of mass: '))
    energy : float = mass*(C**2)
    print(f'{mass}kg is equivalent to {energy:,.0f} joules of energy')
    
if __name__ == '__main__':
    main()