import socket
import sys
from datetime import datetime


if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])

else:
    print('Invalid amout of arguments.')
    sys.exit()

print('-'*50)
print('Scanning target '+target)
print('Time started: '+str(datetime.now()))
print('-'*50)

try:
    for port in range(50,90):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        print('Checking port {}'.format(port))
        if result == 0:
            print('Port {} is open'.format(port))
        
        s.close()

except:
   print('error')
   sys.exit()   



