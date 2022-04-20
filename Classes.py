class Info:
  def __init__(self):
    ...

class Coord:
  def __init__(self):
    x:float
    y:float
  def getCord(x,y):
    ...
      #Will convert the coordinates obtained from the folium map, pinpoint,
      #or the input of the user to a format that can be used for comparing


class Category(Info):
  #This class will inherit from the Info class, so that it searches through
  #the database and get the category of the building needed, and then display
  #it and also compare it if needed
  def __init__(self):
    type_bldn: str
  def displayCat(type_bldn):
    #Will display the category
    print(type_bldn)
    ...
  def compareCat(type_bldn, temp):
    #If called, will compare the categories for an inquiry
    # (Probably won´t be needed)
    ...

class Building(Info):
  #This class will inherit from the Info class, so that it searches through
  #the database and get the name of the building needed, and then display
  #it and also compare it if needed
  def __init__(self):
    bldn_name: str
    bldn_cat: Category
    bldn_coord: Coord
  def displayBldn(type_bldn):
    #Will display the category
    print(type_bldn)
    ...
  def compareBldn(type_bldn, temp):
    #If called, will compare the categories for an inquiry
    # (Probably won´t be needed)
    ...



class Input(Info):
  #This class will ask for the input of the user, it will have many uses
  #and will be used in different classes and functional code,
  #for example, could ask for the location of the user
  #and also ask for what the user is looking for
  #This class also inherits from info so that it can look for the data
  #in the database and compare
  def __init__(self):
      user_input:str
      bldn_temp: Building
      curr_userLoc: str
      act_info: Info
  def getInput():
    #This method will ask for the user to input it´s location
    #It could receive "Fuente", also, could ask for a search inquiry,
    #i.g "Busca salones"
    return user_input
  def search(user_input):
    #This method will compare the user´s input in the database
    #and get the location in coordinates, and return it for using
    return curr_userLoc
  def _showInfo_(user_input, bldn_temp, curr_userLoc):
    #This method will be used for the developing phase
    #Will help to display the results obtained by the methods
    pass
  

class Nearest(Input):
  #If the inquiry is location related, this class will look for the nearest
  #location of the search inquiry, for example, "look for bathrooms"
  def __init__(self):
    current_input: Input
    user_coords: Input
  def displayNearest(current_input, user_coords):
    #This method will return the nearest location of the inquiry
    return nearest


class UID:
    # Class that contain the name of the 
    # university network
     def getUID(red_nombre):
        return red_nombre
      

class File:
    # Class that contain all the database
    # of the university places

    def _init_(self):
      filelocate: str
        
    def getFile(filelocate):
      # Look for the file of the database
      return filelocate


class Photo(File):
    # Class that contain all the photos 
    # of each place in the university

    def _init_(self):
      foto: File

    def display_photo(foto):
      # Method that display a photo 
      return foto


class Authenticator(UID):
    # Class that compare and verify that the user
    # is in the university network

    # Atributes of this class
    def _init_(self):
      current_UID: UID
      usernet: str

    def validate(current_UID):
      # method that compare if the user is in 
      # university network 
      if (usernet == current_UID):
        return True
      
class Legend(Info):
  # Class that display on the screnn the icons and legends
  # that are on the map
  def __init__(self):
    name: Info
    b_ind: Info
      
  def displayLegend(name, b_ind):
    # Method that display on screen the legends "name" and "b_ind"
    print(name)
    print(b_ind)

class Bubble(Info, Photo, File):
  # Class that shows bubbles of information of each building
  def __init__(self):
    info: Info
    bubb_loc: Coord
    foto_e: Photo
  def displayBubble(info, bubble_loc, foto_e):
    # Method that display a bubble with the info, location 
    # and photo of a place
    pass

class Map(Input, Legend, Bubble):
  # Class that contain and display the map, legend and bubbles all
  # together
  def __init__(self):
    bubbles: Bubble
    legend: Legend
    user_track: Input
  def displayMap(bubbles, legend, user_track):
    # Method that display the map, legend and buubles all together
    pass
  


  
    
