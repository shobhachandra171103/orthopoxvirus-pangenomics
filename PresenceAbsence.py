import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Since you are ALREADY in the panaroo_results folder, use the direct filename
try:
    df = pd.read_csv('gene_presence_absence.csv', low_memory=False)
    print("File loaded successfully!")
    
    # Extract presence/absence matrix (columns 13 onwards are samples)
    pa_matrix = df.iloc[:, 12:].notnull().astype(int)

    # Filter for "Shell" variation (present in >1% and <99% of genomes)
    n_samples = pa_matrix.shape[1]
    variation_filter = (pa_matrix.sum(axis=1) < (n_samples * 0.99)) & (pa_matrix.sum(axis=1) > (n_samples * 0.01))
    filtered_matrix = pa_matrix[variation_filter]

    plt.figure(figsize=(25, 12))
    # 'rasterized=True' ensures the dots show up in the image
    sns.heatmap(filtered_matrix, cmap="Greens", cbar=False, xticklabels=False, yticklabels=False, rasterized=True)

    plt.title(f'Pangenome Family Partition: Shell Genome ({filtered_matrix.shape[0]} genes)')
    plt.xlabel(f'Genomes (n={n_samples})')
    plt.ylabel('Accessory Genes')
    
    plt.savefig('Pangenome_Partition_Plot.png', dpi=300, bbox_inches='tight')
    print("Graph saved as Pangenome_Partition_Plot.png")

except FileNotFoundError:
    print("Error: Could not find gene_presence_absence.csv. Are you sure you are in the panaroo_results folder?")