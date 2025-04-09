def display_message(name):
    print('Hello '+name.title())
def favourite_book(books):
    print('One of my favourite books is '+books)
def Usernames(fname,lname):
    print('\nMy first name is '+fname.title())
    print('My second name is '+lname.title())
def make_tshirt(size='Large',textshirt='i love python'):
    print('The size of the T-shirt '+size+' '+'and the message is '+textshirt)
def describe_city(city,country):
    print(city +' is in '+country)
def get_names(fname,lname):
    full_name=fname+' '+lname
    return full_name.title()
Names=get_names('Tumelo','Tlouamma')
print(Names)

def get_allnames(first_name,last_name,Mname=''):
    if Mname:
        full_name=first_name+' '+Mname+' '+last_name
    else:
        full_name=first_name+' '+last_name
        
        return full_name.title()
fullnames=get_allnames('Tumelo','Tlouamma')
print(fullnames)

def build_profile(Name,Second_name,Career):
    person={'First name':Name,
            'Second_name':Second_name,
            'Career':Career
           }
    return person
myself=build_profile('Tumelo','Etiane','Programmer')
print(myself)

def ask_user(First_name,second_name):
    Fullname=First_name+' '+second_name
    return Fullname
while True:
    print('\nEnter your credentials')
    f_name=input('Enter your first name: ')
    l_name=input('Enter you last name: ')
    
    
    Full_cred=ask_user(f_name,l_name)
    print('\nHello '+ Full_cred)
    break
def ask_user2(firstname1,lastname1):
    fullname1=firstname1+' '+lastname1
    return fullname1
while True:
    print('\nEnter your names')
    print('(Enter X to quit)')
    
    f_name1=input("Enter your First name: ")
    if f_name1=='X':
        break
    l_name1=input('Enter your Second name')
    if l_name1=='X':
        break
    Full_cred1=ask_user2(f_name1,l_name1)
    print('\nHello '+Full_cred1)