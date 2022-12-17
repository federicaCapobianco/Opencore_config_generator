#import the required libraries
import os
#get the system  architecture i.e: Haswell, Skylake, Coffeelake
def get_architecture():
    # get the system architecture
    arch = os.popen("lscpu | grep 'Architecture' | awk '{print $2}'").read()
    # remove the new line character

get_architecture()