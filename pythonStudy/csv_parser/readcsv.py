#!/usr/bin/python

import numpy as np
import pandas as pd

input_file = "mydata.csv"


# comma delimited is the default
df = pd.read_csv(input_file, header = 0)

# for space delimited use:
# df = pd.read_csv(input_file, header = 0, delimiter = " ")

# for tab delimited use:
# df = pd.read_csv(input_file, header = 0, delimiter = "\t")

# put the original column names in a python list
original_headers = list(df.columns.values)

# remove the non-numeric columns
df = df._get_numeric_data()

# put the numeric column names in a python list
numeric_headers = list(df.columns.values)

# create a numpy array with the numeric values for input into scikit-learn
numpy_array = df.as_matrix()

# reverse the order of the columns
numeric_headers.reverse()
reverse_df = df[numeric_headers]

print numpy_array
# write the reverse_df to an excel spreadsheet
#reverse_df.to_excel('path_to_file.xls')
