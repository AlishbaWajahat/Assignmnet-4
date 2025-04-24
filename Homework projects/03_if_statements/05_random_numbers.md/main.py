import random
def main():
    r=(' ').join([str(random.randint(1,100)) for _ in range(10)])
    print(r)

    
if __name__ == '__main__':
    main() 