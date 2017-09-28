class CreateTagOption:
	def __init__ (self, client): 
		self.client = client

	def handleRequest(self, input):
		key = input["key"]
		value = input["value"]
		response = self.client.create_tag_option( Key=key,Value=value)
		print response
