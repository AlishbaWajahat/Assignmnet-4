def add_number(list:list[int])->int:
    sum:int=0
    for num in list:
        sum+=num
    return sum

def main():
    number:list[int]=[1,2,3,4,5,5]
    sum=add_number(number)
    print(sum)
    
if __name__ == '__main__':
    main()
    
    
        