import generate
import set_print

if __name__ == '__main__':
    print('Example: 7_123_Y')
    user_inp = input('Enter as shown: ')
    underscore = False
    if '_' not in user_inp:
        print('ERROR[T=00]: Enter underscores to seperate the parts!')
    else:
        split_choice = [x for x in user_inp.split('_')]
        if split_choice[0].isalpha() and split_choice[1].isalpha():
            print('ERROR[T=01]: Enter integers for length and types!')
        else:
            pswd_len = int(split_choice[0])
            if pswd_len > 20:
                print("ERROR[T=02]: Woah! That's too long for a password!")
            else:
                pswd_type = (split_choice[1])
                pswd_type = set_print.set_pswd_type(pswd_type)
                if len(split_choice) >= 3:
                    pswd_kywd = split_choice[2]
                    if len(split_choice) > 3:
                        if split_choice[3].isalpha():
                            underscore = True
                        else:
                            print('ERROR[T=03]: Add some letters in the end to enable underscore!')
                else:
                    pswd_kywd = 'None'
                if pswd_kywd == 'None': 
                    final = generate.noKeyword(pswd_type, pswd_len)
                    print('\nLength :', len(final), end=' ')
                    set_print.printType(pswd_type)
                    print('Final Password :', final)
                else: 
                    final = generate.yesKeyword(pswd_kywd, pswd_type, pswd_len, underscore)
                    print('\nFinal Password Generated :', final)
                    print('Length :', len(final), end=' ')
                    set_print.printType(pswd_type)