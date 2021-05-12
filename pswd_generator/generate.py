import randomize

def yesKeyword(pswd_kywd, pswd_type, pswd_len, underscore):
    chars = []
    kywd_pswd = 'ERROR'
    kywd_len = len(pswd_kywd)
    for ch in pswd_kywd:
        chars.append(ch)
    for _ in range(randomize.math.floor(kywd_len/2)):
        randomChar = randomize.random.randint(0,kywd_len-1)
        chars[randomChar] = chars[randomChar].upper()
    mixed_kywd = ''.join(chars)
    if len(mixed_kywd) < pswd_len:
        if underscore==True:
            mixed_kywd += '_'
            diff = pswd_len - (len(mixed_kywd) - 1)
            kywd_pswd = (mixed_kywd + noKeyword(pswd_type, diff-1))
        else:
            diff = pswd_len - len(mixed_kywd)
            kywd_pswd = (mixed_kywd + noKeyword(pswd_type, diff))
        return kywd_pswd
    else:
        kywd_pswd = ''.join(chars)
        print('(Requested pswd length < Keyword length!)')
        return kywd_pswd
    return kywd_pswd

def noKeyword(pswd_type, pswd_len):
    kywd_letters = []
    possible = []
    types = [1,2,3,12,23,13,123]
    if pswd_len != 0:
        for _ in range(pswd_len):
            if pswd_type in types:
                
                if pswd_type==1:possible.append(randomize.alphabetic())
                elif pswd_type==2:possible.append(randomize.numerical())
                elif pswd_type==3:possible.append(randomize.symbolic())
                    
                elif pswd_type==12:
                    if randomize.eitherOr(2)==1:possible.append(randomize.alphabetic())
                    else:possible.append(randomize.numerical())
                elif pswd_type==23:
                    if randomize.eitherOr(2)==1:possible.append(randomize.numerical())
                    else:possible.append(randomize.symbolic())
                elif pswd_type==13:
                    if randomize.eitherOr(2)==1:possible.append(randomize.alphabetic())
                    else:possible.append(randomize.symbolic())
                        
                elif pswd_type==123:
                    if randomize.eitherOr(3)==1:possible.append(randomize.alphabetic())
                    elif randomize.eitherOr(3)==2:possible.append(randomize.numerical())
                    else:possible.append(randomize.symbolic())
    return (''.join(possible))
