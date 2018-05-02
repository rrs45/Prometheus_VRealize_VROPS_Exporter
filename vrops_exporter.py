#!/bin/env python

from prometheus_client import start_http_server
from prometheus_client.core import GaugeMetricFamily, REGISTRY
import nagini
from systemd import journal
import json
import requests
import sys
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pydblite import Base

class vropsCollector(object):
    def __init__(self):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        self.config = json.loads(open("/opt/prometheus/vrops_exporter/vrops.json").read() )
        journal.send("Connecting to vROPs host: ", FIELD2=self.config["server"]["hostname"])
        self.vcops = nagini.Nagini(host=self.config["server"]["hostname"], user_pass=(self.config["server"]["user"], self.config["server"]["pwd"]))
        #print vcops.get_resources(resourceKind="VirtualMachine", pageSize=1)
        self.db = Base('/tmp/vrops.pd1')
        #logging.basicConfig(format='vrops_exporter - %(levelname)s:%(message)s', stream=sys.stdout, level=logging.DEBUG)

    def collect(self):
        self.db.open()
        journal.send("======Starting Collection=========")
        for r in self.config["metrics"]:
            #get_metrics(r["kind"],config["adapterKind"],r["keys"], iclient, db)
            stat_key = r["keys"].keys()
            #metric = Metric('compute_cluster_health', 'VROPS Compute Cluster Health', 'gauge')
            metric = GaugeMetricFamily('compute_cluster_health', 'VROPS Compute Cluster Health', labels=['vrops_host','site','cluster'])
            for i in self.db(type=r["kind"]):
                for j in self.vcops.get_latest_stats(id=i['id'], statKey=stat_key )['values']:
                    for st in  j['stat-list']['stat']:
                        metric.add_metric( [self.config["server"]["hostname"],i["site"], i["object"]], st['data'][0] )
                        #print i["site"],i["object"],st['data'][0], st['data'][0]
            yield metric
        journal.send("======Completed Collection=========")

if __name__ == '__main__':
    journal.send("======Registering Collector service=========")
    REGISTRY.register(vropsCollector())
    journal.send(" =========Starting VROPS Collector on :8020===========")
    start_http_server(8020)
    while True: 
        journal.send("======Sleeping for 60 seconds=========")
        time.sleep(60)
        
        
        
    
