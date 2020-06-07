import sys
import os

print(os.system('tracert' + ' '+ sys.argv[1]))
