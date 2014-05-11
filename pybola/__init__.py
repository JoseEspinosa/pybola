"""
===========
Description
===========

pybola is a library to transform behavioral data in the form of csv files into files 
directly loadable into a genome browser (bed or bedGraph) for its easy visualization and browsing.
"""
from __future__ import division
import argparse
import csv
import os
import itertools
import operator

__all__ = ["tracks"]

__author__ = 'Jose Espinosa-Carrasco'