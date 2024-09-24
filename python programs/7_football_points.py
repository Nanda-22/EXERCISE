#7.program to get total number of points obtained by the team by wins,loses and draw
def football_points(x,y,z):
    wins_points=3*x
    draws_points=y*1
    loses_points=z*0
    total_football_points=wins_points+draws_points+loses_points
    return total_football_points
wins=eval(input("Enter number of wins : "))
draws=eval(input("Enter number of draws : "))
loses=eval(input("Enter number of loses: "))
print("Total number of points for given football team are : ",football_points(wins,draws,loses))
