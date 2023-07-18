from datetime import datetime

test_date = input(">>")
print(test_date)
birh = datetime.strptime(test_date, '%d.%m.%Y')
print(birh.date())
