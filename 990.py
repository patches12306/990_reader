import pandas as pd
from irsx.xmlrunner import XMLRunner
import json
import numpy as np

#call xml runner

xml_runner = XMLRunner()

#funtion to return parsed 990s information
def fill_parse(id_number):
	org_name_parsed_filling = xml_runner.run_filing(id_number)
	return org_name_parsed_filling

#function to return array of parsed schedules
def parsed_schedues(org_name_parsed_filling):
	result = org_name_parsed_filling.get_result()
	return result

# return array of form names
def get_list_of_schedules(org_name_parsed_filling):
	schedule_list = org_name_parsed_filling.list_schedules()
	return schedule_list

#check if type is dictionary and if so, fix
def dictionary_fix(possible_dict):
	if type(possible_dict) is dict == True:
		my_dict = {}
		for key in possible_dict:
		    val = []
		    for value in (possible_dict):
		        if value == key:
		            tru_val = possible_dict[value]
		            val.append(tru_val)
		    my_dict[key] = val
		df = pd.DataFrame(my_dict)
		return df
	else:
		df = pd.DataFrame(possible_dict)
		return df

#get group_data, returns array of dataframes of all groups
def get_group_data(array_of_parsed_schedules):
	df_array = []
	for i in array_of_parsed_schedules[1]["groups"].keys():
		df = dictionary_fix(array_of_parsed_schedules[1]['groups'][i])
		df_array.append(df)
	return df_array

#get schedule part data, returns array of dataframes of all schedules parts
def get_schedule_data(array_of_parsed_schedules):
	df_array = []
	for i in array_of_parsed_schedules[1]["schedule_parts"].keys():
		df = dictionary_fix(array_of_parsed_schedules[1]['schedule_parts'][i])
		df_array.append(df)
	return df_array

