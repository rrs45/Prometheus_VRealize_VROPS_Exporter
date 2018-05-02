# vrops_exporter for Prometheus
This exporter collects metrics from vROPS API endpoint. Metrics to collect can be defined in the 'vrops.json' file.

#Caching
In order to avoid # of API calls, it caches metadata related to cluster UUID's in an in-memory DB. This is done by 'vrops_db.py' script which is run periodically using cronjob.

#Kubernetes
The exporter is Kubernetes ready. THe manifest in given in 'kubernetes.yaml'

#TLS Ingress Ready
The exporter itself can be secured with TLS and basic authentication using ingress controller. Here i am using Treafik to that. Sample config is given in traefik.yaml

Appreciate the feedback!
