class Parameters:

    def __init__(self):
        self.period = 28
        self.number_of_problems = 20
        all_parameters = {'Client': {'Actual': 31,
                            'Small': 10,
                            'Medium': 20,
                            'Large': 30},
                'FE': {'Actual': 96,
                            'Small': 40,
                            'Medium': 70,
                            'Large': 100},
                'FE_Per_Client': {'Actual': [1,26],
                            'Small': [1,10],
                            'Medium': [11,20],
                            'Large': [21,30]},
                'Capacity_Per_Client': {'Actual': [1,47],
                            'Small': [1,15],
                            'Medium': [16,30],
                            'Large': [31,45]},
                'Lifecycle': {'Actual': [10,300],
                            'Small': [10,90],
                            'Medium': [91,170],
                            'Large': [171,250]},
                'Jobs_Per_Client': {'Actual': [1,95],
                            'Small': [1,32],
                            'Medium': [33,64],
                            'Large': [65,96]},
                'Utilisation': {'Actual': [0,1],
                            'Small': [0,0.33],
                            'Medium': [0.34,0.67],
                            'Large': [0.67,1]}
            }



        folder_name = 'MediumAll'
        medium_params = {parameter: all_parameters[parameter]['Medium'] for parameter in list(all_parameters.keys())}
        folder_names_and_parameters = {folder_name: medium_params}


        for p in all_parameters.keys():
            for size in ['Small', 'Large']:
                medium_params = {parameter: all_parameters[parameter]['Medium'] for parameter in list(all_parameters.keys())}
                medium_params[p] = all_parameters[p][size]
                folder_name = size + p
                folder_names_and_parameters[folder_name] = medium_params

        folder_name = 'Actual'
        medium_params = {parameter: all_parameters[parameter]['Actual'] for parameter in list(all_parameters.keys())}
        folder_names_and_parameters = {folder_name: medium_params}
                

        self.folder_names_and_parameters = folder_names_and_parameters

