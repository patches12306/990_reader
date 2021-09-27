import tool_990
import pandas as pd
from irsx.xmlrunner import XMLRunner
import json
import numpy as np


#201901129349300905
def main():

	health_2019 = 201901129349300905

	parsed_health_filling_2019 = tool_990.fill_parse(health_2019)
	print(parsed_health_filling_2019)

	health_2019_parsed_schedules = tool_990.parsed_schedues(parsed_health_filling_2019)
	print(health_2019_parsed_schedules)
	
	health_2019_schedule_list = tool_990.get_list_of_schedules(parsed_health_filling_2019)
	print(health_2019_schedule_list)

	group_df_array = tool_990.get_group_data(health_2019_parsed_schedules)
	print((group_df_array))
	print(len(group_df_array))

	schedule_df_array = tool_990.get_schedule_data(health_2019_parsed_schedules)
	print(schedule_df_array)
	print(len(schedule_df_array))

	



	health_2018 = 201840729349200734

	parsed_health_filling_2018 = tool_990.fill_parse(health_2018)
	print(parsed_health_filling_2018)


	health_2018_parsed_schedules = tool_990.parsed_schedues(parsed_health_filling_2018)

	health_2018_schedule_list = tool_990.get_list_of_schedules(parsed_health_filling_2018)

	group_df_array_2018 = tool_990.get_group_data(health_2018_parsed_schedules)
	print((group_df_array_2018))
	print(len(group_df_array_2018))

	schedule_df_array_2018 = tool_990.get_schedule_data(health_2018_parsed_schedules)
	print(schedule_df_array_2018)
	print(len(schedule_df_array_2018))

	# df = schedule_df_array_2020[0].merge(schedule_df_array[0], how='right', left_index = True)
	# frames = [schedule_df_array_2020[0],schedule_df_array[0]]

	# result = pd.concat(frames)
	# print(result)
	combined_schedules = tool_990.combine_dataframes(schedule_df_array, schedule_df_array_2018)
	# print(combined_schedules)

	combined_groups = tool_990.combine_dataframes(group_df_array, group_df_array_2018)
	# print(combined_groups)

	tool_990.to_excel(combined_schedules, "Marilac_combined_schedules.xlsx")
	tool_990.to_excel(combined_groups, "Marilac_combined_groups.xlsx")

	print(len(schedule_df_array))
	print(len(schedule_df_array_2018))

	print(len(group_df_array))
	print(len(group_df_array_2018))
	

main()