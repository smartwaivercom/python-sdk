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
from smartwaiver.exceptions import SmartwaiverHTTPException

# The API Key for your account
api_key = '[INSERT API KEY]'

# The Waiver ID to access
waiver_id = 'InvalidWaiverId'

# Set up your Smartwaiver connection using your API Key
sw = smartwaiver.Smartwaiver(api_key)

try:
    # Try to get the waiver object
    waiver = sw.get_waiver(waiver_id)
except SmartwaiverHTTPException as err:
    # SmartwaiverHTTPException will be thrown for any errors returned by the
    # API in a RESTful way.
    # Examples include: 404 Not Found, 401 Not Authorized, etc.
    print('Error retrieving waiver from API server...\n')

    # The code will be the HTTP Status Code returned
    print('Error Code: ' + str(err.status_code))

    # The message will be informative about what was wrong with the request
    print('Error Message: ' + err.response_info['message'] + '\n')

    # Also included in the exception is the header information returned about
    # the response.
    print('API Version: ' + str(err.response_info['version']))
    print('UUID: ' + err.response_info['id'])
    print('Timestamp: ' + err.response_info['ts'])
