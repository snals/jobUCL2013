
 
# common methods for netkit components
# 2 spaces indentation.
#
import os
import sys

class NetkitComponent:

  reminder = [] # static variable to share something between component.
                # like a config already used for a particular component

  def __init__(self, name):
    
    self.attr = dict()
    self.attr['map_IF_zone'] = dict() # Map interface to netkit zone and its neighbor
    self.attr['map_IF_neighbor'] = dict()
    self.attr['name'] = name
    self.attr['map_weight'] = dict()
    self.attr['IF'] = []
    self.attr['nbr_IF'] = 0 
    self.attr['ipv6'] = None     # more than 1 times
 
  def __cmp__(self, other):
    return cmp(self.attr['nbr_IF'], other.attr['nbr_IF'])


  def set_interface(self, interface, zone, neighbor): 
    """interface is an int and zone something between A0 and Z99"""
    self.attr['map_IF_zone'][interface] = zone
    self.attr['map_IF_neighbor'][interface] = neighbor
    self.attr['IF'] += [interface]

  def get_next_interface(self):
    if not self.attr['IF']:
      return 0
    else:
      self.attr['IF'].sort(reverse=True)
      L = self.attr['IF']
      if L[0]+1 < self.attr['nbr_IF']:
        return L[0]+1
      else:
	return None
  
  def get_interface_used_between(self, neighbor):
    for key, value in self.attr['map_IF_neighbor'].items():
      if value.attr['name'] == neighbor:
	return key
    return None

  def create_dir(self, path):
    if not os.path.isdir(path+"/+"+self.attr['name']):
      try:
	os.mkdir(path+""+self.attr['name'])
      except OSError:
	if not os.path.isdir(path+""+self.attr['name']) :
	  print "Error happened when mkdir of "+self.attr['name']
  def create_startup(self, path):
    file(path+""+self.attr['name']+".startup", "w")
