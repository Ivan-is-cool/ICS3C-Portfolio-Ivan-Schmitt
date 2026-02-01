scores = []
print("Enter test scores (enter -1 to finish):")
while True:
    try:
        score_input = input("Enter score: ")
        score = float(score_input)

        if score == -1:
            break 
        elif score >= 0:
            scores.append(score) 
        else:
            print("Invalid input. Please enter a positive score or -1.")
    except ValueError:
        print("Invalid input. Please enter a valid number (e.g., 85.5, 90).")


print("Entered Test Scores")
if scores: 
    for s in scores:
        print(s)

    total_score = sum(scores)
    average_score = total_score / len(scores)
    print(f"\nAverage Score: {average_score:.2f}") 
else:
    print("No valid scores were entered.")
