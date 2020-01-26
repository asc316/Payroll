print('Welcome to YourJob!')

name = input('Enter your First and Last name: ')

wage = float(input('What is your hourly wage? '))
hours = float(input('How many hours a week did you work? '))
normalwkhrs = 40
overtime = wage*1.5
weekpay = (wage*hours)
biweekly = wage*hours*2
monthpay = wage*hours*4
salary = wage*hours*52
monthgross = wage*hours*52/12
fedtax = (wage*hours*52/12) *.10
statetax = (wage*hours*52/12) *.03


if hours <= normalwkhrs:
    print(name)
    print('Weekly Pay ' + str(weekpay))
    print('Biweekly Pay ' + str(biweekly))
    print('Monthly ' + str(monthpay))
    print('Federal Taxes ' + str(fedtax))
    print('State Taxes ' + str(statetax))
    print('Salary ' + str(salary))
    print(name + "'s rundown. "  'Weekly Pay ' + str(weekpay) + ' Biweekly Pay ' + str(biweekly) + ' Monthly ' + str(monthpay) + ' Federal Taxes ' + str(fedtax) + ' State Taxes ' + str(statetax) + ' Salary ' + str(salary))



if hours > normalwkhrs:
    print(name)
    print('Weekly Pay ' + str(weekpay))
    print('Overtime ' + str(overtime))
    print('Biweekly Pay ' + str(biweekly))
    print('Monthly ' + str(monthpay))
    print('Federal Taxes ' + str(fedtax))
    print('State Taxes ' + str(statetax))
    print('Salary ' + str(salary))




