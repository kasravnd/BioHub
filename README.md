# BioHub

> A curated encyclopedia of biological databases - helping researchers find the perfect database for their needs.

## About

BioHub is a comprehensive, community-driven catalog of biological databases organized by category, data type, and research domain. Whether you're looking for genomic data, protein structures, or metabolic pathways, BioHub helps you discover the right resource.

## Features

- **Organized by Category** - Browse databases by domain (genomics, proteomics, systems biology, etc.)
- **Rich Metadata** - Each database includes description, data types, access methods, and use cases
- **Easy to Search** - Programmatic search and filter capabilities
- **Community-Driven** - Easy contribution process with templates and guidelines
- **Always Up-to-Date** - Active maintenance and community contributions

## Quick Start

### Browse the Catalog

Navigate to the [`databases/`](databases/) directory to explore databases by category:

```
databases/
├── genomics/
├── proteomics/
├── structural-biology/
├── metabolomics/
├── systems-biology/
└── ...
```

### Search for Databases

Use the search script to find databases by keyword, data type, or category:

```bash
python search.py --keyword "protein" --category "proteomics"
```

### View All Databases

See the complete catalog with metadata in [`databases/catalog.json`](databases/catalog.json)

## Database Categories

- **Genomics** - Nucleotide sequences, genome annotations, genetic variation, and functional genomics
  - Nucleotide Archives, Gene Annotation, Genome Browsers, Genetic Variation, Functional Genomics
- **Proteomics** - Protein sequences, families, domains, structures, and experimental proteomics
  - Protein Sequences, Protein Families, Protein Structures, Proteomics Experiments
- **Pathways & Interactions** - Biological pathways and molecular interaction networks
  - Biological Pathways, Molecular Interactions
- **Metabolomics & Chemistry** - Small molecules, metabolites, drugs, and experimental metabolomics
  - Chemical Databases, Metabolite Databases, Drug Databases, Metabolomics Experiments
- **Ontologies** - Controlled vocabularies and formal definitions for data annotation
- **Literature** - Scientific literature databases, citation indexes, full-text archives
- **Clinical & Medical** - Disease data, clinical trials, phenotypes, medical genetics
- **Model Organisms** - Organism-specific curated resources (MODs)
- **Structural Biology** - 3D structures, molecular interactions, structural data
- **Tools & Resources** - Analysis tools, repositories, and general resources

## Contributing

We welcome contributions! Whether you want to:
- Add a new database
- Update existing information
- Suggest new categories
- Improve documentation

Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Quick Contribution

1. Fork the repository
2. Use the [database template](.github/ISSUE_TEMPLATE/add_database.md)
3. Add your database entry to the appropriate category
4. Submit a pull request

## Structure

```
BioHub/
├── databases/              # Database entries organized by category
│   ├── catalog.json       # Complete catalog with all metadata
│   ├── genomics/
│   │   ├── nucleotide-archives/
│   │   ├── genome-browsers/
│   │   └── ...
│   ├── proteomics/
│   │   ├── protein-sequences/
│   │   ├── protein-families/
│   │   └── ...
│   ├── pathways/
│   ├── metabolomics/
│   └── ...
├── .github/
│   ├── ISSUE_TEMPLATE/    # Templates for adding databases
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/         # CI/CD automation
├── scripts/               # Utility scripts
│   ├── search.py         # Search and filter databases
│   ├── update_catalog.py # Update main catalog
│   └── validate.py       # Validate database entries
├── schema.json           # Schema definition
├── SCHEMA.md            # Schema documentation
├── CONTRIBUTING.md      # Contribution guidelines
├── QUICKSTART.md        # Quick start guide
└── README.md           # This file
```

## License

MIT License - see [LICENSE](LICENSE) for details

## Acknowledgments

Built by the community, for the community. Thanks to all contributors!

---

**Star** this repo if you find it useful! **Contribute** to help others discover great biological databases.
