# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from form.read_template import ReadTemplate
from form.write_template import WriteTemplate
from form.form_selector import FormSelector

class GenForm(ReadTemplate, WriteTemplate):
	"""
	Define class GenForm with attribute(s) and method(s).
	Generate form model by template and parameters.
	It defines:
		attribute:
			__status - Operation status
		method:
			__init__ - Initial constructor
			gen_form - Generate form module file
	"""

	def __init__(self):
		ReadTemplate.__init__(self)
		WriteTemplate.__init__(self)
		self.__status = False

	def gen_form(self, form_name):
		"""
		:param form_name: Parameter form class name
		:type: str
		:return: Boolean status
		:rtype: bool
		"""
		form_type = FormSelector.choose_form()
		if form_type != FormSelector.Cancel:
			form_content = self.read(form_type)
			if form_content:
				self.__status = self.write(form_content, form_name)
		else:
			self.__status = True
		return self.__status
