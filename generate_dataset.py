import pandas as pd
import random
from datetime import datetime, timedelta
# -----------------------------------
# RetailIQ Sample Data
# -----------------------------------

customers = [
    "Rahul Sharma",
    "Priya Reddy",
    "Amit Kumar",
    "Sneha Patel",
    "Arjun Singh",
    "Neha Gupta",
    "Vamsi Krishna",
    "Anjali Mehta",
    "Rohit Verma",
    "Pooja Nair"
]

cities = [
    "Hyderabad",
    "Bengaluru",
    "Chennai",
    "Mumbai",
    "Delhi"
]

products = {
    "Electronics": [
        ("Laptop", 65000, 52000),
        ("Mobile", 30000, 24000),
        ("Keyboard", 1500, 900),
        ("Mouse", 800, 450),
        ("Smart Watch", 12000, 8500)
    ],

    "Furniture": [
        ("Chair", 2500, 1800),
        ("Sofa", 25000, 18000)
    ],

    "Home Appliances": [
        ("Refrigerator", 40000, 31000),
        ("Washing Machine", 35000, 27000)
    ],

    "Fashion": [
        ("T-Shirt", 800, 300),
        ("Jeans", 1800, 900)
    ],

    "Grocery": [
        ("Rice Bag", 1800, 1400)
    ]
}

payment_methods = [
    "UPI",
    "Cash",
    "Credit Card",
    "Debit Card"
]
sales_data = []
# -----------------------------------
# Generate 500 Sales Records
# -----------------------------------

for order_number in range(1, 501):
    customer = random.choice(customers)
    city = random.choice(cities)
    category = random.choice(list(products.keys()))
    product, unit_price, unit_cost = random.choice(products[category])
    quantity = random.randint(1, 5)
    revenue = quantity * unit_price
    profit = quantity * (unit_price - unit_cost)
    sales_data.append({
    "Order_ID": f"ORD{order_number:04}",
    "Order_Date": (
    datetime(2025, 1, 1) +
    timedelta(days=random.randint(0, 364))
    ).strftime("%Y-%m-%d"),
    "Customer_Name": customer,
    "City": city,
    "Category": category,
    "Product": product,
    "Quantity": quantity,
    "Unit_Price": unit_price,
    "Unit_Cost": unit_cost,
    "Revenue": revenue,
    "Profit": profit,
    "Payment_Method": random.choice(payment_methods)
})
# -----------------------------------
# Convert to DataFrame
# -----------------------------------

df = pd.DataFrame(sales_data)

# -----------------------------------
# Save CSV
# -----------------------------------

df.to_csv("data/raw/sales.csv", index=False)

print("✅ Dataset created successfully!")
print("📁 File saved at: data/raw/sales.csv")