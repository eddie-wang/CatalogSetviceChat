class Router:
	def __init__ (self, pathMap):
		self.pathMap = pathMap

	def getActivity(self, activity):
		# TODO : add path check
		return self.pathMap[activity] 
