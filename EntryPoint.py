import boto3 
from Activities import *
from  Router import *
def lambda_handler(event, context):
	client = initSCSClient();
	router = initRouter()
	print event
	name= event['currentIntent']['name']
	input = event['currentIntent']['slots']
	activityResult = router.getActivity(name)(client,input)
	return handleResult(activityResult)

def handleResult (activityResult):
	return {
		"dialogAction": {
    		"type": "Close"
    		}
	}

def initRouter():
	# add acitivity in this map
	pathMap = {
		"CreateTagOption":createTagOption
	}
	return Router(pathMap)

def initSCSClient():
	# TODO add credential login later
	return boto3.client('servicecatalog')

if __name__ == "__main__":
	input = {
		"activity" : "createTagOption",
		"input" : {
			"key":"key1",
			"value":"value2"
		}
	}
	lambda_handler(input , None)