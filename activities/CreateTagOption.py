class CreateTagOption:
	def __init__ (self, client): 
		self.client = client

	def handleRequest(self, input):
		key = input["key"]
		value = input["value"]
		try:
			response = self.client.create_tag_option(Key=key,Value=value)
		except Exception, e:
			return self.failedCreateTagOptionResponse(str(e))

		print response
		return self.fulfillCreateTagOptionResponse(response['TagOptionDetail']['Id'])

	def failedCreateTagOptionResponse(self, errorMessage):
		return {
			"dialogAction": {
			    "type": "Close",
			    "fulfillmentState": "Failed",
			    "message": {
			      "contentType": "PlainText",
			      "content": errorMessage
			    }
  			}
		}

	def fulfillCreateTagOptionResponse(self, tagOptionId):
		return {
			"dialogAction": {
			    "type": "Close",
			    "fulfillmentState": "Fulfilled",
			    "message": {
			      "contentType": "PlainText",
			      "content": "Successfull create Tag Option with Id:" + tagOptionId,
			    }
  			}
		}
