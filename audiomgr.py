from time import sleep                                                                                                      
import broadlink                                                                                                            
                                                                                                                            
v1 = b"&\x00X\x00\x00\x01(\x93\x13\x12\x136\x14\x11\x14\x11\x137\x13\x12\x136\x146\x137\x13\x12\x136\x146\x13\x12\x136\x146\
x14\x11\x146\x136\x146\x146\x13\x12\x13\x12\x13\x11\x14\x11\x14\x11\x14\x11\x13\x12\x13\x12\x136\x146\x137\x136\x14\x00\x04\
xf8\x00\x01(J\x13\x00\x0cO\x00\x01'J\x14\x00\r\x05"                                                                         
power = b'&\x00X\x00\x00\x01(\x93\x13\x12\x136\x14\x11\x14\x11\x146\x13\x12\x136\x146\x14\x11\x13\x12\x137\x136\x14\x11\x146
\x136\x14\x11\x146\x146\x13\x12\x136\x14\x11\x14\x11\x146\x136\x14\x11\x14\x11\x146\x13\x12\x136\x146\x14\x11\x13\x12\x13\x0
0\x05\x1d\x00\x01(J\x13\x00\x0cO\x00\x01(J\x13\x00\r\x05'                                                                   
cd = b"&\x00X\x00\x00\x01'\x93\x14\x11\x146\x13\x12\x13\x11\x146\x14\x11\x137\x136\x146\x14\x11\x146\x136\x14\x11\x146\x146\
x13\x11\x146\x14\x11\x14\x11\x137\x13\x11\x14\x11\x14\x11\x14\x11\x14\x11\x136\x146\x14\x11\x146\x136\x146\x146\x14\x00\x04\
xf8\x00\x01'J\x14\x00\x0cO\x00\x01'J\x13\x00\r\x05"                                                                         
v2 = b"&\x00X\x00\x00\x01(\x93\x13\x12\x136\x14\x11\x14\x11\x137\x13\x11\x146\x146\x137\x13\x11\x146\x146\x13\x12\x136\x146\
x14\x11\x14\x11\x136\x146\x146\x14\x11\x13\x12\x13\x12\x13\x11\x146\x14\x11\x13\x12\x13\x12\x136\x146\x146\x136\x14\x00\x04\
xf8\x00\x01(J\x13\x00\x0cO\x00\x01'J\x14\x00\r\x05"                                                                         
v3 = b"&\x00X\x00\x00\x01'\x93\x14\x11\x146\x14\x11\x13\x12\x136\x14\x11\x146\x146\x136\x14\x11\x146\x146\x13\x12\x136\x146\
x14\x11\x137\x13\x11\x146\x146\x13\x12\x13\x12\x13\x11\x14\x11\x14\x11\x146\x13\x12\x13\x11\x146\x146\x137\x136\x14\x00\x04\
xf8\x00\x01'J\x14\x00\x0cO\x00\x01'J\x14\x00\r\x05"                                                                         
                                                                                                                            
volume_up = b"&\x00\x90\x00\x00\x01'\x93\x14\x11\x146\x13\x12\x13\x12\x136\x14\x11\x146\x136\x146\x14\x11\x146\x137\x13\x11\
x146\x146\x13\x12\x13\x12\x136\x14\x11\x14\x11\x13\x12\x13\x12\x13\x11\x14\x11\x146\x13\x12\x136\x146\x146\x137\x136\x146\x1
4\x00\x04\xf8\x00\x01'\x93\x14\x11\x145\x14\x12\x13\x12\x136\x14\x11\x146\x136\x146\x14\x11\x146\x137\x13\x11\x146\x146\x13\
x12\x13\x11\x146\x14\x11\x14\x11\x13\x12\x13\x12\x13\x11\x14\x11\x146\x14\x11\x136\x146\x146\x146\x136\x146\x14\x00\r\x05\x0
0\x00\x00\x00\x00\x00\x00\x00"                                                                                              
volume_down = b"&\x00\xd8\x00\x00\x01'\x93\x14\x11\x137\x13\x11\x14\x11\x146\x14\x11\x136\x146\x146\x14\x11\x136\x146\x14\x1
1\x146\x136\x14\x11\x146\x146\x13\x12\x13\x12\x13\x11\x14\x11\x14\x11\x14\x11\x13\x12\x13\x11\x146\x146\x137\x136\x146\x146\
x13\x00\x04\xf9\x00\x01'\x93\x14\x11\x137\x13\x11\x14\x11\x146\x14\x11\x136\x146\x146\x14\x11\x136\x146\x14\x11\x146\x137\x1
3\x11\x146\x146\x13\x12\x13\x12\x13\x11\x14\x11\x14\x11\x14\x11\x13\x12\x13\x12\x136\x146\x146\x136\x146\x146\x13\x00\x04\xf
8\x00\x01(\x93\x13\x12\x136\x14\x11\x14\x11\x146\x13\x12\x136\x146\x146\x13\x12\x136\x146\x14\x11\x146\x136\x14\x11\x146\x14
7\x12\x12\x13\x11\x14\x11\x14\x11\x14\x11\x13\x12\x13\x12\x13\x11\x146\x146\x136\x146\x146\x146\x13\x00\r\x05"              
                                                                                                                            
# initially setup.                                                                                                          
# put the devie into ap mode                                                                                                
# Long press the reset button until the blue LED is blinking quickly.                                                       
# Long press again until blue LED is blinking slowly.                                                                       
# and then connect WIFI BROADLINK AP before setup()                                                                         
def setup():                                                                                                                
    broadlink.setup('AP', 'PASSWD',3)                                                                                       
                                                                                                                            
def check_audio():                                                                                                          
    file = open('/proc/asound/card2/stream0', 'r')                                                                          
    res = file.readlines()                                                                                                  
    ret = False                                                                                                             
    for line in res :                                                                                                       
        if line.find('Status: Running') >= 0:                                                                               
            ret = True                                                                                                      
            break                                                                                                           
    file.close()                                                                                                            
    return ret                                                                                                              
                                                                                                                            
device = broadlink.hello('192.168.219.115')                                                                                 
device.auth()                                                                                                               
                                                                                                                            
#device.send_data(v1)                                                                                                       
#sleep(1)                                                                                                                   
#device.send_data(power)                                                                                                    
                                                                                                                            
state = False                                                                                                               
cnt = 0                                                                                                                     
                                                                                                                            
while 1 :                                                                                                                   
    new_state = check_audio()                                                                                               
    if state != new_state :                                                                                                 
        cnt -= 1                                                                                                            
    else :                                                                                                                  
        if state :                                                                                                          
            cnt = 30                                                                                                        
        else :                                                                                                              
            cnt = 0                                                                                                         
    if cnt < 0 :                                                                                                            
        if new_state :                                                                                                      
            cnt = 30                                                                                                        
        else :                                                                                                              
            cnt = 0                                                                                                         
        state = not state                                                                                                   

    print('state = ' + str(state) + ' cnt = ' + str(cnt))                                                                   
    sleep(1)                                                                                                                
