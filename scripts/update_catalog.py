#!/usr/bin/env python3
"""
Update the main catalog.json file from individual database JSON files.

This script scans all category directories and aggregates individual
database JSON files into the main catalog.json file.
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any


def load_database_file(file_path: Path) -> Dict[str, Any]:
    """Load and validate a database JSON file."""
    try:
        with open(file_path, 'r') as f:
            db = json.load(f)

        # Validate required fields
        required_fields = ['name', 'url', 'description', 'category']
        missing_fields = [field for field in required_fields if field not in db]

        if missing_fields:
            print(f"Warning: {file_path} missing required fields: {missing_fields}")
            return None

        return db

    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in {file_path}: {e}")
        return None
    except Exception as e:
        print(f"Error: Could not read {file_path}: {e}")
        return None


def scan_databases(databases_dir: Path) -> Dict[str, List[Dict[str, Any]]]:
    """Scan all category directories and collect database entries."""
    categories = {}

    # Iterate through category directories
    for category_dir in databases_dir.iterdir():
        if not category_dir.is_dir() or category_dir.name.startswith('.'):
            continue

        category_name = category_dir.name
        categories[category_name] = []

        # Load all JSON files in the category
        for json_file in category_dir.glob('*.json'):
            db = load_database_file(json_file)
            if db:
                categories[category_name].append(db)

    return categories


def update_catalog(databases_dir: Path, catalog_path: Path):
    """Update the main catalog.json file."""
    print("Scanning database files...")

    # Load existing catalog to preserve category descriptions
    category_descriptions = {}
    if catalog_path.exists():
        try:
            with open(catalog_path, 'r') as f:
                existing_catalog = json.load(f)
                for cat_id, cat_info in existing_catalog.get('categories', {}).items():
                    category_descriptions[cat_id] = {
                        'name': cat_info.get('name', cat_id.title()),
                        'description': cat_info.get('description', '')
                    }
        except Exception as e:
            print(f"Warning: Could not load existing catalog: {e}")

    # Scan databases
    databases_by_category = scan_databases(databases_dir)

    # Build new catalog
    catalog = {
        'version': '1.0.0',
        'last_updated': datetime.now().strftime('%Y-%m-%d'),
        'total_databases': sum(len(dbs) for dbs in databases_by_category.values()),
        'categories': {}
    }

    # Add categories and databases
    for category_id, databases in sorted(databases_by_category.items()):
        # Use existing description if available, otherwise use a default
        cat_info = category_descriptions.get(category_id, {
            'name': category_id.replace('-', ' ').title(),
            'description': f'Databases in the {category_id} category'
        })

        catalog['categories'][category_id] = {
            'name': cat_info['name'],
            'description': cat_info['description'],
            'count': len(databases),
            'databases': sorted(databases, key=lambda x: x['name'].lower())
        }

        print(f"  {category_id}: {len(databases)} database(s)")

    # Write updated catalog
    print(f"\nWriting catalog to {catalog_path}...")
    with open(catalog_path, 'w') as f:
        json.dump(catalog, f, indent=2, ensure_ascii=False)

    print(f"\nCatalog updated successfully!")
    print(f"Total databases: {catalog['total_databases']}")
    print(f"Categories: {len(catalog['categories'])}")


def main():
    # Find the databases directory
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    databases_dir = repo_root / 'databases'
    catalog_path = databases_dir / 'catalog.json'

    if not databases_dir.exists():
        print(f"Error: Databases directory not found at {databases_dir}")
        return 1

    update_catalog(databases_dir, catalog_path)
    return 0


if __name__ == '__main__':
    exit(main())
