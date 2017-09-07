# -*- coding: utf-8 -*-

class Access_Modifiler() :

	public = "PUBLIC"
	__private = "PRIVATE"
	_protected = "PROTECTED"

	def print_test(self):
		print("public : %s" %self.public)
	 	print("__private : %s" %self.__private)
	 	print("_protected : %s" %self._protected)

	def get_private(self) :
	 	return self.__private

	def set_private(self, p) :
	 	self.__private = p


test = Access_Modifiler()
print test.get_private()
test.set_private("CHANG_PRIVATE")

print test.get_private()