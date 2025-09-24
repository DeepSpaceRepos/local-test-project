#!/usr/bin/env python3

def fibonacci(n):
    """
    Generate the nth Fibonacci number.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
    
    Returns:
        int: The nth Fibonacci number
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_sequence(count):
    """
    Generate a list of Fibonacci numbers.
    
    Args:
        count (int): Number of Fibonacci numbers to generate
    
    Returns:
        list: List of Fibonacci numbers
    """
    return [fibonacci(i) for i in range(count)]

def fibonacci_iterative(n):
    """
    Generate the nth Fibonacci number using iterative approach (more efficient).
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
    
    Returns:
        int: The nth Fibonacci number
    """
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b

def main():
    print("Fibonacci Sequence Generator")
    print("=" * 30)
    
    # Generate first 10 Fibonacci numbers
    print("First 10 Fibonacci numbers:")
    fib_sequence = fibonacci_sequence(10)
    for i, num in enumerate(fib_sequence):
        print(f"F({i}) = {num}")
    
    print("\n" + "=" * 30)
    
    # Demonstrate both recursive and iterative approaches
    n = 15
    print(f"F({n}) using recursive method: {fibonacci(n)}")
    print(f"F({n}) using iterative method: {fibonacci_iterative(n)}")

if __name__ == "__main__":
    main()