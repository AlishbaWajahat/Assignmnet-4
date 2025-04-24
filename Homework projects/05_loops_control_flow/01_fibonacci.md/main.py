MAX_LENGTH :int=10000
def main():
    current_value:int=0
    next_value:int=1
    lst=[]
    while current_value<=MAX_LENGTH:
        lst.append(current_value)
        value_after_next=current_value+next_value
        current_value=next_value
        next_value=value_after_next
    joined=(' ').join(str(num) for num in lst)
    print(joined)
if __name__ == '__main__':
    main()