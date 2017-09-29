import uuid 
class ListLaunchPaths:
    def __init__ (self, client):
        self.client = client

    def handleRequest(self, input):
        try:
            response = self.client.list_launch_path(
              ProductId=input['productId']
              )
        except Exception, e:
            return self.failedResponse(str(e))

        return self.fufillResponse(response)

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

    def fulfillResponse(self, response):
        return {
            "dialogAction": {
                "type": "Close",
                "fulfillmentState": "Fulfilled",
                "message": {
                  "contentType": "PlainText",
                  "content": "Success!"+ response 
                }
            }
        }