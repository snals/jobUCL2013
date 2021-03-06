#Non-generic file, specially written for this lab

import sys
from switch import Switch
from create_lab import Create_lab

class Create_stp_lab(Create_lab):


  def __init__(self, pathToGraph, pathToDir):
    Create_lab.__init__(self, pathToGraph)
    for node in self.graph.nodes():
      s = Switch(node)
      self.netkit_components += [s]
    self.set_interface_and_zone()
    self.set_data_from_edges()
    for switch in self.netkit_components:
      switch.create_dir(pathToDir)
      switch.fill_startup_file(pathToDir)


    self.create_conf(pathToDir)


def usage():
  print "python create_stp_lab -f [pathToDotFile] [pathToNetkitDirectory]"


def main(argv):
  if len(argv) == 0:
    usage()
  else:
    if argv[0] == "-f":
      lab = Create_stp_lab(argv[1], argv[2])
    elif argv[0] == "-h":
      usage()
    else:
      usage()


if __name__ == "__main__":
  main(sys.argv[1:])
