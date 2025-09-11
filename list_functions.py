my_list = [5, 2, 3, 1, 4]
greatest = max(my_list) #find the greatest value
print(f"the greatest number in the list is: {greatest}")

smallest = min(my_list) #finds the smallest number
print(f"the smallest number in the list is: {smallest}")

list_sum = sum(my_list) #sums all the list numbers
print(f"the sum of the list is: {list_sum}")

list_length =  len(my_list) #length of the list
print(f"this list has {list_length} elements")

in_order = sorted(my_list)
print(in_order)

def filter_price(price):
    if (price < 400):
        return True
    else:
        return False

item_price = [230, 400, 450, 350, 370]
filtered_price = filter(filter_price, item_price)
print(list(filtered_price))