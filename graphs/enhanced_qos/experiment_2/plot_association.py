#!/usr/bin/env python
__author__ = "Daniel Kulenkamp"
__copyright__ = "Copyright 2020, QoS-aware WiFi Slicing"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Daniel Kulenkamp"
__email__ = "dkulenka@asu.edu"
__status__ = "Prototype"

" Python script for testing association plot"

from graphs.enhanced_qos.association_graph import *

make_association_graph(
    experiment_path='gomez/association/',
    filenames=['wtp1_association', 'wtp2_association', 'wtp3_association']
)

make_association_graph(
    experiment_path='isolani/association/',
    filenames=['wtp1_association', 'wtp2_association', 'wtp3_association']
)