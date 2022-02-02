import openpyxl
from classes import Ressource,RessourceUnavailibility,Task,TaskUnavailibility


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

def read_unavalabilities():

    # Define variable to load the wookbook
    wookbook = openpyxl.load_workbook("InstancesV1/InstanceBordeauxV1.xlsx")

    # Define variable to read the active sheet:
    worksheet = wookbook['Employees Unavailabilities']

    # Iterate the loop to read the cell values
    for row in worksheet.iter_rows(2, max_row=15):
        if row[0].value == None:
            break
        EmployeeName = row[0].value
        latitude = row[1].value
        longitude = row[2].value
        start = row[3].value
        end = row[4].value

    print('ok')
read_unavalabilities()
