import csv
from typing import List, Dict

def read_orders(file_path: str) -> List[Dict[str, str]]:
    try:
        with open(file_path, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)
    except FileNotFoundError:
        print("Error: File not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

def calculate_order_total(order: Dict[str, str]) -> float:
    try:
        quantity = int(order["quantity"])
        price = float(order["price_per_item"])
        return quantity * price
    except (KeyError, ValueError) as e:
        print(f"Invalid order data: {e}")
        return 0.0

def process_orders(file_path: str) -> None:
    orders = read_orders(file_path)
    for order in orders:
        total = calculate_order_total(order)
        print(f"Order ID: {order['order_id']}")
        print(f"Item: {order['item']}")
        print(f"Quantity: {order['quantity']}")
        print(f"Total Cost: ${total:.2f}")
        print("-" * 30)

if __name__ == "__main__":
    process_orders("orders.csv")
