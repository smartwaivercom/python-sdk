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

# Set up your Smartwaiver connection using your API Key
sw = smartwaiver.Smartwaiver(api_key)

# Get a list of all templates
templates = sw.get_waiver_templates()

print('List all waiver templates:\n')
for template in templates:
    print(template.template_id + ': ' + template.title)

# If we have at least one template
if len(templates) > 1:

    # Get a specific template
    template = sw.get_waiver_template(templates[0].template_id)

    # Access properties of the template
    print('\nList single template:\n')
    print(template.template_id + ': ' + template.title)
