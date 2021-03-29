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
            list(
                n.COLUMNS.keys())) + '. You can rename the columns if needed (see Column name change arguments below).',
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
                              help="identifier column name ('" + n.COLUMNS['identifier'] + "' by default), Text")
    column_names.add_argument("-n", "--name", type=str,
                              help="name column name ('" + n.COLUMNS['name'] + "' by default), Text")
    column_names.add_argument("-ink", "--inChIKey", type=str,
                              help="inChIKey column name ('" + n.COLUMNS['inChIKey'] + "' by default), Text")
    column_names.add_argument("-in", "--inChI", type=str,
                              help="inChI column name ('" + n.COLUMNS['inChI'] + "' by default), Text")
    column_names.add_argument("-s", "--smiles", type=str,
                              help="smiles column name ('" + n.COLUMNS['smiles'] + "' by default), Text")
    column_names.add_argument("-u", "--url", type=str,
                              help="url column name ('" + n.COLUMNS['url'] + "' by default), URL")
    column_names.add_argument("-iu", "--iupacName", type=str,
                              help="iupacName column name ('" + n.COLUMNS['iupacName'] + "' by default), Text")
    column_names.add_argument("-mf", "--molecularFormula", type=str,
                              help="molecularFormula column name ('" + n.COLUMNS[
                                  'molecularFormula'] + "' by default), Text")
    column_names.add_argument("-w", "--molecularWeight", type=str,
                              help="molecularWeight column name ('" + n.COLUMNS[
                                  'molecularWeight'] + "' by default), Mass e.g. 0.01 mg)")
    column_names.add_argument("-mw", "--monoisotopicMolecularWeight", type=str,
                              help="monoisotopicMolecularWeight column name ('" + n.COLUMNS[
                                  'monoisotopicMolecularWeight'] + "' by default), Mass e.g. 0.01 mg")
    column_names.add_argument("-d", "--description", type=str,
                              help="description column name ('" + n.COLUMNS['description'] + "' by default), Text")
    column_names.add_argument("-dd", "--disambiguatingDescription", type=str,
                              help="disambiguatingDescription column name ('" + n.COLUMNS[
                                  'disambiguatingDescription'] + "' by default), Text")
    column_names.add_argument("-img", "--image", type=str,
                              help="image column name ('" + n.COLUMNS['image'] + "' by default), URL")
    column_names.add_argument("-an", "--alternateName", type=str,
                              help="alternateName column name ('" + n.COLUMNS['alternateName'] + "' by default), Text")
    column_names.add_argument("-sa", "--sameAs", type=str,
                              help="sameAs column name ('" + n.COLUMNS['sameAs'] + "' by default), URL")

    additional_settings = parser.add_argument_group('Additional settings arguments')
    additional_settings.add_argument("-p", "--preset", choices=['drugbank'],
                                     help="apply presets for individual CSV sources to avoid setting individual options manually")
    additional_settings.add_argument("-c", "--columns",
                                     help="use only columns with renamed names",
                                     action="store_true")
    additional_settings.add_argument("-b", "--subject-base", type=str,
                                     help="subject base of molecule ('" + n.SUBJECT_BASE + "' by default)")
    additional_settings.add_argument("-vd", "--value-delimiter", type=str,
                                     help="value delimiter ('" + n.VALUE_DELIMITER + "' by default)")
    additional_settings.add_argument("-l", "--limit", type=int, help="maximum number of results (unlimited by default)")

    args = parser.parse_args()

    # set presets
    if args.preset == 'drugbank':
        args.value_delimiter = ' | '
        args.columns = True
        args.identifier = 'CAS'
        args.name = 'Common name'
        args.inChIKey = 'Standard InChI Key'
        args.alternateName = 'Synonyms'

    # replace default base molecule URI
    if args.baseURI:
        n.SUBJECT_BASE = args.baseURI

    # replace default value delimiter
    if args.value_delimiter:
        n.VALUE_DELIMITER = args.value_delimiter

    # replace default column names
    if args.identifier or args.columns:
        n.COLUMNS['identifier'] = args.identifier
    if args.name or args.columns:
        n.COLUMNS['name'] = args.name
    if args.inChIKey or args.columns:
        n.COLUMNS['inChIKey'] = args.inChIKey
    if args.inChI or args.columns:
        n.COLUMNS['inChI'] = args.inChI
    if args.smiles or args.columns:
        n.COLUMNS['smiles'] = args.smiles
    if args.url or args.columns:
        n.COLUMNS['url'] = args.url
    if args.iupacName or args.columns:
        n.COLUMNS['iupacName'] = args.iupacName
    if args.molecularFormula or args.columns:
        n.COLUMNS['molecularFormula'] = args.molecularFormula
    if args.molecularWeight or args.columns:
        n.COLUMNS['molecularWeight'] = args.molecularWeight
    if args.monoisotopicMolecularWeight or args.columns:
        n.COLUMNS['monoisotopicMolecularWeight'] = args.monoisotopicMolecularWeight
    if args.description or args.columns:
        n.COLUMNS['description'] = args.description
    if args.disambiguatingDescription or args.columns:
        n.COLUMNS['disambiguatingDescription'] = args.disambiguatingDescription
    if args.image or args.columns:
        n.COLUMNS['image'] = args.image
    if args.alternateName or args.columns:
        n.COLUMNS['alternateName'] = args.alternateName
    if args.sameAs or args.columns:
        n.COLUMNS['sameAs'] = args.sameAs

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
            exit(1)


if __name__ == "__main__":
    main()
