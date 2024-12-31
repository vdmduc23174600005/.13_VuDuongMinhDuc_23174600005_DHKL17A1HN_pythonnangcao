import threading
import time

class SimpleTask:
    def run_task(self):
        global counter
        for _ in range(4):
            time.sleep(2)
            counter += 1  # Tăng counter mà không sử dụng lock
            print(f"Counter đã tăng lên: {counter}")

def main():
    global counter
    counter = 0  # Khởi tạo biến toàn cục counter
    tasks = [threading.Thread(target=SimpleTask().run_task) for _ in range(4)]
    for task in tasks:
        task.start()
    for task in tasks:
        task.join()

if __name__ == "__main__":
    main()