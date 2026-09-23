def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


user_input = input("Введите год: ")
year = int(user_input)
result = is_year_leap(year)

print(f"год {year}: {result}")
