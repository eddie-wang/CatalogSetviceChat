class UpdateTagOption:
    def __init__ (self, client):
        self.client = client

    def handleRequest(self, input):
        _id=input["id"]
        value=input["value"]
        try:
            response = self.client.update_tag_option(Id=_id, Value = value)
        except Exception, e:
            return self.failedResponse(str(e))

        return self.fufillResponse()

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
                  "content": "Successfull update tagOption"
                }
            }
        }