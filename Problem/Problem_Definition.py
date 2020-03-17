import random as r
from random import randrange

class Problem_Definition:

    def __init__(self, params):
        self.job_client = {}
        self.client_fe_lifecyle = {}
        self.fe_capacity = {}
        self.schedule = {}
        self.params = params
        self.number_of_client = params['Client']
        self.number_of_fe = params['FE']
        self.min_fe_per_client = params['FE_Per_Client'][0]
        self.max_fe_per_client = params['FE_Per_Client'][1]
        self.min_capacity_per_fe = params['Capacity_Per_Client'][0]
        self.max_capacity_per_fe = params['Capacity_Per_Client'][1]
        self.min_lifecycle = params['Lifecycle'][0]
        self.max_lifecycle = params['Lifecycle'][1]
        self.min_jobs_per_client = params['Jobs_Per_Client'][0]
        self.max_jobs_per_client = params['Jobs_Per_Client'][1]
        self.min_utilisation_per_fe = params['Utilisation'][0]
        self.max_utilisation_per_fe = params['Utilisation'][1]


        self.fe_indices = list(range(self.number_of_fe))
        self.generate_client_jobs()


    def generate_client_jobs(self):
        jobs = []
        fes = []
        capacities = []
        for i in range(self.number_of_client):
            jobs.append(r.randint(self.min_jobs_per_client,self.max_jobs_per_client))
            fes.append(r.randint(self.min_fe_per_client,self.max_fe_per_client))
        
        for i in self.fe_indices:
            capacities.append(r.randint(self.min_capacity_per_fe,self.max_capacity_per_fe))

        jobs = sorted(jobs)
        fes = sorted(fes)
        capacities = sorted(capacities)

        for j in self.fe_indices:
            self.fe_capacity[j] = capacities[j] 

        job_index = 0
        job_id_count = 0
        for i in range(self.number_of_client):
            fes_lifecyles = {}
            fe_indices_temp = self.fe_indices.copy()
            #set job id  and corresponding client id
            for j in range(jobs[i]):
                self.job_client[job_index] = i
                job_index = job_index + 1
            #set lifecyles by client id and fe id
            for j in range(fes[i]):
                fe_index= r.choice(fe_indices_temp)
                fe_indices_temp.remove(fe_index)
                temp_lifecycle = r.randint(self.min_lifecycle,self.max_lifecycle)
                fes_lifecyles[fe_index] = temp_lifecycle
            #set capacity and schedule of each fe id
            client_fes_temp = list(fes_lifecyles.keys())
            
            for j in client_fes_temp:
                temp_capacity_min = int(round(self.fe_capacity[j] * self.min_utilisation_per_fe))
                temp_capacity_max = int(round(self.fe_capacity[j] * self.max_utilisation_per_fe))
                temp_utilisation = r.randint(temp_capacity_min, temp_capacity_max)
                temp_lifecycle = fes_lifecyles[j]
                temp_schedule = {}
                if(j not in self.schedule):
                    for k in range(temp_utilisation):
                        rand = r.randrange(1,temp_lifecycle)
                        temp_schedule['p' + str(job_id_count)] = rand
                        job_id_count = job_id_count +1
                    self.schedule[j] = temp_schedule
            self.client_fe_lifecyle[i] = fes_lifecyles

    def get_jobs(self, number_of_subproblems):
        clients = set(self.job_client.values())
        sub_job_client = {}
        for client in clients:
            temp_job_client = {key: value for key, value in self.job_client.items() if value == client }
            problem_size = len(temp_job_client)

            each_problem_size = problem_size//number_of_subproblems
            remainder = problem_size - (each_problem_size * number_of_subproblems)

            problem_sizes = [each_problem_size]*number_of_subproblems

            for i in range(remainder):
                random_position = randrange(number_of_subproblems)
                problem_sizes[random_position] = problem_sizes[random_position] + 1

            index = 0
            for j in range(len(problem_sizes)):
                temp = {key: temp_job_client[key] for key in list(temp_job_client.keys())[index: index + problem_sizes[j]]}
                index = index + problem_sizes[j]
                if(j in sub_job_client.keys()):
                    sub_job_client[j].update(temp)
                else:
                    sub_job_client[j] = temp
        return sub_job_client
                    

    


