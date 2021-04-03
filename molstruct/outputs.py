#!/usr/bin/env python
import html
import json
import uuid

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
    i = 0

    out_str = '{\n'
    out_str += '  "@graph" : [\n'
    for row in reader:
        out_str += '  {\n'

        if n.SUBJECT_BASE:
            out_str += '  "@id" : ' + json.dumps(n.SUBJECT_BASE + str(i))
        else:
            out_str += '  "@id" : ' + json.dumps('urn:uuid:' + str(uuid.uuid4()))

        out_str += ',\n  "@type" : "https://schema.org/MolecularEntity",\n'

        for key, value in n.COLUMNS.items():
            if n.VALUE_DELIMITER in str(row.get(value)):
                out_str += '  "' + key + '" : ' + json.dumps(row.get(value).split(n.VALUE_DELIMITER)) + ',\n'
            elif row.get(value):
                out_str += '  "' + key + '" : ' + json.dumps(row.get(value)) + ',\n'

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
    "alternateName" : {
      "@id" : "https://schema.org/alternateName"
    },
    "sameAs" : {
      "@id" : "https://schema.org/sameAs"
    },
    "schema" : "https://schema.org/"
  }
}''')


def rdfa(reader, limit):
    i = 0
    print('''<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Example Document</title>
  </head>
  <body vocab="http://schema.org/">''')
    for row in reader:
        if n.SUBJECT_BASE:
            print('    <div typeof="schema:MolecularEntity" about="' + html.escape(n.SUBJECT_BASE + str(
                i), quote=True), end='')

            if '#' in n.SUBJECT_BASE:
                print('" id="' + html.escape(n.SUBJECT_BASE.rpartition('#')[-1] + str(i), quote=True), end='')

        else:
            print('    <div typeof="schema:MolecularEntity" about="urn:uuid:' + str(uuid.uuid4()), end='')

        print('">')

        for key, value in n.COLUMNS.items():
            if row.get(value):
                values = row.get(value).split(n.VALUE_DELIMITER)
                for v in values:
                    if key == 'url' or key == 'sameAs':
                        print('      <a href="' + html.escape(v,
                                                              quote=True) + '" rel="schema:' + key + '">' + html.escape(
                            v) + '</a>')
                    elif key == 'image':
                        print('      <img src="' + html.escape(v, quote=True) + '" alt="Image of the Molecule' + str(
                            i) + '" rel="schema:' + key + '">')
                    else:
                        print('      <div property="schema:' + key + '">' + html.escape(v) + '</div>')

        print('    </div>')

        if i == limit:
            break

        i = i + 1
    print('  </body>')
    print('</html>')


def microdata(reader, limit):
    i = 0
    print('''<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Example Document</title>
  </head>
  <body>''')
    for row in reader:
        if n.SUBJECT_BASE:
            print('    <div itemscope itemtype="http://schema.org/MolecularEntity" itemid="' + html.escape(
                n.SUBJECT_BASE + str(
                    i), quote=True), end='')

            if '#' in n.SUBJECT_BASE:
                print('" id="' + html.escape(n.SUBJECT_BASE.rpartition('#')[-1] + str(i), quote=True), end='')
        else:
            print(
                '    <div itemscope itemtype="http://schema.org/MolecularEntity" itemid="urn:uuid:' + str(uuid.uuid4()),
                end='')

        print('">')

        for key, value in n.COLUMNS.items():
            if row.get(value):
                values = row.get(value).split(n.VALUE_DELIMITER)
                for v in values:
                    if key == 'url' or key == 'sameAs':
                        print(
                            '      <a href="' + html.escape(v, quote=True) + '" itemprop="' + key + '">' + html.escape(
                                v) + '</a>')
                    elif key == 'image':
                        print('      <img src="' + html.escape(v, quote=True) + '" alt="Image of the Molecule' + str(
                            i) + '" itemprop="' + key + '">')
                    else:
                        print('      <div itemprop="' + key + '">' + html.escape(v) + '</div>')

        print('    </div>')

        if i == limit:
            break

        i = i + 1
    print('  </body>')
    print('</html>')
