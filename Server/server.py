from socket import *
import time

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 8889))
s.listen(5)


while 1:
    print '.',
    client,addr = s.accept()
    print "Polaczenie z", addr
    client.send(time.ctime(time.time()))
    client.send(time.ctime(time.time()))
    client.close()
    
    #time.sleep(3)




