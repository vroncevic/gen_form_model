# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

import sys
from app.cfg_base import CfgBase
from form.gen_form import GenForm
from os.path import dirname, realpath, exists
from datetime import datetime

class GenFormModel(CfgBase, GenForm):
	"""
	Define class GenFormModel with attribute(s) and method(s).
	Load a settings, create a CL interface and run operation(s).
	It defines:
		attribute:
			__CONFIG - Configuration file path
			__OPS -  Tool options (list)
		method:
			__init__ - Initial constructor
			process - Process and run tool option
	"""

	__CONFIG = "/../conf/gen_form_model.cfg"
	__OPS = ["-g", "--gen", "-h", "--version"]

	def __init__(self):
		current_dir = dirname(realpath(__file__))
		base_config_file = "{0}{1}".format(current_dir, GenFormModel.__CONFIG)
		CfgBase.__init__(self, base_config_file)
		if self.get_tool_status():
			self.add_new_option(
				GenFormModel.__OPS[0], GenFormModel.__OPS[1], dest="mod",
				help="generate form model"
			)
			GenForm.__init__(self)

	def process(self):
		if self.get_tool_status():
			tool = "[{0}]".format(self.get_name())
			ver = "version {0}".format(self.get_version())
			print("\n{0} {1} {2}".format(tool, ver, datetime.now().date()))
			if len(sys.argv) > 1:
				op = sys.argv[1]
				if op not in GenFormModel.__OPS:
					sys.argv = []
					sys.argv.append("-h")
			else:
				sys.argv.append("-h")
			opts, args = self.parse_args(sys.argv)
			form_file = "{0}{1}".format(opts.mod, ".py")
			if len(args) == 1 and opts.mod and not exists(form_file):
				console_txt = "generating setup.py for package"
				print("{0} {1} [{2}]".format(tool, console_txt, opts.mod))
				status = self.gen_form("{0}".format(opts.mod))
				if status:
					print("{0} {1}".format(tool, "done!\n"))
				else:
					console_txt = "failed to process and run option!\n"
					print("{0} {1}".format(tool, console_txt))
			else:
				console_txt = "module setup.py already exist in local folder!\n"
				print("{0} {1}".format(tool, console_txt))
		else:
			console_txt = "tool is not operational!\n"
			print("[{0}] {1}".format("gen_form_model", console_txt))
