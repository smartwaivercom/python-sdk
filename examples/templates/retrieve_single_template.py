# Copyright 2017 Smartwaiver
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import smartwaiver

# The API Key for your account
api_key = '[INSERT API KEY]'

# The unique identifier of the template to retrieve
template_id = '[INSERT TEMPLATE ID]'

# Set up your Smartwaiver connection using your API Key
sw = smartwaiver.Smartwaiver(api_key)

# Retrieve a specific template (SmartwaiverTemplate object)
template = sw.get_waiver_template(template_id)

# Access properties of the template
print('\nList single template:\n')
print(template.template_id + ': ' + template.title)

# View all accessible properties of a waiver template object in:
# examples/templates/template_properties.php
