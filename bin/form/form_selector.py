# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

class FormSelector(object):
	"""
	Define class ModelSelector with attribute(s) and method(s).
	Selecting python template form for generating process.
	It defines:
		attribute:
			Django - 0 Django form
			Flask - 1 Flask form
			Cancel - 2 Cancel option
			__MODULES - Dictionary with options
		method:
			choose_form - Selecting type of form for generating process
			format_name - Formatting name (class and file name)
	"""

	Django, Flask, Cancel = range(3)

	__MODULES = {
		Django : "Django form",
		Flask : "Flask form",
		Cancel : "Cancel"
	}

	@classmethod
	def choose_form(cls):
		"""
		:return: Form type
		:rtype: int
		"""
		print("\n form option list:")
		for key in sorted(FormSelector.__MODULES):
			print("  {0} {1}".format(key, FormSelector.__MODULES[key]))
		while True:
			form_type = input(" Select form: ")
			if form_type not in FormSelector.__MODULES.keys():
				print(" Not an appropriate choice.")
			else:
				break
		return form_type

	@classmethod
	def format_name(cls, form_name):
		"""
		:param form_name: Form name
		:type: str
		:return: File name with extension
		:rtype: str or NoneType
		"""
		if form_name:
			return "form_{0}{1}".format(form_name.lower(), ".py")
		return None
