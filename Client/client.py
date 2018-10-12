from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8889))

tm = s.recv(40)
print 'Czas serwera:', tm

tm = s.recv(40)
print 'Czas serwera:', tm

s.close()