responses={}
polling_active=True
while polling_active:
    name=input('\nWhat is your name')
    response=input('which mountain would you like to climb?')
    responses[name]=response
    repeat=input('would you like  another person to respond (yes/no)')
if repeat == 'no':
    polling_active = False
print('\n--- POLL RESULTS---')
for name, response in responses.items():
    print( name  +  'would like to climb'  +  response  )
               
 

