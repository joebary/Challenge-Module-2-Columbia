
# pytest
import pytest

# Import pathlib
from pathlib import Path

#Import fileio
from qualifier.utils import fileio

# Import Calculators
from qualifier.utils import calculators

#importing the os
import os

# Import Filters
from qualifier.filters import credit_score
from qualifier.filters import debt_to_income
from qualifier.filters import loan_to_value
from qualifier.filters import max_loan_size

# import the csv function from file.io
from qualifier.utils.fileio import save_csv



def test_save_csv():
    # @TODO: Your code here!
    # Use Path from pathlib to output the test csv to ./data/output/qualifying_loans.csv
    data1 = [["West Central Credit Union - Premier Option",400000,0.9,0.35,760,2.7],
             ["Joe bank",100000,0.8,0.25,750,2.0]
             ] 
    
    # checking for no data behavior.
    data2 = [[]]
    
    # actual test.
    save_csv(data1, "./data/output/qualifying_loans.csv")
    # asserting the path.
    assert Path('./data/output/qualifying_loans_test.csv').exists() == True
    # removing the file post testing.
    os.remove("./data/output/qualifying_loans_test.csv")
    # giving an update.
    print("File saved & Tested successfully, File Removed!")
    

    save_csv(data2, "./data/output/qualifying_loans.csv")
    assert not Path('./data/output/qualifying_loans_test2.csv').exists() == True
    

def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84

def test_filters():
    bank_data = fileio.load_csv(Path('./data/daily_rate_sheet.csv'))
    current_credit_score = 750
    debt = 1500
    income = 4000
    loan = 210000
    home_value = 250000

    monthly_debt_ratio = 0.375

    loan_to_value_ratio = 0.84


    # testing the calculate monthly debt function
    test_calculate_monthly_debt_ratio()
    
    # testing the calc loan to val function.
    test_calculate_loan_to_value_ratio()
    
    
    # Test the new save_csv code!
    test_save_csv()
