#!/usr/bin/env python
import argparse
import csv
import sys

import molstruct.names as n
import molstruct.outputs as o
from molstruct import __version__


def main():
    parser = argparse.ArgumentParser(
        description='Converts chemical molecule data CSV files to Structured Data formats - JSON-LD, RDFa and Microdata. Supported MolecularEntitly properties that corresponds to default CSV column names: ' + str(
            n.DEFAULT_COLUMN_NAMES) + '. You can rename the columns if needed (see Column name change arguments below).',
        add_help=False, prog='molstruct')
    informative = parser.add_argument_group('Informative arguments')
    informative.add_argument("-h", "--help", help='show this help message and exit', action="help")
    informative.add_argument("--version", help='show program version and exit', action="version", version=__version__)
    required = parser.add_argument_group('Required arguments')
    required.add_argument("-f", "--format", choices=['jsonld_html', 'jsonld', 'rdfa', 'microdata'],
                          help="output format",
                          required=True)
    required.add_argument('file', type=str,
                          help='CSV file path with molecule data to convert')

    # optional column name change
    column_names = parser.add_argument_group('Column name change arguments',
                                             'Arguments for changing the default column names')
    column_names.add_argument("-i", "--identifier", type=str,
                              help="identifier column name (" + n.IDENTIFIER + " by default), Text")
    column_names.add_argument("-n", "--name", type=str, help="name column name (" + n.NAME + " by default), Text")
    column_names.add_argument("-ink", "--inChIKey", type=str,
                              help="inChIKey column name (" + n.INCHIKEY + " by default), Text")
    column_names.add_argument("-in", "--inChI", type=str, help="inChI column name (" + n.INCHI + " by default), Text")
    column_names.add_argument("-s", "--smiles", type=str, help="smiles column name (" + n.SMILES + " by default), Text")
    column_names.add_argument("-u", "--url", type=str, help="url column name (" + n.URL + " by default), URL")
    column_names.add_argument("-iu", "--iupacName", type=str,
                              help="iupacName column name (" + n.IUPAC_NAME + " by default), Text")
    column_names.add_argument("-mf", "--molecularFormula", type=str,
                              help="molecularFormula column name (" + n.MOLECULAR_FORMULA + " by default), Text")
    column_names.add_argument("-w", "--molecularWeight", type=str,
                              help="molecularWeight column name (" + n.MOLECULAR_WEIGHT + " by default), Mass e.g. 0.01 mg)")
    column_names.add_argument("-mw", "--monoisotopicMolecularWeight", type=str,
                              help="monoisotopicMolecularWeight column name (" + n.MONOISOTOPIC_MOLECULAR_WEIGHT + " by default), Mass e.g. 0.01 mg")
    column_names.add_argument("-d", "--description", type=str,
                              help="description column name (" + n.DESCRIPTION + " by default), Text")
    column_names.add_argument("-dd", "--disambiguatingDescription", type=str,
                              help="disambiguatingDescription column name (" + n.DISAMBIGUATING_DESCRIPTION + " by default), Text")
    column_names.add_argument("-img", "--image", type=str,
                              help="image column name (" + n.IMAGE + " by default), URL")
    column_names.add_argument("-at", "--additionalType", type=str,
                              help="additionalType column name (" + n.ADDITIONAL_TYPE + " by default), URL")
    column_names.add_argument("-an", "--alternateName", type=str,
                              help="alternateName column name (" + n.ALTERNATE_NAME + " by default), Text")
    column_names.add_argument("-sa", "--sameAs", type=str,
                              help="sameAs column name (" + n.SAME_AS + " by default), URL")

    additional_settings = parser.add_argument_group('Additional settings arguments')
    additional_settings.add_argument("-c", "--columns",
                                     help="use only columns with renamed names",
                                     action="store_true")
    additional_settings.add_argument("-b", "--baseURI", type=str,
                                     help="base URI of molecule (" + n.BASE_URI_MOLECULE + " by default)")
    additional_settings.add_argument("-l", "--limit", type=int, help="maximum number of results")

    args = parser.parse_args()

    # replace default base molecule URI
    if args.baseURI:
        n.BASE_URI_MOLECULE = args.baseURI

    # replace default column names
    if args.identifier or args.columns:
        n.IDENTIFIER = args.identifier
    if args.name or args.columns:
        n.NAME = args.name
    if args.inChIKey or args.columns:
        n.INCHIKEY = args.inChIKey
    if args.inChI or args.columns:
        n.INCHI = args.inChI
    if args.smiles or args.columns:
        n.SMILES = args.smiles
    if args.url or args.columns:
        n.URL = args.url
    if args.iupacName or args.columns:
        n.IUPAC_NAME = args.iupacName
    if args.molecularFormula or args.columns:
        n.MOLECULAR_FORMULA = args.molecularFormula
    if args.molecularWeight or args.columns:
        n.MOLECULAR_WEIGHT = args.molecularWeight
    if args.monoisotopicMolecularWeight or args.columns:
        n.MONOISOTOPIC_MOLECULAR_WEIGHT = args.monoisotopicMolecularWeight
    if args.description or args.columns:
        n.DESCRIPTION = args.description
    if args.disambiguatingDescription or args.columns:
        n.DISAMBIGUATING_DESCRIPTION = args.disambiguatingDescription
    if args.image or args.columns:
        n.IMAGE = args.image
    if args.additionalType or args.columns:
        n.ADDITIONAL_TYPE = args.additionalType
    if args.alternateName or args.columns:
        n.ALTERNATE_NAME = args.alternateName
    if args.sameAs or args.columns:
        n.SAME_AS = args.sameAs

    # read csv file and generate outputs
    if args.file:
        try:
            with open(args.file, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                if args.format == 'jsonld_html':
                    o.jsonld_html(reader, args.limit)
                elif args.format == 'jsonld':
                    o.jsonld(reader, args.limit)
                elif args.format == 'rdfa':
                    o.rdfa(reader, args.limit)
                elif args.format == 'microdata':
                    o.microdata(reader, args.limit)
        except Exception as e:
            print("Error:", e, file=sys.stderr)
            exit()


if __name__ == "__main__":
    main()
