import parse_str 
import view
import errors
import exp 

def init():
    number = view.inputer()
    number = parse_str.parse(number)
    if errors.errors(number)==True:
        number = exp.expression(number)
    view.printer(number)   

