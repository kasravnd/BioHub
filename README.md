# BioAwesome

> A curated encyclopedia of biological databases - helping researchers find the perfect database for their needs.

## About

BioAwesome is a comprehensive, community-driven catalog of biological databases organized by category, data type, and research domain. Whether you're looking for genomic data, protein structures, or metabolic pathways, BioAwesome helps you discover the right resource.

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

- **Genomics** - Genome sequences, variations, annotations
- **Proteomics** - Protein sequences, structures, functions
- **Structural Biology** - 3D structures, molecular interactions
- **Metabolomics** - Metabolites, pathways, reactions
- **Systems Biology** - Networks, pathways, models
- **Transcriptomics** - Gene expression, RNA-seq data
- **Epigenomics** - Epigenetic modifications, chromatin
- **Phylogenetics** - Evolutionary relationships, taxonomy
- **Clinical & Medical** - Disease data, clinical trials, phenotypes
- **Model Organisms** - Organism-specific databases
- **Tools & Resources** - Analysis tools, repositories, archives

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
BioAwesome/
├── databases/           # Database entries organized by category
│   ├── catalog.json    # Complete catalog with all metadata
│   ├── genomics/
│   ├── proteomics/
│   └── ...
├── .github/
│   ├── ISSUE_TEMPLATE/ # Templates for adding databases
│   └── PULL_REQUEST_TEMPLATE.md
├── scripts/            # Utility scripts
│   └── search.py       # Search and filter databases
├── CONTRIBUTING.md     # Contribution guidelines
└── README.md          # This file
```

## License

MIT License - see [LICENSE](LICENSE) for details

## Acknowledgments

Built by the community, for the community. Thanks to all contributors!

---

**Star** this repo if you find it useful! **Contribute** to help others discover great biological databases.
