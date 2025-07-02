def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

# Example usage
scores = [85, 92, 78, 96, 88]
average = calculate_average(scores)
print(f"Average score: {average}")
