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

# Get a list of all signed waivers for this account
summaries = sw.get_waiver_summaries()

# List waiver ID and title for each summary returned
print('List all waivers:\n')
for summary in summaries:
    print(summary.waiver_id + ': ' + summary.title)

# Get details for a specific waiver (include participants)
if len(summaries) > 1:

    # Pull out waiver ID from summary
    waiver_id = summaries[0].waiver_id

    # Get the waiver object
    waiver = sw.get_waiver(waiver_id)

    # Access properties of the waiver
    print('\nList single waiver:\n')
    print(waiver.waiver_id + ': ' + waiver.title)

    # List all participants
    for participant in waiver.participants:
        print('Participant: ' + participant.first_name
            + ', ' + participant.middle_name
            + ', ' + participant.last_name
            + ' - ' + participant.dob)
