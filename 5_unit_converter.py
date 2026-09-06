while True:
    print("===UNIT CONVERTER===")
    print("------------------------------------------")
    print("Choose a category:")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    print("4. Time")
    print("5. Speed")
    print("6. Area")
    print("7. Volume")
    print("------------------------------------------")

    category = input("Category (1-7): ")
    print("------------------------------------------")

    try:
        if category == "1":
            print("Length Conversions:")
            print("1. m to km")
            print("2. km to m")
            print("3. cm to m")
            print("4. m to cm")
            print("5. in to cm")
            print("6. cm to in")
            print("------------------------------------------")
            choice = input("Choose: ")
            print()
            value = float(input("Value: "))

            if choice == "1":
                print(value, "m =", value / 1000, "km")
            elif choice == "2":
                print(value, "km =", value * 1000, "m")
            elif choice == "3":
                print(value, "cm =", value / 100, "m")
            elif choice == "4":
                print(value, "m =", value * 100, "cm")
            elif choice == "5":
                print(value, "in =", value * 2.54, "cm")
            elif choice == "6":
                print(value, "cm =", value / 2.54, "in")
            else:
                print("Invalid choice. Please try again.")
                print("------------------------------------------")
                continue

        elif category == "2":
            print("Weight Conversions:")
            print("1. g to kg")
            print("2. kg to g")
            print("3. lb to kg")
            print("4. kg to lb")
            print("5. oz to g")
            print("6. g to oz")
            print("------------------------------------------")
            choice = input("Choose: ")
            print()
            value = float(input("Value: "))

            if choice == "1":
                print(value, "g =", value / 1000, "kg")
            elif choice == "2":
                print(value, "kg =", value * 1000, "g")
            elif choice == "3":
                print(value, "lb =", value * 0.453592, "kg")
            elif choice == "4":
                print(value, "kg =", value / 0.453592, "lb")
            elif choice == "5":
                print(value, "oz =", value * 28.3495, "g")
            elif choice == "6":
                print(value, "g =", value / 28.3495, "oz")
            else:
                print("Invalid choice. Please try again.")
                print("------------------------------------------")
                continue

        elif category == "3":
            print("Temperature Conversions:")
            print("1. C to F")
            print("2. F to C")
            print("3. C to K")
            print("4. K to C")
            print("------------------------------------------")
            choice = input("Choose: ")
            print()
            value = float(input("Value: "))

            if choice == "1":
                print(value, "C =", (value * 9 / 5) + 32, "F")
            elif choice == "2":
                print(value, "F =", (value - 32) * 5 / 9, "C")
            elif choice == "3":
                print(value, "C =", value + 273.15, "K")
            elif choice == "4":
                print(value, "K =", value - 273.15, "C")
            else:
                print("Invalid choice. Please try again.")
                print("------------------------------------------")
                continue

        elif category == "4":
            print("Time Conversions:")
            print("1. sec to min")
            print("2. min to sec")
            print("3. min to hr")
            print("4. hr to min")
            print("5. hr to days")
            print("6. days to hr")
            print("------------------------------------------")
            choice = input("Choose: ")
            print()
            value = float(input("Value: "))

            if choice == "1":
                print(value, "sec =", value / 60, "min")
            elif choice == "2":
                print(value, "min =", value * 60, "sec")
            elif choice == "3":
                print(value, "min =", value / 60, "hr")
            elif choice == "4":
                print(value, "hr =", value * 60, "min")
            elif choice == "5":
                print(value, "hr =", value / 24, "days")
            elif choice == "6":
                print(value, "days =", value * 24, "hr")
            else:
                print("Invalid choice. Please try again.")
                print("------------------------------------------")
                continue

        elif category == "5":
            print("Speed Conversions:")
            print("1. km/h to mph")
            print("2. mph to km/h")
            print("3. m/s to km/h")
            print("4. km/h to m/s")
            print("------------------------------------------")
            choice = input("Choose: ")
            print()
            value = float(input("Value: "))

            if choice == "1":
                print(value, "km/h =", value * 0.621371, "mph")
            elif choice == "2":
                print(value, "mph =", value / 0.621371, "km/h")
            elif choice == "3":
                print(value, "m/s =", value * 3.6, "km/h")
            elif choice == "4":
                print(value, "km/h =", value / 3.6, "m/s")
            else:
                print("Invalid choice. Please try again.")
                print("------------------------------------------")
                continue

        elif category == "6":
            print("Area Conversions:")
            print("1. m2 to km2")
            print("2. km2 to m2")
            print("3. ft2 to m2")
            print("4. m2 to ft2")
            print("------------------------------------------")
            choice = input("Choose: ")
            print()
            value = float(input("Value: "))

            if choice == "1":
                print(value, "m2 =", value / 1000000, "km2")
            elif choice == "2":
                print(value, "km2 =", value * 1000000, "m2")
            elif choice == "3":
                print(value, "ft2 =", value * 0.092903, "m2")
            elif choice == "4":
                print(value, "m2 =", value / 0.092903, "ft2")
            else:
                print("Invalid choice. Please try again.")
                print("------------------------------------------")
                continue

        elif category == "7":
            print("Volume Conversions:")
            print("1. L to mL")
            print("2. mL to L")
            print("3. gal to L")
            print("4. L to gal")
            print("------------------------------------------")
            choice = input("Choose: ")
            print()
            value = float(input("Value: "))

            if choice == "1":
                print(value, "L =", value * 1000, "mL")
            elif choice == "2":
                print(value, "mL =", value / 1000, "L")
            elif choice == "3":
                print(value, "gal =", value * 3.78541, "L")
            elif choice == "4":
                print(value, "L =", value / 3.78541, "gal")
            else:
                print("Invalid choice. Please try again.")
                print("------------------------------------------")
                continue

        else:
            print("Invalid category. Please try again.")
            print("------------------------------------------")
            continue

        print("------------------------------------------")
        break

    except ValueError:
        print("Please enter a valid number. Try again.")
        print("------------------------------------------")
