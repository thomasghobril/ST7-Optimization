### Ressources
class RessourceUnavailability:
  def __init__(self, latitude,longitude,unavailabilityStart,unavailabilityEnd):
    self.latitude=latitude
    self.longitude=longitude
    self.unavailabilityStart=unavailabilityStart
    self.unavailabilityEnd=unavailabilityEnd

class Ressource:
  def __init__(self, latitude,longitude,skill,level,workingStart,workingEnd):
    self.latitude=latitude
    self.longitude=longitude
    self.skill=skill
    self.level=level
    self.workingStart=workingStart
    self.workingEnd=workingEnd

  unavailibilities=[]

  def addUnavailability(self, unavailability):
    self.unavailibilities.append(unavailability)


### Tâches
class TaskUnavailability:
  def __init__(self, unavailabilityStart,unavailabilityEnd):
    self.unavailabilityStart=unavailabilityStart
    self.unavailabilityEnd=unavailabilityEnd

class Task:
  def __init__(self, latitude,longitude,duration,skill,level,openingTime,closingTime):
    self.latitude=latitude
    self.longitude=longitude
    self.duration=duration
    self.skill=skill
    self.level=level
    self.openingTime=openingTime
    self.closingTime=closingTime

  unavailibilities=[]

  def addUnavailability(self, unavailability):
    self.unavailibilities.append(unavailability)

