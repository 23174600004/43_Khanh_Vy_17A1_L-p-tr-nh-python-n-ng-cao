class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Thêm một phần tử vào ngăn xếp."""
        self.items.append(item)

    def pop(self):
        """Lấy phần tử từ đỉnh ngăn xếp và trả về nó. Trả về None nếu ngăn xếp rỗng."""
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        """Xem phần tử trên đỉnh ngăn xếp mà không xóa nó."""
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        """Kiểm tra xem ngăn xếp có rỗng không."""
        return len(self.items) == 0

    def count(self):
        """Trả về số phần tử trong ngăn xếp."""
        return len(self.items)

# Sử dụng lớp Stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Số phần tử trong Stack:", stack.count())  # Output: 3

stack.pop()
print("Số phần tử trong Stack sau khi pop:", stack.count())  # Output: 2
