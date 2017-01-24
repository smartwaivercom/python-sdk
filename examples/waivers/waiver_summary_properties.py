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

# Get a list of recent signed waivers for this account
waiver_summaries = sw.get_waiver_summaries()

# Access waiver properties
# These are all the available properties for a SmartwaiverWaiverSummary
if len(waiver_summaries) > 1:
    waiver_summary = waiver_summaries[0]
    print('Waiver Id: ' + waiver_summary.waiver_id)
    print('Template Id: ' + waiver_summary.template_id)
    print('Title: ' + waiver_summary.title)
    print('Created On: ' + waiver_summary.created_on)
    print('Expiration Date: ' + waiver_summary.expiration_date)
    print('Expired: ' + str(waiver_summary.expired))
    print('Verified: ' + str(waiver_summary.verified))
    print('Kiosk: ' + str(waiver_summary.kiosk))
    print('First Name: ' + waiver_summary.first_name)
    print('Middle Name: ' + waiver_summary.middle_name)
    print('Last Name: ' + waiver_summary.last_name)
    print('Dob: ' + waiver_summary.dob)
    print('Is Minor: ' + str(waiver_summary.is_minor))
    print('Tags:\t' + ', '.join(waiver_summary.tags))
