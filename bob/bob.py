def hey(speech):
    speech = speech.rstrip()
    if speech.isupper() == True:
        print('Whoa, chill out!')
        return 'Whoa, chill out!'
    elif speech.endswith('?') == True:
        print('Sure.')
        return 'Sure.'
    elif speech == '':
        print('Fine. Be that way!')
        return 'Fine. Be that way!'
    else:
        print('Whatever.')
        return 'Whatever.'
