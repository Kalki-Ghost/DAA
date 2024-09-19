"""January-2200
February-2350
March-2600
April-2130
May-2190"""

expense = [2200, 2350, 2600, 2130, 2190]
month = ['January', 'February', 'March', 'April', 'May']

"""In Feb,how many dollars you spent extra compare to january"""
print(f"{expense[1] - expense[0]} more expenditure in february compare to january")

"""Find out your total expense in first quarter(first three months) of the month."""
sum1 = 0
for i in range(3):
    sum1 += expense[i]
print(f"The Expenditure of first quarter is {sum1}.")

"""Find out if you spent exactly 2000 dollars in any month."""
if 2000 in expense:
    print("Yes,i spent exactly 2000 dollars in month.")
else:
    print("No,i not spent exactly 2000 dollars in any month.")

"""June month just finished and your expense is 1980 dollars.Add this item to our monthly expense list."""
expense.append(1980)
month.append('June')

"""You return an item that you bought in a month of April and got a refund of 2005.Make a correction to your monthly expense list based on this."""

expense[3] -= 200
print(expense)
