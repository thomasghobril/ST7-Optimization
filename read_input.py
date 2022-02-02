# Import openyxl module
import openpyxl

def read_employee():

    # Define variable to load the wookbook
    wookbook = openpyxl.load_workbook("InstancesV1/InstanceBordeauxV1.xlsx")

    # Define variable to read the active sheet:
    worksheet = wookbook.active

    # Iterate the loop to read the cell values


    for row in worksheet.iter_rows(2, max_row=15):
        if row[0].value == None:
            break
        EmployeeName = row[0].value
        latitude = row[1].value
        longitude = row[2].value
        skill = row[3].value
        level = row[4].value
        workingStartTime = row[4].value
        workingEndTime = row[6].value

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
