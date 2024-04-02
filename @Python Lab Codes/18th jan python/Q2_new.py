import pandas as pd


df = pd.read_csv('New_Q1_output_file.csv')


output_dict = {}


for index, row in df.iterrows():
    entry_id = row['Entry ID']
    accession_codes = row['Accession Code(s)'].split(',')
    pairs = [[accession_codes[i], accession_codes[(i + 1) % len(accession_codes)]] for i in range(len(accession_codes))]
    output_dict[entry_id] = pairs
    print(f"{entry_id}: {pairs}")


#dictionary to a DataFrame
output_df = pd.DataFrame(list(output_dict.items()), columns=['Entry ID', 'Pairs of Acession Code(s)'])
print ("\n\n\nThe out put files row number:",len(output_df))

output_df.to_csv('New_Q2_output_file.csv', index=False)
