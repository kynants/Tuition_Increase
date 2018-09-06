# At one college, the tuition for a full time student is $6,000 per semester.
# It has been announced that the tuition will increase by 2 percent each year
# for the next five years. Design a program with a loop that displays the
# projected semester tuition amount for the next five years.

# Initialized Variables
tuit = 6000
sem = 1

# Semester number and tuition increase is automated
while sem < 6:
    print('Projected tuition for semester number',
          sem, '${0:.2f}'.format(tuit))
    tuit = round(tuit * (1 + 0.02), 2)
    sem += 1