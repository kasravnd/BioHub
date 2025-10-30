# BioHub Quick Start Guide

Get started with BioHub in 5 minutes!

## For Users: Finding Databases

### 1. Browse by Category

Navigate through the [`databases/`](databases/) directory to explore databases by field:

```
databases/
├── genomics/          # Genome data
├── proteomics/        # Protein data
├── metabolomics/      # Metabolite data
├── clinical-medical/  # Disease & clinical data
└── ...
```

### 2. Search for Databases

Use the search tool to find what you need:

```bash
# Search by keyword
python3 scripts/search.py --keyword "protein"

# Filter by category
python3 scripts/search.py --category "genomics"

# Filter by organism
python3 scripts/search.py --organism "human"

# Show detailed info
python3 scripts/search.py --keyword "expression" --detailed
```

### 3. Browse the Full Catalog

View all databases with complete metadata:
- **JSON format**: [`databases/catalog.json`](databases/catalog.json)
- **By category**: See [`databases/README.md`](databases/README.md)

## For Contributors: Adding Databases

### Quick Contribution (via GitHub Issue)

1. Go to [Issues](../../issues/new/choose)
2. Select "Add Database" template
3. Fill in the database information
4. Submit!

We'll review and add it to the catalog.

### Direct Contribution (via Pull Request)

#### Step 1: Fork and Clone

```bash
# Fork the repo on GitHub, then:
git clone https://github.com/YOUR-USERNAME/BioHub.git
cd BioHub
```

#### Step 2: Create a Database Entry

Create a JSON file in the appropriate category:

```bash
# Example: adding a new genomics database
nano databases/genomics/my-database.json
```

Use this template:

```json
{
  "name": "Database Full Name",
  "abbreviation": "DBN",
  "url": "https://example.org",
  "description": "Clear, concise description (2-3 sentences).",
  "category": "genomics",
  "data_types": ["type1", "type2"],
  "access": ["web", "API", "download"],
  "license": "Open access",
  "organism": "Humans, mice",
  "format": ["FASTA", "JSON"],
  "updated": "Monthly updates",
  "documentation": "https://example.org/docs"
}
```

#### Step 3: Validate Your Entry

```bash
# Check for errors
python3 scripts/validate.py

# Update the catalog
python3 scripts/update_catalog.py

# Test your entry is searchable
python3 scripts/search.py --keyword "my-database"
```

#### Step 4: Submit Pull Request

```bash
git checkout -b add-my-database
git add databases/
git commit -m "Add My Database"
git push origin add-my-database
```

Then open a PR on GitHub!

## Database Entry Fields

### Required
- `name` - Full database name
- `url` - Website URL
- `description` - Clear description (2-3 sentences)
- `category` - Primary category
- `data_types` - Array of data types

### Recommended
- `access` - How to access (web, API, download)
- `license` - Usage terms
- `organism` - Target organisms
- `format` - Data formats available
- `documentation` - Docs URL

### Optional
- `subcategories` - Additional categories
- `abbreviation` - Common abbreviation
- `api_docs` - API documentation URL
- `references` - Publications (PMID)
- `use_cases` - Research applications
- `funding` - Funding sources
- `updated` - Maintenance status

See [CONTRIBUTING.md](CONTRIBUTING.md) for full details.

## Categories

- `genomics` - Genome sequences, variations, annotations
- `proteomics` - Protein sequences, structures, functions
- `structural-biology` - 3D structures, molecular interactions
- `metabolomics` - Metabolites, pathways, reactions
- `systems-biology` - Networks, pathways, models
- `transcriptomics` - Gene expression, RNA-seq data
- `epigenomics` - Epigenetic modifications, chromatin
- `phylogenetics` - Evolutionary relationships, taxonomy
- `clinical-medical` - Disease data, clinical trials, phenotypes
- `model-organisms` - Organism-specific databases
- `tools-resources` - Analysis tools, repositories, archives

## Tools & Scripts

### search.py
Find databases by keyword, category, data type, etc.

```bash
python3 scripts/search.py --help
```

### update_catalog.py
Regenerate the main catalog from individual files

```bash
python3 scripts/update_catalog.py
```

### validate.py
Check database entries for errors

```bash
python3 scripts/validate.py
```

## Examples

### Find protein structure databases
```bash
python3 scripts/search.py --keyword "structure" --category "structural-biology"
```

### Find human disease databases with API access
```bash
python3 scripts/search.py --organism "human" --category "clinical-medical" --access "API"
```

### Find all databases with expression data
```bash
python3 scripts/search.py --data-type "expression"
```

## Getting Help

- **Questions?** Open an [issue](../../issues)
- **Ideas?** Start a [discussion](../../discussions)
- **Problems?** Check [CONTRIBUTING.md](CONTRIBUTING.md)

## Community

BioHub is community-driven! We welcome:
- Database additions and updates
- Documentation improvements
- New features and tools
- Bug reports
- Suggestions

See you in the issues and pull requests!

---

**Happy database hunting!**
