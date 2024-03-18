def inputer():
    text = input('Input expression: ')
    return text

def printer(num:float):
        if str(type(num)) == "<class 'float'>":
            print(f'The answer is {num}')
        
