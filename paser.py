# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 19:54:42 2018

@author: ShidongLi
"""

import numpy as np
import os
import sys


sms_value = ['uid','opp_num','opp_head','opp_len','start_time','in_out'] 
voice_value  = ['uid','opp_num','opp_head','opp_len','start_time','end_time','call_type','in_out']
web_value = ['uid','wa_name','visit_cnt','visit_dura','up_flow','down_flow','wa_type','date']        
log_type = ['voice','sms','web']
def load_log(path):
    
    uidpath = os.path.join(path,'uid_train.txt')
    with open(uidpath, 'r') as file:
    
        uid_set = dict( line.strip().split() for line in file)
    
    
    sms =dict((key,[]) for key in uid_set.keys())
    
    sms_path = os.path.join(path,'sms_train.txt')
    with open(sms_path, 'r') as file:
        
        for line in file:
            
            log_dict = dict(zip(sms_value,line.strip().split()))
            uid = log_dict['uid']
            del log_dict['uid']
            sms[uid].append(log_dict)
    
    voice = dict((key,[]) for key in uid_set.keys())
    voice_path = os.path.join(path,'voice_train.txt')
    with open(voice_path, 'r') as file:
        
        for line in file:
            log_dict = dict(zip(voice_value,line.strip().split()))
            uid = log_dict['uid']
            del log_dict['uid']
            voice[uid].append(log_dict)        
    
    web = dict((key,[]) for key in uid_set.keys())

    wa_path = os.path.join(path,'wa_train.txt')
    with open(wa_path, 'r', encoding = 'utf-8') as file:        
        for line in file:
            log_dict = dict(zip(web_value,line.strip().split()))
            uid = log_dict['uid']
            del log_dict['uid']
            web[uid].append(log_dict)        
    raw_set = {}
    for key in uid_set.keys():
        
        tmp = {'label':uid_set[key],'voice':voice[key],'sms' :sms[key],'web':web[key] }
        raw_set[key] = tmp
        
    np.save('train_set',raw_set)



    
def main():
    
    default_path = 'C:/Users/Sdli/Jdata'
    
    if len(sys.argv) > 1 :
        path = sys.argv[1]
    else:
        path  = default_path
    load_log(path)
    
    return
    
if __name__ == '__main__':
    main()
    
    
    















if __name__ == '__main__':
    #load_log()
    main()



