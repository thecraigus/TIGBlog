from ncclient import manager
import xml.dom.minidom
import xmltodict
from pprint import pprint

nexus = {"host": "clab-srlceos01-vr-csr01", "port": "830",
          "username": "admin", "password": "admin"}


with manager.connect(host=nexus["host"], port=nexus["port"], username=nexus["username"], password=nexus["password"], hostkey_verify=False) as m:
    for capability in m.server_capabilities:
        print ('*' * 50)
        print (capability)

