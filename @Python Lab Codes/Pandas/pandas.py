# Importing numpy and pandas
import numpy as np
import pandas as pd

# Create a dict to make a data frame 
dict1 = {

    "name" :['Ujjwal', 'Raj' , 'Akash','Shubo'],
    "marks" : [91,80,72,59],
    "city" : ['kolkata','kalyani','bihar','howrah']
}

# to convert into df
df = pd.DataFrame(dict1)
print(df)
print(df.head(2))

#to do with out index
df.to_csv('friends_falseIndex.csv',index = False)

