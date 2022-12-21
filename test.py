import csv
import subprocess
# import paramiko

import pandas as pd
import io
import requests

# Reading Data from CSV 
def readCSV():
    with open('TestSheet .csv', mode ='r') as file:
    
        # reading the CSV file
        csvFile = csv.reader(file)
        
        # displaying the contents of the CSV file
        data=[]
        for lines in csvFile:
                user=[]
                for line in lines:
                    user.append(line)
                data.append(user)
    file.close()
    return data

def readCSV2():
    df=pd.read_csv('TestSheet .csv')
    print(df.head())    



# Copying script from remote server 
# def copyScript():

#     ssh = paramiko.SSHClient()
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     ssh.connect(hostname='',username='',password='',port=22)
#     sftp_client = ssh.open_sftp()

#     sftp_client.get('source script file path','createUser.py')

#     sftp_client.close()
#     ssh.close()


def executeScript(username,grpname,key):
    process = subprocess.Popen(['python3','createUser.py',username,grpname,key],shell=False,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    stdout,stderr = process.communicate()
    print(stdout)
    
    
def service():
    data=readCSV()
    
    dict= {}
    for i in range(0,len(data)):
        username = data[i][0]
        grpname = data[i][1]
        key = data[i][2]
        executeScript(username,grpname,key)         

readCSV2()