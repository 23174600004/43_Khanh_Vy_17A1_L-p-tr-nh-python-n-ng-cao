import json

class JSONReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def read_json(self):
        with open(self.file_path, 'r') as file:
            self.data = json.load(file)

    def display_data(self):
        if self.data:
            for user in self.data:
                print(f"Name: {user['name']}, Age: {user['age']}, Address: {user['address']}")
        else:
            print("No data to display. Please read the JSON file first.")

# Sử dụng lớp JSONReaderS
if __name__ == "__main__":
    path = 'D:/Lab 1/Code/users.json'
    reader = JSONReader(path)
    reader.read_json()
    reader.display_data()