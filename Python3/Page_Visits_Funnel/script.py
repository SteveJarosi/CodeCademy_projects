#import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
print(visits.head())                       
print(cart.head())  
print(checkout.head())  
print(purchase.head())  

vis_cart = pd.merge(visits, cart, how='left')
print(len(pd.merge(visits, cart, how='inner')))
print(vis_cart)
print(len(visits), len(vis_cart), len(cart))
vis_cart_null = vis_cart[vis_cart['cart_time'].isnull()]
print(vis_cart_null)
print(vis_cart_null.info())
print(len(vis_cart)-len(vis_cart_null))
print(float(len(vis_cart_null))/len(vis_cart)*100, '%')
car_check = pd.merge(cart, checkout, how='left')
print(car_check)
car_check_null = car_check[car_check['checkout_time'].isnull()]
print(float(len(car_check_null))/len(car_check)*100, '%')
all_data = visits.merge(cart, how='left').merge(checkout, how='left').merge(purchase, how='left')
print(all_data.head(10))
#print(float(len(car_check_null))/len(car_check)*100, '%')
check_pur = pd.merge(checkout, purchase, how='left')
check_pur_null = check_pur[check_pur['purchase_time'].isnull()]
print(float(len(check_pur_null))/len(check_pur)*100, '%')
all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time
print(all_data['time_to_purchase'])
print(all_data.time_to_purchase.mean())


