import time
class SimpleTask:
    def run_task(self):
        for i in range(1, 11):
            print('Đã in lần thứ :', 1)
            time.sleep(2) # Dùng 2 giây giữa mỗi lần in

def main():
    task = SimpleTask()
    task.run_task()

if __name__ == "__main__":
    main()