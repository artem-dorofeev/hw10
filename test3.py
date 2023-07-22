from datetime import datetime

test_date = input(">>")
print(test_date)
birth = datetime.strptime(test_date, '%d.%m.%Y')
current_date = datetime.now()
# current_date = datetime(year=2023, month=12, day=25)
print(birth.date(), current_date.date())

next_birth = datetime(current_date.year, birth.month, birth.day)
print(next_birth.date())
if next_birth < current_date:
    next_birth = datetime(current_date.year + 1, birth.month, birth.day)

print(next_birth.date())

day_for_birth = next_birth - current_date
print(day_for_birth.days)

# today = date.today() 
# next_birthday = date( today.year, bday.month, bday.day) 
# if next_birthday < today: 
#     next_birthday = date(today.year + 1, bday.month, bday.day) 
#     return f"{(next_birthday - today).days} days left till birthday"
