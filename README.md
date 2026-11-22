# Orthopoxvirus Pangenomics & Phylogenetics (`orthopoxvirus-pangenomics`)

> **Objective 2** of the B.Sc. (Life Sciences) 4th-Year Dissertation: *"Multi-Scale Genomic Architecture of Monkeypox Virus Human Adaptation: Mutation Hotspots, Structural Variants, and Ortholog Divergence in Sustained-Transmission Lineages"* (Department of Zoology, Deshbandhu College, University of Delhi, 2026).

## Overview

This repository documents the comparative pangenome and evolutionary workflow across **1,525 *Orthopoxvirus* genomes**, combining pangenome graph reconstruction and partition analysis with maximum-likelihood phylogenetic inference to examine gene presence/absence, core vs. accessory/shell/cloud gene compartments, and evolutionary relationships.

## Dataset & Scope

* **Cohort Size:** **1,525** *Orthopoxvirus* genomes.
* **Annotation Inputs:** Annotated gene/protein feature files (`.gff` / `.gbk` / `.faa`) prepared for pangenome comparison.

## Methodology Pipeline

1. **Genome Annotation & Standardization:**
   * Standardize input assemblies and gene annotations across the 1,525 *Orthopoxvirus* genomes.
2. **Pangenome Graph & Partition Analysis:**
   * Reconstruct gene families and pangenome graphs using **Panaroo** and **PPanGGOLiN** to classify core, shell, and cloud/accessory gene sets.
3. **Phylogenetic Inference & Visualization:**
   * Align core/shared markers and infer Maximum Likelihood (ML) phylogenies using **IQ-TREE** / **IQ-TREE 2**.
   * Generate summary tables and visualizations in Python and R (`ggplot2` / `ComplexHeatmap` / `circlize`).

## Repository Structure

```text
orthopoxvirus-pangenomics/
├── README.md
├── scripts/          # Bash, Python, and R scripts for pangenome runs, IQ-TREE phylogeny, and plotting
├── results/          # Summary tables and generated figures
└── docs/             # Workflow notes and parameter logs
