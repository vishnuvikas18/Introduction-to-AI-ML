def grade_student():
    print("\nAI Grading Assistant")

    subjects = ["Intro to AI/ML", "DSA", "Discrete Maths", "Engineering Maths III", "German"]
    marks = []
    failed = []

    for subject in subjects:
        score = float(input(f"Enter marks for {subject} (0–100): "))
        if score < 0 or score > 100:
            print("Invalid marks entered! Must be between 0 and 100.")
            return
        marks.append(score)
        if score < 35:
            failed.append(subject)

    if 0 in marks:
        print("Result invalid! Student got zero in some subject.")
        return

    total = sum(marks)
    percentage = total / len(subjects)

    print("\nResults:")
    print("Total Marks:", total)
    print("Percentage :", percentage, "%")

    if failed:
        print("\nStudent FAILED in:")
        for sub in failed:
            print("-", sub)
    else:
        print("\nStudent PASSED!")


while True:
    grade_student()
    again = input("\nDo you want to grade another student? (y/n): ")
    if again.lower() != "y":
        print("Exiting program...")
        break
