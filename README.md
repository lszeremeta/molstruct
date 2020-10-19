# <img src="https://raw.githubusercontent.com/lszeremeta/molstruct/master/logo/molstruct.png" alt="Molstruct logo" width="300">

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/3602c4be20d14be1b750db5a1875263a)](https://www.codacy.com/gh/lszeremeta/molstruct/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=lszeremeta/molstruct&amp;utm_campaign=Badge_Grade) [![PyPI](https://img.shields.io/pypi/v/molstruct)](https://pypi.org/project/molstruct/) [![Docker Image Size (latest by date)](https://img.shields.io/docker/image-size/lszeremeta/molstruct?label=Docker%20image%20size)](https://hub.docker.com/r/lszeremeta/molstruct)

Molstruct is a lightweight Python CLI tool that converts chemical molecule data [Comma Separated Values (CSV)](https://en.wikipedia.org/wiki/Comma-separated_values) files to structured data formats - [JSON-LD](https://json-ld.org/), [RDFa](http://rdfa.info/) and [Microdata](https://schema.org/docs/gs.html). Molstruct has a lot of customization options that you can but don't have to use. Python 3.2+ are supported and no dependencies are required. Sounds good so far? What would you say to a really tiny [Molstruct Docker container](https://hub.docker.com/r/lszeremeta/molstruct)? Just try Molstruct!

## What are structured data

Structured data are additional data placed on websites. They are not visible to ordinary internet users, but can be easily processed by machines. There are 3 formats that we can use to save structured data - [JSON-LD](https://json-ld.org/), [RDFa](http://rdfa.info/) and [Microdata](https://www.w3.org/TR/microdata/). Molstruct supports them all and use [MolecularEntitly](https://bioschemas.org/types/MolecularEntity/) type.

## Where to find a CSV file with molecule data

There are many possibilities. The easiest way is to download a CSV file from one of the chemical databases, e.g. [DrugBank](https://www.drugbank.ca/releases/latest#open-data). You can also create the CSV file yourself.

## Installation

You can install the Molstruct from [PyPI](https://pypi.org/project/molstruct/):

    pip install molstruct

Python 3.2 and above are supported. No additional dependencies are required. To use Molstruct just type the `molstruct` command in terminal.

## Docker image

If you have [Docker](https://docs.docker.com/engine/install/) installed, you can use tiny Molstruct image from [Docker Hub](https://hub.docker.com/r/lszeremeta/molstruct).

Because the tool is closed inside the container, you have to [mount](https://docs.docker.com/storage/bind-mounts/#start-a-container-with-a-bind-mount) local directory with your input file. The default working directory of the image is `/app`. You need to mount your local directory inside it (e.g. `/app/input`):

```shell
docker run -it --rm --name molstruct-app --mount type=bind,source=/home/user/input,target=/app/input,readonly lszeremeta/molstruct:latest
```

In this case, the local directory `/home/user/input` has been mounted under `/app/input`.

You can also simply mount current working directory using `$(pwd)` sub-command:

```shell
docker run -it --rm --name molstruct-app --mount type=bind,source="$(pwd)",target=/app/input,readonly lszeremeta/molstruct:latest
```

## Other options

You may want to run Molstruct from sources or build a Docker image yourself. In most cases, one of the methods mentioned in the sections above should be sufficient and convenient for you.

### Run Molstruct from sources

1. Clone this repository:

```shell
git clone https://github.com/lszeremeta/molstruct.git
```

If you don't want or can't use git, you can [download the zip archive](https://github.com/lszeremeta/molstruct/archive/master.zip) and extract it.

2. Go to the project directory and run Molstruct:

```shell
cd molstruct
python -m molstruct
```

### Local Docker build

You need [Docker](https://docs.docker.com/engine/install/) installed.

1. Clone this repository:

```shell
git clone https://github.com/lszeremeta/molstruct.git
```

If you don't want or can't use git, you can [download the zip archive](https://github.com/lszeremeta/molstruct/archive/master.zip) and extract it. 

2. Go to the project directory and build Docker image:

```shell
cd molstruct
docker build -t molstruct .
```

3. Run Docker container:

```shell
docker run -it --rm --name molstruct-app --mount type=bind,source=/home/user/input,target=/app/input,readonly molstruct
```

In this case, your local directory `/home/user/input` has been mounted under `/app/input`.

## Usage

    usage: molstruct [-h] [--version] -f {jsonld_html,jsonld,rdfa,microdata} [-i IDENTIFIER]
                     [-n NAME] [-ink INCHIKEY] [-in INCHI] [-s SMILES] [-u URL]
                     [-iu IUPACNAME] [-mf MOLECULARFORMULA] [-w MOLECULARWEIGHT]
                     [-mw MONOISOTOPICMOLECULARWEIGHT] [-d DESCRIPTION]
                     [-dd DISAMBIGUATINGDESCRIPTION] [-img IMAGE] [-at ADDITIONALTYPE]
                     [-an ALTERNATENAME] [-sa SAMEAS] [-c] [-b BASEURI] [-l LIMIT]
                     file

Supported [MolecularEntitly](https://bioschemas.org/types/MolecularEntity/) properties that corresponds to default CSV column names: `identifier`, `name`, `inChIKey`, `inChI`, `smiles`, `url`, `iupacName`, `molecularFormula`, `molecularWeight`, `monoisotopicMolecularWeight`, `description`, `disambiguatingDescription`, `image`, `additionalType`, `alternateName` and `sameAs`. You can rename the columns if needed (see Column name change arguments below).

### Informative arguments

* `-h`, `--help` show help message and exit
* `--version` show program version and exit

### Required arguments

* `-f {jsonld_html,jsonld,rdfa,microdata}`, `--format {jsonld_html,jsonld,rdfa,microdata}` output format
* `file` CSV file path with molecule data to convert

Remember about the appropriate file path when using Docker image. Suppose you mounted your local directory `/home/user/input` under `/app/input` and the path to the CSV file you want to use in molstruct is `/home/user/input/file.csv`. In this case, enter the path `/app/input/file.csv` or `input/file.csv` as `file` argument value.

### Column name change arguments

Arguments for changing the default column names

* `-i IDENTIFIER`, `--identifier IDENTIFIER` identifier column name (identifier by default), Text
* `-n NAME`, `--name NAME` name column name (name by default), Text
* `-ink INCHIKEY`, `--inChIKey INCHIKEY` inChIKey column name (inChIKey by default), Text
* `-in INCHI`, `--inChI INCHI` inChI column name (inChI by default), Text
* `-s SMILES`, `--smiles SMILES` smiles column name (smiles by default), Text
* `-u URL`, `--url URL` url column name (url by default), URL type
* `-iu IUPACNAME`, `--iupacName IUPACNAME` iupacName column name (iupacName by default), Text
* `-mf MOLECULARFORMULA`, `--molecularFormula MOLECULARFORMULA` molecularFormula column name (molecularFormula by default), Text
* `-w MOLECULARWEIGHT`, `--molecularWeight MOLECULARWEIGHT` molecularWeight column name (molecularWeight by default), Mass e.g. 0.01 mg)
* `-mw MONOISOTOPICMOLECULARWEIGHT`, `--monoisotopicMolecularWeight MONOISOTOPICMOLECULARWEIGHT` monoisotopicMolecularWeight column name (monoisotopicMolecularWeight by default), Mass e.g. 0.01 mg
* `-d DESCRIPTION`, `--description DESCRIPTION` description column name (description by default), Text
* `-dd DISAMBIGUATINGDESCRIPTION`, `--disambiguatingDescription DISAMBIGUATINGDESCRIPTION` disambiguatingDescription column name (disambiguatingDescription by default), Text
* `-img IMAGE`, `--image IMAGE` image column name (image by default), URL
* `-at ADDITIONALTYPE`, `--additionalType ADDITIONALTYPE` additionalType column name (additionalType by default), URL
* `-an ALTERNATENAME`, `--alternateName ALTERNATENAME` alternateName column name (alternateName by default), Text
* `-sa SAMEAS`, `--sameAs SAMEAS` sameAs column name (sameAs by default), URL

### Additional settings arguments

* `-c, --columns` use only columns with renamed names
* `-b BASEURI`, `--baseURI BASEURI` base URI of molecule (<http://example.com/molecule/> by default)
* `-l LIMIT`, `--limit LIMIT` maximum number of results

Available options may vary depending on the version. To display all available options with their descriptions use ``molstruct -h``.

## Examples

    molstruct -f rdfa data.csv

Returns simple HTML with added RDFa. Assumes that the column names in CSV file are the default ones.

    molstruct -f microdata -mf "formula" data.csv

Returns simple HTML with added Microdata. Assumes that the column names in CSV file are the default ones but replaces default `molecularformula` column name by `formula`.

    molstruct -f microdata --columns --id "CAS" --name "Common name" --inChIKey "Standard InChI Key" --limit 50 "drugbank vocabulary.csv"

Returns simple HTML with added Microdata. When generating a file, only selected columns will be taken into account. A limit of 50 molecules has been specified.

    molstruct -f microdata --columns --id "CAS" --name "Common name" --inChIKey "Standard InChI Key" --limit 50 "drugbank vocabulary.csv" > output.html

Do the same as example above but save results to `output.html`.

    docker run -it --rm --name molstruct-app --mount type=bind,source=/home/user/input,target=/app/input,readonly lszeremeta/molstruct:latest -f microdata --columns --id "CAS" --name "Common name" --inChIKey "Standard InChI Key" --limit 50 "input/drugbank vocabulary.csv" > output.html

Do the same as example above (run from pre-build Docker image).

Returns simple HTML with added [Microdata](https://www.w3.org/TR/microdata/) and redirect output to `molecules.html` file. Run from pre-build Docker image.

## Contribution

Would you like to improve this project? Great! We are waiting for your help and suggestions. If you are new in open source contributions, read [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/).

## License

Distributed under [MIT license](https://github.com/lszeremeta/molstruct/blob/master/LICENSE).

## See also

These projects can also be useful:

* [SDFEater](https://github.com/lszeremeta/SDFEater) - Always hungry SDF chemical file format parser with many output formats
* [MEgen](https://github.com/lszeremeta/MEgen) - Convenient online form to generate structured data about molecules
