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

class SmartwaiverSDKException(Exception):
    """This class handles all exceptions that have to do with communicating
    with the API and interpreting the responses
    """

    def __init__(self, response, message):
        """Create this type of exception

        :param response: The http response object from the attempted API call
        :type response: requests.Response

        :param message: The message for the exception
        :type message: ``string``
        """

        # Call the base class constructor with the parameters it needs
        super(SmartwaiverSDKException, self).__init__(message)

        # Save the Requests response
        self._response = response

    @property
    def response(self):
        """Returns the response object from the attempted API call

        :return: The response object
        :rtype: requests.Response
        """
        return self._response


class SmartwaiverHTTPException(SmartwaiverSDKException):

    def __init__(self, response, response_info):
        """Create this type of exception. Created a by a successful HTTP
         request to the API server that failed because of a bad route,
         parameter or something else.

        :param response: The Requests response object
        :type response: requests.Response

        :param response_info: The JSON response from the server
        :type response_info: ``dict``
        """

        # Call the base class constructor with the parameters it needs
        super(SmartwaiverHTTPException, self).__init__(response, response_info['message'])

        self._response_info = response_info
        self._status_code = response.status_code

    @property
    def response_info(self):
        """The JSON response information that was given back by the API server
        when it generated the error response.

        :return: The parsed JSON information
        :rtype: ``dict``
        """
        return self._response_info

    @property
    def status_code(self):
        """Returns the status code of the request to the API server

        :return: The status code
        :rtype: ``integer``
        """
        return self._status_code
