import time

def timer_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        duration = end_time - start_time
        print("Функция выполнилась за ", duration, "секунд")

    return wrapper

@timer_decorator
def my_function():
    time.sleep(1)


my_function()

