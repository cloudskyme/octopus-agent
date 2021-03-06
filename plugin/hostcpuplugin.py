# -*- coding: UTF-8 -*-
#*************************************
#author:zhengqs
#create:201707
#desc: 
#**********************************

from hostutil import Host
from datetime import datetime

class HostCpuPlugin(object):
    def __init__(self, octopusd, paramter) :
        self.paramter = paramter
        self.octopusd = octopusd
        if paramter and paramter.get('hostname') :
            self.hostname = paramter.get('hostname')
        else :
            self.hostname = Host.getHostname()
    
    def get_now_utc_time(self):
        utc = datetime.utcnow()
        return datetime.strftime(utc, "%Y-%m-%dT%H:%M:%S.%fZ")
        
    def run(self):
        try:
            utc_time = self.get_now_utc_time()
            usage_rate = Host.get_cpu_rate()
            event = {"time":utc_time, "host":self.hostname, "type":"cpu","type_instance":"usage_rate","value":usage_rate}
            self.octopusd.sendMessage(self.paramter['output'], event)
            
            loadavg = Host.get_load_stat()
            event = {"time":utc_time, "host":self.hostname, "type":"cpu","type_instance":"lavg_1","value":loadavg['lavg_1']}
            self.octopusd.sendMessage(self.paramter['output'], event)
            
        except Exception,ex:
            print ex