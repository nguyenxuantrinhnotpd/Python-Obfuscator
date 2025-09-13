#!/usr/bin/env python3
"""
File ví dụ để demo Python Code Obfuscator
"""

def fibonacci(n):
    """Tính số Fibonacci thứ n"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def greet(name):
    """Chào hỏi người dùng"""
    return f"Xin chào, {name}!"

def calculate_sum(numbers):
    """Tính tổng các số trong list"""
    total = 0
    for num in numbers:
        total += num
    return total

def main():
    """Hàm main chạy các ví dụ"""
    print("=== DEMO PYTHON CODE OBFUSCATOR ===")
    print()
    
    # Test fibonacci
    n = 10
    result = fibonacci(n)
    print(f"Fibonacci({n}) = {result}")
    
    # Test greet
    name = "NGUYEN XUAN TRINH"
    greeting = greet(name)
    print(greeting)
    
    # Test calculate_sum
    numbers = [1, 2, 3, 4, 5, 10, 20]
    total = calculate_sum(numbers)
    print(f"Tổng của {numbers} = {total}")
    
    # Test with loop
    print("\nCác số chẵn từ 1 đến 20:")
    for i in range(1, 21):
        if i % 2 == 0:
            print(f"  {i}")
    
    print("\n=== KẾT THÚC DEMO ===")

if __name__ == "__main__":
    main()

