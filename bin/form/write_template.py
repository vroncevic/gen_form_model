# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from datetime import date
from os import getcwd
from string import Template
from form.form_selector import FormSelector

class WriteTemplate(object):
	"""
	Define class WriteTemplate with attribute(s) and method(s).
	Write a template content with parameters to a file.
	It defines:
		attribute:
			None
		method:
			__init__ - Initial constructor
			write - Write a template content with parameters to a file
	"""

	def __init__(self):
		pass

	def write(self, form_content, form_name):
		"""
		:param form_content: Template form content
		:type: str
		:param form_name: Parameter form name
		:type: str
		:return: Boolean status
		:rtype: bool
		"""
		current_dir = getcwd()
		file_name = FormSelector.format_name(form_name)
		if file_name:
			module_file = "{0}/{1}".format(current_dir, file_name)
			module_info = {
				"mod" : "{0}".format(form_name),
				"modlc": "{0}".format(form_name.lower()),
				"date" : "{0}".format(date.today()),
				"year" : "{0}".format(date.today().year)
			}
			try:
				template = Template(form_content)
				form_file = open(module_file, "w")
				form_file.write(template.substitute(module_info))
			except (IOError, KeyError) as e:
				print("I/O error({0}): {1}".format(e.errno, e.strerror))
			else:
				form_file.close()
				return True
		return False
