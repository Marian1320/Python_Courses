# Write a function that finds the key with the maximum value in a dictionary.

def find_key_with_max_value(data_dict):
    return max(data_dict, key=data_dict.get)

dict1 = {"Ani": 98, "Gor": 92, "Diana": 95}
key_with_max_value = find_key_with_max_value(dict1)
print(f"The key is '{key_with_max_value}'.")
