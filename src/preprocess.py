#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

_MAP_COUNTRIES = {
    'Republic of Congo': 'Congo'
}

# Import dataset
dataset = pd.read_csv('pax_all_agreements_data.csv')

"""
# Split countries
countries = dataset['Con'].str.split('/', expand=True)

# Remove trailing parentheses
countries = countries.replace(r"[()]", "", regex=True)

countries_freq = countries.stack().value_counts()
countries_freq.columns = ['country_name', 'frequency']
countries_freq.to_csv('country_frequencies.csv')
"""

dataset['GRef_boolean'] = dataset['GRef'] > 0
dataset['GRa_boolean'] = dataset['GRa'] > 0
dataset['GCh_boolean'] = dataset['GCh'] > 0
dataset['GRe_boolean'] = dataset['GRe'] > 0
dataset['GeWom_boolean'] = dataset['GeWom'] > 0
dataset['GDis_boolean'] = dataset['GDis'] > 0
dataset['GInd_boolean'] = dataset['GInd'] > 0
dataset['GeLgbti_boolean'] = dataset['GeLgbti'] > 0

dataset.to_csv('data_preprocessed.csv')
