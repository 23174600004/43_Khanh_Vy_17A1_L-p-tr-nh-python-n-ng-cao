import json
from datetime import datetime

transactions = []

# Thêm giao dịch
def add_transaction():
    transactions.append({
        "transaction_type": input("Loại giao dịch (tiền/vàng): "),
        "customer": input("Tên khách hàng: "),
        "amount": float(input("Số tiền: ")),
        "status": input("Trạng thái: "),
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

# Ghi giao dịch vào file JSON
def write_transactions():
    file_name = datetime.now().strftime("%Y-%m-%d-%H-%M-%S.json")
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(transactions, file, ensure_ascii=False, indent=4)
    print(f"Ghi giao dịch vào {file_name}")