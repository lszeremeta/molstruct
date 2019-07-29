#!/usr/bin/python3
import argparse
import csv
import html


def create_rdfa_output(reader):
    i = 1
    print('<!DOCTYPE html>')
    print('<html lang="en">')
    print('  <head>')
    print('    <title>Example Document</title>')
    print('  </head>')
    print('  <body vocab="http://schema.org/">')
    for row in reader:
        print('    <div typeof="schema:MolecularEntity" about="http://example.org/me' + str(i) + '">')
        if row.get(ID):
            print('      <div property="schema:identifier">' + html.escape(row.get(ID)) + '</div>')
        if row.get(NAME):
            print('      <div property="schema:name">' + html.escape(row.get(NAME)) + '</div>')
        if row.get(INCHIKEY):
            print('      <div property="schema:inChIKey">' + html.escape(row.get(INCHIKEY)) + '</div>')
        if row.get(INCHI):
            print('      <div property="schema:inChI">' + html.escape(row.get(INCHI)) + '</div>')
        if row.get(SMILES):
            print('      <div property="schema:smiles">' + html.escape(row.get(SMILES)) + '</div>')
        if row.get(URL):
            print(
                '      <a rel="schema:url" href="' + html.escape(row.get(URL)) + '">' + html.escape(
                    row.get(URL)) + '</a>')
        if row.get(IUPACNAME):
            print('      <div property="schema:iupacName">' + html.escape(row.get(IUPACNAME)) + '</div>')
        if row.get(MOLECULARFORMULA):
            print('      <div property="schema:molecularFormula">' + html.escape(row.get(MOLECULARFORMULA)) + '</div>')
        print('    </div>')

        if i == args.limit:
            break

        i = i + 1
    print('  </body>')
    print('</html>')


def create_microdata_output(reader):
    i = 1
    print('<!DOCTYPE html>')
    print('<html lang="en">')
    print('  <head>')
    print('    <title>Example Document</title>')
    print('  </head>')
    print('  <body>')
    for row in reader:
        print('    <div itemscope itemtype="http://schema.org/MolecularEntity" itemid="http://example.org/me' + str(
            i) + '">')
        if row.get(ID):
            print('      <div itemprop="identifier">' + html.escape(row.get(ID)) + '</div>')
        if row.get(NAME):
            print('      <div itemprop="name">' + html.escape(row.get(NAME)) + '</div>')
        if row.get(INCHIKEY):
            print('      <div itemprop="inChIKey">' + html.escape(row.get(INCHIKEY)) + '</div>')
        if row.get(INCHI):
            print('      <div itemprop="inChI">' + html.escape(row.get(INCHI)) + '</div>')
        if row.get(SMILES):
            print('      <div itemprop="smiles">' + html.escape(row.get(SMILES)) + '</div>')
        if row.get(URL):
            print('      <a href="' + html.escape(row.get(URL)) + '" itemprop="url">' + html.escape(
                row.get(URL)) + '</a>')
        if row.get(IUPACNAME):
            print('      <div itemprop="iupacName">' + html.escape(row.get(IUPACNAME)) + '</div>')
        if row.get(MOLECULARFORMULA):
            print('      <div itemprop="molecularFormula">' + html.escape(row.get(MOLECULARFORMULA)) + '</div>')
        print('    </div>')

        if i == args.limit:
            break

        i = i + 1
    print('  </body>')
    print('</html>')


# set column names
ID = 'id'
NAME = 'name'
INCHIKEY = 'inchikey'
INCHI = 'inchi'
SMILES = 'smiles'
URL = 'url'
IUPACNAME = 'iupacname'
MOLECULARFORMULA = 'molecularformula'
DEFAULT_COLUMN_NAMES = [ID, NAME, INCHIKEY, INCHI, SMILES, URL, IUPACNAME, MOLECULARFORMULA]

parser = argparse.ArgumentParser(
    description='Converts chemical molecule data CSV files to Structured Data formats - RDFa and Microdata. '
                'Supported CSV columns: ' +
                str(DEFAULT_COLUMN_NAMES))
parser.add_argument('file', type=str,
                    help='CSV file with molecule data to convert')
formats_group = parser.add_mutually_exclusive_group(required=True)
formats_group.add_argument("-r", "--rdfa", help="RDFa output",
                           action="store_true")
formats_group.add_argument("-m", "--microdata", help="Microdata output",
                           action="store_true")

# optional column names changes
parser.add_argument("-i", "--id", type=str, help="identifier column name (" + ID + " by default)")
parser.add_argument("-n", "--name", type=str, help="name column name (" + NAME + " by default)")
parser.add_argument("-ink", "--inchikey", type=str, help="inchikey column name (" + INCHIKEY + " by default)")
parser.add_argument("-in", "--inchi", type=str, help="inchi column name (" + INCHI + " by default)")
parser.add_argument("-s", "--smiles", type=str, help="smiles column name (" + SMILES + " by default)")
parser.add_argument("-u", "--url", type=str, help="url column name (" + URL + " by default)")
parser.add_argument("-iu", "--iupacname", type=str, help="iupacname column name (" + IUPACNAME + " by default)")
parser.add_argument("-f", "--molecularformula", type=str,
                    help="molecularformula column name (" + MOLECULARFORMULA + " by default)")

parser.add_argument("-c", "--columns",
                    help="Use only columns with renamed names",
                    action="store_true")
parser.add_argument("-l", "--limit", type=int, help="Maximum number of results")

args = parser.parse_args()

# replace default column names
if args.id or args.columns:
    ID = args.id
if args.name or args.columns:
    NAME = args.name
if args.inchikey or args.columns:
    INCHIKEY = args.inchikey
if args.inchi or args.columns:
    INCHI = args.inchi
if args.smiles or args.columns:
    SMILES = args.smiles
if args.url or args.columns:
    URL = args.url
if args.iupacname or args.columns:
    IUPACNAME = args.iupacname
if args.molecularformula or args.columns:
    MOLECULARFORMULA = args.molecularformula

# read csv file and generate outputs
if args.file:
    with open(args.file, 'r') as csvfile:
        try:
            reader = csv.DictReader(csvfile)
            if args.rdfa:
                create_rdfa_output(reader)
            elif args.microdata:
                create_microdata_output(reader)
        except Exception as e:
            print("Error:", e)
            exit()
