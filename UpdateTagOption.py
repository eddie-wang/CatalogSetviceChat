class UpdateTagOption:
	def __init__ (self, client):
		self.client = client

	def handleRequest(self, input):
		_id=input["id"]
		value=input["value"]
		active=input["active"]
		response = self.client.update_tag_option(Id=_id, Value = value, Active = active)
		return response