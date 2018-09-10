import requests # http://docs.python-requests.org/en/master/
import psutil   # https://pypi.python.org/pypi/psutil
import time, sys, platform

hostiotmms = 'iotmmsa2667617c.hana.ondemand.com'
apiiotmmsdata = '/com.sap.iotservices.mms/v1/api/http/data/'
msgtypeid = 'd2b2db6980f940fae7d3'

deviceid = 'AEBBD0DD0C224945BDB178004364327D'
authtoken = 'f01b815d9429f2e58bfee94be2164241'

url = "https://"+hostiotmms+apiiotmmsdata+deviceid

def readsensors():
	global d_pctCPU
	d_pctCPU = psutil.cpu_percent(percpu=False, interval = 1)
	return

def postiotneo ():
	global d_pctCPU

	s_pctCPU = str(d_pctCPU)
	d_tstamp = int(round(time.time()))

	s_tstamp = str(d_tstamp)

	print("\nValues to post: ", d_pctCPU, d_tstamp)

	payload = "{\"mode\":\"sync\",\"messageType\":\""+msgtypeid+"\",\"messages\":[{\"cpu_usage\":"+s_pctCPU+",\"cpu_type\":\"generic\",\"_time\":"+s_tstamp+"}]}"
	headers = {
			'content-type': "application/json",
			'authorization': "Bearer "+authtoken,
			'cache-control': "no-cache"
			}

	print("Payload to post: ", payload)

	response = requests.request("POST", url, data=payload, headers=headers)

	print(response.status_code, response.text)

	return

try:
	while(True):
		readsensors()
		postiotneo()
		time.sleep(2)
except KeyboardInterrupt:
	print("Stopped by the user!")
