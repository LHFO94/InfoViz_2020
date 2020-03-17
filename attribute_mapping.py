def map_attributes(input_array,attribute_map):
    output_array = []

    for i in input_array:
        output_array.append(attribute_map.iloc[i])

    output_list = list(sum(output_array))
    return output_list
