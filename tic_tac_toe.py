a = '         '
p = 0
print('---------')
print('|', a[0], a[1], a[2], '|')
print('|', a[3], a[4], a[5], '|')
print('|', a[6], a[7], a[8], '|')
print('---------')
while True:
    tracker = 'L'
    if p % 2 == 0:
        tracker = 'X'
    elif p % 2 == 1:
        tracker = 'O'
    try:
        user = input()
        if len(user) <= 1:
            print('Invalid input kid')
            continue
        if user.isalpha():
            print('You should enter numbers!')
            continue
        h, i = user.split(" ")
        if int(h) >= 4 or int(h) <= 0:
            print('Coordinates should be from 1 to 3!')
            continue
        if int(i) >= 4 or int(i) <= 0:
            print('Coordinates should be from 1 to 3!')
            continue
        if user == '1 1':
            if 'X' == a[0]:
                print('This cell is occupied! Choose another one!')
                continue
            if 'O' == a[0]:
                print('This cell is occupied! Choose another one!')
                continue
            a = a[:0] + tracker + a[0+1:]
            print('---------')
            print('|', a[0], a[1], a[2], '|')
            print('|', a[3], a[4], a[5], '|')
            print('|', a[6], a[7], a[8], '|')
            print('---------')
            p += 1
        if user == '1 2':
            if 'X' == a[1]:
                print('This cell is occupied! Choose another one!')
                continue
            if 'O' == a[1]:
                print('This cell is occupied! Choose another one!')
                continue
            a = a[:1] + tracker + a[1+1:]
            print('---------')
            print('|', a[0], a[1], a[2], '|')
            print('|', a[3], a[4], a[5], '|')
            print('|', a[6], a[7], a[8], '|')
            print('---------')
            p += 1
        if user == '1 3':
            if 'X'== a[2]:
                print('This cell is occupied! Choose another one!')
                continue
            if 'O' == a[2]:
                print('This cell is occupied! Choose another one!')
                continue
            a = a[:2] + tracker + a[2+1:]
            print('---------')
            print('|', a[0], a[1], a[2], '|')
            print('|', a[3], a[4], a[5], '|')
            print('|', a[6], a[7], a[8], '|')
            print('---------')
            p += 1
        if user == '2 1':
            if 'X' == a[3]:
                print('This cell is occupied! Choose another one!')
                continue
            if 'O' == a[3]:
                print('This cell is occupied! Choose another one!')
                continue
            a = a[:3] + tracker + a[3+1:]
            print('---------')
            print('|', a[0], a[1], a[2], '|')
            print('|', a[3], a[4], a[5], '|')
            print('|', a[6], a[7], a[8], '|')
            p += 1
            print('---------')
        if user == '2 2':
            if 'X' == a[4]:
                print('This cell is occupied! Choose another one!')
                continue
            if 'O' == a[4]:
                print('This cell is occupied! Choose another one!')
                continue
            a = a[:4] + tracker + a[4+1:]
            print('---------')
            print('|', a[0], a[1], a[2], '|')
            print('|', a[3], a[4], a[5], '|')
            print('|', a[6], a[7], a[8], '|')
            print('---------')
            p += 1
        if user == '2 3':
            if 'X' == a[5]:
                print('This cell is occupied! Choose another one!')
                continue
            if 'O' == a[5]:
                print('This cell is occupied! Choose another one!')
                continue
            a = a[:5] + tracker + a[5+1:]
            print('---------')
            print('|', a[0], a[1], a[2], '|')
            print('|', a[3], a[4], a[5], '|')
            print('|', a[6], a[7], a[8], '|')
            print('---------')
            p += 1
        if user == '3 1':
            if 'X' == a[6]:
                print('This cell is occupied! Choose another one!')
                continue
            if 'O' == a[6]:
                print('This cell is occupied! Choose another one!')
                continue
            a = a[:6] + tracker + a[6+1:]
            print('---------')
            print('|', a[0], a[1], a[2], '|')
            print('|', a[3], a[4], a[5], '|')
            print('|', a[6], a[7], a[8], '|')
            print('---------')
            p += 1
        if user == '3 2':
            if 'X' == a[7]:
                print('This cell is occupied! Choose another one!')
                continue
            if 'O' == a[7]:
                print('This cell is occupied! Choose another one!')
                continue
            a = a[:7] + tracker + a[7+1:]
            print('---------')
            print('|', a[0], a[1], a[2], '|')
            print('|', a[3], a[4], a[5], '|')
            print('|', a[6], a[7], a[8], '|')
            print('---------')
            p += 1
        if user == '3 3':
            if 'X' == a[8]:
                print('This cell is occupied! Choose another one!')
                continue
            if 'O' == a[8]:
                print('This cell is occupied! Choose another one!')
                continue
            a = a[:8] + tracker + a[8+1:]
            print('---------')
            print('|', a[0], a[1], a[2], '|')
            print('|', a[3], a[4], a[5], '|')
            print('|', a[6], a[7], a[8], '|')
            print('---------')
        if a[0] == a[1] == a[2] and a[0] != ' ' or\
            a[0] == a[3] == a[6] and a[0] != ' ' or\
                a[0] == a[4] == a[8] and a[0] != ' ':
                print(a[0] + ' wins')
                break
        elif a[2] == a[4] == a[6] and a[2] != ' ' or\
            a[2] == a[5] == a[8] and a[2] != ' ':
            print(a[2] + ' wins')
            break
        elif a[3] == a[4] == a[5] and a[3] != ' ':
            print(a[3] + ' wins')
            break
        elif a[6] == a[7] == a[8] and a[6] != ' ':
            print(a[6] + ' wins')
            break
        elif a[1] == a[4] == a[7] and a[1] != ' ':
            print(a[1] + ' wins')
            break
        elif ' ' not in a:
            print('Draw')
            break
    except ValueError:
        print('Invalid Value Kid')
