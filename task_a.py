def get_day_number(day):
    days_of_week = {
        "monday": 1,
        "tuesday": 2,
        "wednesday": 3,
        "thursday": 4,
        "friday": 5,
        "saturday": 6,
        "sunday": 7
    }

    day = day.strip().lower()

    if day in days_of_week:
        print(f"{day.capitalize()} is day {days_of_week[day]}")

    else:
        print("Please enter a valid day")

user_input = input("Enter a day of the week: ")
get_day_number(user_input)
