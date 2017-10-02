import uuid 
class ProvisionProduct:
    def __init__ (self, client):
        self.client = client

    def handleRequest(self, input):
        productId = input["productId"]
        ppName = input["provisionedName"]

        try:
          llp_response = self.client.list_launch_paths(ProductId=productId)
        except Exception as e:
          self.failedResponse("No valid launch path for this product")
        
        try:
          lppara_response = self.client.list_provisioning_artifacts(ProductId=productId)
        except Exception as e:
          self.failedResponse("No valid provisioning artifact for this product")


        try:
            pp_response = self.client.provision_product(
                ProductId=productId,
                ProvisioningArtifactId=lppara_response["ProvisioningArtifactDetails"][0]['Id'],
                PathId = llp_response["LaunchPathSummaries"][0]["Id"],
                ProvisionedProductName = ppName,
                ProvisionToken = str(uuid.uuid4())
              )
        except Exception, e:
            return self.failedResponse(str(e))

        print pp_response

        return self.fulfillResponse()

    def failedResponse(self, errorMessage):
        print errorMessage
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
                  "content": "Successfull  ProvisionProduct"
                }
            }
        }