from Parameters import *
import json
from Problem_Definition import *
import os
import copy

params = Parameters()


for folder_name, parameters in params.folder_names_and_parameters.items():
    path = './Data/' + folder_name 
    try:
        os.mkdir(path)
    except:
        print(path +' already exists')
    for count in range(params.number_of_problems):
        sub_folder_name = 'Problem'+ str(count+1)
        inner_path = path + '/' + sub_folder_name
        try:
            os.mkdir(inner_path)
        except:
            print(inner_path +' already exists')
        #print(sub_folder_name)
        #print(path)
        prob = Problem_Definition(copy.deepcopy(parameters))
        prob.generate_client_jobs()
        temp_data = prob.get_jobs(params.period)

        #print('JOBS')
        with open(inner_path + '/Day_Job_Client.txt', 'w') as outfile:
            json.dump(temp_data, outfile)


        #print('CLIENT, FE and LIFECYCLES')
        with open(inner_path + '/Client_FE_Lifecyle.txt', 'w') as outfile:
            json.dump(prob.client_fe_lifecyle, outfile)



        #print('FE and CAPACITY')
        with open(inner_path + '/FE_Capacity.txt', 'w') as outfile:
            json.dump(prob.fe_capacity, outfile)

            


        #print('FE and AVAILABILITIES')
        with open(inner_path + '/FE_Schedule.txt', 'w') as outfile:
            json.dump(prob.schedule, outfile)

