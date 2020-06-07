from sys import argv
import os
from re import findall
from subprocess import check_output
from json import loads
from urllib import request

#result = os.system('tracert -d' + ' '+ sys.argv[1])

IP = argv[1]
output = []

result = check_output('tracert -4 -d ' + IP, shell=True).decode('cp866')
#print(result)

list_of_ip_adresses = findall('\d+.\d+.\d+.\d+', result)
list_of_ip_adresses.pop(0)

#print(list_of_ip_adresses)


def get_information_about_ip(IP):
    return loads(request.urlopen('https://ipinfo.io/' + IP + '/json').read())


for ip in list_of_ip_adresses:
    info = get_information_about_ip(ip)
    if 'bogon' in info:
        output.append(info['ip'])
    else:
        output.append(str(info['ip']) + '\t' + info['country'] + '\t' + info['org'] + '\t\t' + info['city'])


for i in range(1, len(output)):
    print(i, '\t', output[i])
