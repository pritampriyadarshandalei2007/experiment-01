# wap to enter time in minutes and print it in hour and minute format.
m = int(input("Enter time in minutes: "))

hour = m // 60
minute = m % 60

print("Time =", hour, "hour", minute, "minute")