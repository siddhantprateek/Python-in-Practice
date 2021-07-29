# have high income and good credit then Eligible for Loan (Logical operator)
has_high_income = True
has_good_credit = True
has_criminal_record = True

if has_high_income and has_good_credit and not has_criminal_record:
    print("Eligible for Loan")
else:
    print("Not Eligible for Loan")

# and >> both condition should be true
# or  >>  one statement should be true
# NOT >> inverses the boolean value
