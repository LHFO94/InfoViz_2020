#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd

# pd.options.display.max_rows = 999

input_array = [4, 9, 14, 19, 24, 29, 34, 39, 44, 49, 54, 59, 64, 69, 74]

map_filepath = 'quiz_attributes_commas.csv'
attribute_map = pd.read_csv(file_path, index_col = 0)


def check_attribute_range(attribute_map):
    '''Checks if max. attribute values are too small or large.'''
    
    for col in attribute_map.columns:
            total = sum(attribute_map[col])
            if 0.0 < total < 0.8:
                print(col, total)
            elif 2.0 > total > 1.0:
                print(col, total)
            else:
                pass
            
def map_attributes(input_array):
    '''Sums attributes for given answers to make a pseudo-photo.'''
    output_array = []
    
    for i in input_array:
        output_array.append(attribute_map.iloc[i])
        
    output_list = list(sum(output_array))
    return output_list

check_attribute_range(attribute_map)
map_attributes(input_array)
