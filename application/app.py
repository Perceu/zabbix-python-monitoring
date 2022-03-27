import os
import logging
from random import randint
from time import sleep
from pyzabbix import ZabbixAPI, ZabbixMetric, ZabbixSender


logger = logging.getLogger('crawler_InfraPrefSP_{host}')
handler = logging.StreamHandler()
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

zapi = ZabbixAPI('http://192.168.0.108:8080/', user='*', password='*')

host = os.environ.get('HOSTNAME')
zapi.do_request(method="host.create",params= {
        "host": f'crawler_InfraPrefSP_{host}',
        "groups": [
            {
                "groupid": "19"
            }
        ],
    }
)

sender = ZabbixSender(zabbix_server='192.168.0.108')
while True:
 
    packet = [
        ZabbixMetric(f'crawler_InfraPrefSP_{host}', 'start_time', 10),
        ZabbixMetric(f'crawler_InfraPrefSP_{host}', 'end_time', randint(1,100)),
    ]
    
    response = sender.send(packet)
    logger.info(response)
    sleep(10)
    