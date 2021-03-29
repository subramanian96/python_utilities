import json
import yaml
with open('./sample.json') as f:
  data = f.read()
  data = json.loads(data)
# data is a dictionary of the given json
print(data)
f = open('/etc/netplan/sample.yaml', 'w+')
yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
f.close()
