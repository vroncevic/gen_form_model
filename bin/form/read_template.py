# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from os.path import dirname, realpath
from form.form_selector import FormSelector

class ReadTemplate(object):
	"""
	Define class ReadTemplate with attribute(s) and method(s).
	Read a template file (setup.template) and return a string representation.
	It defines:
		attribute:
			__TEMPLATE_DIR - Prefix path to templates
			__TEMPLATES - Modules (python templates)
			__template - Absolute template file path
		method:
			__init__ - Create and initial instance
			read - Read a template and return a string representation
	"""

	__TEMPLATE_DIR = "/../../conf/template"

	__TEMPLATES = {
		FormSelector.Django : "django.template",
		FormSelector.Flask : "flask.template"
	}

	def __init__(self):
		current_dir = dirname(realpath(__file__))
		self.__template = "{0}{1}".format(
			current_dir, ReadTemplate.__TEMPLATE_DIR
		)

	def read(self, form_type):
		"""
		:arg: form_type - Type of form
		:type: int
		:return: Form content
		:rtype: str or NoneType
		"""
		try:
			template_file = "{0}/{1}".format(
				self.__template, ReadTemplate.__TEMPLATES[form_type]
			)
			form_file = open(template_file, "r")
			form_content = form_file.read()
		except IOError as e:
			print("I/O error({0}): {1}".format(e.errno, e.strerror))
		else:
			form_file.close()
			return form_content
		return None
