#! /usr/bin/python

from check_dependencies import CheckDependencies

def test_default():
    CheckDependencies(None)

def test_hydrotrend():
    CheckDependencies("hydrotrend")
