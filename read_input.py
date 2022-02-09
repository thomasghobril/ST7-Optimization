# Import openyxl module
import openpyxl
from classes import Ressource,RessourceUnavailability,Task,TaskUnavailability


def read_ressources(v):
    ressources={}
    # Define variable to load the wookbook
    wookbook = openpyxl.load_workbook("InstancesV"+str(v)+"/InstanceBordeauxV"+str(v)+".xlsx")

    # Define variable to read the active sheet:
    worksheet = wookbook.active

    # Iterate the loop to read the cell values
    for row in worksheet.iter_rows(2, max_row=15):
        if row[0].value == None:
            break
        ressources[row[0].value] = Ressource(row[1].value,row[2].value,row[3].value,row[4].value,row[5].value,row[6].value)
    return ressources

def read_ressources_unavailabilities(v):
    ressources_unavailabilities={}
    # Define variable to load the wookbook
    wookbook = openpyxl.load_workbook("InstancesV"+str(v)+"/InstanceBordeauxV"+str(v)+".xlsx")

    # Define variable to read the active sheet:
    worksheet = wookbook['Employees Unavailabilities']

    # Iterate the loop to read the cell values
    for row in worksheet.iter_rows(2, max_row=15):
        if row[0].value == None:
            break
        ressources_unavailabilities[row[0].value] = RessourceUnavailability(row[1].value,row[2].value,row[3].value,row[4].value)
    return ressources_unavailabilities

def read_tasks(v):
    tasks={}
    # Define variable to load the wookbook
    wookbook = openpyxl.load_workbook("InstancesV"+str(v)+"/InstanceBordeauxV"+str(v)+".xlsx")

    # Define variable to read the active sheet:
    worksheet = wookbook['Tasks']

    # Iterate the loop to read the cell values
    for row in worksheet.iter_rows(2, max_row=15):
        if row[0].value == None:
            break
        tasks[row[0].value] = Task(row[1].value,row[2].value,row[3].value,row[4].value,row[5].value,row[6].value,row[7].value)
        print(row[1].value,row[2].value,row[3].value,row[4].value,row[5].value,row[6].value,row[7].value)
    return tasks

def read_tasks_unavailabilities(v):
    tasks_unavailabilities={}
    # Define variable to load the wookbook
    wookbook = openpyxl.load_workbook("InstancesV"+str(v)+"/InstanceBordeauxV"+str(v)+".xlsx")

    # Define variable to read the active sheet:
    worksheet = wookbook['Tasks Unavailabilities']

    # Iterate the loop to read the cell values
    for row in worksheet.iter_rows(2, max_row=15):
        if row[0].value == None:
            break
        tasks_unavailabilities[row[0].value] = TaskUnavailability(row[1].value,row[2].value)
    return tasks_unavailabilities

