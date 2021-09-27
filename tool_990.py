#https://registry.opendata.aws/irs990/
#https://github.com/jsfenfen/990-xml-reader
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
	array_of_parsed_schedules = org_name_parsed_filling.get_result()
	return array_of_parsed_schedules

# return array of form names
def get_list_of_schedules(org_name_parsed_filling):
	schedule_list = org_name_parsed_filling.list_schedules()
	return schedule_list

#check if type is dictionary and if so, fix
#returns as a dataframe
def dictionary_fix(possible_dict):
	if (type(possible_dict) is dict) == True:
		print('HELLO')
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


#combine array of group dataframes and array of scehdule dataframes
def combine_group_schedule(group_array,schedules_array):
	combined = group_array + schedules_array
	return combined

	
#combine dataframes and return array of combine dataframes
def combine_dataframes(array_of_dataframes_A, array_of_dataframes_B):
	combined = []
	for x, y in zip(array_of_dataframes_A, array_of_dataframes_B):
		frames = [x,y]
		result = pd.concat(frames)
		combined.append(result)
	return combined


#takes array of dataframes and turns in into an excel document
def to_excel(array_of_dataframes, name_excel_doc):
	index = 0
	with pd.ExcelWriter(name_excel_doc) as writer:  
		for i in array_of_dataframes:
		    index += 1
		    i.to_excel(writer,sheet_name = str(index))
		  
