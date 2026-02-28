"""
AI Logic Evaluation Suite: Python Sorting & Edge Case Analysis
This project demonstrates the ability to critique, debug, and optimize 
algorithmic logic for AI training (RLHF) purposes.
"""

def flawed_find_max(numbers):
    """
    A 'Hallucinated' approach an AI might take. 
    Issue: Fails on empty lists and doesn't handle non-integer types.
    """
    max_val = 0 # Logical error: If the list is [-5, -10], it returns 0 incorrectly.
    for n in numbers:
        if n > max_val:
            max_val = n
    return max_val

def optimized_find_max(numbers):
    """
    The 'Gold Standard' approach.
    Handles empty lists, negative numbers, and type checking.
    """
    if not numbers:
        return None
    
    if not all(isinstance(n, (int, float)) for n in numbers):
        raise ValueError("List must contain only numbers.")

    max_val = numbers[0]
    for n in numbers[1:]:
        if n > max_val:
            max_val = n
    return max_val

# --- Test Suite ---
test_data = [-10, -5, -2]
print(f"Flawed Result: {flawed_find_max(test_data)}")    # Outputs 0 (Wrong)
print(f"Optimized Result: {optimized_find_max(test_data)}") # Outputs -2 (Correct)
