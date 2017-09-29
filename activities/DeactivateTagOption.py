class DeactivateTagOption:
	def __init__ (self, client):
		self.client = client

	def handleRequest(self, input):
		_id=input["id"]
		try:
			response = self.client.update_tag_option(Id=_id, Active = False)
		except Exception, e: 
			return self.failedResponse(str(e))
		return self.fulfillResponse()

	def failedResponse(self, errorMessage):
		return {
			"dialogAction": {
			    "type": "Close",
			    "fulfillmentState": "Failed",
			    "message": {
			      "contentType": "PlainText",
			      "content": errorMessage
			    },
			   "responseCard": {
			      "version": 1,
			      "contentType": "application/vnd.amazonaws.card.generic",
			      "genericAttachments": [
			          {
			             "title":"You Failed",
			             "subTitle":"We are sorry about that.",
			             "imageUrl":"goo.gl/ou6g9X",
			             "attachmentLinkUrl":"URL of the attachment to be associated with the card",
			           } 
			        ] 
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
			      "content": "Successfull deactive tagOption"
			    }
  			}
		}