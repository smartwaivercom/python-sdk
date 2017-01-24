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

from datetime import datetime
from datetime import timezone
import smartwaiver

# The API Key for your account
api_key = '[INSERT API KEY]'

# Set up your Smartwaiver connection using your API Key
sw = smartwaiver.Smartwaiver(api_key)

# Get a list of recent signed waivers for this account
summaries = sw.get_waiver_summaries()

# List waiver ID and title for each summary returned
print('List all waivers:\n')
for summary in summaries:
    print(summary.waiver_id + ': ' + summary.title)

# Specify parameters for listing signed waivers

# These are the default values

# Limit number of waivers returned to twenty (Allowed values: 1-100)
limit = 20

# Do not care about whether the waiver has been verified by email or not (Allowed values: true, false, None)
verified = None

# Do not limit the waivers returned to a specific template (Allowed values: Valid template ID)
template_id = ''

# Do not enforce a date range on the query for waivers (Allowed values: ISO 8601 Date) (Requires to_dts parameter)
from_dts = ''

# Used with 'from_dts' to provide the date range (Allowed values: ISO 8601 Date) (Requires from_dts parameter)
to_dts = ''

# This will return the the same as the above query because these are the default values
waiver_summaries = sw.get_waiver_summaries(limit, verified, template_id, from_dts, to_dts)

# An example limiting the parameters

# Limit number returned to 5
limit = 5

# Limit only to waivers that were signed at a kiosk or verified over email
verified = True

# Limit query to waivers of this template ID
template_id = '[INSERT TEMPLATE ID]'

# Limit to waivers signed in November of 2016
from_dts = datetime(2016, 11, 1, tzinfo=timezone.utc).isoformat()
to_dts = datetime(2016, 12, 1, tzinfo=timezone.utc).isoformat()

waiver_summaries = sw.get_waiver_summaries(limit, verified, template_id, from_dts, to_dts)

# View all accessible properties of a waiver summary object in:
# examples/waivers/WaiverSummaryProperties.php
