#!/usr/bin/env python
import argparse
import csv

import molstruct.names as n
import molstruct.outputs as o


def main():
    parser = argparse.ArgumentParser(
        description='Converts chemical molecule data CSV files to Structured Data formats - JSON-LD, RDFa and '
                    'Microdata. Supported CSV columns: ' +
                    str(n.DEFAULT_COLUMN_NAMES))
    parser.add_argument('file', type=str,
                        help='CSV file with molecule data to convert')
    formats_group = parser.add_mutually_exclusive_group(required=True)
    formats_group.add_argument("-jh", "--jsonldhtml", help="JSON-LD with HTML output",
                               action="store_true")
    formats_group.add_argument("-j", "--jsonld", help="JSON-LD output",
                               action="store_true")
    formats_group.add_argument("-r", "--rdfa", help="RDFa output",
                               action="store_true")
    formats_group.add_argument("-m", "--microdata", help="Microdata output",
                               action="store_true")

    # optional column names changes
    parser.add_argument("-i", "--identifier", type=str,
                        help="identifier column name (" + n.IDENTIFIER + " by default), Text")
    parser.add_argument("-n", "--name", type=str, help="name column name (" + n.NAME + " by default), Text")
    parser.add_argument("-ink", "--inChIKey", type=str,
                        help="inChIKey column name (" + n.INCHIKEY + " by default), Text")
    parser.add_argument("-in", "--inChI", type=str, help="inChI column name (" + n.INCHI + " by default), Text")
    parser.add_argument("-s", "--smiles", type=str, help="smiles column name (" + n.SMILES + " by default), Text")
    parser.add_argument("-u", "--url", type=str, help="url column name (" + n.URL + " by default), URL type")
    parser.add_argument("-iu", "--iupacName", type=str,
                        help="iupacName column name (" + n.IUPAC_NAME + " by default), Text")
    parser.add_argument("-f", "--molecularFormula", type=str,
                        help="molecularFormula column name (" + n.MOLECULAR_FORMULA + " by default), Text")
    parser.add_argument("-w", "--molecularWeight", type=str,
                        help="molecularWeight column name (" + n.MOLECULAR_WEIGHT + " by default), Mass e.g. 0.01 mg)")
    parser.add_argument("-mw", "--monoisotopicMolecularWeight", type=str,
                        help="monoisotopicMolecularWeight column name (" + n.MONOISOTOPIC_MOLECULAR_WEIGHT + " by default), Mass e.g. 0.01 mg")
    parser.add_argument("-d", "--description", type=str,
                        help="description column name (" + n.DESCRIPTION + " by default), Text")
    parser.add_argument("-dd", "--disambiguatingDescription", type=str,
                        help="disambiguatingDescription column name (" + n.DISAMBIGUATING_DESCRIPTION + " by default), Text")
    parser.add_argument("-img", "--image", type=str,
                        help="image column name (" + n.IMAGE + " by default), URL")
    parser.add_argument("-at", "--additionalType", type=str,
                        help="additionalType column name (" + n.ADDITIONAL_TYPE + " by default), URL")
    parser.add_argument("-an", "--alternateName", type=str,
                        help="alternateName column name (" + n.ALTERNATE_NAME + " by default), Text")
    parser.add_argument("-sa", "--sameAs", type=str,
                        help="sameAs column name (" + n.SAME_AS + " by default), URL")

    parser.add_argument("-c", "--columns",
                        help="Use only columns with renamed names",
                        action="store_true")
    parser.add_argument("-l", "--limit", type=int, help="Maximum number of results")

    args = parser.parse_args()

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
        with open(args.file, 'r') as csvfile:
            try:
                reader = csv.DictReader(csvfile)
                if args.jsonldhtml:
                    o.create_jsonldhtml_output(reader, args.limit)
                elif args.jsonld:
                    o.create_jsonld_output(reader, args.limit)
                elif args.rdfa:
                    o.create_rdfa_output(reader, args.limit)
                elif args.microdata:
                    o.create_microdata_output(reader, args.limit)
            except Exception as e:
                print("Error:", e)
                exit()


if __name__ == "__main__":
    main()
