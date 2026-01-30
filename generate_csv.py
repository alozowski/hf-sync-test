#!/usr/bin/env python3
"""Generate a sample CSV file with 10,000 rows for Test 2"""

import csv
import random
import datetime
from faker import Faker

fake = Faker()
Faker.seed(42)
random.seed(42)

# Generate 10,000 rows
rows = 10_000

with open('sample_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'timestamp', 'user_name', 'email', 'country', 'product', 'price', 'quantity', 'total']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    
    products = ['Widget A', 'Gadget B', 'Tool C', 'Device D', 'Component E']
    
    for i in range(1, rows + 1):
        timestamp = fake.date_time_between(start_date='-1y', end_date='now')
        user = fake.name()
        email = fake.email()
        country = fake.country()
        product = random.choice(products)
        price = round(random.uniform(10, 1000), 2)
        quantity = random.randint(1, 10)
        total = round(price * quantity, 2)
        
        writer.writerow({
            'id': i,
            'timestamp': timestamp.isoformat(),
            'user_name': user,
            'email': email,
            'country': country,
            'product': product,
            'price': price,
            'quantity': quantity,
            'total': total
        })

print(f"✅ Generated sample_data.csv with {rows:,} rows")

# Get file size
import os
file_size = os.path.getsize('sample_data.csv')
print(f"   File size: {file_size:,} bytes ({file_size / 1024 / 1024:.2f} MB)")
