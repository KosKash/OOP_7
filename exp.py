def expression(num:list) ->float:
    for i in range(len(num)):
        if num[i].isdigit() == True:
            num[i] = float(num[i])
    while ('*' not in num and  '/' not in num) == False:
            for i in range(len(num)):
                if num[i] == '*'  or num[i] == '/':
                    if num[i] == '*':
                        res = float(num[i - 1]) * float(num[i + 1])
                    if num[i] == '/':
                        res = float(num[i - 1]) / float(num[i + 1])
                    num[i] = res
                    num.pop(i+1) 
                    num.pop(i-1)
                    break
    while ('+' not in num and '-' not in num) == False:
            for i in range(len(num)):
                if num[i] == '+'  or num[i] == '-':
                    if num[i] == '+':
                        res = float(num[i - 1]) + float(num[i + 1])
                    if num[i] == '-':
                        res = num[i - 1] - num[i + 1]
                    num[i] = res
                    num.pop(i+1) 
                    num.pop(i-1)
                    break
    num = float(*num)        
    return num

