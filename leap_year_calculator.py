import roman

while True:
    year_main = input(
        "Enter any year you want to check (or you can type 'exit' to exit): ").lower()

    if "exit" in year_main:
        print("Thanks for your time.")
        break
    try:
        year = int(year_main)

        if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
            print(f"\n{year} is a leap year.")
            print(f"It's {(year + 99) // 100}th century and {year} in roman is {roman.toRoman(year)}")
        else:
            print(f"\n{year} is not a leap year.")
            print(f"It's {(year + 99) // 100}th century and {year} in roman is {roman.toRoman(year)}")

    except ValueError:
        print(f"\n{year_main} is a not valid year. \nPlease enter a valid year.\n")
