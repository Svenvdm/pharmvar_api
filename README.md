# pharmvar_api

A Python wrapper for the [PharmVar](https://www.pharmvar.org/) REST API.

## Installation

```bash
pip install pharmvar_api
```

Or clone and install locally:

```bash
git clone https://github.com/Svenvdm/pharmvar_api.git
cd pharmvar_api
pip install .
```

## Basic usage

```python
from pharmvar_api import PharmVarApi

# An API key is currently required to access data from PharmVar. You can get your API key on the PharmVar website.
api = PharmVarApi(api_key="")

# Get info for a gene by its symbol
gene = api.get_gene_by_gene_symbol("CYP2D6")
print(gene)

# Get all alleles for a gene
alleles = api.get_all_alleles()
for allele in alleles:
    print(allele.allele_name, allele.function)

# Get variants for a specific allele
variants = api.get_allele_variants("CYP2D6*4.001")
for variant in variants:
    print(variant.hgvs, variant.rs_id)

# Get all gene symbols known to PharmVar
gene_symbols = api.get_gene_list()
print(gene_symbols)
```

## Notes

- Results come back as collection objects (`AlleleCollection`, `VariantCollection`, `GeneCollection`) that support iteration, indexing, `len()`, and a `.filter(**kwargs)` method.
