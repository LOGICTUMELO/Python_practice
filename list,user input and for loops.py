name=input('what is your name?')
surname=input('what is your surname?')
full_names=name +surname
print('so your names are '+full_names)
answer=input('do you have other names')
if answer=='yes':
    name2=input('what is your other names?')
    print('so your names are: '+full_names+name2)
else:
    print('Nice to meet you')
