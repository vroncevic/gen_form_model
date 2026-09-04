#!/bin/bash
#
# @brief   gen_form_model
# @version 2.0.0
# @date    Fri Sep 04 07:35:10 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 coverage/ats_coverage.py gen_form_model
pylint gen_form_model > gen_form_model.report
echo "Done"
