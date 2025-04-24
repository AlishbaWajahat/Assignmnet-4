# def double(number:list[int])->list[int]:
#     doubling_lis:list[int]=[x*2 for x in number]
#     return doubling_lis

# def main():
#     number:list[int]=[2,4,6,8,10]
#     doubles:list[int]=double(number)
#     print(doubles)


def main():
    number:list[int]=[2,4,6,8,10]
    for i in range(len(number)):
        number[i]=number[i]*2
        
    print(number)
    
    
if __name__ == '__main__':
    main()