import pandas as pd

# Load the actual headers from Panaroo
df = pd.read_csv("panaroo_results/gene_presence_absence.csv", nrows=0)
all_samples = [c for c in df.columns if c not in ['Gene', 'Non-unique Gene name', 'Annotation']]

# Common MPXV accession prefixes or strings to look for
# (Adjust this list if you know your MPXV samples have specific IDs)
mpxv_keywords = ['ON', 'OP', 'OQ', 'NC_063383', 'DQ', 'KJ'] 

metadata = []
for s in all_samples:
    # Logic: If it starts with common MPXV prefixes, label as MPXV
    if any(s.startswith(k) for k in mpxv_keywords):
        metadata.append([s, 'MPXV'])
    else:
        metadata.append([s, 'Other_OPV'])

meta_df = pd.DataFrame(metadata, columns=['Sample', 'Group'])
meta_df.to_csv("metadata.csv", index=False)
print(f"Created metadata.csv with {len(meta_df[meta_df['Group']=='MPXV'])} MPXV samples.")
