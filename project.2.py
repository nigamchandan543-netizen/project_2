print("____________________________________________")
print(" Welcome to the Pattern Generator and")
print(" Number Analyzer!")
print("____________________________________________")

while True:
    print("\nSelect an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    task = input("Enter your tasks: ")

    if task == "1":
        rows = int(input("Enter the number of rows for the pattern: "))

        if rows <= 0:
            print("Invalid row count! Pattern generation stopped.")
            break

        print("\nPattern:")
        for i in range(1, rows + 1):
            for j in range(i):
                print("*", end="")
            print()

    elif task == "2":
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))

        if end < start:
            print("Error: End number must be greater than or equal to start number.")
            continue

        total = 0

        print()
        for num in range(start, end + 1):

            if num == -1:
                pass

            if num % 2 == 0:
                print(f"Number {num} is Even")
            else:
                print(f"Number {num} is Odd")

            total += num

        print(f"\nSum of all numbers from {start} to {end} is: {total}")

    elif task == "3":
        print("Thank you for using the Pattern Generator and Number Analyzer!")
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
