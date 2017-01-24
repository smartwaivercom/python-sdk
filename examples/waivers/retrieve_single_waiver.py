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

# The unique ID of the signed waiver to be retrieved
waiver_id = '[INSERT WAIVER ID]'

# Set up your Smartwaiver connection using your API Key
sw = smartwaiver.Smartwaiver(api_key)

# Get the waiver object
waiver = sw.get_waiver(waiver_id)

# Access properties of the waiver
print('\nList single waiver:\n')
print(waiver.waiver_id + ': ' + waiver.title)

# Optionally include the Base64 encoded PDF
pdf = True

# Get the waiver object
waiver = sw.get_waiver(waiver_id, pdf)

print('\nPDF: ' + waiver.pdf)

# View all accessible properties of a waiver object in:
# examples/waivers/waiver_properties.php
