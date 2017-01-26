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

import json
from platform import python_version
from urllib.parse import urlencode
import unittest
from unittest import mock

import sys
sys.path.insert(0, '../')

import smartwaiver
import factory

headers = {
    'user-agent': 'SmartwaiverSDK:4.0.1-python:' + python_version(),
    'sw-api-key': 'TestApiKey'
}

class MockResponse:

    def __init__(self, status_code, text):
        self.status_code = status_code
        self.text = text

    def json(self):
        return json.loads(self.text)


def mock_get_responses(*args, **kwargs):

    if kwargs['headers'] != headers:
        raise Exception('Headers are not what is expected')

    if args[0] == 'https://api.smartwaiver.com/v4/templates':
        return MockResponse(200, factory.api_response_templates(3))
    elif args[0] == 'https://api.smartwaiver.com/v4/templates/alkagaldeab':
        return MockResponse(200, factory.api_response_template())
    elif args[0] == 'https://api.smartwaiver.com/v4/waivers?limit=20':
        return MockResponse(200, factory.api_response_waivers(3))
    elif args[0] == 'https://api.smartwaiver.com/v4/waivers?limit=5':
        return MockResponse(200, factory.api_response_waivers(3))
    elif args[0] == 'https://api.smartwaiver.com/v4/waivers?limit=20&verified=true':
        return MockResponse(200, factory.api_response_waivers(3))
    elif args[0] == 'https://api.smartwaiver.com/v4/waivers?limit=20&templateId=alkagaldeab':
        return MockResponse(200, factory.api_response_waivers(3))
    elif args[0] == 'https://api.smartwaiver.com/v4/waivers?limit=20&' + urlencode({'fromDts': '2016-11-01 00:00:00'}):
        return MockResponse(200, factory.api_response_waivers(3))
    elif args[0] == 'https://api.smartwaiver.com/v4/waivers?limit=20&' + urlencode({'toDts': '2016-11-01 00:00:00'}):
        return MockResponse(200, factory.api_response_waivers(3))
    elif args[0] == 'https://api.smartwaiver.com/v4/waivers/6jebdfxzvrdkd?pdf=false':
        return MockResponse(200, factory.api_response_waiver())
    elif args[0] == 'https://api.smartwaiver.com/v4/waivers/6jebdfxzvrdkd?pdf=true':
        return MockResponse(200, factory.api_response_waiver())
    elif args[0] == 'https://api.smartwaiver.com/v4/webhooks/configure':
        return MockResponse(200, factory.api_response_webhooks())
    else:
        raise Exception('Unexpected GET URL: ' + args[0])


def mock_put_responses(*args, **kwargs):

    expected_json = {
        'endpoint': 'http://endpoint.example.org',
        'emailValidationRequired': 'both'
    }

    if args[0] == 'https://api.smartwaiver.com/v4/webhooks/configure':
        if kwargs['headers'] == headers:
            if kwargs['json'] == expected_json:
                return MockResponse(201, factory.api_response_webhooks())
            else:
                raise Exception('JSON is not what is expected')
        else:
            raise Exception('Headers are not what is expected')
    else:
        raise Exception('Unexpected PUT URL: ' + args[0])


@mock.patch('smartwaiver.requests.get', mock.Mock(side_effect=mock_get_responses))
@mock.patch('smartwaiver.requests.put', mock.Mock(side_effect=mock_put_responses))
class SmartwaiverTest(unittest.TestCase):

    test_api_key = 'TestApiKey'

    def test_get_waiver_templates(self):

        sw = smartwaiver.Smartwaiver(self.test_api_key)
        templates = sw.get_waiver_templates()

        self.assertTrue(3, len(templates))
        for template in templates:
            self.assertIs(type(template), smartwaiver.types.SmartwaiverTemplate)

    def test_get_waiver_template(self):

        sw = smartwaiver.Smartwaiver(self.test_api_key)
        template = sw.get_waiver_template('alkagaldeab')

        self.assertIs(type(template), smartwaiver.types.SmartwaiverTemplate)

    def test_get_waivers(self):

        def test_waiver_summaries(waiver_summaries):
            self.assertTrue(3, len(waiver_summaries))
            for waiver_summary in waiver_summaries:
                self.assertIs(type(waiver_summary), smartwaiver.types.SmartwaiverWaiverSummary)

        sw = smartwaiver.Smartwaiver(self.test_api_key)

        test_waiver_summaries(sw.get_waiver_summaries())
        test_waiver_summaries(sw.get_waiver_summaries(limit=5))
        test_waiver_summaries(sw.get_waiver_summaries(verified=True))
        test_waiver_summaries(sw.get_waiver_summaries(template_id='alkagaldeab'))
        test_waiver_summaries(sw.get_waiver_summaries(from_dts='2016-11-01 00:00:00'))
        test_waiver_summaries(sw.get_waiver_summaries(to_dts='2016-11-01 00:00:00'))

    def test_get_waiver(self):

        sw = smartwaiver.Smartwaiver(self.test_api_key)

        waiver = sw.get_waiver('6jebdfxzvrdkd')
        self.assertIs(type(waiver), smartwaiver.types.SmartwaiverWaiver)

        waiver = sw.get_waiver('6jebdfxzvrdkd', pdf=False)
        self.assertIs(type(waiver), smartwaiver.types.SmartwaiverWaiver)

        waiver = sw.get_waiver('6jebdfxzvrdkd', pdf=True)
        self.assertIs(type(waiver), smartwaiver.types.SmartwaiverWaiver)

    def test_get_webhook_config(self):

        sw = smartwaiver.Smartwaiver(self.test_api_key)
        webhook = sw.get_webhook_config()

        self.assertIs(type(webhook), smartwaiver.types.SmartwaiverWebhook)

    def test_set_webhook_config(self):

        sw = smartwaiver.Smartwaiver(self.test_api_key)
        webhook = sw.set_webhook_config('http://endpoint.example.org',
                                        smartwaiver.types.SmartwaiverWebhook.WEBHOOK_BEFORE_AND_AFTER_EMAIL)

        self.assertIs(type(webhook), smartwaiver.types.SmartwaiverWebhook)

    def test_set_webhook(self):

        webhook = smartwaiver.types.SmartwaiverWebhook({
            'endpoint': 'http://endpoint.example.org',
            'emailValidationRequired': smartwaiver.types.SmartwaiverWebhook.WEBHOOK_BEFORE_AND_AFTER_EMAIL
        })

        sw = smartwaiver.Smartwaiver(self.test_api_key)
        new_webhook = sw.set_webhook(webhook)

        self.assertIs(type(new_webhook), smartwaiver.types.SmartwaiverWebhook)

    def test_get_waiver_templates_raw(self):

        sw = smartwaiver.Smartwaiver(self.test_api_key)
        response = sw.get_waiver_templates_raw()

        self.assertIs(type(response), smartwaiver.responses.SmartwaiverRawResponse)

    def test_get_waiver_template_raw(self):

        sw = smartwaiver.Smartwaiver(self.test_api_key)
        response = sw.get_waiver_template_raw('alkagaldeab')

        self.assertIs(type(response), smartwaiver.responses.SmartwaiverRawResponse)

    def test_get_waiver_raw(self):

        sw = smartwaiver.Smartwaiver(self.test_api_key)
        response = sw.get_waiver_raw('6jebdfxzvrdkd')

        self.assertIs(type(response), smartwaiver.responses.SmartwaiverRawResponse)

    def test_get_webhook_config_raw(self):

        sw = smartwaiver.Smartwaiver(self.test_api_key)
        response = sw.get_webhook_config_raw()

        self.assertIs(type(response), smartwaiver.responses.SmartwaiverRawResponse)

    def test_set_webhook_config_raw(self):

        sw = smartwaiver.Smartwaiver(self.test_api_key)
        response = sw.set_webhook_config_raw('http://endpoint.example.org',
                                        smartwaiver.types.SmartwaiverWebhook.WEBHOOK_BEFORE_AND_AFTER_EMAIL)

        self.assertIs(type(response), smartwaiver.responses.SmartwaiverRawResponse)


class SmartwaiverRoutesTest(unittest.TestCase):

    base_uri = 'https://api.smartwaiver.com'

    def test_get_waiver_templates(self):

        url = smartwaiver.SmartwaiverRoutes.get_waiver_templates()
        self.assertEqual(self.base_uri + '/v4/templates', url)

    def test_get_waiver_template(self):

        url = smartwaiver.SmartwaiverRoutes.get_waiver_template('alkagaldeab')
        self.assertEqual(self.base_uri + '/v4/templates/alkagaldeab', url)

    def test_get_waiver_summaries(self):

        url = smartwaiver.SmartwaiverRoutes.get_waiver_summaries()
        self.assertEqual(self.base_uri + '/v4/waivers?limit=20', url)

        url = smartwaiver.SmartwaiverRoutes.get_waiver_summaries(limit=5)
        self.assertEqual(self.base_uri + '/v4/waivers?limit=5', url)

        url = smartwaiver.SmartwaiverRoutes.get_waiver_summaries(verified=True)
        self.assertEqual(self.base_uri + '/v4/waivers?limit=20&verified=true', url)

        url = smartwaiver.SmartwaiverRoutes.get_waiver_summaries(template_id='alkagaldeab')
        self.assertEqual(self.base_uri + '/v4/waivers?limit=20&templateId=alkagaldeab', url)

        url = smartwaiver.SmartwaiverRoutes.get_waiver_summaries(from_dts='2016-11-01 00:00:00')
        self.assertEqual(self.base_uri + '/v4/waivers?limit=20&' + urlencode({'fromDts': '2016-11-01 00:00:00'}), url)

        url = smartwaiver.SmartwaiverRoutes.get_waiver_summaries(to_dts='2016-11-01 00:00:00')
        self.assertEqual(self.base_uri + '/v4/waivers?limit=20&' + urlencode({'toDts': '2016-11-01 00:00:00'}), url)

    def test_get_waiver(self):

        url = smartwaiver.SmartwaiverRoutes.get_waiver('6jebdfxzvrdkd')
        self.assertEqual(self.base_uri + '/v4/waivers/6jebdfxzvrdkd?pdf=false', url)

        url = smartwaiver.SmartwaiverRoutes.get_waiver('6jebdfxzvrdkd', False)
        self.assertEqual(self.base_uri + '/v4/waivers/6jebdfxzvrdkd?pdf=false', url)

        url = smartwaiver.SmartwaiverRoutes.get_waiver('6jebdfxzvrdkd', True)
        self.assertEqual(self.base_uri + '/v4/waivers/6jebdfxzvrdkd?pdf=true', url)

    def test_get_webhook_config(self):

        url = smartwaiver.SmartwaiverRoutes.get_webhook_config()
        self.assertEqual(self.base_uri + '/v4/webhooks/configure', url)

    def test_set_webhook_config(self):

        url = smartwaiver.SmartwaiverRoutes.set_webhook_config()
        self.assertEqual(self.base_uri + '/v4/webhooks/configure', url)

if __name__ == "__main__":
    unittest.main()
