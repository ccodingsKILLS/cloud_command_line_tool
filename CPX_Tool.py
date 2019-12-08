import subprocess
import os
import pandas as pd
LIST_OF_SERVICES_BY_IP = list()


#1. return a printout of all running hosts and corresponding health status, running services, CPU and memory usage stats
def running_services():
    df = pd.DataFrame({'IP':[],
                       'Service':[],
                       'Status':[],
                       'CPU':[],
                       'Memory':[]})
    IPs = []
    print("Working on providing your running services now")
    #x = str(os.system("curl localhost:8081/servers")) #Must ensure the server is running on port 8081.
    x = subprocess.run("curl localhost:8081/servers", shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
    y = str(x)
    newString = y.replace('"',' ')
    newString = newString.replace("[","").replace("]","").replace("]","").replace(" ","").replace(","," ")
    l= list(newString.split(" "))
    for ip in l:
        n = subprocess.run("curl localhost:8081/"+ip, shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
        xString = str(n)
        resultStringPerIP = xString.replace("{"," ").replace('"','').replace("}","")
        resultStringPerIP = ip+","+resultStringPerIP
        LIST_OF_SERVICES_BY_IP.append(resultStringPerIP)
    for item in LIST_OF_SERVICES_BY_IP:
        service_married_to_ip = item
        splitService = service_married_to_ip.split(",")
        '''data = [{'IP': splitService[0],
                 'Service': splitService[3],
                 'Status': 'null',
                 'CPU': splitService[1],
                 'Memory': splitService[2]}]'''
        df3 = pd.DataFrame({'IP':[splitService[0]],
                           'Service':[splitService[3]],
                           'Status': ['null'],
                           'CPU':[splitService[1]],
                           'Memory': [splitService[2]]})
        print(df3, "\n")
        df.append(df3)

    print(LIST_OF_SERVICES_BY_IP[0], LIST_OF_SERVICES_BY_IP[3])
    print(df)



        #list_of_service = list(resultStringPerIP)





#2.
def CPU_Usage_of_Service(service):
    print ("Working on "+ service)




#Start of Script: basic selection of which API service to use. The assumption here is that the required keys/secrets (for example, access ekys and secrets in AWS)
#are provided already in the CLI tool configuration - elsewise I would write an initial configuration that takes kesy and secrets as the input and pumps those out
# in order to bash to configure the CLI tool to have the proper permissions to make those requests. I am also assuming that this script will run on keys that have
# admin rights, and I have not included "unauthorized" returns.
print("Please choose the service you would like \n"
      "1. a view of all running services \n2. A view of the average CPU/memory usage of a particular service \n3. Flag services with fewer than 2 healthy services running\n4. track and print CPU/Memory of all instances of a given service over time (until the command is stopped, e.g. ctrl + c)")

selection = input("Make your selection by typing a number: ")
print("you selected " + selection)
if selection == "1":
    running_services()
elif selection == "2":
    print("Choose from the following services: \n1. PermissionsService\n2. AuthService\n3. MLService\n4. StorageService\n5. ")
    selection = input("Please type the number of the service: ")
    if selection == "1":
        service = "PermissionsService"
    elif selection == "2":
        service = "AuthService"
    CPU_Usage_of_Service(service)

