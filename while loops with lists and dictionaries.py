unconfirmed_users=['tumelo','logic','Huey','rilley','Smoke','Ruckus']
confirmed_users=[ ]

while unconfirmed_users:
    current_user =unconfirmed_users.pop()

    print('verifying user: ' + current_user.title())
    confirmed_users.append(current_user)
print('\nConfirmed users:')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

car_brands=['toyota','hyundai','mercedes','bmw']
print(car_brands)

while 'hyundai' in car_brands:
    car_brands.remove('hyundai')

    print(car_brands)
