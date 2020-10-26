#!/usr/bin/env python
import html
import json

import molstruct.names as n


def jsonld_html(reader, limit):
    print('''<!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Example Document</title>
        <script type="application/ld+json">''')
    jsonld(reader, limit)
    print('''        </script>
      </head>
    </html>''')


def jsonld(reader, limit):
    i = 1

    out_str = '{\n'
    out_str += '  "@graph" : [\n'
    for row in reader:
        out_str += '  {\n'
        out_str += '  "@id" : ' + json.dumps(n.BASE_URI_MOLECULE + str(i)) + ',\n'
        out_str += '  "@type" : "https://schema.org/MolecularEntity",\n'
        if row.get(n.IDENTIFIER):
            out_str += '  "identifier" : ' + json.dumps(row.get(n.IDENTIFIER)) + ',\n'
        if row.get(n.NAME):
            out_str += '  "name" : ' + json.dumps(row.get(n.NAME)) + ',\n'
        if row.get(n.INCHIKEY):
            out_str += '  "inChIKey" : ' + json.dumps(row.get(n.INCHIKEY)) + ',\n'
        if row.get(n.INCHI):
            out_str += '  "inChI" : ' + json.dumps(row.get(n.INCHI)) + ',\n'
        if row.get(n.SMILES):
            out_str += '  "smiles" : ' + json.dumps(row.get(n.SMILES)) + ',\n'
        if row.get(n.URL):
            out_str += '  "url" : ' + json.dumps(row.get(n.URL)) + ',\n'
        if row.get(n.IUPAC_NAME):
            out_str += '  "iupacName" : ' + json.dumps(row.get(n.IUPAC_NAME)) + ',\n'
        if row.get(n.MOLECULAR_FORMULA):
            out_str += '  "molecularFormula" : ' + json.dumps(row.get(n.MOLECULAR_FORMULA)) + ',\n'
        if row.get(n.MOLECULAR_WEIGHT):
            out_str += '  "molecularWeight" : ' + json.dumps(row.get(n.MOLECULAR_WEIGHT)) + ',\n'
        if row.get(n.MONOISOTOPIC_MOLECULAR_WEIGHT):
            out_str += '  "monoisotopicMolecularWeight" : ' + json.dumps(
                row.get(n.MONOISOTOPIC_MOLECULAR_WEIGHT)) + ',\n'
        if row.get(n.DESCRIPTION):
            out_str += '  "description" : ' + json.dumps(row.get(n.DESCRIPTION)) + ',\n'
        if row.get(n.DISAMBIGUATING_DESCRIPTION):
            out_str += '  "disambiguatingDescription" : ' + json.dumps(row.get(n.DISAMBIGUATING_DESCRIPTION)) + ',\n'
        if row.get(n.ADDITIONAL_TYPE):
            out_str += '  "additionalType" : ' + json.dumps(row.get(n.ADDITIONAL_TYPE)) + ',\n'
        if row.get(n.ALTERNATE_NAME):
            out_str += '  "alternateName" : ' + json.dumps(row.get(n.ALTERNATE_NAME)) + ',\n'
        if row.get(n.SAME_AS):
            out_str += '  "sameAs" : ' + json.dumps(row.get(n.SAME_AS)) + ',\n'
        out_str = out_str[:-2] + '\n'
        out_str += '  },'

        if i == limit:
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


def rdfa(reader, limit):
    i = 1
    print('''<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Example Document</title>
  </head>
  <body vocab="http://schema.org/">''')
    for row in reader:
        print('    <div typeof="schema:MolecularEntity" about="' + html.escape(n.BASE_URI_MOLECULE, quote=True) + str(
            i) + '">')
        if row.get(n.IDENTIFIER):
            print('      <div property="schema:identifier">' + html.escape(row.get(n.IDENTIFIER)) + '</div>')
        if row.get(n.NAME):
            print('      <div property="schema:name">' + html.escape(row.get(n.NAME)) + '</div>')
        if row.get(n.INCHIKEY):
            print('      <div property="schema:inChIKey">' + html.escape(row.get(n.INCHIKEY)) + '</div>')
        if row.get(n.INCHI):
            print('      <div property="schema:inChI">' + html.escape(row.get(n.INCHI)) + '</div>')
        if row.get(n.SMILES):
            print('      <div property="schema:smiles">' + html.escape(row.get(n.SMILES)) + '</div>')
        if row.get(n.URL):
            print(
                '      <a rel="schema:url" href="' + html.escape(row.get(n.URL), quote=True) + '">' + html.escape(
                    row.get(n.URL)) + '</a>')
        if row.get(n.IUPAC_NAME):
            print('      <div property="schema:iupacName">' + html.escape(row.get(n.IUPAC_NAME)) + '</div>')
        if row.get(n.MOLECULAR_FORMULA):
            print(
                '      <div property="schema:molecularFormula">' + html.escape(row.get(n.MOLECULAR_FORMULA)) + '</div>')
        if row.get(n.MOLECULAR_WEIGHT):
            print('      <div property="schema:molecularWeight">' + html.escape(row.get(n.MOLECULAR_WEIGHT)) + '</div>')
        if row.get(n.MONOISOTOPIC_MOLECULAR_WEIGHT):
            print('      <div property="schema:monoisotopicMolecularWeight">' + html.escape(
                row.get(n.MONOISOTOPIC_MOLECULAR_WEIGHT)) + '</div>')
        if row.get(n.DESCRIPTION):
            print('      <div property="schema:description">' + html.escape(row.get(n.DESCRIPTION)) + '</div>')
        if row.get(n.DISAMBIGUATING_DESCRIPTION):
            print('      <div property="schema:disambiguatingDescription">' + html.escape(
                row.get(n.DISAMBIGUATING_DESCRIPTION)) + '</div>')
        if row.get(n.IMAGE):
            print(
                '      <a rel="schema:image" href="' + html.escape(row.get(n.IMAGE), quote=True) + '">' + html.escape(
                    row.get(n.IMAGE)) + '</a>')
        if row.get(n.ADDITIONAL_TYPE):
            print(
                '      <a rel="schema:additionalType" href="' + html.escape(
                    row.get(n.ADDITIONAL_TYPE), quote=True) + '">' + html.escape(
                    row.get(n.ADDITIONAL_TYPE)) + '</a>')
        if row.get(n.ALTERNATE_NAME):
            print('      <div property="schema:alternateName">' + html.escape(row.get(n.ALTERNATE_NAME)) + '</div>')
        if row.get(n.SAME_AS):
            print(
                '      <a rel="schema:sameAs" href="' + html.escape(row.get(n.SAME_AS),
                                                                    quote=True) + '">' + html.escape(
                    row.get(n.SAME_AS)) + '</a>')
        print('    </div>')

        if i == limit:
            break

        i = i + 1
    print('  </body>')
    print('</html>')


def microdata(reader, limit):
    i = 1
    print('''<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Example Document</title>
  </head>
  <body>''')
    for row in reader:
        print('    <div itemscope itemtype="http://schema.org/MolecularEntity" itemid="' + html.escape(
            n.BASE_URI_MOLECULE, quote=True) + str(
            i) + '">')
        if row.get(n.IDENTIFIER):
            print('      <div itemprop="identifier">' + html.escape(row.get(n.IDENTIFIER)) + '</div>')
        if row.get(n.NAME):
            print('      <div itemprop="name">' + html.escape(row.get(n.NAME)) + '</div>')
        if row.get(n.INCHIKEY):
            print('      <div itemprop="inChIKey">' + html.escape(row.get(n.INCHIKEY)) + '</div>')
        if row.get(n.INCHI):
            print('      <div itemprop="inChI">' + html.escape(row.get(n.INCHI)) + '</div>')
        if row.get(n.SMILES):
            print('      <div itemprop="smiles">' + html.escape(row.get(n.SMILES)) + '</div>')
        if row.get(n.URL):
            print('      <a href="' + html.escape(row.get(n.URL), quote=True) + '" itemprop="url">' + html.escape(
                row.get(n.URL)) + '</a>')
        if row.get(n.IUPAC_NAME):
            print('      <div itemprop="iupacName">' + html.escape(row.get(n.IUPAC_NAME)) + '</div>')
        if row.get(n.MOLECULAR_FORMULA):
            print('      <div itemprop="molecularFormula">' + html.escape(row.get(n.MOLECULAR_FORMULA)) + '</div>')
        if row.get(n.MOLECULAR_WEIGHT):
            print('      <div itemprop="molecularWeight">' + html.escape(row.get(n.MOLECULAR_WEIGHT)) + '</div>')
        if row.get(n.MONOISOTOPIC_MOLECULAR_WEIGHT):
            print('      <div itemprop="monoisotopicMolecularWeight">' + html.escape(
                row.get(n.MONOISOTOPIC_MOLECULAR_WEIGHT)) + '</div>')
        if row.get(n.DESCRIPTION):
            print('      <div itemprop="description">' + html.escape(row.get(n.DESCRIPTION)) + '</div>')
        if row.get(n.DISAMBIGUATING_DESCRIPTION):
            print('      <div itemprop="disambiguatingDescription">' + html.escape(
                row.get(n.DISAMBIGUATING_DESCRIPTION)) + '</div>')
        if row.get(n.IMAGE):
            print('      <a href="' + html.escape(row.get(n.IMAGE), quote=True) + '" itemprop="image">' + html.escape(
                row.get(n.IMAGE)) + '</a>')
        if row.get(n.ADDITIONAL_TYPE):
            print('      <a href="' + html.escape(
                row.get(n.ADDITIONAL_TYPE), quote=True) + '" itemprop="additionalType">' + html.escape(
                row.get(n.ADDITIONAL_TYPE)) + '</a>')
        if row.get(n.ALTERNATE_NAME):
            print('      <div itemprop="alternateName">' + html.escape(row.get(n.ALTERNATE_NAME)) + '</div>')
        if row.get(n.SAME_AS):
            print('      <a href="' + html.escape(row.get(n.ADDITIONAL_TYPE),
                                                  quote=True) + '" itemprop="sameAs">' + html.escape(
                row.get(n.SAME_AS)) + '</a>')
        print('    </div>')

        if i == limit:
            break

        i = i + 1
    print('  </body>')
    print('</html>')
