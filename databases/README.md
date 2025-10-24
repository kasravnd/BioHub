# Database Catalog

This directory contains the curated catalog of biological databases organized by category.

## Structure

Each database has a JSON file in its primary category directory:

```
databases/
├── catalog.json              # Complete catalog with all databases
├── genomics/
│   ├── ensembl.json
│   ├── genbank.json
│   └── ...
├── proteomics/
│   ├── uniprot.json
│   ├── pfam.json
│   └── ...
└── ...
```

## Categories

### Genomics
Genome sequences, variations, annotations, and comparative genomics
- Example databases: Ensembl, GenBank, UCSC Genome Browser, dbSNP

### Proteomics
Protein sequences, structures, functions, and interactions
- Example databases: UniProt, Pfam, InterPro, STRING

### Structural Biology
3D structures, molecular interactions, and structural data
- Example databases: PDB, SCOP, CATH, AlphaFold DB

### Metabolomics
Metabolites, metabolic pathways, and biochemical reactions
- Example databases: KEGG, MetaboLights, HMDB, METLIN

### Systems Biology
Biological networks, pathways, and computational models
- Example databases: Reactome, WikiPathways, BioModels, PathwayCommons

### Transcriptomics
Gene expression, RNA-seq data, and transcriptional regulation
- Example databases: GEO, ArrayExpress, GTEx, ENCODE

### Epigenomics
Epigenetic modifications, chromatin states, and DNA methylation
- Example databases: ENCODE, Roadmap Epigenomics, IHEC, MethBase

### Phylogenetics
Evolutionary relationships, taxonomy, and phylogenetic trees
- Example databases: NCBI Taxonomy, TreeBASE, OrthoMCL, PhylomeDB

### Clinical & Medical
Disease data, clinical trials, phenotypes, and medical genetics
- Example databases: ClinVar, OMIM, DisGeNET, ClinicalTrials.gov

### Model Organisms
Organism-specific databases and resources
- Example databases: FlyBase, WormBase, SGD, MGI, TAIR

### Tools & Resources
Analysis tools, data repositories, and general resources
- Example databases: NCBI, EBI, ExPASy, Galaxy

## Database Entry Format

Each database is stored as a JSON file with the following structure:

```json
{
  "name": "Database Full Name",
  "abbreviation": "DBN",
  "url": "https://example.org",
  "description": "Clear description of the database",
  "category": "primary-category",
  "subcategories": ["additional", "categories"],
  "data_types": ["type1", "type2"],
  "access": ["web", "API", "download"],
  "license": "License information",
  "organism": "Target organisms",
  "format": ["format1", "format2"],
  "updated": "Maintenance status",
  "references": ["PMID:12345678"],
  "api_docs": "https://api.example.org",
  "documentation": "https://docs.example.org"
}
```

See [CONTRIBUTING.md](../CONTRIBUTING.md) for detailed field descriptions.

## Adding a Database

1. Create a JSON file in the appropriate category directory
2. Follow the database entry format
3. Run `python scripts/update_catalog.py` to update the main catalog
4. Submit a pull request

Or use the GitHub issue template to submit a database for inclusion.

## Searching

Use the search script to find databases:

```bash
# Search by keyword
python scripts/search.py --keyword "protein"

# Search by category
python scripts/search.py --category "genomics"

# Search by data type
python scripts/search.py --data-type "variants"

# Combine filters
python scripts/search.py --keyword "expression" --organism "human"
```
