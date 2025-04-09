sandwhich_orders=['salad sandwhich', 'butter sandwhich', 'jam sandwhivh', 'peanut sandwhich']
finished_orders=[]

while sandwhich_orders:
    serving_order=sandwhich_orders.pop()

print('sandwhiches ready...' + serving_order.title())
finished_orders.append(serving_order)
print('\nOrders are coming')
for finished_order in finished_orders:
    print(finished_order.title())
