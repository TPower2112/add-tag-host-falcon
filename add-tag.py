############################################################################################################
# This script is used to tag a host with in the CrowdStrike Faclon Platform.
# The script will prompt the user for the client ID and secret, the hostname of the endpoint, and the tag.
############################################################################################################

import falconpy
from getpass import getpass
from falconpy import Hosts

# Authenticate to the CrowdStrike Falcon platform
# User inputs their CrowdStrike API ID and API Secret

cs_api_id = input("Please enter your CrowdStrike API ID: ")
cs_api_secret = getpass("Please enter your CrowdStrike API Secret (input hidden): ")

falcon = Hosts(client_id=cs_api_id, client_secret=cs_api_secret)

# The user inputs the hostname
host_name = input("Enter the hostname: ")

# Fetch AID of the host to be tagged
host_aid = falcon.QueryDevicesByFilter(filters={"hostname": host_name})

# The id list of hosts to tag
id_list = host_aid['body']['resources'][0]

# The user inputs the Falcon Grouping tag
tag_name = input("Enter the Falcon Grouping tag: ")
tag_list = [tag_name]

response = falcon.update_device_tags(action_name='add',ids=id_list, tags=tag_list)
print(response)
