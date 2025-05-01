def in_range(n:int,low:int,high:int):
    return low <= n <= high

def main():
    try:
        n: int = int(input('Enter number: '))
        low: int = int(input('Enter lowest number: '))
        high: int = int(input('Enter highest number: '))

        if high < low:
            raise ValueError("Highest number must be greater than or equal to lowest number.")

        print(in_range(n, low, high))
    except ValueError as e:
        print("Error:", e)
    
if __name__ == '__main__':
    main()
