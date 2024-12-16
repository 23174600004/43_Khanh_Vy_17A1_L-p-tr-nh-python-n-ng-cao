import xml.etree.ElementTree as ET

class XMLReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_xml(self):
        tree = ET.parse(self.file_path)
        return tree.getroot()

    def display_data(self, data):
        for product in data.findall('product'):
            name = product.find('name').text
            price = product.find('price').text
            quantity = product.find('quantity').text
            units = product.find('units').text
            print(f"Product: {name}, Price: {price}, Quantity: {quantity} {units}")
# Sử dụng lớp XMLReader
if __name__ == "__main__":
    reader = XMLReader('./DATA/products.xml')
    root = reader.read_xml()
    reader.display_data(root)