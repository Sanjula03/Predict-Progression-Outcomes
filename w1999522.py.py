# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1999522
# Date: 20/4/2023
credit_table = [
    [120, 0, 0, "Progress"],
    [100, 20, 0, "Progress (module trailer)"],
    [100, 0, 20, "Progress (module trailer)"],
    [80, 40, 0, "Do not Progress - module retriever"],
    [80, 20, 20, "Do not Progress - module retriever"],
    [80, 0, 40, "Do not Progress - module retriever"],
    [60, 60, 0, "Do not progress - module retriever"],
    [60, 40, 20, "Do not progress - module retriever"],
    [60, 20, 40, "Do not progress - module retriever"],
    [60, 0, 60, "Do not progress - module retriever"],
    [40, 80, 0, "Do not progress - module retriever"],
    [40, 60, 20, "Do not progress - module retriever"],
    [40, 40, 40, "Do not progress - module retriever"],
    [40, 20, 60, "Do not progress - module retriever"],
    [40, 0, 80, "Exclude"],
    [20, 100, 0, "Do not progress - module retriever"],
    [20, 80, 20, "Do not progress - module retriever"],
    [20, 60, 40, "Do not progress - module retriever"],
    [20, 40, 60, "Do not progress - module retriever"],
    [20, 20, 80, "Exclude"],
    [20, 0, 100, "Exclude"],
    [0, 120, 0, "Do not progress - module retriever"],
    [0, 100, 20, "Do not progress - module retriever"],
    [0, 80, 40, "Do not progress - module retriever"],
    [0, 60, 60, "Do not progress - module retriever"],
    [0, 40, 80, "Exclude"],
    [0, 20, 100, "Exclude"],
    [0, 0, 120, "Exclude"]
]

progression_data = []

def create_histogram(progress_count, trailer_count, retriever_count, exclude_count):
    print("\n---------------------------------------------------------------")
    print("Histogram")
    print("Progress", progress_count, ": ", "*"*progress_count)
    print("Trailer", trailer_count, ": ", "*"*trailer_count)
    print("Retriever", retriever_count, ": ", "*"*retriever_count)
    print("Excluded", exclude_count, ": ", "*"*exclude_count)
    print("Total Students: ", progress_count + trailer_count + retriever_count + exclude_count)
    print("---------------------------------------------------------------")

while True: # using a while to loop the program until get the right input

    progress_count = 0
    trailer_count = 0
    retriever_count = 0
    exclude_count = 0

    try: # to handle value error
        option=int(input("Enter 1 to access the option for student\nEnter 2 to access the option for staff\n>>> ")) 
        if option not in range(1,3):
            print("Enter a valid option number")
        else:
            break
    except ValueError:
        print("Enter a valid option number")

if option == 1: # student version
    while True: # to loop the program until getting the right total

        while True: # to loop the program until getting the right credits
            try:
                pass_credits=int(input("Please enter your credits at pass: "))
                if pass_credits not in range(0,121,20):
                    print("Out of range")
                else:
                    break
            except ValueError:
                print("Integer required")

        while True: # to loop the program until getting the right credits
            try:
                defer_credits=int(input("Please enter your credits at defer: "))
                if defer_credits not in range(0,121,20):
                    print("Out of range")
                else:
                    break
            except ValueError:
                print("Integer required")

        while True: # to loop the program until getting the right credits
            try:
                fail_credits=int(input("Please enter your credits at fail: "))
                if fail_credits not in range(0,121,20):
                    print("Out of range")
                else:
                    break
            except ValueError:
                print("Integer required")

        if pass_credits + defer_credits + fail_credits != 120:
            print("Total incorrect")
        else:
            break

    if pass_credits==120: # Checking the grades
        print("Progress")

    elif pass_credits == 100:
        print("Progress (module trailer)")
    elif pass_credits<60 and defer_credits<60 and fail_credits>60:
        print("Exclude")
        
    else:
        print("Do not progress - module retriever")

else: # staff version
    while True: # Loop to continue input until user chooses to exit
        try:
            pass_credits = int(input("Please enter your credits at pass: "))
            if pass_credits not in [0, 20, 40, 60, 80, 100, 120]:
                raise ValueError("Out of range")  # Raise a value error if input is out of range
                # w3schools
                # https://www.w3schools.com/python/ref_keyword_raise.asp#:~:text=The%20raise%20keyword%20is%20used,to%20print%20to%20the%20user.
            defer_credits = int(input("Please enter your credits at defer: "))
            if defer_credits not in [0, 20, 40, 60, 80, 100, 120]:
                raise ValueError("Out of range")
            
            fail_credits = int(input("Please enter your credits at fail: "))
            if fail_credits not in [0, 20, 40, 60, 80, 100, 120]:
                raise ValueError("Out of range")
                
            if pass_credits + defer_credits + fail_credits != 120:
                raise ValueError("Total incorrect")
                
            for row in credit_table:
                if pass_credits == row[0] and defer_credits == row[1] and fail_credits == row[2]:
                    progression_outcome = row[3] # Assign progression outcome from credit_table
                    if progression_outcome == "Progress":
                        progress_count += 1
                    elif progression_outcome == "Progress (module trailer)":
                        trailer_count += 1
                    elif progression_outcome == "Do not Progress - module retriever":
                        retriever_count += 1
                    elif progression_outcome == "Exclude":
                        exclude_count += 1
                    else:
                        print("Progression outcome:", row[3])
                    break # Break out of the loop if user does not want to continue
            else:
                retriever_count += 1
                print("Progression outcome: Do not progress - module retriever")
            
            # Save the input progression data to the nested list
            progression_data.append([pass_credits, defer_credits, fail_credits, progression_outcome])

            # Ask if the staff member wants to continue
            choice = input("Do you want to predict the progression outcome for another student? (y/q): ")
            if choice.lower() != 'y':
                break
            
        except ValueError as v: # Catch any value errors and print the error message
            print(v)

    # call the create_histogram function
    create_histogram(progress_count, trailer_count, retriever_count, exclude_count)
    
    # Display the input progression data
    print("_Part 2_\n")
    print("Progression Data")
    print("{:<12} {:<12} {:<12} {:<25}".format("Pass", "Defer", "Fail", "Progression Outcome"))
    for data in progression_data:
        print("{:<12} {:<12} {:<12} {:<25}".format(data[0], data[1], data[2], data[3]))

    with open('progression_data.txt', 'w') as file: # save as a text file
        for data in progression_data:
            file.write(','.join(map(str, data)) + '\n') 