import json
import yaml
import os
with open('./sample.json') as f:
  data = f.read()
  data = json.loads(data)
# data is a dictionary of the given json
print(data)
f = open('./sample.yaml', 'w+')
yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
f.close()
password = 'ubuntu'
command = 'mv ./sample.yaml /etc/netplan/sample.yaml'
os.popen("sudo -S %s"%(command), 'w').write(password)
