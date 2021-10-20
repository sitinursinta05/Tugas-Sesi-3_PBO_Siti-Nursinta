class RADIO:
  brand=None
  wave=None
  source=None
  activeChannel=None
  channels = []
  on=False

  def __init__(self, brand, source):
      self.brand = brand
      self.source = source

  def __getActiveIndex(self):
      currentActive = -1
      try :
           currentActive = self.channels.index(self.activeChannel)
      except :
           currentActive = -1
      return currentActive

  def turnOn(self):
      self.on  = True
      self.channels = []
      self.activeChannel = None

  def turnOff(self):
      self.on = False
      self.channels = []   
      self.activeChannel = None 

  def scanChannel(self):
      newChannels = []  
      for i in range(99, 105):
          newChannels.append(i)
      self.channels = newChannels

  def setChannel(self, newChannel):
      self.activeChannel = newChannel

  def setChannelUp(self):
      if self.__getActiveIndex() == len(self.channels) - 1:
         self.activeChannel = 0
      else:
         self.activeChannel = self.__getActiveIndex() + 1
         
  def setChannelDown(self):
      if self.__getActiveIndex() == 0:
         self.activeChannel = len(self.channels) - 1
      else:
         self.activeChannel = self.__getActiveIndex() - 1

  def printData(self):
      print("------------------------------")   
      print(f'Brand : {self.brand}')    
      print(f'Wave : {self.wave}')       
      print(f'On : {"Nyala" if self.on else "Mati"}')
      print(f'Source : {self.source}')  
      print(f'Channels : {self.channels}') 
      print(f'Active Channel : {self.activeChannel}')   
      print("--------------------------------\n")

#BedRoom
class AMRadio(RADIO):
    def __init__(self, brand, source):
        super(AMRadio, self).__init__(brand, source)    
        self.wave = 'AM'

    def scanChannel(self):
        newChannels = []    
        for i in range(99, 250):
            newChannels.append(i)
        self.channels = newChannels


class FMRadio(RADIO):
    def __init__(self, brand, source):
        super (FMRadio, self).__init__(brand,source)         
        self.wave = 'FM'

    def scanChannel(self):
        newChannels = []    
        for i in range(95, 125):
            newChannels.append(i)
        self.channels = newChannels



bedroomRadio = AMRadio('Polytron', 'AC') 
bedroomRadio.turnOn()
bedroomRadio.scanChannel()    
bedroomRadio.setChannel(bedroomRadio.channels[5])   
bedroomRadio.setChannelUp()
bedroomRadio.printData()

bedroomRadio.turnOff()
bedroomRadio.printData()

#LivingRoom

livingroomRadio = FMRadio('LG', 'DC')
livingroomRadio.turnOn()
livingroomRadio.scanChannel()
livingroomRadio.setChannel(livingroomRadio.channels[5])
livingroomRadio.setChannelDown()
livingroomRadio.printData()

livingroomRadio.turnOff()
livingroomRadio.printData()
