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

import unittest
import json

import sys
sys.path.insert(0, '../')

import smartwaiver
import factory


class MockResponse:

    def __init__(self, status_code, text):
        self.status_code = status_code
        self.text = text

    def json(self):
        return json.loads(self.text)


class SmartwaiverResponseTest(unittest.TestCase):

    def test_construct_empty_body(self):
        with self.assertRaises(smartwaiver.exceptions.SmartwaiverSDKException) as cm:
            response = MockResponse(200, '')
            smartwaiver.responses.SmartwaiverResponse(response)

        self.assertEqual('Malformed JSON response from API server', str(cm.exception))

    def test_construct_invalid_json(self):
        with self.assertRaises(smartwaiver.exceptions.SmartwaiverSDKException) as cm:
            response = MockResponse(200, '<html>This Is Invalid Json</html>')
            smartwaiver.responses.SmartwaiverResponse(response)

        self.assertEqual('Malformed JSON response from API server', str(cm.exception))

    def test_missing_version(self):
        self.missing_field('version')

    def test_missing_id(self):
        self.missing_field('id')

    def test_missing_timestamp(self):
        self.missing_field('ts')

    def test_missing_type(self):
        self.missing_field('type')

    def missing_field(self, name):
        with self.assertRaises(smartwaiver.exceptions.SmartwaiverSDKException) as cm:
            template = factory.api_response_template_raw()
            template.pop(name)

            response = MockResponse(200, json.dumps(template))
            smartwaiver.responses.SmartwaiverResponse(response)

        self.assertEqual('API server response missing expected field: ' + name, str(cm.exception))

    def test_success_unknown_type(self):
        with self.assertRaises(smartwaiver.exceptions.SmartwaiverSDKException) as cm:
            template = factory.api_response_template_raw()
            template['type'] = 'unknown'

            response = MockResponse(200, json.dumps(template))
            smartwaiver.responses.SmartwaiverResponse(response)

        self.assertEqual('JSON response contains unknown type: "unknown"', str(cm.exception))

    def test_success_no_content(self):
        with self.assertRaises(smartwaiver.exceptions.SmartwaiverSDKException) as cm:
            template = factory.api_response_template_raw()
            template.pop('template')

            response = MockResponse(200, json.dumps(template))
            smartwaiver.responses.SmartwaiverResponse(response)

        self.assertEqual('JSON response does not contain field of type: "template"', str(cm.exception))

    def test_http_errors(self):
        with self.assertRaises(smartwaiver.exceptions.SmartwaiverHTTPException) as cm:
            response = MockResponse(400, factory.api_response_parameter_error())
            smartwaiver.responses.SmartwaiverResponse(response)

        self.assertEqual('Invalid parameter', str(cm.exception))

    def test_http_no_message(self):
        with self.assertRaises(smartwaiver.exceptions.SmartwaiverSDKException) as cm:
            response = MockResponse(500, factory.api_response_no_message_error())
            smartwaiver.responses.SmartwaiverResponse(response)

        self.assertEqual('Error response does not include message', str(cm.exception))

    def test_unknown_error(self):
        with self.assertRaises(smartwaiver.exceptions.SmartwaiverSDKException) as cm:
            response = MockResponse(430, factory.api_response_no_message_error())
            smartwaiver.responses.SmartwaiverResponse(response)

        self.assertEqual('Unknown HTTP code returned: 430', str(cm.exception))

    def test_http_exception_info(self):
        with self.assertRaises(smartwaiver.exceptions.SmartwaiverHTTPException) as cm:
            response = MockResponse(500, factory.api_response_server_error())
            smartwaiver.responses.SmartwaiverResponse(response)

        self.assertEqual('Internal server error', str(cm.exception))
        self.assertDictEqual(factory.api_response_server_error_raw(), cm.exception.response_info)
        self.assertEqual(500, cm.exception.status_code)
        self.assertIs(type(cm.exception.response), MockResponse)

    def test_success(self):
        template_data = factory.api_response_template_raw()
        mock_response = MockResponse(200, factory.api_response_template())
        response = smartwaiver.responses.SmartwaiverResponse(mock_response)

        self.assertEqual(template_data['version'], response.version)
        self.assertEqual(template_data['id'], response.id)
        self.assertEqual(template_data['ts'], response.ts)
        self.assertEqual(template_data['type'], response.type)
        self.assertEqual(template_data['template'], response.response_data)
        self.assertIs(type(response.response), MockResponse)


class SmartwaiverRawResponseTest(unittest.TestCase):

    def test_response_creation(self):
        mock_response = MockResponse(200, factory.api_response_template())
        raw_response = smartwaiver.responses.SmartwaiverRawResponse(mock_response)

        self.assertEqual(200, raw_response.status_code)
        self.assertEqual(factory.api_response_template(), raw_response.body)

if __name__ == "__main__":
    unittest.main()
