memory = 0
msg = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
"Are you sure? It is only one digit! (y / n)",
"Don't be silly! It's just one number! Add to the memory? (y / n)",
"Last chance! Do you really want to embarrass yourself? (y / n)" ]
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
def is_one_digit(v):
    v = float(v)
    if -10 < v < 10 and v == int(v):
        return True
    else:
        return False
def check(v1,v2,v3):
    msg = ''
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg = msg + msg_7
    if (v1==0 or v2==0) and (v3== '*' or v3=='+' or v3== '-'):
        msg=msg+msg_8
    if msg!= '':
        msg=msg_9 + msg
    print(msg)
while True:
    print("Enter an equation")
    try:
        x, oper, y = input().split(" ")
        if x == 'M':
            x = memory
        if y == 'M':
            y = memory
        x = float(x)
        y = float(y)
    except ValueError:
        print("Do you even know what numbers are? Stay focused!")
        continue

    if oper == '+' or oper == '-' or oper == '*' or oper == '/':
        pass
    else:
        print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
        continue
    check(x,y,oper) 
    if oper == '+':
        result = x + y
    elif oper == '-':
        result = x - y
    elif oper == '*':
        result = x * y
    elif oper == '/' and y != 0:
        result = x / y
    else:
        print("Yeah... division by zero. Smart move...")
        continue
    print(result)
    print("Do you want to store the result? (y / n):")
    store = input()
    if store == 'y':
        if is_one_digit(result):
            msg_index = 10
            while True:
                print(msg[msg_index])
                answer = input()
                if answer == 'y':
                    if msg_index < 12:
                        msg_index += 1
                        
                    elif msg_index >= 12:
                        memory = result
                        break
                    
                elif answer == 'n':
                    break
            
        elif is_one_digit(result) == False:
            memory = result
                
    if store == 'n':
        pass
    print("Do you want to continue calculations? (y / n):")
    cal_again = input()
    if cal_again == 'y':
        continue
    break
