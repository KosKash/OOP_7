
def parse(num:str) ->list:    
    num = num.replace(' ', '')
    num = num.replace('+', ' + ')
    num = num.replace('-',' - ') 
    num = num.replace('*', ' * ')
    num = num.replace('/', ' / ')
    num = num.split()
    return num