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

from platform import python_version
from urllib.parse import urlencode

import requests

import smartwaiver.exceptions
import smartwaiver.responses
import smartwaiver.types


class Smartwaiver():

    _version = '4.0.1'

    def __init__(self, api_key):
        """Creates a new Smartwaiver object.

        :param api_key: The API Key for the account
        :type api_key: ``string``
        """

        self._last_response = None
        self._headers = {
            'user-agent': 'SmartwaiverSDK:' + self._version + '-python:' + python_version(),
            'sw-api-key': api_key
        }

    def get_waiver_templates(self):
        """Get a list of waiver templates for this account

        :return: The :class:`SmartwaiverTemplate` object that represents the waiver template
        :rtype: smartwaiver.types.SmartwaiverTemplate
        """

        url = SmartwaiverRoutes.get_waiver_templates()
        self._last_response = responses.SmartwaiverResponse(requests.get(url, headers=self._headers))

        return [types.SmartwaiverTemplate(template) for template in self._last_response.response_data]

    def get_waiver_template(self, template_id):
        """Get a specific waiver template by providing the unique identifier

        :param template_id: The unique identifier of the specific waiver template
        :type template_id: ``string``

        :return: The :class:`SmartwaiverTemplate` object that represents the waiver template
        :rtype: smartwaiver.types.SmartwaiverTemplate
        """

        url = SmartwaiverRoutes.get_waiver_template(template_id)
        self._last_response = responses.SmartwaiverResponse(requests.get(url, headers=self._headers))

        return types.SmartwaiverTemplate(self._last_response.response_data)

    def get_waiver_summaries(self, limit=20, verified=None, template_id='', from_dts='', to_dts=''):
        """Execute a query to find waivers, the returned objects will be waiver summaries

        :param limit: Limit query to this number of the most recent waivers.
        :type limit: ``integer``

        :param verified: Limit query to verified by email (true) or not verified (false) or both (None).
        :type verified: ``boolean``

        :param template_id: Limit query to signed waivers of the given waiver template ID.
        :type template_id: ``string``

        :param from_dts: Limit query to waivers between this ISO 8601 date and the toDts parameter.
        :type from_dts: ``string``

        :param to_dts: Limit query to waivers between this ISO 8601 date and the fromDts parameter.
        :type to_dts: ``string``

        :return: A list of :class:`SmartwaiverWaiverSummary` object's that represent the waivers.
        :rtype: ``list``
        """

        url = SmartwaiverRoutes.get_waiver_summaries(limit, verified, template_id, from_dts, to_dts)
        self._last_response = responses.SmartwaiverResponse(requests.get(url, headers=self._headers))

        return [types.SmartwaiverWaiverSummary(waiver_summary) for waiver_summary in self._last_response.response_data]

    def get_waiver(self, waiver_id, pdf=False):
        """Get a specific waiver by the unique identifier

        :param waiver_id: The Unique identifier of the waiver to retrieve
        :type waiver_id: ``string``

        :param pdf: Whether to include the Base64 Encoded PDF
        :type pdf: ``boolean``

        :return: The :class:`SmartwaiverWaiver` object that represents the waiver
        :rtype: smartwaiver.types.SmartwaiverWaiver
        """

        url = SmartwaiverRoutes.get_waiver(waiver_id, pdf)
        self._last_response = responses.SmartwaiverResponse(requests.get(url, headers=self._headers))

        return types.SmartwaiverWaiver(self._last_response.response_data)

    def get_webhook_config(self):
        """Get your account's current webhook configuration

        :return: The new webhook settings
        :rtype: smartwaiver.types.SmartwaiverWebhook
        """

        url = SmartwaiverRoutes.get_webhook_config()
        self._last_response = responses.SmartwaiverResponse(requests.get(url, headers=self._headers))

        return types.SmartwaiverWebhook(self._last_response.response_data)

    def set_webhook_config(self, endpoint, email_validation_required):
        """Set your account's webhook configuration

        :param endpoint: The URL endpoint for the webhook
        :type endpoint: ``string``

        :param email_validation_required: When to send the webhook, see :class:`SmartwaiverWebhook` for constants to use
        :type email_validation_required: ``string``

        :return: The new webhook settings
        :rtype: smartwaiver.types.SmartwaiverWebhook
        """

        config = {
            'endpoint': endpoint,
            'emailValidationRequired': email_validation_required
        }
        url = SmartwaiverRoutes.set_webhook_config()
        self._last_response = responses.SmartwaiverResponse(requests.put(url, headers=self._headers, json=config))

        return types.SmartwaiverWebhook(self._last_response.response_data)

    def set_webhook(self, webhook):
        """Set your account's webhook configuration

        :param webhook: The webhook settings to send to the API server
        :type webhook: smartwaiver.types.SmartwaiverWebhook

        :return: The new webhook settings
        :rtype: smartwaiver.types.SmartwaiverWebhook
        """

        return self.set_webhook_config(webhook.endpoint, webhook.email_validation_required)

    def get_waiver_templates_raw(self):
        """Get a list of waiver templates for this account (raw version)

        :return: The raw body and status code of the response from the server
        :rtype: smartwaiver.responses.SmartwaiverRawResponse
        """

        url = SmartwaiverRoutes.get_waiver_templates()
        return responses.SmartwaiverRawResponse(requests.get(url, headers=self._headers))

    def get_waiver_template_raw(self, template_id):
        """Get a specific waiver template by providing the unique identifier (raw version)

        :param template_id: The unique identifier of the specific waiver template
        :type template_id: ``string``

        :return: The raw body and status code of the response from the server
        :rtype: smartwaiver.responses.SmartwaiverRawResponse
        """

        url = SmartwaiverRoutes.get_waiver_template(template_id)
        return responses.SmartwaiverRawResponse(requests.get(url, headers=self._headers))

    def get_waiver_summaries_raw(self, limit=20, verified=None, template_id='', from_dts='', to_dts=''):
        """Execute a query to find waivers, the returned objects will be waiver summaries (raw version)

        :param limit: Limit query to this number of the most recent waivers.
        :type limit: ``integer``

        :param verified: Limit query to verified by email (true) or not verified (false) or both (None).
        :type verified: ``boolean``

        :param template_id: Limit query to signed waivers of the given waiver template ID.
        :type template_id: ``string``

        :param from_dts: Limit query to waivers between this ISO 8601 date and the toDts parameter.
        :type from_dts: ``string``

        :param to_dts: Limit query to waivers between this ISO 8601 date and the fromDts parameter.
        :type to_dts: ``string``

        :return: The raw body and status code of the response from the server
        :rtype: smartwaiver.responses.SmartwaiverRawResponse
        """

        url = SmartwaiverRoutes.get_waiver_summaries(limit, verified, template_id, from_dts, to_dts)
        return responses.SmartwaiverRawResponse(requests.get(url, headers=self._headers))

    def get_waiver_raw(self, waiver_id, pdf=False):
        """Get a specific waiver by the unique identifier (raw version)

        :param waiver_id: The Unique identifier of the waiver to retrieve
        :type waiver_id: ``string``

        :param pdf: Whether to include the Base64 Encoded PDF
        :type pdf: ``boolean``

        :return: The raw body and status code of the response from the server
        :rtype: smartwaiver.responses.SmartwaiverRawResponse
        """

        url = SmartwaiverRoutes.get_waiver(waiver_id, pdf)
        return responses.SmartwaiverRawResponse(requests.get(url, headers=self._headers))

    def get_webhook_config_raw(self):
        """Get your account's current webhook configuration (raw version)

        :return: The raw body and status code of the response from the server
        :rtype: smartwaiver.responses.SmartwaiverRawResponse
        """

        url = SmartwaiverRoutes.get_webhook_config()
        return responses.SmartwaiverRawResponse(requests.get(url, headers=self._headers))

    def set_webhook_config_raw(self, endpoint, email_validation_required):
        """Set your account's webhook configuration (raw version)

        :param endpoint: The URL endpoint for the webhook
        :type endpoint: ``string``

        :param email_validation_required: When to send the webhook, see :class:`SmartwaiverWebhook` for constants to use
        :type email_validation_required: ``string``

        :return: The raw body and status code of the response from the server
        :rtype: smartwaiver.responses.SmartwaiverRawResponse
        """

        config = {
            'endpoint': endpoint,
            'emailValidationRequired': email_validation_required
        }
        url = SmartwaiverRoutes.set_webhook_config()
        return responses.SmartwaiverRawResponse(requests.put(url, headers=self._headers, json=config))

    @property
    def last_response(self):
        """Get the SmartwaiverResponse objected created for the most recent API
        request. Useful for error handling if an exception is thrown.

        :return: The last response this object received from the API
        :rtype: smartwaiver.responses.SmartwaiverResponse
        """
        return self._last_response


class SmartwaiverRoutes():
    """This class provides and easy way to create the actual URLs for the
    routes.
    """

    _base_uri = 'https://api.smartwaiver.com'

    _route_templates = '/v4/templates'
    _route_waivers = '/v4/waivers'
    _route_webhooks = '/v4/webhooks/configure'

    @staticmethod
    def get_waiver_templates():
        """Returns the URL to get waiver templates

        :return: The URL to get waiver templates
        :rtype: ``string``
        """
        return SmartwaiverRoutes._base_uri + SmartwaiverRoutes._route_templates

    @staticmethod
    def get_waiver_template(template_id):
        """Return the URL to get a specific waiver template

        :param template_id: The unique identifier of the specific waiver template
        :type template_id: ``string``

        :return: The URL to get a specific waiver template
        :rtype: ``string``
        """
        return SmartwaiverRoutes._base_uri + SmartwaiverRoutes._route_templates + '/' + template_id

    @staticmethod
    def get_waiver_summaries(limit=20, verified=None, template_id='', from_dts='', to_dts=''):
        """Return the URL to execute the query for waiver summaries

        :param limit: Limit query to this number of the most recent waivers.
        :type limit: ``integer``

        :param verified: Limit query to verified by email (true) or not verified (false) or both (None).
        :type verified: ``boolean``

        :param template_id: Limit query to signed waivers of the given waiver template ID.
        :type template_id: ``string``

        :param from_dts: Limit query to waivers between this ISO 8601 date and the toDts parameter.
        :type from_dts: ``string``

        :param to_dts: Limit query to waivers between this ISO 8601 date and the fromDts parameter.
        :type to_dts: ``string``

        :return: The URL to execute this query for waiver summaries
        :rtype: ``string``
        """

        # Always include the limit, default (same as the API) is 20
        url = SmartwaiverRoutes._base_uri + SmartwaiverRoutes._route_waivers + '?'

        params = {
            'limit': limit
        }

        # Add in other parameters
        if verified is not None:
            params['verified'] = str.lower(str(verified))

        if not template_id == '':
            params['templateId'] = str(template_id)

        if not from_dts == '':
            params['fromDts'] = str(from_dts)

        if not to_dts == '':
            params['toDts'] = str(to_dts)

        return url + urlencode(params)

    @staticmethod
    def get_waiver(waiver_id, pdf=False):
        """Get the URL to retrieve a waiver with the given waiver ID

        :param waiver_id: The Unique identifier of the waiver to retrieve
        :type waiver_id: ``string``

        :param pdf: Whether to include the Base64 Encoded PDF
        :type pdf: ``boolean``

        :return: The URL to retrieve a waiver with the given waiver ID
        :rtype: ``string``
        """

        url = SmartwaiverRoutes._base_uri + SmartwaiverRoutes._route_waivers + '/' + waiver_id
        url += '?pdf=' + str.lower(str(pdf))

        return url

    @staticmethod
    def get_webhook_config():
        """Get the URL to retrieve the current webhook configuration for the account

        :return: The URL to retrieve the current webhook configuration for the account
        :rtype: ``string``
        """
        return SmartwaiverRoutes._base_uri + SmartwaiverRoutes._route_webhooks

    @staticmethod
    def set_webhook_config():
        """Get the URL to set the webhook configuration for the account

        :return: The URL to set the webhook configuration for the account
        :rtype: ``string``
        """
        return SmartwaiverRoutes._base_uri + SmartwaiverRoutes._route_webhooks
