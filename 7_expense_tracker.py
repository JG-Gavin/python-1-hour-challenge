import csv

filename = "expenses.csv"

while True:
    print("===EXPENSE TRACKER===")
    print("------------------------------------------")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Quit")
    print("------------------------------------------")

    choice = input("Choose: ")
    print("------------------------------------------")

    if choice == "1":
        name = input("Expense name: ").strip()

        print()
        print("Choose a category:")
        print("1. Food")
        print("2. Transport")
        print("3. School")
        print("4. Entertainment")
        print("5. Shopping")
        print("6. Bills")
        print("7. Other")
        print("------------------------------------------")
        category_choice = input("Category (1-7): ")

        if category_choice == "1":
            category = "Food"
        elif category_choice == "2":
            category = "Transport"
        elif category_choice == "3":
            category = "School"
        elif category_choice == "4":
            category = "Entertainment"
        elif category_choice == "5":
            category = "Shopping"
        elif category_choice == "6":
            category = "Bills"
        elif category_choice == "7":
            category = "Other"
        else:
            print("Invalid category. Please try again.")
            print("------------------------------------------")
            continue

        try:
            print()
            amount = float(input("Amount: "))

            if name == "":
                print("Expense name cannot be empty.")
            elif amount <= 0:
                print("Amount must be greater than 0.")
            else:
                with open(filename, "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([name, category, amount])

                print("Expense added.")
        except ValueError:
            print("Please enter a valid amount.")

    elif choice == "2":
        total = 0
        count = 0

        print("Your Expenses:")
        print("------------------------------------------")

        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    count += 1
                    amount = float(row[2])
                    total += amount

                    print(str(count) + ".", row[0], "-", row[1], "- $" + str(amount))

            if count == 0:
                print("No expenses yet.")
            else:
                print("------------------------------------------")
                print("Total spending: $" + str(total))
        except FileNotFoundError:
            print("No expenses yet.")
        except ValueError:
            print("There is an invalid amount in the expenses file.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

    print("------------------------------------------")
