#!/usr/bin/python3
import argparse
import csv
import html
import json


def create_jsonld_output(reader):
    i = 1

    out_str = '{\n'
    out_str += '  "@graph" : [\n'
    for row in reader:
        out_str += '  {\n'
        out_str += '  "@id" : "http://example.org/me' + str(i) + '",\n'
        out_str += '  "@type" : "https://schema.org/MolecularEntity",\n'
        if row.get(IDENTIFIER):
            out_str += '  "identifier" : ' + json.dumps(row.get(IDENTIFIER)) + ',\n'
        if row.get(NAME):
            out_str += '  "name" : ' + json.dumps(row.get(NAME)) + ',\n'
        if row.get(INCHIKEY):
            out_str += '  "inChIKey" : ' + json.dumps(row.get(INCHIKEY)) + ',\n'
        if row.get(INCHI):
            out_str += '  "inChI" : ' + json.dumps(row.get(INCHI)) + ',\n'
        if row.get(SMILES):
            out_str += '  "smiles" : ' + json.dumps(row.get(SMILES)) + ',\n'
        if row.get(URL):
            out_str += '  "url" : ' + json.dumps(row.get(URL)) + ',\n'
        if row.get(IUPAC_NAME):
            out_str += '  "iupacName" : ' + json.dumps(row.get(IUPAC_NAME)) + ',\n'
        if row.get(MOLECULAR_FORMULA):
            out_str += '  "molecularFormula" : ' + json.dumps(row.get(MOLECULAR_FORMULA)) + ',\n'
        if row.get(MOLECULAR_WEIGHT):
            out_str += '  "molecularWeight" : ' + json.dumps(row.get(MOLECULAR_WEIGHT)) + ',\n'
        if row.get(MONOISOTOPIC_MOLECULAR_WEIGHT):
            out_str += '  "monoisotopicMolecularWeight" : ' + json.dumps(row.get(MONOISOTOPIC_MOLECULAR_WEIGHT)) + ',\n'
        if row.get(DESCRIPTION):
            out_str += '  "description" : ' + json.dumps(row.get(DESCRIPTION)) + ',\n'
        if row.get(DISAMBIGUATING_DESCRIPTION):
            out_str += '  "disambiguatingDescription" : ' + json.dumps(row.get(DISAMBIGUATING_DESCRIPTION)) + ',\n'
        if row.get(ADDITIONAL_TYPE):
            out_str += '  "additionalType" : ' + json.dumps(row.get(ADDITIONAL_TYPE)) + ',\n'
        if row.get(ALTERNATE_NAME):
            out_str += '  "alternateName" : ' + json.dumps(row.get(ALTERNATE_NAME)) + ',\n'
        if row.get(SAME_AS):
            out_str += '  "sameAs" : ' + json.dumps(row.get(SAME_AS)) + ',\n'
        out_str = out_str[:-2] + '\n'
        out_str += '  },'

        if i == args.limit:
            break

        i = i + 1
    out_str = out_str[:-1]

    print(out_str + ''' ],
  "@context" : {
    "identifier" : {
      "@id" : "https://schema.org/identifier"
    },
    "name" : {
      "@id" : "https://schema.org/name"
    },
    "inChIKey" : {
      "@id" : "https://schema.org/inChIKey"
    },
    "inChI" : {
      "@id" : "https://schema.org/inChI"
    },
    "smiles" : {
      "@id" : "https://schema.org/smiles"
    },
    "url" : {
      "@id" : "https://schema.org/url"
    },
    "iupacName" : {
      "@id" : "https://schema.org/iupacName"
    },
    "molecularFormula" : {
      "@id" : "https://schema.org/molecularFormula"
    },
    "molecularWeight" : {
      "@id" : "https://schema.org/molecularWeight"
    },
    "monoisotopicMolecularWeight" : {
      "@id" : "https://schema.org/monoisotopicMolecularWeight"
    },
    "description" : {
      "@id" : "https://schema.org/description"
    },
    "disambiguatingDescription" : {
      "@id" : "https://schema.org/disambiguatingDescription"
    },
    "image" : {
      "@id" : "https://schema.org/image"
    },
    "additionalType" : {
      "@id" : "https://schema.org/additionalType"
    },
    "alternateName" : {
      "@id" : "https://schema.org/alternateName"
    },
    "sameAs" : {
      "@id" : "https://schema.org/sameAs"
    },
    "schema" : "https://schema.org/",
    "rdf" : "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  }
}''')


def create_rdfa_output(reader):
    i = 1
    print('''<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Example Document</title>
  </head>
  <body vocab="http://schema.org/">''')
    for row in reader:
        print('    <div typeof="schema:MolecularEntity" about="http://example.org/me' + str(i) + '">')
        if row.get(IDENTIFIER):
            print('      <div property="schema:identifier">' + html.escape(row.get(IDENTIFIER)) + '</div>')
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
        if row.get(IUPAC_NAME):
            print('      <div property="schema:iupacName">' + html.escape(row.get(IUPAC_NAME)) + '</div>')
        if row.get(MOLECULAR_FORMULA):
            print('      <div property="schema:molecularFormula">' + html.escape(row.get(MOLECULAR_FORMULA)) + '</div>')
        if row.get(MOLECULAR_WEIGHT):
            print('      <div property="schema:molecularWeight">' + html.escape(row.get(MOLECULAR_WEIGHT)) + '</div>')
        if row.get(MONOISOTOPIC_MOLECULAR_WEIGHT):
            print('      <div property="schema:monoisotopicMolecularWeight">' + html.escape(
                row.get(MONOISOTOPIC_MOLECULAR_WEIGHT)) + '</div>')
        if row.get(DESCRIPTION):
            print('      <div property="schema:description">' + html.escape(row.get(DESCRIPTION)) + '</div>')
        if row.get(DISAMBIGUATING_DESCRIPTION):
            print('      <div property="schema:disambiguatingDescription">' + html.escape(
                row.get(DISAMBIGUATING_DESCRIPTION)) + '</div>')
        if row.get(IMAGE):
            print(
                '      <a rel="schema:image" href="' + html.escape(row.get(IMAGE)) + '">' + html.escape(
                    row.get(IMAGE)) + '</a>')
        if row.get(ADDITIONAL_TYPE):
            print(
                '      <a rel="schema:additionalType" href="' + html.escape(
                    row.get(ADDITIONAL_TYPE)) + '">' + html.escape(
                    row.get(ADDITIONAL_TYPE)) + '</a>')
        if row.get(ALTERNATE_NAME):
            print('      <div property="schema:alternateName">' + html.escape(row.get(ALTERNATE_NAME)) + '</div>')
        if row.get(SAME_AS):
            print(
                '      <a rel="schema:sameAs" href="' + html.escape(row.get(SAME_AS)) + '">' + html.escape(
                    row.get(SAME_AS)) + '</a>')
        print('    </div>')

        if i == args.limit:
            break

        i = i + 1
    print('  </body>')
    print('</html>')


def create_microdata_output(reader):
    i = 1
    print('''<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Example Document</title>
  </head>
  <body>''')
    for row in reader:
        print('    <div itemscope itemtype="http://schema.org/MolecularEntity" itemid="http://example.org/me' + str(
            i) + '">')
        if row.get(IDENTIFIER):
            print('      <div itemprop="identifier">' + html.escape(row.get(IDENTIFIER)) + '</div>')
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
        if row.get(IUPAC_NAME):
            print('      <div itemprop="iupacName">' + html.escape(row.get(IUPAC_NAME)) + '</div>')
        if row.get(MOLECULAR_FORMULA):
            print('      <div itemprop="molecularFormula">' + html.escape(row.get(MOLECULAR_FORMULA)) + '</div>')
        if row.get(MOLECULAR_WEIGHT):
            print('      <div itemprop="molecularWeight">' + html.escape(row.get(MOLECULAR_WEIGHT)) + '</div>')
        if row.get(MONOISOTOPIC_MOLECULAR_WEIGHT):
            print('      <div itemprop="monoisotopicMolecularWeight">' + html.escape(
                row.get(MONOISOTOPIC_MOLECULAR_WEIGHT)) + '</div>')
        if row.get(DESCRIPTION):
            print('      <div itemprop="description">' + html.escape(row.get(DESCRIPTION)) + '</div>')
        if row.get(DISAMBIGUATING_DESCRIPTION):
            print('      <div itemprop="disambiguatingDescription">' + html.escape(
                row.get(DISAMBIGUATING_DESCRIPTION)) + '</div>')
        if row.get(IMAGE):
            print('      <a href="' + html.escape(row.get(IMAGE)) + '" itemprop="image">' + html.escape(
                row.get(IMAGE)) + '</a>')
        if row.get(ADDITIONAL_TYPE):
            print('      <a href="' + html.escape(
                row.get(ADDITIONAL_TYPE)) + '" itemprop="additionalType">' + html.escape(
                row.get(ADDITIONAL_TYPE)) + '</a>')
        if row.get(ALTERNATE_NAME):
            print('      <div itemprop="alternateName">' + html.escape(row.get(ALTERNATE_NAME)) + '</div>')
        if row.get(SAME_AS):
            print('      <a href="' + html.escape(row.get(ADDITIONAL_TYPE)) + '" itemprop="sameAs">' + html.escape(
                row.get(SAME_AS)) + '</a>')
        print('    </div>')

        if i == args.limit:
            break

        i = i + 1
    print('  </body>')
    print('</html>')


# set column names
IDENTIFIER = 'identifier'
NAME = 'name'
INCHIKEY = 'inChIKey'
INCHI = 'inChI'
SMILES = 'smiles'
URL = 'url'
IUPAC_NAME = 'iupacName'
MOLECULAR_FORMULA = 'molecularFormula'
MOLECULAR_WEIGHT = 'molecularWeight'
MONOISOTOPIC_MOLECULAR_WEIGHT = 'monoisotopicMolecularWeight'
DESCRIPTION = 'description'
DISAMBIGUATING_DESCRIPTION = 'disambiguatingDescription'
IMAGE = 'image'
ADDITIONAL_TYPE = 'additionalType'
ALTERNATE_NAME = 'alternateName'
SAME_AS = 'sameAs'
DEFAULT_COLUMN_NAMES = [IDENTIFIER, NAME, INCHIKEY, INCHI, SMILES, URL, IUPAC_NAME, MOLECULAR_FORMULA, MOLECULAR_WEIGHT,
                        MONOISOTOPIC_MOLECULAR_WEIGHT, DESCRIPTION, DISAMBIGUATING_DESCRIPTION, IMAGE, ADDITIONAL_TYPE,
                        ALTERNATE_NAME, SAME_AS]

parser = argparse.ArgumentParser(
    description='Converts chemical molecule data CSV files to Structured Data formats - JSON-LD, RDFa and Microdata. '
                'Supported CSV columns: ' +
                str(DEFAULT_COLUMN_NAMES))
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
parser.add_argument("-i", "--identifier", type=str, help="identifier column name (" + IDENTIFIER + " by default), Text")
parser.add_argument("-n", "--name", type=str, help="name column name (" + NAME + " by default), Text")
parser.add_argument("-ink", "--inChIKey", type=str, help="inChIKey column name (" + INCHIKEY + " by default), Text")
parser.add_argument("-in", "--inChI", type=str, help="inChI column name (" + INCHI + " by default), Text")
parser.add_argument("-s", "--smiles", type=str, help="smiles column name (" + SMILES + " by default), Text")
parser.add_argument("-u", "--url", type=str, help="url column name (" + URL + " by default), URL type")
parser.add_argument("-iu", "--iupacName", type=str, help="iupacName column name (" + IUPAC_NAME + " by default), Text")
parser.add_argument("-f", "--molecularFormula", type=str,
                    help="molecularFormula column name (" + MOLECULAR_FORMULA + " by default), Text")
parser.add_argument("-w", "--molecularWeight", type=str,
                    help="molecularWeight column name (" + MOLECULAR_WEIGHT + " by default), Mass e.g. 0.01 mg)")
parser.add_argument("-mw", "--monoisotopicMolecularWeight", type=str,
                    help="monoisotopicMolecularWeight column name (" + MONOISOTOPIC_MOLECULAR_WEIGHT + " by default), Mass e.g. 0.01 mg")
parser.add_argument("-d", "--description", type=str,
                    help="description column name (" + DESCRIPTION + " by default), Text")
parser.add_argument("-dd", "--disambiguatingDescription", type=str,
                    help="disambiguatingDescription column name (" + DISAMBIGUATING_DESCRIPTION + " by default), Text")
parser.add_argument("-img", "--image", type=str,
                    help="image column name (" + IMAGE + " by default), URL")
parser.add_argument("-at", "--additionalType", type=str,
                    help="additionalType column name (" + ADDITIONAL_TYPE + " by default), URL")
parser.add_argument("-an", "--alternateName", type=str,
                    help="alternateName column name (" + ALTERNATE_NAME + " by default), Text")
parser.add_argument("-sa", "--sameAs", type=str,
                    help="sameAs column name (" + SAME_AS + " by default), URL")

parser.add_argument("-c", "--columns",
                    help="Use only columns with renamed names",
                    action="store_true")
parser.add_argument("-l", "--limit", type=int, help="Maximum number of results")

args = parser.parse_args()

# replace default column names
if args.identifier or args.columns:
    ID = args.identifier
if args.name or args.columns:
    NAME = args.name
if args.inChIKey or args.columns:
    INCHIKEY = args.inChIKey
if args.inChI or args.columns:
    INCHI = args.inChI
if args.smiles or args.columns:
    SMILES = args.smiles
if args.url or args.columns:
    URL = args.url
if args.iupacName or args.columns:
    IUPAC_NAME = args.iupacName
if args.molecularFormula or args.columns:
    MOLECULAR_FORMULA = args.molecularFormula
if args.molecularWeight or args.columns:
    MOLECULAR_WEIGHT = args.molecularWeight
if args.monoisotopicMolecularWeight or args.columns:
    MONOISOTOPIC_MOLECULAR_WEIGHT = args.monoisotopicMolecularWeight
if args.description or args.columns:
    DESCRIPTION = args.description
if args.disambiguatingDescription or args.columns:
    DISAMBIGUATING_DESCRIPTION = args.disambiguatingDescription
if args.image or args.columns:
    IMAGE = args.image
if args.additionalType or args.columns:
    ADDITIONAL_TYPE = args.additionalType
if args.alternateName or args.columns:
    ALTERNATE_NAME = args.alternateName
if args.sameAs or args.columns:
    SAME_AS = args.sameAs

# read csv file and generate outputs
if args.file:
    with open(args.file, 'r') as csvfile:
        try:
            reader = csv.DictReader(csvfile)
            if args.jsonldhtml:
                print('''<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Example Document</title>
    <script type="application/ld+json">''')
                create_jsonld_output(reader)
                print('''    </script>
  </head>
</html>
                ''')
            elif args.jsonld:
                create_jsonld_output(reader)
            elif args.rdfa:
                create_rdfa_output(reader)
            elif args.microdata:
                create_microdata_output(reader)
        except Exception as e:
            print("Error:", e)
            exit()
