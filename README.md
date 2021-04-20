# <img src="https://raw.githubusercontent.com/lszeremeta/molstruct/master/logo/molstruct.png" alt="Molstruct logo" width="300">

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/3602c4be20d14be1b750db5a1875263a)](https://www.codacy.com/gh/lszeremeta/molstruct/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=lszeremeta/molstruct&amp;utm_campaign=Badge_Grade) [![PyPI](https://img.shields.io/pypi/v/molstruct)](https://pypi.org/project/molstruct/) [![Docker Image Size (latest by date)](https://img.shields.io/docker/image-size/lszeremeta/molstruct?label=Docker%20image%20size)](https://hub.docker.com/r/lszeremeta/molstruct)

Molstruct is a lightweight Python CLI tool that converts chemical molecule data [Comma Separated Values (CSV)](https://en.wikipedia.org/wiki/Comma-separated_values) files to structured data formats - [JSON-LD](https://json-ld.org/), [RDFa](http://rdfa.info/), and [Microdata](https://schema.org/docs/gs.html). Molstruct has a lot of customization options that you can, but don't have to use. Python 3.2+ is supported and no dependencies are required. Sounds good so far? What would you say to a really tiny [Molstruct Docker container](https://hub.docker.com/r/lszeremeta/molstruct)? Just try Molstruct!

## What is structured data

[Structured data](https://developers.google.com/search/docs/guides/intro-structured-data) is additional data placed on websites. It is not visible to ordinary internet users but can be easily processed by machines. There are 3 formats that we can use to save structured data - [JSON-LD](https://json-ld.org/), [RDFa](http://rdfa.info/), and [Microdata](https://www.w3.org/TR/microdata/). Molstruct supports them all and uses the [MolecularEntity profile](https://bioschemas.org/profiles/MolecularEntity/0.5-RELEASE/).

## Where to find a CSV file with molecule data

There are many possibilities. The easiest way is to download a CSV file from one of the chemical databases, e.g. [DrugBank](https://www.drugbank.ca/releases/latest#open-data). You can also create the CSV file yourself.

## Quick start

Use Molstruct in 3 easy steps. In this example, we will use the [DrugBank open dataset](https://www.drugbank.ca/releases/latest#open-data). You need Python 3.2+ and pip installed.

1. Open a terminal and install Molstruct

You can install the Molstruct from [PyPI](https://pypi.org/project/molstruct/):

```shell
pip install molstruct
```

Molstruct is also available as a [Docker image](#docker-image). In most cases, installing Molstruct from PyPI or using Docker should be sufficient and convenient, but you may want to [run Molstruct from sources or build a Docker image yourself](https://github.com/lszeremeta/molstruct/wiki/Run-from-sources-and-manual-Docker-build).

2. Download [DrugBank open dataset](https://go.drugbank.com/releases/latest/downloads/all-drugbank-vocabulary) in CSV format and unzip downloaded archive.
3. Molstruct has a [predefined preset](#predefined-presets) for this dataset. You just need to select the output format and enter the path to the CSV file. Assuming the `drugbank vocabulary.csv` file is in the current directory and the output format you're interested in is RDFa, the command will be as follows:

```shell
molstruct -p drugbank-open -f rdfa "drugbank vocabulary.csv" > drugbank_cc0_rdfa.html
```

That's all. Now you have the RDFa file ready in the current directory. You can try other output formats and options as described below. You can also use Molstruct to convert other data in CSV format.

## Docker image

If you have [Docker](https://docs.docker.com/engine/install/) installed, you can use a tiny Molstruct image from [Docker Hub](https://hub.docker.com/r/lszeremeta/molstruct).

Because the tool is closed inside the container, you have to [mount](https://docs.docker.com/storage/bind-mounts/#start-a-container-with-a-bind-mount) the local directory with your input file. The default working directory of the image is `/app`. You need to mount your local directory inside it (e.g. `/app/input`):

```shell
docker run -it --rm --name molstruct-app --mount type=bind,source=/home/user/input,target=/app/input,readonly lszeremeta/molstruct:latest
```

In this case, the local directory `/home/user/input` has been mounted under `/app/input`.

You can also simply mount the current working directory using `$(pwd)` sub-command:

```shell
docker run -it --rm --name molstruct-app --mount type=bind,source="$(pwd)",target=/app/input,readonly lszeremeta/molstruct:latest
```

## Usage

```
usage: molstruct [-h] [--version] -f {jsonldhtml,jsonld,rdfa,microdata} [-i IDENTIFIER]
                 [-n NAME] [-ink INCHIKEY] [-in INCHI] [-sm SMILES] [-u URL]
                 [-iu IUPACNAME] [-mf MOLECULARFORMULA] [-w MOLECULARWEIGHT]
                 [-mw MONOISOTOPICMOLECULARWEIGHT] [-d DESCRIPTION]
                 [-dd DISAMBIGUATINGDESCRIPTION] [-img IMAGE] [-an ALTERNATENAME]
                 [-sa SAMEAS] [-p {drugbank-open} | -c] [-s {iri,uuid,bnode}] [-b BASE]
                 [-vd VALUE_DELIMITER] [-l LIMIT]
                 file
```

Supported [MolecularEntity](https://bioschemas.org/profiles/MolecularEntity/0.5-RELEASE/) properties that correspond to default CSV column names: `identifier`, `name`, `inChIKey`, `inChI`, `smiles`, `url`, `iupacName`, `molecularFormula`, `molecularWeight`, `monoisotopicMolecularWeight`, `description`, `disambiguatingDescription`, `image`, `alternateName` and `sameAs`. You can rename the columns if needed (see [Column name change arguments](#column-name-change-arguments) below). You can also use a [preset](#predefined-presets) with the appropriate settings for your dataset.

### Informative arguments

* `-h`, `--help` show help message and exit
* `--version` show program version and exit

### Required arguments

* `-f {jsonldhtml,jsonld,rdfa,microdata}`, `--format {jsonldhtml,jsonld,rdfa,microdata}` output format
* `file` CSV file path with molecule data to convert

Remember about the appropriate file path when using the Docker image. Suppose you mounted your local directory `/home/user/input` under `/app/input` and the path to the CSV file you want to use in Molstruct is `/home/user/input/file.csv`. In this case, enter the path `/app/input/file.csv` or `input/file.csv` as `file` argument value.

### Column name change arguments

Arguments for changing the default column names

* `-i IDENTIFIER`, `--identifier IDENTIFIER` identifier column name ('identifier' by default), Text
* `-n NAME`, `--name NAME` name column name ('name' by default), Text
* `-ink INCHIKEY`, `--inChIKey INCHIKEY` inChIKey column name ('inChIKey' by default), Text
* `-in INCHI`, `--inChI INCHI` inChI column name ('inChI' by default), Text
* `-sm SMILES`, `--smiles SMILES` smiles column name ('smiles' by default), Text
* `-u URL`, `--url URL` url column name ('url' by default), URL
* `-iu IUPACNAME`, `--iupacName IUPACNAME` iupacName column name ('iupacName' by default), Text
* `-mf MOLECULARFORMULA`, `--molecularFormula MOLECULARFORMULA` molecularFormula column name ('molecularFormula' by default), Text
* `-w MOLECULARWEIGHT`, `--molecularWeight MOLECULARWEIGHT` molecularWeight column name ('molecularWeight' by default), Mass e.g. 0.01 mg)
* `-mw MONOISOTOPICMOLECULARWEIGHT`, `--monoisotopicMolecularWeight MONOISOTOPICMOLECULARWEIGHT` monoisotopicMolecularWeight column name ('monoisotopicMolecularWeight' by default), Mass e.g. 0.01 mg
* `-d DESCRIPTION`, `--description DESCRIPTION` description column name ('description' by default), Text
* `-dd DISAMBIGUATINGDESCRIPTION`, `--disambiguatingDescription DISAMBIGUATINGDESCRIPTION` disambiguatingDescription column name ('disambiguatingDescription' by default), Text
* `-img IMAGE`, `--image IMAGE` image column name ('image' by default), URL
* `-an ALTERNATENAME`, `--alternateName ALTERNATENAME` alternateName column name ('alternateName' by default), Text
* `-sa SAMEAS`, `--sameAs SAMEAS` sameAs column name ('sameAs' by default), URL

### Additional settings arguments

* `-p {drugbank-open}`, `--preset {drugbank-open}` apply presets for individual CSV sources to avoid setting individual options manually (['drugbank-open'](#drugbank-open))
* `-c`, `--columns` use only columns with renamed names; not available when using a preset
* `-s {iri,uuid,bnode}`, `--subject {iri,uuid,bnode}` molecule subject type ('iri' by default)
* `-b BASE`, `--base BASE` molecule subject base for 'iri' subject type ('http://example.com/molecule#entity' by default)
* `-vd VALUE_DELIMITER`, `--value-delimiter VALUE_DELIMITER` value delimiter (' | ' by default)
* `-l LIMIT`, `--limit LIMIT` maximum number of results (unlimited by default)

Available options may vary depending on the version. To display all available options with their descriptions use ``molstruct -h``.

## Predefined presets

To make your work easier, Molstruct has built-in preset support. Thanks to this, you do not have to set everything manually, you just select the appropriate preset and it's ready. The presets are flexible. If you want to change, e.g. the column names selected for a preset, you can do so. At the moment you can use the [DrugBank open](https://www.drugbank.ca/releases/latest#open-data) preset. There are plans to add more in the future. Any [suggestions](https://github.com/lszeremeta/molstruct/issues/new?template=new-preset-suggestion.md) are welcome!

### `drugbank-open`

Settings for the [open DrugBank dataset](https://www.drugbank.ca/releases/latest#open-data) in CSV file:

* `--value-delimiter` is set to ' | '
* `--identifier` is set to 'CAS'
* `--name` is set to 'Common name'
* `--inChIKey` is set to 'Standard InChI Key'
* `--alternateName` is set to 'Synonyms'

## Additional examples

```shell
molstruct -f jsonldhtml data.csv
```

Returns simple HTML with added JSON-LD. Assumes that the column names in the CSV file are the default ones.

```shell
molstruct -f microdata -mf "formula" data.csv
```

Returns simple HTML with added Microdata. Assumes that the column names in CSV file are the default ones but replaces default `molecularformula` column name by `formula`.

```shell
molstruct -f microdata --columns --id "CAS" --name "Common name" --inChIKey "Standard InChI Key" --limit 50 "drugbank vocabulary.csv"
```

Returns simple HTML with added Microdata. When generating a file, only selected columns will be taken into account. A limit of 50 molecules has been specified.

```shell
molstruct -f microdata --columns --id "CAS" --name "Common name" --inChIKey "Standard InChI Key" --limit 50 "drugbank vocabulary.csv" > output.html
```

Does the same as the example above but saves results to `output.html`.

```shell
docker run -it --rm --name molstruct-app --mount type=bind,source=/home/user/input,target=/app/input,readonly lszeremeta/molstruct:latest -f microdata --columns --id "CAS" --name "Common name" --inChIKey "Standard InChI Key" --limit 50 "input/drugbank vocabulary.csv" > output.html
```

Does the same as the example above (run from pre-built Docker image).

Returns simple HTML with added [Microdata](https://www.w3.org/TR/microdata/) and redirects output to `molecules.html` file. Run from pre-build Docker image.

## Contribution

Would you like to improve this project? Great! We are waiting for your help and suggestions. If you are new to open source contributions, read [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/).

## License

Distributed under [MIT License](https://github.com/lszeremeta/molstruct/blob/master/LICENSE).

## See also

These projects can also be useful:

* [SDFEater](https://github.com/lszeremeta/SDFEater) - Always hungry SDF chemical file format parser with many output formats
* [MEgen](https://github.com/lszeremeta/MEgen) - Convenient online form to generate structured data about molecules
