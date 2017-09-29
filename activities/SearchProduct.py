from pprint import pprint

class SearchProduct:
    def __init__ (self, client):
        self.client = client

    def handleRequest(self, input):

        try:
            response = self.client.search_products()
        except Exception, e:
            return self.failedResponse(str(e))

        #if "NextPageToken" in response:
        #    nextPageToken = response["NextPageToken"]
        print response

        result = response["ProductViewSummaries"]

        #while nextPageToken is not None and len(nextPageToken)>0:
        #    try:
        #        response = self.client.search_products(NextPageToken = nextPageToken)
        #    except Exception as e:
        #        return self.failedResponse(str(e))
        #    else:
        #        nextPageToken = response["NextPageToken"]
        #        result.extend(response["ProductViewSummaries"])            

        print result
        return self.fulfillResponse(result)

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

    def fulfillResponse(self, result):
        string1 = len(result)
        string2 = pprint(result)
        return {
            "dialogAction": {
                "type": "Close",
                "fulfillmentState": "Fulfilled",
                "message": {
                  "contentType": "PlainText",
                  "content": """You have {string1} Products in your account.
                                Here is a list of your products:
                                {string2}
                                """
                }
            }
        }