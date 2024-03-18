
def errors(num_list) ->bool: 
    status = True
    for i in range(len(num_list)):
        if num_list[i].isdigit() == False and num_list[i]  not in '/*-+':
            print('error_type')
            status = False
    for i in range(len(num_list)-1):        
        if num_list[i] in '/*-+' and num_list[i+1] in '/*-+':
            print('error_double_sign')
            status = False
    if num_list[-1] in '/*-+' or num_list[0] in '/*-+':
        print('error_start_end')
        status = False
    for i in range(len(num_list)-1):
        if num_list[i] == '/' and num_list[i+1] == '0':
            print("error_zero_div")
            status = False
    return status
    
