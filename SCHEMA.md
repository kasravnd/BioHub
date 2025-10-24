# BioAwesome Database Schema Documentation

## Overview

BioAwesome uses a structured JSON schema to capture comprehensive information about biological databases, including their relationships and roles within the broader bioinformatics ecosystem.

## Schema File

The complete schema definition is available in [`schema.json`](schema.json), which includes:
- Field definitions and types
- Category descriptions
- Database type classifications
- Known federations and consortia

## Database Entry Structure

### Required Fields

#### `name` (string)
Full official name of the database.
```json
"name": "Gene Expression Omnibus"
```

#### `url` (string, URI format)
Primary website URL for the database.
```json
"url": "https://www.ncbi.nlm.nih.gov/geo"
```

#### `description` (string, 50-1000 characters)
Clear, concise description (2-3 sentences) explaining what the database contains and its purpose.
```json
"description": "A public repository for high-throughput functional genomics data..."
```

#### `category` (string, enum)
Primary category for the database. Valid values:
- `genomics`
- `proteomics`
- `pathways`
- `metabolomics`
- `ontologies`
- `literature`
- `clinical-medical`
- `model-organisms`
- `structural-biology`
- `tools-resources`

```json
"category": "genomics"
```

#### `data_types` (array of strings)
Types of data available in the database.
```json
"data_types": [
  "gene expression data",
  "microarray data",
  "RNA-seq data"
]
```

### Recommended Fields

#### `abbreviation` (string)
Common abbreviation or acronym.
```json
"abbreviation": "GEO"
```

#### `access` (array of strings)
Methods available for accessing the database.
Valid values: `web`, `API`, `download`, `FTP`, `CLI`

```json
"access": ["web", "API", "download", "FTP"]
```

#### `license` (string)
Data license or usage terms.
```json
"license": "Open access (public domain)"
```

#### `organism` (string)
Target organisms (if specific to certain species).
```json
"organism": "All organisms"
```

#### `format` (array of strings)
Data formats available for download or access.
```json
"format": ["SOFT", "MINiML", "TSV", "FASTQ"]
```

#### `updated` (string)
Maintenance status or update frequency.
```json
"updated": "Daily updates"
```

#### `documentation` (string, URI format)
Link to official documentation.
```json
"documentation": "https://www.ncbi.nlm.nih.gov/geo/info"
```

#### `api_docs` (string, URI format)
API documentation URL.
```json
"api_docs": "https://www.ncbi.nlm.nih.gov/geo/info/geo_paccess.html"
```

### Optional Fields

#### `subcategories` (array of strings)
Additional categories or subcategories this database fits into.
```json
"subcategories": ["functional-genomics", "transcriptomics"]
```

#### `references` (array of strings)
Key publications in PMID or DOI format.
```json
"references": ["PMID:33290552", "DOI:10.1093/nar/gkaa1100"]
```

#### `funding` (string)
Funding sources.
```json
"funding": "NCBI, NLM, NIH"
```

#### `contact` (string)
Contact information or support email.
```json
"contact": "geo-help@ncbi.nlm.nih.gov"
```

#### `tutorials` (array of strings)
Tutorial or guide URLs.
```json
"tutorials": ["https://example.org/tutorial"]
```

#### `use_cases` (array of strings)
Example research applications.
```json
"use_cases": [
  "Meta-analysis of gene expression",
  "Biomarker discovery"
]
```

### Relationship Fields

These fields capture the database's position within the bioinformatics ecosystem.

#### `parent` (string)
Parent organization or consortium.
```json
"parent": "INSDC"
```

#### `member_of` (array of strings)
Federations or collaborations this database is part of.
```json
"member_of": ["INSDC", "ELIXIR"]
```

#### `curated_from` (array of strings)
Primary archives this knowledgebase draws from.
```json
"curated_from": ["GenBank", "ENA", "DDBJ"]
```

#### `integrates` (array of strings)
Other databases integrated by this meta-database.
```json
"integrates": ["Pfam", "PROSITE", "SMART"]
```

#### `mirrors` (array of strings)
Mirror sites or regional portals.
```json
"mirrors": ["ENA", "DDBJ"]
```

#### `related_to` (array of strings)
Related or complementary databases.
```json
"related_to": ["STRING", "Reactome"]
```

#### `data_type_analog` (string)
Analogous database in a different domain.
```json
"data_type_analog": "GEO"
```
Example: PRIDE is to proteomics what GEO is to genomics.

#### `database_type` (string)
Classification of the database's role. Valid values:
- `primary_archive` - Raw, minimally annotated data from researchers
- `curated_knowledgebase` - Manually reviewed, richly annotated data
- `integrative_meta_database` - Aggregates data from multiple sources
- `genome_browser` - Visualization and integration platform

```json
"database_type": "primary_archive"
```

## Database Types

### Primary Archives
Repositories for raw, unprocessed, or minimally annotated data submitted directly by researchers.
**Examples:** GenBank, GEO, PRIDE, MetaboLights

### Curated Knowledgebases
Value-added resources with non-redundant, manually reviewed, and richly annotated data.
**Examples:** RefSeq, UniProtKB/Swiss-Prot, Reactome

### Integrative Meta-Databases
Resources that aggregate data from numerous databases to provide unified access.
**Examples:** InterPro, STRING

### Genome Browsers
Visualization and integration platforms for genomic data.
**Examples:** UCSC Genome Browser, Ensembl

## Category Structure

Categories may have subcategories for more granular organization:

```
genomics/
├── nucleotide-archives/
├── gene-annotation/
├── genome-browsers/
├── genetic-variation/
└── functional-genomics/

proteomics/
├── protein-sequences/
├── protein-families/
├── protein-structures/
└── proteomics-experiments/

pathways/
├── biological-pathways/
└── molecular-interactions/

metabolomics/
├── chemical-databases/
├── metabolite-databases/
├── drug-databases/
└── metabolomics-experiments/
```

## Understanding Relationships

### Federations
Some databases are part of global collaborations:
- **INSDC**: GenBank, ENA, DDBJ (nucleotide sequences)
- **wwPDB**: RCSB PDB, PDBe, PDBj (protein structures)
- **UniProt**: Swiss-Prot, TrEMBL, UniParc (protein data)

### Curation Hierarchy
Data flows from raw archives to curated knowledgebases:
- Raw sequences (GenBank) → Curated references (RefSeq)
- Raw variants (dbSNP) → Clinical interpretations (ClinVar)
- Predicted proteins (TrEMBL) → Reviewed proteins (Swiss-Prot)

### Integration
Meta-databases combine multiple resources:
- InterPro integrates: Pfam, PROSITE, SMART, PANTHER, CDD, and 8 others
- STRING integrates: BioGRID, IntAct, KEGG, Reactome, and more

### Data Type Analogs
Similar roles across different domains:
- **Genomics**: GEO (gene expression experiments)
- **Proteomics**: PRIDE (mass spectrometry experiments)
- **Metabolomics**: MetaboLights (metabolomics experiments)

## Complete Example

```json
{
  "name": "Gene Expression Omnibus",
  "abbreviation": "GEO",
  "url": "https://www.ncbi.nlm.nih.gov/geo",
  "description": "A public repository for high-throughput functional genomics data, including gene expression, methylation, and chip-seq data.",
  "category": "genomics",
  "subcategories": ["functional-genomics"],
  "data_types": [
    "gene expression data",
    "microarray data",
    "RNA-seq data",
    "ChIP-seq data"
  ],
  "access": ["web", "API", "download", "FTP"],
  "license": "Open access (public domain)",
  "organism": "All organisms",
  "format": ["SOFT", "MINiML", "TSV", "FASTQ", "CEL"],
  "updated": "Daily updates",
  "documentation": "https://www.ncbi.nlm.nih.gov/geo/info",
  "api_docs": "https://www.ncbi.nlm.nih.gov/geo/info/geo_paccess.html",
  "references": ["PMID:33290552"],
  "funding": "NCBI, NLM, NIH",
  "use_cases": [
    "Meta-analysis of gene expression",
    "Differential expression analysis",
    "Biomarker discovery"
  ],
  "related_to": ["ArrayExpress", "SRA"],
  "data_type_analog": "PRIDE",
  "database_type": "primary_archive"
}
```

## Validation

Use the validation script to check your entries:

```bash
python scripts/validate.py
```

The validator checks for:
- Valid JSON syntax
- Required fields present
- Valid URLs
- Correct category assignments
- Proper field types

## See Also

- [Contributing Guidelines](CONTRIBUTING.md)
- [Quick Start Guide](QUICKSTART.md)
- [Schema Definition](schema.json)
