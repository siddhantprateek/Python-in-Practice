high_income = False
good_credits = True
student = True
# HIGH_INCOME AND GOOD_CREDIT ARE ALREADY BOOLEAN SO IN CONDITIONAL
# STATEMENT YOU DON'T HAVE TO WRITE == TRUE (IT IS UNPROFESSIONAL)


if high_income and good_credits and not student:
    print("Elligible")
else:
    print("Not Elligible")
