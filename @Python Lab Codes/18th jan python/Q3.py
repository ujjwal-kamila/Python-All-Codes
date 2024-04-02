import pandas as pd

data = pd.read_csv("file.csv")
file2 = "e_file2.csv"
df2 = pd.read_csv(file2, header=None, names=["Accession1", "Accession2"])
matching_pairs = pd.DataFrame(columns=["Accession1", "Accession2"])
for _, row in data.iterrows():
    accessions = set(row["Accession Code(s)"].split(','))
    matching_rows = df2[df2.isin(accessions).any(axis=1)]
    if not matching_rows.empty:
        matching_pairs = pd.concat([matching_pairs, matching_rows])
matching_pairs = matching_pairs.drop_duplicates()
matching_pairs.to_csv("matching_pairs.csv", index=False)
