import sys
import os
from re import findall
from subprocess import check_output

#result = os.system('tracert -d' + ' '+ sys.argv[1])

result = check_output('tracert -4 -d ' + sys.argv[1], shell=True).decode('cp866')

#print(result)

list_of_ip_adresses = findall('\d+.\d+.\d+.\d+', result)
list_of_ip_adresses.pop(0)

print(list_of_ip_adresses)

