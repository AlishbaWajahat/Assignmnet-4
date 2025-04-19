def main():
    fahrenheit : float=float(input('Enter temperature in Fahrenheit: '))
    degrees_celsius = ( fahrenheit- 32) * 5.0/9.0
    print(f'Temperature: {fahrenheit}F = {degrees_celsius}C')
    
if __name__ == '__main__':
    main()