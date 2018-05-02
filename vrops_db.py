#!/usr/bin/env python
import nagini
import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pydblite import Base

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
#config = dump(safe_load(open("/root/vrops/vrops.yaml", 'r')))
config = json.loads(open("/opt/prometheus/vrops_exporter/vrops.json").read() )

print  "Connecting to vROPs host: ",config["server"]["hostname"]
vcops = nagini.Nagini(host=config["server"]["hostname"], user_pass=(config["server"]["user"], config["server"]["pwd"]))
db = Base('/tmp/vrops.pd1')
db.create('type','object','id','site', mode="override")


for d_id in vcops.get_resources(resourceKind="Datacenter")['resourceList']:
 #if d_id['resourceKey']['name'] in [site for site in config["datacenter"] ]:
  #print d_id['identifier'],d_id['resourceKey']['name']
  for d_r in vcops.get_relationships(id=d_id['identifier'],relationshipType='CHILD')['resourceList']:
   if d_r['resourceKey']['resourceKindKey'] in [x["kind"] for x in config["metrics"]]:
    db.insert(type=d_r['resourceKey']['resourceKindKey'], object=d_r['resourceKey']['name'], id=d_r['identifier'], site=d_id['resourceKey']['name'])
    #print d_r['resourceKey']['resourceKindKey'], d_r['resourceKey']['name'], d_r['identifier'], d_id['resourceKey']['name']
     

db.commit()
