# molstruct

Converts chemical molecule data [Comma Separated Values (CSV)](https://en.wikipedia.org/wiki/Comma-separated_values) files to structured data formats - [RDFa](http://rdfa.info/) and [Microdata](https://schema.org/docs/gs.html). Supported
CSV columns: `id`, `name`, `inchikey`, `inchi`, `smiles`, `url`, `iupacname` and `molecularformula`. Written in [Python](https://www.python.org/) 3. Works from CLI.

## What are structured data?
Structured data are additional data placed on websites. They are not visible to ordinary internet users, but can be easily processed by machines. There are 3 formats that we can use to save structured data - [JSON-LD](https://json-ld.org/), [RDFa](http://rdfa.info/) and [Microdata](https://www.w3.org/TR/microdata/). This tool supports [RDFa](http://rdfa.info/) and [Microdata](https://www.w3.org/TR/microdata/) formats, and use [MolecularEntitly](https://bioschemas.org/types/MolecularEntity/) type.

## Where to find a CSV file with molecule data?
There are many possibilities. The easiest way is to download a CSV file from one of the chemical databases, e.g. [DrugBank](https://www.drugbank.ca/releases/latest#open-data). You can also create the CSV file yourself.

## Usage

```shell
usage: molstruct.py [-h] (-r | -m) [-i ID] [-n NAME] [-ink INCHIKEY] [-in INCHI]
                 [-s SMILES] [-u URL] [-iu IUPACNAME] [-f MOLECULARFORMULA]
                 [-c] [-l LIMIT]
                 file
```

### Positional arguments

```shell
  file                  CSV file with molecule data to convert
```

### Optional arguments

```shell
  -h, --help            show help message and exit
  -r, --rdfa            RDFa output
  -m, --microdata       Microdata output
  -i ID, --id ID        identifier column name (id by default)
  -n NAME, --name NAME  name column name (name by default)
  -ink INCHIKEY, --inchikey INCHIKEY
                        inchikey column name (inchikey by default)
  -in INCHI, --inchi INCHI
                        inchi column name (inchi by default)
  -s SMILES, --smiles SMILES
                        smiles column name (smiles by default)
  -u URL, --url URL     url column name (url by default)
  -iu IUPACNAME, --iupacname IUPACNAME
                        iupacname column name (iupacname by default)
  -f MOLECULARFORMULA, --molecularformula MOLECULARFORMULA
                        molecularformula column name (molecularformula by
                        default)
  -c, --columns         Use only columns with renamed names
  -l LIMIT, --limit LIMIT
                        Maximum number of results
```

Available options may vary depending on the version. To display all available options with their descriptions use ``molstruct.py -h``.

## Examples
```shell
python molstruct.py --rdfa data.csv"
```
Returns simple HTML with added RDFa. Assumes that the column names in CSV file are the default ones.

```shell
python molstruct.py --microdata -f "formula" data.csv"
```
Returns simple HTML with added Microdata. Assumes that the column names in CSV file are the default ones but replaces `molecularformula` by `formula`.

```shell
python molstruct.py --microdata --column --id "CAS" --name "Common name" --inchikey "Standard InChI Key" --limit 50 "drugbank vocabulary.csv"
```

Returns simple HTML with added Microdata. When generating a file, only selected columns will be taken into account. A limit of 50 molecules has been specified.

```shell
python molstruct.py --microdata --column --id "CAS" --name "Common name" --inchikey "Standard InChI Key" --limit 50 "drugbank vocabulary.csv" > output.html
```

Do the same as example above but save results to `output.html`.

## Contribution

Would you like to improve this project? Great! We are waiting for your help and suggestions. If you are new in open source contributions, read [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/).

## License

Distributed under [MIT license](https://github.com/lszeremeta/molstruct/blob/master/LICENSE).
