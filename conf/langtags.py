# from https://github.com/capstanlqc/langtags_basic_api/blob/main/functions.py 
# with a few changes e.g. added fetch_langtags_data()

import pprint
import requests

# ==== Fetch data ==== 

def fetch_langtags_data(url):
	response = requests.get(url)
	langtags = response.json()
	return langtags

# ==== Functions ==== 

# get language tag dictionary (if it exists)
def get_langtag_dict(data, input_tag):
	return next((tag for tag in data if tag["cApStAn"] == input_tag), None)

# corresponding tag in another convention 
def get_correspondent_tag(data, input_tag, source_convention, target_convention):
	return next((tag[target_convention] for tag in data if tag[source_convention] == input_tag), None)

# all tag dictionaries that have language subtag 'srb' (in cApStAn convention)
def get_tags_with_language_subtag(data, language_subtag):
	return [tag for tag in data if tag['cApStAn'].startswith(language_subtag + '-')]

# get all region subtags for a specific language subtag (in cApStAn convention)
def get_region_subtags_for_language(data, language_subtag):
	return [tag['cApStAn'].split('-')[1] for tag in data if tag['cApStAn'].startswith(language_subtag + '-')]

def get_langtags_in_convention(data, convention):
	if convention not in data[0].keys():
		print(f"Unknown convention: {convention}")
	return [entry[convention] for entry in data]

# ==== Calls ==== 

# get the whole list of cApStAn codes
# capstan_codes = [tag['cApStAn'] for tag in langtags]

# tag_dict = get_langtag_dict(langtags, 'val-ESP')
# tag = get_correspondent_tag(langtags, 'glg-ESP', 'cApStAn', 'OmegaT')
# tag_dicts = get_tags_with_language_subtag(langtags, 'srp')
# region_subtags = get_region_subtags_for_language(langtags, 'srp')


# ==== Output ==== 

# print(capstan_codes)
# pprint.pprint(tag_dict)
# pprint.pprint(tag)
# pprint.pprint(tag_dicts)
# pprint.pprint(f"Country tags language `srp` combines with: {region_subtags}")

# print("\nShould you want to get some other output, please uncomment other lines in the Output section, or modify the code as you like.")