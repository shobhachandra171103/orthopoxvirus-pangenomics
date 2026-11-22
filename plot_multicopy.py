
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

try:
    df = pd.read_csv('gene_presence_absence.csv', low_memory=False)
    
    # 1. Count function
    def count_copies(val):
        if pd.isna(val) or val == "": return 0
        return len(str(val).split('\t'))

    # 2. Use .map() instead of .applymap() for Pandas 2.1+
    # This was the cause of your error
    mc_matrix = df.iloc[:, 12:].map(count_copies)

    # 3. Filter for multicopy genes
    multicopy_filter = (mc_matrix > 1).any(axis=1)
    filtered_mc = mc_matrix[multicopy_filter]

    if filtered_mc.empty:
        print("No multicopy genes found to plot.")
    else:
        plt.figure(figsize=(24, 12))
        sns.heatmap(filtered_mc, 
                    cmap="YlOrRd", 
                    xticklabels=False, 
                    yticklabels=False, 
                    rasterized=True)

        plt.title(f'Gene Duplication Hotspots ({len(filtered_mc)} genes)')
        plt.savefig('Pangenome_Multicopy_Plot.png', dpi=300, bbox_inches='tight')
        print("Successfully saved: Pangenome_Multicopy_Plot.png")

except Exception as e:
    print(f"Error: {e}")
