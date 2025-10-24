# BioAwesome Scripts

Utility scripts for managing and searching the BioAwesome database catalog.

## Available Scripts

### search.py

Search and filter databases from the catalog.

**Usage:**
```bash
# Search by keyword
python scripts/search.py --keyword "protein"

# Filter by category
python scripts/search.py --category "genomics"

# Filter by data type
python scripts/search.py --data-type "variants"

# Filter by organism
python scripts/search.py --organism "human"

# Filter by access method
python scripts/search.py --access "API"

# Show detailed information
python scripts/search.py --keyword "expression" --detailed

# Combine multiple filters
python scripts/search.py --category "genomics" --organism "human" --access "API"

# List all categories
python scripts/search.py --list-categories
```

**Options:**
- `--keyword, -k`: Search keyword (searches name, description, data types)
- `--category, -c`: Filter by category
- `--data-type, -d`: Filter by data type
- `--organism, -o`: Filter by organism
- `--access, -a`: Filter by access method (web, API, download)
- `--detailed, -v`: Show detailed information
- `--list-categories`: List all available categories

### update_catalog.py

Update the main catalog.json file from individual database JSON files.

**Usage:**
```bash
python scripts/update_catalog.py
```

Run this script after adding or modifying database entries to update the main catalog.

**What it does:**
- Scans all category directories
- Loads individual database JSON files
- Validates required fields
- Updates the main catalog.json with aggregated data
- Preserves category descriptions

### validate.py

Validate database JSON files for correctness and completeness.

**Usage:**
```bash
python scripts/validate.py
```

**Checks performed:**
- Valid JSON syntax
- Required fields present
- Valid URL formats
- Consistent category assignments
- Data type and access method formats
- Description length recommendations

**Output:**
- Lists all errors (must be fixed)
- Lists all warnings (recommendations)
- Provides validation summary

## Requirements

All scripts use only Python standard library, no additional dependencies required.

**Python version:** 3.6+

## For Contributors

### Adding a Database

1. Create a JSON file in the appropriate category directory
2. Follow the database entry format (see CONTRIBUTING.md)
3. Run validation: `python scripts/validate.py`
4. Update catalog: `python scripts/update_catalog.py`
5. Test search: `python scripts/search.py --keyword "your-database"`

### Before Submitting a PR

```bash
# Validate all entries
python scripts/validate.py

# Update the catalog
python scripts/update_catalog.py

# Test your database is searchable
python scripts/search.py --keyword "your-database-name"
```

## Examples

### Find all protein databases
```bash
python scripts/search.py --keyword "protein" --detailed
```

### Find genomics databases with API access
```bash
python scripts/search.py --category "genomics" --access "API"
```

### Find human disease databases
```bash
python scripts/search.py --organism "human" --category "clinical-medical"
```

### Search for expression data
```bash
python scripts/search.py --data-type "expression"
```
