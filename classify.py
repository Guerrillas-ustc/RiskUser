# -*- coding: utf-8 -*-
"""
Created on Mon May 21 21:37:08 2018

@author: Sdli
"""

import numpy as np
import torch
from collections import Counter
'''
Set 结构如下：
    set:
        uid_Key:
            label: (int) 0/1
            voice: (list) [ 
                            sample:
                                opp_num (str) AE209057CE98A9833E56C2A8362900F9
                                opp_head (str) 130
                                ....
                            ]
            sms : (list) [
                            sample:
                                opp_num (str) AE209057CE98A9833E56C2A8362900F9
                                opp_head (str) 130
                                call_type (str) 
                                ....
                            ]
            web : (list) [
                            sample:
                                wa_name (str) 155导航
                                visit_cnt (int) 21
                                visit_dura (int) 12
                                up_flow (int) 13
                            ]
'''





def feature_extract(path = 'train_set.npy'):
    
    sets = np.load('train_set.npy')[()]
    
#sets = np.load('train_set.npy')[()]
ukey = list(sets.keys())
p_sample = [sets[key] for key in ukey if sets[key]['label'] == '1']

p_sms_list = []
for i in p_sample:
    p_sms_list += i['sms']
p_sms_opp = [sms['opp_num'] for sms in p_sms_list]
p_sms_opphead = [sms['opp_head'] for sms in p_sms_list]

statis_opp = Counter(p_sms_opp)







