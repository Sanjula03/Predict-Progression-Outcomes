progression_data = {}  # Initialize an empty dictionary to store progression data

while True:
    student_id = input("Enter student ID (or 'q' to quit): ")  # Prompt user to enter student ID or exit to quit
    if student_id == "q":  # If user enters 'exit', break out of the loop
        break

    progress = input("Enter progress separated by commas (e.g. 120,0,0): ")  # Prompt user to enter progress separated by commas
    progress = [int(p) for p in progress.split(",")]  # Convert the progress input to a list of integers

    # Determine the outcome based on the sum of progress values
    if sum(progress) == 300:
        outcome = "Progress"
    elif progress[0] >= 80 and sum(progress) >= 100:
        outcome = "Progress (module trailer)"
    elif progress[0] >= 40:
        outcome = "Module retriever"
    else:
        outcome = "Exclude"

    # Store the progression data in the dictionary with student ID as the key
    progression_data[student_id] = {"Outcome": outcome, "Progress": progress}

# Print the progression data stored in the dictionary
print("\nProgression Data:")
for student_id, data in progression_data.items():
    print(f"{student_id}: {data['Outcome']} - {data['Progress'][0]}, {data['Progress'][1]}, {data['Progress'][2]}") 