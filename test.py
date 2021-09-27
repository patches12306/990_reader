import tool_990
import pandas as pd
from irsx.xmlrunner import XMLRunner
import json
import numpy as np

def main():
	health_2019 = 201910149349301126

	parsed_health_filling_2019 = tool_990.fill_parse(health_2019)
	print(parsed_health_filling_2019)

	health_2019_parsed_schedules = tool_990.parsed_schedues(parsed_health_filling_2019)

	health_2019_schedule_list = tool_990.get_list_of_schedules(parsed_health_filling_2019)

	group_df_array = tool_990.get_group_data(health_2019_parsed_schedules)
	print((group_df_array))


	schedule_df_array = tool_990.get_schedule_data(health_2019_parsed_schedules)
	print(schedule_df_array)
	print(len(schedule_df_array))

	



	health_2020 = 202010159349300471

	parsed_health_filling_2020 = tool_990.fill_parse(health_2020)
	print(parsed_health_filling_2020)


	health_2020_parsed_schedules = tool_990.parsed_schedues(parsed_health_filling_2020)

	health_2020_schedule_list = tool_990.get_list_of_schedules(parsed_health_filling_2020)

	group_df_array_2020 = tool_990.get_group_data(health_2020_parsed_schedules)
	print((group_df_array_2020))

	schedule_df_array_2020 = tool_990.get_schedule_data(health_2020_parsed_schedules)
	print(schedule_df_array_2020)
	print(len(schedule_df_array_2020))

	# df = schedule_df_array_2020[0].merge(schedule_df_array[0], how='right', left_index = True)
	# frames = [schedule_df_array_2020[0],schedule_df_array[0]]

	# result = pd.concat(frames)
	# print(result)
	combined_schedules = tool_990.combine_dataframes(schedule_df_array_2020,schedule_df_array)
	# print(combined_schedules)

	combined_groups = tool_990.combine_dataframes(group_df_array_2020,group_df_array)
	# print(combined_groups)

	combined = tool_990.combine_group_schedule(combined_groups,combined_schedules)
	print(len(combined_groups))
	print(len(combined_schedules))

	print(len(combined))
	#tool_990.to_excel(combined, "combined.xlsx")
	
	
	# MARILLAC
	##########
	##########


	marillac_2019 = 201901129349300905

	marillac_parsed_health_filling_2019 = tool_990.fill_parse(marillac_2019)


	marillac_health_2019_parsed_schedules = tool_990.parsed_schedues(marillac_parsed_health_filling_2019)

	marillac_health_2019_schedule_list = tool_990.get_list_of_schedules(marillac_parsed_health_filling_2019)


	marillac_group_df_array_2019 = tool_990.get_group_data(marillac_health_2019_parsed_schedules)


	marillac_schedule_df_array_2019 = tool_990.get_schedule_data(marillac_health_2019_parsed_schedules)
	

	



	marillac_2018 = 201840729349200734

	marillac_parsed_health_filling_2018 = tool_990.fill_parse(marillac_2018)


	marillac_health_2018_parsed_schedules = tool_990.parsed_schedues(marillac_parsed_health_filling_2018)

	marillac_health_2018_schedule_list = tool_990.get_list_of_schedules(marillac_parsed_health_filling_2018)


	marillac_group_df_array_2018 = tool_990.get_group_data(marillac_health_2018_parsed_schedules)


	marillac_schedule_df_array_2018 = tool_990.get_schedule_data(marillac_health_2018_parsed_schedules)

	# df = schedule_df_array_2020[0].merge(schedule_df_array[0], how='right', left_index = True)
	# frames = [schedule_df_array_2020[0],schedule_df_array[0]]

	# result = pd.concat(frames)
	# print(result)
	marillac_combined_schedules = tool_990.combine_dataframes(marillac_schedule_df_array_2019, marillac_schedule_df_array_2018)
	# print(combined_schedules)

	marillac_combined_groups = tool_990.combine_dataframes(marillac_group_df_array_2019, marillac_group_df_array_2018)

	marillac_combined = tool_990.combine_group_schedule(marillac_combined_groups,marillac_combined_schedules)

	all_combined = tool_990.combine_group_schedule(combined,marillac_combined)
	print((combined))

	tool_990.to_excel(all_combined, "all_combined.xlsx")
main()

