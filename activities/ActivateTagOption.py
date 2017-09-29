class ActivateTagOption:
	def __init__ (self, client):
		self.client = client

	def handleRequest(self, input):
		_id=input["id"]
		try:
			response = self.client.update_tag_option(Id=_id, Active = True)
		except Exception, e: 
			return self.failedeResponse(str(e))
		return self.fulfillResponse()

	def failedResponse(self, errorMessage):
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

	def fulfillResponse(self):
		return {
			"dialogAction": {
			    "type": "Close",
			    "fulfillmentState": "Fulfilled",
			    "message": {
			      "contentType": "PlainText",
			      "content": "Successfull ActivateTagOption"
			    }
  			}
		}		