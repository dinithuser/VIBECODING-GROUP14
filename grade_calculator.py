

def main():
    while True:
        # ask for student's name
        name = input("Enter student name (or type Exit to quit): ")
        if name.strip().lower() == "exit":
            print("Goodbye!")
            break
        try:
            grades = []
            for i in range(1, 4):
                val = float(input(f"Enter mark for subject {i}: "))
                grades.append(val)
        except ValueError:
            print("Please enter numeric values for marks.")
            continue

        avg = sum(grades) / 3
        # determine grade
        if avg >= 75:
            grade = "A"
        elif avg >= 60:
            grade = "B"
        elif avg >= 40:
            grade = "C"
        else:
            grade = "Fail"
        # formatted output
        print("-" * 30)
        print(f"Name : {name}")
        print(f"Average: {avg:.1f}")
        print(f"Grade : {grade}")
        print("-" * 30)


if __name__ == "__main__":
    main()
