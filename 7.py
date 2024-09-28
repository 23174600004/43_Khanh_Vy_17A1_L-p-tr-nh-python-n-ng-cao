class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day, self.month, self.year = day, month, year

    def display(self):
        print(f"{self.day}/{self.month}/{self.year}")

    def next(self):
        days_in_month = [31, 28 + (self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0)), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.day += 1
        if self.day > days_in_month[self.month - 1]:
            self.day, self.month = 1, self.month + 1
            if self.month > 12:
                self.month, self.year = 1, self.year + 1


# Kiểm tra chức năng
date = Date(28, 2, 2024)
date.display()  # Output: 28/2/2024
date.next()
date.display()  # Output: 29/2/2024
date.next()
date.display()  # Output: 1/3/2024
