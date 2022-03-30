### Ressources
class RessourceUnavailability:
  def __init__(self, latitude,longitude,unavailabilityStart,unavailabilityEnd):
    self.latitude=float(latitude)
    self.longitude=float(longitude)
    self.unavailabilityStart=unavailabilityStart
    self.unavailabilityEnd=unavailabilityEnd

class Ressource:
  def __init__(self, latitude,longitude,skill,level,workingStart,workingEnd):
    self.latitude=float(latitude)
    self.longitude=float(longitude)
    self.skill=skill
    self.level=level
    self.workingStart=workingStart
    self.workingEnd=workingEnd
    self.unavailabilities=[]
    self.tasks=[]
    self.hours=[]

  def addUnavailability(self, unavailability):
    self.unavailabilities.append(unavailability)


### Tâches
class TaskUnavailability:
  def __init__(self, unavailabilityStart,unavailabilityEnd):
    self.unavailabilityStart=unavailabilityStart
    self.unavailabilityEnd=unavailabilityEnd

class Task:
  def __init__(self, latitude,longitude,duration,skill,level,openingTime,closingTime):
    self.latitude=float(latitude)
    self.longitude=float(longitude)
    self.duration=int(duration)
    self.skill=skill
    self.level=level
    self.openingTime=openingTime
    self.closingTime=closingTime
    self.unavailabilities=[]

  def addUnavailability(self, unavailability):
    self.unavailabilities.append(unavailability)

