# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
from pathlib import Path
import sys
def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(qualifying_loans, output_path):
    """
    Desc: This function saves all the filtered results,
    in a file with .csv type format in a path 
    that you specify your local computer.
    
    Args:
        qualifying_loans (list[lists]): Has all the data to be saved.
        output_path (string): Has the final location for it to be saved.
    
    Output:
        None There is no output. The file is simply saved to disk.
    
    """
    ## check if it is the correct type.
    if type(qualifying_loans) != list:
        sys.exit("Type error")
    
    
    # Checking for qualifying loans.
    if len(qualifying_loans) == 0:
        sys.exit("Oops! There seems to be no qualifying loans, Exiting the program now.")
    
    # creating a path
    csvpath = Path(output_path)
    # naming the header.
    header = ["bank_data", "credit_score", "debt", "income", "loan_amount", "home_value"] 
    
    # writing the list of lists as a csv.
    with open(csvpath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
    
        # Write our header row first!
        csvwriter.writerow(header)
    
        # Then we can write the data rows
        for row in qualifying_loans:
                csvwriter.writerow(row)