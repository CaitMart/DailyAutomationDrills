def is_leap_year(year):
    if year % 4 == 0 and year % 100 == 0:
            return False
    if year % 400 == 0 and year % 4 == 0:
        return True
    elif year % 4 == 0:
        return True
    else:
         return False

while True:
    print('Enter a year or "done":')
    response = input()
    if response == 'done':
        break
    print('Is leap year:', is_leap_year(int(response)))