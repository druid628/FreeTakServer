#######################################################
# 
# point.py
# Python implementation of the CoT point
# Generated by Enterprise Architect
# Created on:      11-Feb-2020 11:08:07 AM
# Original author: Corvo
# 
#######################################################
# Latitude referred to the WGS 84 ellipsoid in degrees
lat = "00.00000000" 
lon = "00.00000000" 
    # Linear 1-sigma error or an altitude range about the point in meters
le = "9999999.0" 
    # Longitude referred to the WGS 84 in degrees
lon = "0.000000" 
  
# Circular 1-sigma or decimal a circular area about the point in meters
ce = "9999999.0"

hae = "00.00000000"

class COTPoint:


  xmlPoint ='<point lat="43.967087" lon="-66.126393" hae="29.30101602610336" ce="367.1" le="9999999.0" />"'


  """
  I removed hae from getXMLPoint
  """

  def __init__(self):
    True

    # ce getter 
  def getce(self): 
    return self.ce 

    # ce setter 
  def setce(self, ce1):
    global ce
    ce=ce1 

    # le getter 
  def getle(self): 
    return le 

    # le setter 
  def setle(self,le1):  
    global le
    le=le1


    # lat getter 
  def getlat(self):
    return lat 

    # lat setter 
  def setlat(self, lat1):  
    global lat
    lat=lat1

      # lon getter 
  def getlon(self):
    return lon 

    # lon setter 
  def setlon(self,lon1):
    global lon
    lon=lon1
  
  def gethae(self):
    return hae

  def sethae(self,hae1):
    global hae
    hae = hae1

  def getXMLPoint(self):
    apoint = '<point lat="'+self.lat+'" lon="'+self.lon+'" ce="'+self.ce+'" le="'+self.le+'" hae="'+self.hae+'"/>'
    return self.apoint