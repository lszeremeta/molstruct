# molstruct

Converts chemical molecule data [Comma Separated Values (CSV)](https://en.wikipedia.org/wiki/Comma-separated_values) files to structured data formats - [JSON-LD](https://json-ld.org/), [RDFa](http://rdfa.info/) and [Microdata](https://schema.org/docs/gs.html). Supported
CSV columns: `identifier`, `name`, `inChIKey`, `inChI`, `smiles`, `url`, `iupacName`, `molecularFormula`, `molecularWeight`, `monoisotopicMolecularWeight`, `description`, `disambiguatingDescription`, `image`, `additionalType`, `alternateName` and `sameAs`.  Written in [Python](https://www.python.org/) 3. Works from CLI.

## What are structured data?
Structured data are additional data placed on websites. They are not visible to ordinary internet users, but can be easily processed by machines. There are 3 formats that we can use to save structured data - [JSON-LD](https://json-ld.org/), [RDFa](http://rdfa.info/) and [Microdata](https://www.w3.org/TR/microdata/). Molstruct supports them all and use [MolecularEntitly](https://bioschemas.org/types/MolecularEntity/) type.

## Where to find a CSV file with molecule data?
There are many possibilities. The easiest way is to download a CSV file from one of the chemical databases, e.g. [DrugBank](https://www.drugbank.ca/releases/latest#open-data). You can also create the CSV file yourself.

## Usage

```shell
usage: molstruct [-h] (-jh | -j | -r | -m) [-i IDENTIFIER] [-n NAME] [-ink INCHIKEY]
                 [-in INCHI] [-s SMILES] [-u URL] [-iu IUPACNAME]
                 [-f MOLECULARFORMULA] [-w MOLECULARWEIGHT]
                 [-mw MONOISOTOPICMOLECULARWEIGHT] [-d DESCRIPTION]
                 [-dd DISAMBIGUATINGDESCRIPTION] [-img IMAGE] [-at ADDITIONALTYPE]
                 [-an ALTERNATENAME] [-sa SAMEAS] [-c] [-l LIMIT]
                 file
```

### Positional arguments

```shell
  file                  CSV file with molecule data to convert
```

### Optional arguments

```shell
  -h, --help            show this help message and exit
  -jh, --jsonldhtml     JSON-LD with HTML output
  -j, --jsonld          JSON-LD output
  -r, --rdfa            RDFa output
  -m, --microdata       Microdata output
  -i IDENTIFIER, --identifier IDENTIFIER
                        identifier column name (identifier by default), Text
  -n NAME, --name NAME  name column name (name by default), Text
  -ink INCHIKEY, --inChIKey INCHIKEY
                        inChIKey column name (inChIKey by default), Text
  -in INCHI, --inChI INCHI
                        inChI column name (inChI by default), Text
  -s SMILES, --smiles SMILES
                        smiles column name (smiles by default), Text
  -u URL, --url URL     url column name (url by default), URL type
  -iu IUPACNAME, --iupacName IUPACNAME
                        iupacName column name (iupacName by default), Text
  -f MOLECULARFORMULA, --molecularFormula MOLECULARFORMULA
                        molecularFormula column name (molecularFormula by
                        default), Text
  -w MOLECULARWEIGHT, --molecularWeight MOLECULARWEIGHT
                        molecularWeight column name (molecularWeight by
                        default), Mass e.g. 0.01 mg)
  -mw MONOISOTOPICMOLECULARWEIGHT, --monoisotopicMolecularWeight MONOISOTOPICMOLECULARWEIGHT
                        monoisotopicMolecularWeight column name
                        (monoisotopicMolecularWeight by default), Mass e.g.
                        0.01 mg
  -d DESCRIPTION, --description DESCRIPTION
                        description column name (description by default), Text
  -dd DISAMBIGUATINGDESCRIPTION, --disambiguatingDescription DISAMBIGUATINGDESCRIPTION
                        disambiguatingDescription column name
                        (disambiguatingDescription by default), Text
  -img IMAGE, --image IMAGE
                        image column name (image by default), URL
  -at ADDITIONALTYPE, --additionalType ADDITIONALTYPE
                        additionalType column name (additionalType by
                        default), URL
  -an ALTERNATENAME, --alternateName ALTERNATENAME
                        alternateName column name (alternateName by default),
                        Text
  -sa SAMEAS, --sameAs SAMEAS
                        sameAs column name (sameAs by default), URL
  -c, --columns         Use only columns with renamed names
  -l LIMIT, --limit LIMIT
                        Maximum number of results
```

Available options may vary depending on the version. To display all available options with their descriptions use ``molstruct.py -h``.

## Examples
```shell
molstruct --rdfa data.csv
```
Returns simple HTML with added RDFa. Assumes that the column names in CSV file are the default ones.

```shell
molstruct --microdata -f "formula" data.csv
```
Returns simple HTML with added Microdata. Assumes that the column names in CSV file are the default ones but replaces default `molecularformula` column name by `formula`.

```shell
molstruct --microdata --columns --id "CAS" --name "Common name" --inchikey "Standard InChI Key" --limit 50 "drugbank vocabulary.csv"
```

Returns simple HTML with added Microdata. When generating a file, only selected columns will be taken into account. A limit of 50 molecules has been specified.

```shell
molstruct --microdata --columns --id "CAS" --name "Common name" --inchikey "Standard InChI Key" --limit 50 "drugbank vocabulary.csv" > output.html
```

Do the same as example above but save results to `output.html`.

## Contribution

Would you like to improve this project? Great! We are waiting for your help and suggestions. If you are new in open source contributions, read [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/).

## License

Distributed under [MIT license](https://github.com/lszeremeta/molstruct/blob/master/LICENSE).
