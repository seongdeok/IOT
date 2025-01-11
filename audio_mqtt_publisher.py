from time import sleep                                                                                                                     
import paho.mqtt.client as mqtt                                                                                                            
import logging                                                                                                                             
import logging.handlers                                                                                                                    
                                                                                                                                           
# initially setup.                                                                                                                         
# put the devie into ap mode                                                                                                               
# Long press the reset button until the blue LED is blinking quickly.                                                                      
# Long press again until blue LED is blinking slowly.                                                                                      
# and then connect WIFI BROADLINK AP before setup()                                                                                        
                                                                                                                                           
def get_logger() :                                                                                                                         
    log = logging.getLogger(__name__)                                                                                                      
    log.setLevel(logging.DEBUG)                                                                                                            
    handler = logging.handlers.SysLogHandler(address = '/dev/log')                                                                         
    formatter = logging.Formatter('%(module)s.%(funcName)s: %(message)s')                                                                  
    handler.setFormatter(formatter)                                                                                                        
    log.addHandler(handler)                                                                                                                
    return log                                                                                                                             
                                                                                                                                           
def check_audio():
    try:
        with open('/proc/asound/card2/stream0', 'r') as file:
            res = file.readlines()
    except Exception as e:
        # 파일 열기 또는 읽기 과정에서 오류 발생 시 False 반환
        print(f"Error reading audio status: {e}")
        return False

    ret = False
    for line in res:
        if 'Status: Running' in line:
            ret = True
            break

    return ret
  
def publish(on) :                                                                                                                          
    broker_address = '192.168.219.200'                                                                                                     
    mqttc = mqtt.Client('moode')                                                                                                           
    mqttc.connect(broker_address)                                                                                                          
    topic = 'music/moode'                                                                                                                  
    if on :                                                                                                                                
        state = 'playing'                                                                                                                  
    else :                                                                                                                                 
        state = 'stop'                                                                                                                     
    mqttc.publish( topic, state)                                                                                                           
    mqttc.disconnect()                                                                                                                     
                                                                                                           
offcnt = 10                                                                                                                                
logger = get_logger()                                                                                                                      
                                                                                                                                           
state = False                                                                                                                              
cnt = 0                                                                                                                                    
                                                                                                                                           
while 1 :                                                                                                                                  
    new_state = check_audio()                                                                                                              
    if state != new_state :                                                                                                                
        cnt -= 1                                                                                                                           
    else :                                                                                                                                 
        if state :                                                                                                                         
            cnt = offcnt                                                                                                                   
        else :                                                                                                                             
            cnt = 0                                                                                                                        
    if cnt < 0 :                                                                                                                           
        logger.info('Before = ' + str(state) + ' After state = ' + str(new_state))                                                         
        if new_state :                                                                                                                     
            cnt = offcnt                                                                                                                   
            state = True                                                                                                                   
            #mqttc.publish( topic, 'playing')                                                                                              
            publish(True)                                                                                                                  
        else :                                                                                                                             
            cnt = 0                                                                                                                        
            state = False                                                                                                                  
            #mqttc.publish( topic, 'stop')                                                                                                 
            publish(False)                                                                                                                 
    sleep(1)                                                                                                                               
    logger.debug('state = ' + str(state) + ' cnt = ' + str(cnt))                                                                           
                                                                         
