import sys
import os
from subprocess import check_output

#result = os.system('tracert -d' + ' '+ sys.argv[1])

result = check_output('tracert -4 -d ' + sys.argv[1], shell=True).decode('cp866')

print(result)