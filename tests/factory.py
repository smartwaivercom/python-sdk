# Copyright 2017 Smartwaiver
#
# Licensed under the Apache License, Version 2.0 (the "License") you may
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

import json


def api_response_base():

    return {
        'version': 4,
        'id': 'a0256461ca244278b412ab3238f5efd2',
        'ts': '2017-01-23T09:15:45.645Z'
    }


def api_response_parameter_error():

    response = api_response_base()
    response['type'] = 'parameter_error'
    response['message'] = 'Invalid parameter'
    return json.dumps(response)


def api_response_unauthorized_error():
    response = api_response_base()
    response['type'] = 'auth_error'
    response['message'] = 'Unauthorized'
    return json.dumps(response)


def api_response_data_error():
    response = api_response_base()
    response['type'] = 'data_error'
    response['message'] = 'Invalid data'
    return json.dumps(response)


def api_response_not_found_error():
    response = api_response_base()
    response['type'] = 'error'
    response['message'] = 'Not Found'
    return json.dumps(response)


def api_response_wrong_content_type_error():
    response = api_response_base()
    response['type'] = 'error'
    response['message'] = 'Invalid content type'
    return json.dumps(response)


def api_response_server_error():
    return json.dumps(api_response_server_error_raw())

def api_response_server_error_raw():
    response = api_response_base()
    response['type'] = 'error'
    response['message'] = 'Internal server error'
    return response


def api_response_no_message_error():
    response = api_response_base()
    response['type'] = 'error'
    return json.dumps(response)


def api_response_templates(num_templates):

    response = api_response_base()
    response['type'] = 'templates'
    response['templates'] = [template()] * num_templates
    return json.dumps(response)


def api_response_template():

    return json.dumps(api_response_template_raw())


def api_response_template_raw():

    response = api_response_base()
    response['type'] = 'template'
    response['template'] = template()
    return response


def api_response_waivers(num_waivers):

    response = api_response_base()
    response['type'] = 'waivers'
    response['waivers'] = [waiver_summary()] * num_waivers
    return json.dumps(response)


def api_response_waiver():

    response = api_response_base()
    response['type'] = 'waiver'
    response['waiver'] = waiver()
    return json.dumps(response)


def api_response_webhooks():

    response = api_response_base()
    response['type'] = 'webhooks'
    response['webhooks'] = webhook()
    return json.dumps(response)


def template():
    return {
        'templateId': 'sprswrvh2keeh',
        'title': 'Demo Waiver',
        'publishedVersion': 78015,
        'publishedOn': '2017-01-24 11:14:25',
        'webUrl': 'https://www.smartwaiver.com/w/sprswrvh2keeh/web/',
        'kioskUrl': 'https://www.smartwaiver.com/w/sprswrvh2keeh/kiosk/'
    }


def waiver_summary():
    return {
        'waiverId': '6jebdfxzvrdkd',
        'templateId': 'sprswrvh2keeh',
        'title': 'Demo Waiver',
        'createdOn': '2017-01-24 13:12:29',
        'expirationDate': '',
        'expired': False,
        'verified': True,
        'kiosk': False,
        'firstName': 'Kyle',
        'middleName': '',
        'lastName': 'Smith',
        'dob': '2005-12-25',
        'isMinor': True,
        'tags': ['Green Team']
    }


def waiver():
    waiver_data = waiver_summary()
    waiver_data['participants'] = [participant()]
    waiver_data['clientIP'] = '192.0.2.0'
    waiver_data['email'] = 'kyle@example.com'
    waiver_data['marketingAllowed'] = False
    waiver_data['addressLineOne'] = '626 NW Arizona Ave.'
    waiver_data['addressLineTwo'] = 'Suite 2'
    waiver_data['addressCity'] = 'Bend'
    waiver_data['addressState'] = 'OR'
    waiver_data['addressZip'] = '97703'
    waiver_data['addressCountry'] = 'US'
    waiver_data['emergencyContactName'] = 'John Smith'
    waiver_data['emergencyContactPhone'] = '111-111-1111'
    waiver_data['insuranceCarrier'] = 'My Insurance'
    waiver_data['insurancePolicyNumber'] = '1234567'
    waiver_data['driversLicenseNumber'] = '9876543'
    waiver_data['driversLicenseState'] = 'OR'
    waiver_data['customWaiverFields'] = {
        'zrmgxh4ft8sqh': custom_field()
    }
    waiver_data['guardian'] = guardian()
    waiver_data['pdf'] = ''
    return waiver_data


def participant():
    return {
        'firstName': 'Kyle',
        'middleName': '',
        'lastName': 'Smith',
        'dob': '2005-12-25',
        'isMinor': 'true',
        'gender': 'Male',
        'phone': '111-111-1111',
        'tags': ['Beginner'],
        'customParticipantFields': {
            'w5qe9kkh3bxpe' : custom_field()
        }
    }


def custom_field():
    return {
        'value': 'A friend',
        'displayText': 'How did you hear about this company?'
    }


def guardian():
    return {
        'firstName': 'Jane',
        'middleName': '',
        'lastName': 'Smith',
        'phone': '111-111-1111',
        'relationship': 'Mother'
    }


def webhook():
    return {
        'endpoint': 'endpoint',
        'emailValidationRequired': 'both'
    }