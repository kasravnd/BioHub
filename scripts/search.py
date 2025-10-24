#!/usr/bin/env python3
"""
BioAwesome Database Search Tool

Search and filter biological databases from the BioAwesome catalog.
"""

import json
import argparse
import os
from pathlib import Path
from typing import List, Dict, Any


def load_catalog(catalog_path: str) -> Dict[str, Any]:
    """Load the database catalog."""
    with open(catalog_path, 'r') as f:
        return json.load(f)


def load_databases_from_files(databases_dir: str) -> List[Dict[str, Any]]:
    """Load all database entries from individual JSON files."""
    databases = []
    databases_path = Path(databases_dir)

    # Iterate through category directories
    for category_dir in databases_path.iterdir():
        if category_dir.is_dir() and not category_dir.name.startswith('.'):
            # Iterate through JSON files in each category
            for json_file in category_dir.glob('*.json'):
                try:
                    with open(json_file, 'r') as f:
                        db = json.load(f)
                        databases.append(db)
                except Exception as e:
                    print(f"Warning: Could not load {json_file}: {e}")

    return databases


def search_databases(
    databases: List[Dict[str, Any]],
    keyword: str = None,
    category: str = None,
    data_type: str = None,
    organism: str = None,
    access_method: str = None
) -> List[Dict[str, Any]]:
    """Search databases based on various criteria."""
    results = databases

    if keyword:
        keyword_lower = keyword.lower()
        results = [
            db for db in results
            if keyword_lower in db.get('name', '').lower()
            or keyword_lower in db.get('description', '').lower()
            or keyword_lower in db.get('abbreviation', '').lower()
            or any(keyword_lower in dt.lower() for dt in db.get('data_types', []))
        ]

    if category:
        category_lower = category.lower()
        results = [
            db for db in results
            if db.get('category', '').lower() == category_lower
            or any(category_lower == sc.lower() for sc in db.get('subcategories', []))
        ]

    if data_type:
        data_type_lower = data_type.lower()
        results = [
            db for db in results
            if any(data_type_lower in dt.lower() for dt in db.get('data_types', []))
        ]

    if organism:
        organism_lower = organism.lower()
        results = [
            db for db in results
            if organism_lower in db.get('organism', '').lower()
        ]

    if access_method:
        access_lower = access_method.lower()
        results = [
            db for db in results
            if any(access_lower == acc.lower() for acc in db.get('access', []))
        ]

    return results


def format_database_output(db: Dict[str, Any], detailed: bool = False) -> str:
    """Format database information for display."""
    output = []

    # Header
    name = db.get('name', 'Unknown')
    abbr = db.get('abbreviation', '')
    header = f"\n{'='*70}\n"
    if abbr and abbr != name:
        header += f"{name} ({abbr})\n"
    else:
        header += f"{name}\n"
    header += f"{'='*70}"
    output.append(header)

    # URL
    if 'url' in db:
        output.append(f"URL: {db['url']}")

    # Category
    category = db.get('category', 'Unknown')
    output.append(f"Category: {category}")

    # Description
    if 'description' in db:
        output.append(f"\nDescription:\n{db['description']}")

    if detailed:
        # Data types
        if 'data_types' in db:
            output.append(f"\nData Types:\n  - " + "\n  - ".join(db['data_types']))

        # Access methods
        if 'access' in db:
            output.append(f"\nAccess: {', '.join(db['access'])}")

        # Organism
        if 'organism' in db:
            output.append(f"Organisms: {db['organism']}")

        # License
        if 'license' in db:
            output.append(f"License: {db['license']}")

        # Formats
        if 'format' in db:
            output.append(f"Formats: {', '.join(db['format'])}")

        # Documentation
        if 'documentation' in db:
            output.append(f"\nDocumentation: {db['documentation']}")

        # API docs
        if 'api_docs' in db:
            output.append(f"API Documentation: {db['api_docs']}")

        # Use cases
        if 'use_cases' in db:
            output.append(f"\nUse Cases:\n  - " + "\n  - ".join(db['use_cases']))

    return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(
        description='Search BioAwesome database catalog',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --keyword "protein"
  %(prog)s --category "genomics"
  %(prog)s --data-type "variants"
  %(prog)s --keyword "expression" --organism "human"
  %(prog)s --access "API" --detailed
        """
    )

    parser.add_argument(
        '--keyword', '-k',
        help='Search keyword (searches name, description, data types)'
    )
    parser.add_argument(
        '--category', '-c',
        help='Filter by category (e.g., genomics, proteomics)'
    )
    parser.add_argument(
        '--data-type', '-d',
        help='Filter by data type'
    )
    parser.add_argument(
        '--organism', '-o',
        help='Filter by organism'
    )
    parser.add_argument(
        '--access', '-a',
        help='Filter by access method (web, API, download)'
    )
    parser.add_argument(
        '--detailed', '-v',
        action='store_true',
        help='Show detailed information for each database'
    )
    parser.add_argument(
        '--list-categories',
        action='store_true',
        help='List all available categories'
    )

    args = parser.parse_args()

    # Find the databases directory (relative to script location)
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    databases_dir = repo_root / 'databases'
    catalog_path = databases_dir / 'catalog.json'

    if args.list_categories:
        if catalog_path.exists():
            catalog = load_catalog(catalog_path)
            print("\nAvailable Categories:")
            print("=" * 70)
            for cat_id, cat_info in catalog.get('categories', {}).items():
                print(f"\n{cat_info['name']} ({cat_id})")
                print(f"  {cat_info['description']}")
        return

    # Load databases from individual files
    databases = load_databases_from_files(databases_dir)

    if not databases:
        print("No databases found in the catalog.")
        return

    # Search databases
    results = search_databases(
        databases,
        keyword=args.keyword,
        category=args.category,
        data_type=args.data_type,
        organism=args.organism,
        access_method=args.access
    )

    # Display results
    if not results:
        print("No databases found matching your criteria.")
        return

    print(f"\nFound {len(results)} database(s):")
    for db in results:
        print(format_database_output(db, detailed=args.detailed))

    print(f"\n{'='*70}")
    print(f"Total: {len(results)} database(s)")


if __name__ == '__main__':
    main()
