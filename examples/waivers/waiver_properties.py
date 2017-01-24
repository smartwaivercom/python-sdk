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

# Get the waiver object (include the pdf as well)
waiver = sw.get_waiver(waiver_id, True)

# Access waiver properties
# These are all the available properties for a SmartwaiverWaiver
print('Waiver Id: ' + waiver.waiver_id)
print('Template Id: ' + waiver.template_id)
print('Title: ' + waiver.title)
print('Created On: ' + waiver.created_on)
print('Expiration Date: ' + waiver.expiration_date)
print('Expired: ' + str(waiver.expired))
print('Verified: ' + str(waiver.verified))
print('Kiosk: ' + str(waiver.kiosk))
print('First Name: ' + waiver.first_name)
print('Middle Name: ' + waiver.middle_name)
print('Last Name: ' + waiver.last_name)
print('Dob: ' + waiver.dob)
print('Is Minor: ' + str(waiver.is_minor))

print('Tags:\t' + ', '.join(waiver.tags))

print('Participants:')

for index, participant in enumerate(waiver.participants):
    print('\tParticipant ' + str(index) + ':')
    print('\t\tFirst Name: ' + participant.first_name)
    print('\t\tMiddle Name: ' + participant.middle_name)
    print('\t\tLast Name: ' + participant.last_name)
    print('\t\tDOB: ' + participant.dob)
    print('\t\tIs Minor: ' + str(participant.is_minor))
    print('\t\tGender: ' + participant.gender)
    print('\t\tTags: ' + ', '.join(participant.tags))
    print('\t\tCustom Participant Fields: (GUID, Display Text, Value)')

    for guid in participant.custom_participant_fields:
        print('\t\t\t' + guid + ', '
             + participant.custom_participant_fields[guid].display_text
             + ', ' + participant.custom_participant_fields[guid].value)

print('Custom Waiver Fields: (GUID, Display Text, Value)')

for guid in waiver.custom_waiver_fields:
    print('\t' + guid
         + ', ' + waiver.custom_waiver_fields[guid].display_text
         + ', ' + waiver.custom_waiver_fields[guid].value)

print('Guardian:')

if waiver.guardian is not None:
    print('\tFirst Name: ' + waiver.guardian.first_name)
    print('\tMiddle Name: ' + waiver.guardian.middle_name)
    print('\tLast Name: ' + waiver.guardian.last_name)
    print('\tPhone: ' + waiver.guardian.phone)
    print('\tRelationship: ' + waiver.guardian.relationship)

print('Email: ' + waiver.email)
print('Marketing Allowed: ' + str(waiver.marketing_allowed))
print('Address Line One: ' + waiver.address_line_one)
print('Address Line Two: ' + waiver.address_line_two)
print('Address City: ' + waiver.address_city)
print('Address State: ' + waiver.address_state)
print('Address Zip Code: ' + waiver.address_zip)
print('Address Country: ' + waiver.address_country)
print('Emergency Contact Name: ' + waiver.emergency_contact_name)
print('Emergency Contact Phone: ' + waiver.emergency_contact_phone)
print('Insurance Carrier: ' + waiver.insurance_carrier)
print('Insurance Policy Number: ' + waiver.insurance_policy_number)
print('Drivers License Number: ' + waiver.drivers_license_number)
print('Drivers License State: ' + waiver.drivers_license_state)
print('Client IP: ' + waiver.client_ip)
print('PDF: ' + waiver.pdf)
