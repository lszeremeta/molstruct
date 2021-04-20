#!/usr/bin/env python

"""Tests for molstruct package."""
import csv
import json
import os

import pytest

from molstruct import names as n
from molstruct import outputs

# Current directory
HERE = os.path.dirname(__file__)


@pytest.fixture
def csv_reader():
    """Open test file and prepare csv.DictReader."""
    with open(os.path.join(HERE, "drugbank_vocabulary_CC0_first_20_sample.csv"), 'r') as csvfile:
        yield csv.DictReader(csvfile)


#
# Tests
#
def test_jsonld_is_json(capsys, csv_reader):
    """Test if jsonld output is in JSON."""
    outputs.jsonld(csv_reader, None)

    stdout, stderr = capsys.readouterr()
    assert json.loads(stdout)
    assert stderr == ""


def test_jsonld_contains_required_strings(capsys, csv_reader):
    """Test if jsonld output contains required strings."""
    # set column name
    n.COLUMNS['name'] = "Common name"

    # list of strings to check
    strings = ['@id', '{', '}', ',', 'MolecularEntity', 'name']

    outputs.jsonld(csv_reader, None)

    stdout, stderr = capsys.readouterr()
    assert all(s in stdout for s in strings)
    assert stderr == ""


def test_jsonldhtml_contains_required_strings(capsys, csv_reader):
    """Test if jsonldhtml output contains required strings."""
    # set column name
    n.COLUMNS['name'] = "Common name"

    # list of strings to check
    strings = ['<', '>', '</', 'script>', '@id', '{', '}', ',', 'MolecularEntity', 'name']

    outputs.jsonldhtml(csv_reader, None)

    stdout, stderr = capsys.readouterr()
    assert all(s in stdout for s in strings)
    assert stderr == ""


def test_rdfa_contains_required_strings(capsys, csv_reader):
    """Test if rdfa output contains required strings."""
    # set column name
    n.COLUMNS['name'] = "Common name"

    # list of strings to check
    strings = ['<', '>', '</', 'typeof', 'property', 'MolecularEntity', 'name']

    outputs.rdfa(csv_reader, None)

    stdout, stderr = capsys.readouterr()
    assert all(s in stdout for s in strings)
    assert stderr == ""


def test_microdata_contains_required_strings(capsys, csv_reader):
    """Test if microdata output contains required strings."""
    # set column name
    n.COLUMNS['identifier'] = "CAS"

    # list of strings to check
    strings = ['<', '>', '</', 'itemscope', 'itemtype', 'itemprop', 'MolecularEntity', 'identifier']

    outputs.microdata(csv_reader, None)

    stdout, stderr = capsys.readouterr()
    assert all(s in stdout for s in strings)
    assert stderr == ""


def test_jsonld_text_limit_identifier(capsys, csv_reader):
    """Check if required string is in JSON output, limit 2, custom identifier."""
    text = "205923-56-4"
    n.COLUMNS['identifier'] = "CAS"

    outputs.jsonld(csv_reader, 2)

    stdout, stderr = capsys.readouterr()
    assert stderr == ""
    assert text in stdout


def test_jsonldhtml_text_limit_name(capsys, csv_reader):
    """Check if required string is in JSON+HTML output, limit 7, custom name."""
    text = "Leuprolide"
    n.COLUMNS['name'] = "Common name"

    outputs.jsonldhtml(csv_reader, 7)

    stdout, stderr = capsys.readouterr()
    assert stderr == ""
    assert text in stdout


def test_rdfa_text_limit_identifier(capsys, csv_reader):
    """Check if required string is in RDFa output, limit 4, custom identifier."""
    text = "143831-71-4"
    n.COLUMNS['identifier'] = "CAS"

    outputs.rdfa(csv_reader, 4)

    stdout, stderr = capsys.readouterr()
    assert stderr == ""
    assert text in stdout


def test_create_microdata_text_exceeded_limit_name(capsys, csv_reader):
    """Check if required string is in Microdata output, limit 100 (more than lines in file), custom name."""
    text = "Darbepoetin alfa"
    n.COLUMNS['name'] = "Common name"

    outputs.microdata(csv_reader, 100)

    stdout, stderr = capsys.readouterr()
    assert stderr == ""
    assert text in stdout


def test_multiple_values_jsonld(capsys, csv_reader):
    """Check if multiple values are supported in JSON-LD."""
    text = '["Hirudin variant-1", "Lepirudin recombinant"]'
    n.COLUMNS['alternateName'] = "Synonyms"

    outputs.jsonld(csv_reader, 1)

    stdout, stderr = capsys.readouterr()
    assert stderr == ""
    assert text in stdout


def test_multiple_values_rdfa(capsys, csv_reader):
    """Check if multiple values support in RDFa."""
    text = 'property="schema:alternateName"'
    n.COLUMNS['alternateName'] = "Synonyms"

    outputs.rdfa(csv_reader, 1)

    stdout, stderr = capsys.readouterr()
    assert stderr == ""
    assert stdout.count(text) > 1


def test_multiple_values_microdata(capsys, csv_reader):
    """Check if multiple values support in Microdata."""
    text = 'itemprop="alternateName"'
    n.COLUMNS['alternateName'] = "Synonyms"

    outputs.microdata(csv_reader, 1)

    stdout, stderr = capsys.readouterr()
    assert stderr == ""
    assert stdout.count(text) > 1


def test_jsonld_iri_no_id(capsys, csv_reader):
    """Check if JSON-LD output have IRI for IRI subject type without id."""
    text = 'http://example.com/molecule0'
    text2 = 'id="'
    n.COLUMNS['identifier'] = "CAS"
    n.SUBJECT_BASE = "http://example.com/molecule"

    outputs.jsonld(csv_reader)

    stdout, stderr = capsys.readouterr()
    assert stderr == ""
    assert text in stdout
    assert text2 not in stdout


def test_rdfa_iri_id(capsys, csv_reader):
    """Check if RDFa output have IRI for IRI subject type with id."""
    text = 'about="http://example.com/molecule#m1"'
    text2 = 'id="m1"'
    n.COLUMNS['name'] = "Common name"
    n.SUBJECT_BASE = "http://example.com/molecule#m"

    outputs.rdfa(csv_reader)

    stdout, stderr = capsys.readouterr()
    assert stderr == ""
    assert text in stdout
    assert text2 in stdout


def test_microdata_iri_no_id(capsys, csv_reader):
    """Check if Microdata output have IRI for IRI subject type without id."""
    text = 'itemid="http://example-molecules.com/example2"'
    text2 = ' id="'
    n.COLUMNS['alternateName'] = "Synonyms"
    n.SUBJECT_BASE = "http://example-molecules.com/example"

    outputs.microdata(csv_reader)

    stdout, stderr = capsys.readouterr()
    assert stderr == ""
    assert text in stdout
    assert text2 not in stdout


def test_jsonld_uuid(capsys, csv_reader):
    """Check if JSON-LD output have urn:uuid: for UUID subject type."""
    text = '"urn:uuid:'
    n.COLUMNS['alternateName'] = "Synonyms"
    n.SUBJECT_BASE = False

    outputs.jsonld(csv_reader)

    stdout, stderr = capsys.readouterr()
    assert stderr == ""
    assert text in stdout


def test_rdfa_uuid(capsys, csv_reader):
    """Check if RDFa output have urn:uuid: for UUID subject type."""
    text = 'about="urn:uuid:'
    n.COLUMNS['identifier'] = "CAS"
    n.SUBJECT_BASE = False

    outputs.rdfa(csv_reader)

    stdout, stderr = capsys.readouterr()
    assert stderr == ""
    assert text in stdout


def test_microdata_uuid(capsys, csv_reader):
    """Check if Microdata output have urn:uuid: for UUID subject type."""
    text = 'itemid="urn:uuid:'
    n.COLUMNS['name'] = "Common name"
    n.SUBJECT_BASE = False

    outputs.microdata(csv_reader)

    stdout, stderr = capsys.readouterr()
    assert stderr == ""
    assert text in stdout


def test_jsonld_bnode(capsys, csv_reader):
    """Check if JSON-LD output have bnode for bdnode subject type."""
    text = '_:b1'
    n.COLUMNS['name'] = "Common name"
    n.SUBJECT_BASE = '_:b'

    outputs.jsonld(csv_reader)

    stdout, stderr = capsys.readouterr()
    assert stderr == ""
    assert text in stdout


def test_rdfa_bnode(capsys, csv_reader):
    """Check if RDFa output have bnode for bode subject type."""
    text = '_:b0'
    n.COLUMNS['identifier'] = "CAS"
    n.SUBJECT_BASE = '_:b'

    outputs.rdfa(csv_reader)

    stdout, stderr = capsys.readouterr()
    assert stderr == ""
    assert text in stdout


def test_microdata_bnode(capsys, csv_reader):
    """Check if Microdata output have bnode for bnode subject type."""
    text = '_:b2'
    n.COLUMNS['alternateName'] = "Synonyms"
    n.SUBJECT_BASE = '_:b'

    outputs.microdata(csv_reader)

    stdout, stderr = capsys.readouterr()
    assert stderr == ""
    assert text in stdout
