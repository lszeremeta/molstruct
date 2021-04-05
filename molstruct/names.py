#!/usr/bin/env python

# value delimiter
VALUE_DELIMITER = ' | '

# subject base of molecule
# False for 'uuid' subject type
# '_:b' for 'bnode' subject type
SUBJECT_BASE = 'https://example.com/molecule#entity'

# column names
COLUMNS = {'identifier': 'identifier',
           'name': 'name',
           'inChIKey': 'inChIKey',
           'inChI': 'inChI',
           'smiles': 'smiles',
           'url': 'url',
           'iupacName': 'iupacName',
           'molecularFormula': 'molecularFormula',
           'molecularWeight': 'molecularWeight',
           'monoisotopicMolecularWeight': 'monoisotopicMolecularWeight',
           'description': 'description',
           'disambiguatingDescription': 'disambiguatingDescription',
           'image': 'image',
           'alternateName': 'alternateName',
           'sameAs': 'sameAs'
           }
