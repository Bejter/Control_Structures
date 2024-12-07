# Total number of tasks in the test
total_tasks = 20

# List of correctly completed tasks
completed_tasks = [20, 11, 10, 9, 0]

# Process each result
for correct_tasks in completed_tasks:
    print(f"Completed tasks: {correct_tasks}")
    if correct_tasks >= total_tasks / 2:
        print("Test passed!")
    else:
        print("Test not passed.")
    print()  # Blank line for better readability
