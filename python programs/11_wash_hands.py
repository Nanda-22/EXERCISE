#11.program for calculating time in minutes for handwashing in covid time based on given time period
def wash_hands(n,m):
    day_seconds=21*n
    monthly_seconds=day_seconds*30
    total_seconds=monthly_seconds*m
    return total_seconds  
N=eval(input("Enter number of time to wash the hands : "))
M=eval(input("Enter number of months to wash hands : "))
Total_time=wash_hands(N,M)
time_minutes=(Total_time//60)
time_seconds=(Total_time%60)
print("The total time for hand washing in given time period :",time_minutes,"minutes and",time_seconds,"seconds")
