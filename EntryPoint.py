import boto3 
from  Router import *
from CreateTagOption import *
from UpdateTagOption import *

def lambda_handler(event, context):
	client = initSCSClient();
	router = initRouter(client)
	print event
	name= event['currentIntent']['name']
	input = event['currentIntent']['slots']
	#activityResult = router.getActivity(name).handleRequest(input)
	#print activityResult
	return router.getActivity(name).handleRequest(input)

def initRouter(client):
	# add acitivity in this map
	pathMap = {
		"CreateTagOption":CreateTagOption(client),
		"UpdateTagOption":UpdateTagOption(client),
	}
	return Router(pathMap)

def initSCSClient():
	# TODO add credential login later
	return boto3.client('servicecatalog')

if __name__ == "__main__":
	input = {
		"currentIntent":{
		"name":"CreateTagOption",
		"slots":{
			"key":"keyasd",
			"value":"valueasdf"
		}
		}
	}
	lambda_handler(input , None)