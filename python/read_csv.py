######################################################################
Author: Shantanu V. Deshmukh 
######################################################################
import pandas as pd

# note the r is for making the filename raw string sometimes filename is large and 
# pd.read_csv cannot read it, so in order to make the filename readble by interpretor
# we use the r prefix there

df_name = \
    pd.read_csv(r"csv_filepath.csv", index_col=None, header=0, sep=",")
    
