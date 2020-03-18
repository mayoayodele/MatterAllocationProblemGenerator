class Parameters:

    def __init__(self):
        self.period = 28
        self.number_of_problems = 20
        all_parameters = {'Client': {'Actual': 30, #31
                            'Small': 10,
                            'Medium': 20,
                            'Large': 30},
                'FE': {'Actual': 100, #96
                            'Small': 40,
                            'Medium': 70,
                            'Large': 100},
                'FE_Per_Client': {'Actual': [1,27], #[1,26],
                            'Small': [1,9],
                            'Medium': [10,18],
                            'Large': [19,27]},
                'Capacity_Per_FE': {'Actual': [1,45], #[1,47],
                            'Small': [1,15],
                            'Medium': [16,30],
                            'Large': [31,45]},
                'Lifecycle': {'Actual': [11, 250],#[10,300],
                            'Small': [11,100],
                            'Medium': [101,190],
                            'Large': [191,280]},
                'Jobs_Per_Client': {'Actual': [1,96], #[1,95],
                            'Small': [1,32],
                            'Medium': [33,64],
                            'Large': [65,96]},
                'Utilisation': {'Actual': [0,1],
                            'Small': [0,0.33],
                            'Medium': [0.34,0.66],
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
        folder_names_and_parameters[folder_name] = medium_params
                

        self.folder_names_and_parameters = folder_names_and_parameters

