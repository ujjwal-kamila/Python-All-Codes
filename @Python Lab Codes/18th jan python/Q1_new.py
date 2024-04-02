import pandas as pd

df = pd.read_csv('file.csv')

df["Entry ID"] = df["Entry ID"].ffill()

df.dropna(subset=['Accession Code(s)'], inplace=True)


df['Accession Code(s)'] = df['Accession Code(s)'].str.split(',')
df = df.explode('Accession Code(s)')


#df['Source Organism'] = df['Source Organism'].str.split(',')
df = df.explode('Source Organism')


df_hs = df[df['Source Organism'] == 'Homo sapiens']
df_homo_sapiens = df_hs.drop_duplicates()


df_new = df_homo_sapiens.groupby("Entry ID", sort=False).agg({"Source Organism": "first","Accession Code(s)": lambda x: ','.join(x)})


df_new2 = df_new[df_new['Accession Code(s)'].apply(lambda x: x.count(',') == 2)]


print("The "len(df_new2))

print(df_new2.head(10))


df_new2.to_csv('New_Q1_output_file.csv', index=True)



