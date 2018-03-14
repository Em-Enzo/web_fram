# this module contains the classes for the project



class Member(object):
	"""the member's age & name """
	def __init__(self, name, age):
		self.name = name
		self.age = age
		self.id = 0

class Post(object):
	"""the post's manupilations class"""
	def __init__(self, title, subject):
		self.title = title
		self.subject = subject

    