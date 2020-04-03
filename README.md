# MatterAllocationProblemGenerator

A python based matter allocation problem with the following parameters

Client: The number of clients considered in the problem

FE: This is the total number of fee-earners that are able to work on the considered type of matters irrespective of who the client is

FE_Per_Client: The minimum and maximum number of fee-earners that are expected to have a relationship with any give client

Capacity_Per_FE: This is the minimum and maximum number of matters a fee-earner can work on simultaneously.

Lifecycle: This is the minimum and maximum expected lifecycle of any given matter

Jobs_Per_Client: This is the minimum and maximum number of matters expected to be received from a client per day

Utilisation: This is the minimum and maximum number of matters a fee-earner is working on before new jobs are assigned


Each problem contains 4 files:
1. Client_FE_Lifecyle.txt: contains the lifecycle of each fee-earner per client

2. Day_Job_Client.txt: contains the earliest start day, matter id and client id (we use a 28-day period in this study)

3. FE_Capacity.txt: contains the capacity of each fee-eaner

4. FE_Schedule.txt: contains previously allocated matters and the finish times

  
