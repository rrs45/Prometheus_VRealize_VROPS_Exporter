#!//usr/bin/env python
import nagini
import json
from pprint import pprint as pp

vcops = nagini.Nagini(host="ep9-vrealize.dco.elmae", user_pass=("tesaract", '6pQVx!dSPd'))
#{'name': u'HPC01', 'site': u'Chicago', '__id__': 24, '__version__': 0, 'type': u'ClusterComputeResource', 'id': u'58f7f3a5-ba3f-4b3c-a7d5-9b0fc97a8eee'}
#pp(vcops.get_resources(resourceKind="Datacenter")['resourceList'])

#datacenter resource
#pp(vcops.get_relationships(id='edab7b0f-188c-4444-9a93-2e5374bf6d1e',relationshipType='CHILD')['resourceList'])

#host resource
#pp(vcops.get_relationships(id='1a0b64fd-c557-4554-8acc-14386d1d610e',relationshipType='CHILD')['resourceList'])

#Cluster resource
#pp(vcops.get_relationships(id='ff4d159c-e6bc-4d63-881a-5b37fd6e821a',relationshipType='CHILD')['resourceList'])
#pp(vcops.get_relationships(id='a7c9b250-316f-4f1d-9981-2bb7437334c7',relationshipType='CHILD')['resourceList'])


#pp(vcops.get_relationships(id='1a814861-1fdf-4ac3-a3f2-d375fd416d5b',relationshipType='CHILD')['resourceList'])


#pp(vcops.get_latest_stats(id='58f7f3a5-ba3f-4b3c-a7d5-9b0fc97a8eee'))
pp(vcops.get_latest_stats(id='1a814861-1fdf-4ac3-a3f2-d375fd416d5b',statKey='badge|health_state')['values'])

