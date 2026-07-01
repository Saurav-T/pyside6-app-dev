from concurrent.futures import ThreadPoolExecutor
import time

def square(num):
    time.sleep(1)
    return num * num

numbers = [1, 2, 3, 4, 5]

with ThreadPoolExecutor() as executor:
    results = executor.map(square, numbers)

print("Squares:")
for result in results:
    print(result)