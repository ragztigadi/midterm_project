import json
import sys
from collections import defaultdict

def process_orders(file_path):
    # Step 1: Read JSON file
    with open(file_path, 'r') as file:
        orders = json.load(file)
    
    # Step 2: Create customers.json
    customers = {}
    for order in orders:
        phone = format_phone(order['phone'])
        name = order['name']
        customers[phone] = name

    # Step 3: Create items.json
    items = defaultdict(lambda: {"price": 0, "orders": 0})
    
    for order in orders:
        for item in order['items']:
            item_name = item['name']
            price = item['price']
            
            if items[item_name]["price"] == 0:
                items[item_name]["price"] = price
            items[item_name]["orders"] += 1

    # Write to customers.json
    with open('customers.json', 'w') as customers_file:
        json.dump(customers, customers_file, indent=4)
    
    # Write to items.json
    with open('items.json', 'w') as items_file:
        json.dump(items, items_file, indent=4)

def format_phone(phone):
    # Clean and format the phone number to be in xxx-xxx-xxxx format
    cleaned_phone = ''.join(filter(str.isdigit, phone))
    return f'{cleaned_phone[:3]}-{cleaned_phone[3:6]}-{cleaned_phone[6:]}'

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python process_orders.py <orders_file>")
        sys.exit(1)
    
    process_orders(sys.argv[1])
