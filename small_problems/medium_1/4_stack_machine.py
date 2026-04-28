
stack = []
register = 0

def minilang(command_str):
    current_command_list = command_str.split()
    global register
    operation = None
    while current_command_list:
        try: register = int(current_command_list[0])
        except ValueError:
            operation = current_command_list[0]
        if operation:
            perform(operation)
            operation = None
        current_command_list.pop(0)
    
def perform(operation):
    global register
    global stack
    match operation: 
        case "PUSH":
            stack.append(register)
        case "ADD":
            register = register + stack.pop()
        case "SUB":
            register = register - stack.pop()
        case "MULT":
            register = register * stack.pop()
        case "DIV":
            register = register // stack.pop()
        case "REMAINDER":
            register = register % stack.pop()
        case "POP":
            register = stack.pop()
        case "PRINT":
            print(register)


### Test Cases!
minilang('PRINT')
# 0

minilang('5 PUSH 3 MULT PRINT')
# 15

minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# 5
# 3
# 8

minilang('5 PUSH POP PRINT')
# 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# 5
# 10
# 4
# 7

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# 6

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12

minilang('-3 PUSH 5 SUB PRINT')
# 8

minilang('6 PUSH')
# (nothing is printed)