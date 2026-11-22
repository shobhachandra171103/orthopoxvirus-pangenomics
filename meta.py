import pandas as pd
import os

matrix_file = "panaroo_results/gene_presence_absence.csv"
metadata_file = "metadata.csv"

if not os.path.exists(matrix_file):
    print(f"Error: {matrix_file} not found!")
elif not os.path.exists(metadata_file):
    print(f"Error: {metadata_file} not found!")
else:
    df = pd.read_csv(matrix_file, low_memory=False)
    metadata = pd.read_csv(metadata_file)

    # 1. Identify which columns are samples
    # We ignore the standard info columns
    info_cols = ['Gene', 'Non-unique Gene name', 'Annotation']
    sample_cols = [c for c in df.columns if c not in info_cols]
    
    # 2. Get groups from metadata
    mpxv_samples = metadata[metadata['Group'] == 'MPXV']['Sample'].tolist()
    other_samples = metadata[metadata['Group'] != 'MPXV']['Sample'].tolist()

    # Ensure these samples actually exist in our CSV columns
    mpxv_in_df = [s for s in mpxv_samples if s in df.columns]
    other_in_df = [s for s in other_samples if s in df.columns]

    print(f"Found {len(mpxv_in_df)} MPXV samples and {len(other_in_df)} Other samples in the matrix.")

    if len(mpxv_in_df) == 0:
        print("Warning: No samples labeled 'MPXV' found in the matrix. Check your metadata.csv labels!")

    # 3. Calculate "Isolate Count" manually
    # Panaroo fills cells with the gene ID if present, and leaves them NaN/Empty if absent
    df['calculated_count'] = df[sample_cols].notnull().sum(axis=1)

    # 4. Extract Core Genes (present in >99% of total samples)
    total_samples = len(sample_cols)
    core_threshold = total_samples * 0.99
    core_genes = df[df['calculated_count'] >= core_threshold]
    core_genes.to_csv("Core_Orthopox_genes.csv", index=False)
    print(f"Saved {len(core_genes)} core genes to 'Core_Orthopox_genes.csv'")

    # 5. Extract MPXV-Specific Genes
    # Present in at least one MPXV AND absent in ALL others
    if len(mpxv_in_df) > 0 and len(other_in_df) > 0:
        mpxv_spec = df[
            (df[mpxv_in_df].notnull().any(axis=1)) & 
            (df[other_in_df].isnull().all(axis=1))
        ]
        mpxv_spec.to_csv("MPXV_specific_genes.csv", index=False)
        print(f"Saved {len(mpxv_spec)} MPXV-specific genes to 'MPXV_specific_genes.csv'")
    else:
        print("Skipping MPXV-specific extraction: Missing group data.")