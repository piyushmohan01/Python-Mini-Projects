def set_pswd_type(pswd_type):
    ordered_type = []
    [ordered_type.append(digit) for digit in pswd_type]
    ordered_type = list(set(ordered_type))
    ordered_type.sort()
    return int(''.join(ordered_type))

def printType(pswd_type):
    print('| Types :', end=' ')
    if pswd_type==1:print('Alphabetical')
    elif pswd_type==2:print('Numerical')
    elif pswd_type==3:print('Symbolic')
    elif pswd_type==12:print('Alphabetical-Numerical')
    elif pswd_type==23:print('Numerical-Symbolic')
    elif pswd_type==13:print('Alphabetical-Symbolic')
    elif pswd_type==123:print('Alphabetical-Numerical-Symbolic')