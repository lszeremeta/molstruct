#!/usr/bin/env python

"""Tests for molstruct package."""
import csv
import json
import os

import pytest

from molstruct import names
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
    names.NAME = "Common name"

    # list of strings to check
    strings = ['@id', '{', '}', ',', 'MolecularEntity', 'name']

    outputs.jsonld(csv_reader, None)

    stdout, stderr = capsys.readouterr()
    assert all(s in stdout for s in strings)
    assert stderr == ""


def test_jsonld_html_contains_required_strings(capsys, csv_reader):
    """Test if jsonld_html output contains required strings."""
    # set column name
    names.NAME = "Common name"

    # list of strings to check
    strings = ['<', '>', '</', 'script>', '@id', '{', '}', ',', 'MolecularEntity', 'name']

    outputs.jsonld_html(csv_reader, None)

    stdout, stderr = capsys.readouterr()
    assert all(s in stdout for s in strings)
    assert stderr == ""


def test_rdfa_contains_required_strings(capsys, csv_reader):
    """Test if rdfa output contains required strings."""
    # set column name
    names.NAME = "Common name"

    # list of strings to check
    strings = ['<', '>', '</', 'typeof', 'property', 'MolecularEntity', 'name']

    outputs.rdfa(csv_reader, None)

    stdout, stderr = capsys.readouterr()
    assert all(s in stdout for s in strings)
    assert stderr == ""


def test_microdata_contains_required_strings(capsys, csv_reader):
    """Test if microdata output contains required strings."""
    # set column name
    names.IDENTIFIER = "CAS"

    # list of strings to check
    strings = ['<', '>', '</', 'itemscope', 'itemtype', 'itemprop', 'MolecularEntity', 'identifier']

    outputs.microdata(csv_reader, None)

    stdout, stderr = capsys.readouterr()
    assert all(s in stdout for s in strings)
    assert stderr == ""


def test_jsonld_text_limit_identifier(capsys, csv_reader):
    """Check if required string is in JSON output, limit 2, custom identifier."""
    text = "205923-56-4"
    names.IDENTIFIER = "CAS"

    outputs.jsonld(csv_reader, 2)

    stdout, stderr = capsys.readouterr()
    assert stderr == ""
    assert text in stdout


def test_jsonldhtml_text_limit_name(capsys, csv_reader):
    """Check if required string is in JSON+HTML output, limit 7, custom name."""
    text = "Leuprolide"
    names.NAME = "Common name"

    outputs.jsonld_html(csv_reader, 7)

    stdout, stderr = capsys.readouterr()
    assert stderr == ""
    assert text in stdout


def test_rdfa_text_limit_identifier(capsys, csv_reader):
    """Check if required string is in RDFa output, limit 4, custom identifier."""
    text = "143831-71-4"
    names.IDENTIFIER = "CAS"

    outputs.rdfa(csv_reader, 4)

    stdout, stderr = capsys.readouterr()
    assert stderr == ""
    assert text in stdout


def test_create_microdata_text_exceeded_limit_name(capsys, csv_reader):
    """Check if required string is in Microdata output, limit 100 (more than lines in file), custom name."""
    text = "Darbepoetin alfa"
    names.NAME = "Common name"

    outputs.microdata(csv_reader, 100)

    stdout, stderr = capsys.readouterr()
    assert stderr == ""
    assert text in stdout
