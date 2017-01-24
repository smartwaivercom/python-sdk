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

from smartwaiver import exceptions


class SmartwaiverResponse:
    """This class processes general information for all HTTP responses from the API
    server. Version, Unique ID, and Timestamp information for every request are
    stored in this class.
    """

    # Mapping from response type to key in JSON object containing data
    _response_types = {
        'templates': 'templates',
        'template': 'template',
        'waivers': 'waivers',
        'waiver': 'waiver',
        'webhooks': 'webhooks'
    }

    # Required keys in the all response's from the server
    _required_keys = [
        'version',
        'id',
        'ts',
        'type'
    ]

    def __init__(self, response):
        self._response = response

        # Try to get the json
        error_message = ''
        contents = {}
        try:
            contents = response.json()
        except ValueError as err:
            error_message = str(err)

        if error_message is not '':
            raise exceptions.SmartwaiverSDKException(response, 'Malformed JSON response from API server')

        # Check that all required key's exist in the response
        for key in self._required_keys:
            if key not in contents:
                raise exceptions.SmartwaiverSDKException(response, 'API server response missing expected field: ' + key)

        # Pull out generic response information
        self._version = contents['version']
        self._id = contents['id']
        self._ts = contents['ts']
        self._type = contents['type']

        # Check HTTP response code for problems
        success = [200, 201]
        error = [400, 401, 402, 404, 405, 406, 500]

        if response.status_code in success:
            # Check that the response type is in our type mappings
            if self._type in self._response_types:
                # Check that the fields with the data is there
                if self._type in contents:
                    # Save the response data
                    self._response_data = contents[self._response_types[self._type]]
                else:
                    raise exceptions.SmartwaiverSDKException(response, 'JSON response does not contain field of type: "' + str(self._type) + '"')
            else:
                raise exceptions.SmartwaiverSDKException(response, 'JSON response contains unknown type: "' + str(self._type) + '"')
        elif response.status_code in error:
            if 'message' in contents:
                raise exceptions.SmartwaiverHTTPException(response, contents)
            else:
                raise exceptions.SmartwaiverSDKException(response, 'Error response does not include message')
        else:
            raise exceptions.SmartwaiverSDKException(response, 'Unknown HTTP code returned: ' + str(response.status_code))

    @property
    def version(self):
        """Returns the version of the API this response came from.

        :return: The API version
        :rtype: ``integer``
        """
        return self._version

    @property
    def id(self):
        """Returns a unique identifier of the response, useful for debugging

        :return: The UUID of the request
        :rtype: ``string``
        """
        return self._id

    @property
    def ts(self):
        """Returns the timestamp of when the response was created

        :return: The timestamp (ISO 8601 format)
        :rtype: ``string``
        """
        return self._ts

    @property
    def type(self):
        """Returns what type of response this is: error, templates, waiver, webhooks, etc.

        :return: The type of response
        :rtype: ``string``
        """
        return self._type

    @property
    def response_data(self):
        """Returns the particular response data according to the type specified

        :return: The response data
        :rtype: list, dict
        """
        return self._response_data

    @property
    def response(self):
        """Returns the :class:`Response <Response>` object that this response was created from

        :return: The :class:`Response <Response>` object underlying this cobject
        :rtype: requests.Response
        """
        return self._response


class SmartwaiverRawResponse:
    """This class provides a simple response from the API server containing the
    status code and raw body.
    """

    def __init__(self, response):

        self._body = response.text
        self._status_code = response.status_code

    @property
    def status_code(self):
        """Returns the status code of the HTTP request to the API server

        :return: The status code
        :rtype: ``integer``
        """
        return self._status_code

    @property
    def body(self):
        """Returns the raw unprocessed body of the response from the server

        :return: The response body
        :rtype: ``string``
        """
        return self._body
