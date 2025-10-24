#!/usr/bin/env python3
"""
Validate database JSON files for correctness and completeness.

Checks:
- Valid JSON syntax
- Required fields present
- Valid URLs
- Consistent category assignments
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Any, Tuple
from urllib.parse import urlparse


REQUIRED_FIELDS = ['name', 'url', 'description', 'category', 'data_types']
RECOMMENDED_FIELDS = ['abbreviation', 'access', 'license', 'organism', 'updated', 'documentation']
OPTIONAL_FIELDS = ['subcategories', 'references', 'funding', 'contact', 'tutorials', 'use_cases', 'api_docs']
RELATIONSHIP_FIELDS = ['parent', 'member_of', 'curated_from', 'integrates', 'mirrors', 'related_to', 'data_type_analog', 'database_type']
VALID_CATEGORIES = [
    'genomics', 'proteomics', 'pathways', 'metabolomics',
    'ontologies', 'literature', 'clinical-medical',
    'model-organisms', 'structural-biology', 'tools-resources'
]


def validate_url(url: str) -> Tuple[bool, str]:
    """Validate URL format."""
    try:
        result = urlparse(url)
        if all([result.scheme, result.netloc]):
            return True, ""
        return False, "Invalid URL format"
    except Exception as e:
        return False, f"URL validation error: {e}"


def validate_database(db: Dict[str, Any], file_path: Path) -> List[str]:
    """Validate a single database entry."""
    errors = []
    warnings = []

    # Check required fields
    for field in REQUIRED_FIELDS:
        if field not in db:
            errors.append(f"Missing required field: {field}")
        elif not db[field]:
            errors.append(f"Empty required field: {field}")

    # Check recommended fields
    for field in RECOMMENDED_FIELDS:
        if field not in db:
            warnings.append(f"Missing recommended field: {field}")

    # Validate category
    if 'category' in db:
        if db['category'] not in VALID_CATEGORIES:
            errors.append(f"Invalid category: {db['category']}")

        # Check if file is in correct directory
        if file_path.parent.name != db['category']:
            warnings.append(
                f"Category mismatch: file in {file_path.parent.name}/ "
                f"but category is {db['category']}"
            )

    # Validate URLs
    if 'url' in db:
        valid, msg = validate_url(db['url'])
        if not valid:
            errors.append(f"Invalid main URL: {msg}")

    if 'documentation' in db:
        valid, msg = validate_url(db['documentation'])
        if not valid:
            warnings.append(f"Invalid documentation URL: {msg}")

    if 'api_docs' in db:
        valid, msg = validate_url(db['api_docs'])
        if not valid:
            warnings.append(f"Invalid API docs URL: {msg}")

    # Validate data types is a list
    if 'data_types' in db:
        if not isinstance(db['data_types'], list):
            errors.append("data_types must be a list")
        elif not db['data_types']:
            errors.append("data_types list is empty")

    # Validate access is a list
    if 'access' in db:
        if not isinstance(db['access'], list):
            errors.append("access must be a list")

    # Check description length
    if 'description' in db:
        if len(db['description']) < 50:
            warnings.append("Description is very short (< 50 characters)")
        elif len(db['description']) > 1000:
            warnings.append("Description is very long (> 1000 characters)")

    return errors, warnings


def validate_all_databases(databases_dir: Path):
    """Validate all database JSON files."""
    print("Validating database files...\n")

    total_files = 0
    total_errors = 0
    total_warnings = 0

    # Iterate through category directories
    for category_dir in sorted(databases_dir.iterdir()):
        if not category_dir.is_dir() or category_dir.name.startswith('.'):
            continue

        # Validate JSON files in the category
        for json_file in sorted(category_dir.glob('*.json')):
            total_files += 1

            try:
                with open(json_file, 'r') as f:
                    db = json.load(f)

                errors, warnings = validate_database(db, json_file)

                if errors or warnings:
                    print(f"{'='*70}")
                    print(f"{json_file.relative_to(databases_dir)}")
                    print(f"{'='*70}")

                    if errors:
                        print("\nERRORS:")
                        for error in errors:
                            print(f"  ❌ {error}")
                        total_errors += len(errors)

                    if warnings:
                        print("\nWARNINGS:")
                        for warning in warnings:
                            print(f"  ⚠️  {warning}")
                        total_warnings += len(warnings)

                    print()

            except json.JSONDecodeError as e:
                total_errors += 1
                print(f"{'='*70}")
                print(f"{json_file.relative_to(databases_dir)}")
                print(f"{'='*70}")
                print(f"  ❌ Invalid JSON: {e}\n")

            except Exception as e:
                total_errors += 1
                print(f"{'='*70}")
                print(f"{json_file.relative_to(databases_dir)}")
                print(f"{'='*70}")
                print(f"  ❌ Error reading file: {e}\n")

    # Summary
    print(f"{'='*70}")
    print("VALIDATION SUMMARY")
    print(f"{'='*70}")
    print(f"Total files: {total_files}")
    print(f"Errors: {total_errors}")
    print(f"Warnings: {total_warnings}")

    if total_errors == 0 and total_warnings == 0:
        print("\n✅ All database files are valid!")
        return 0
    elif total_errors == 0:
        print(f"\n⚠️  Validation completed with {total_warnings} warning(s)")
        return 0
    else:
        print(f"\n❌ Validation failed with {total_errors} error(s)")
        return 1


def main():
    # Find the databases directory
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    databases_dir = repo_root / 'databases'

    if not databases_dir.exists():
        print(f"Error: Databases directory not found at {databases_dir}")
        return 1

    return validate_all_databases(databases_dir)


if __name__ == '__main__':
    exit(main())
