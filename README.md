![](https://d362q4tvy1elxj.cloudfront.net/header_logoheader.png)

PYTHON-SDK
==========

Table of Contents
=================

  * [Table of contents](#table-of-contents)
  * [Installation](#installation)
  * [Getting Started](#getting-started)
    * [Retrieve a Specific Template](#retrieve-a-specific-template)
    * [List all Signed Waivers](#list-all-signed-waivers)
    * [Retrieve a Specific Waiver](#retrieve-a-specific-waiver)
    * [Retrieve/Set Webhook Config](#retrieveset-webhook-configuration)
  * [Exception Handling](#exception-handling)
    * [Status Codes](#status-codes)
  * [Advanced](#advanced)
    * [Raw Responses](#raw-responses)
    * [URL Generation](#url-generation)
    * [Authentication](#authentication)
  * [API Documentaion](#api-documentation)
    * [smartwaiver.Smartwaiver](#smartwaiversmartwaiver)
    * [smartwaiver.SmartwaiverRoutes](#smartwaiversmartwaiverroutes)
    * [smartwaiver.exceptions.SmartwaiverHTTPException](#smartwaiverexceptionssmartwaiverhttpexception)
    * [smartwaiver.exceptions.SmartwaiverSDKException](#smartwaiverexceptionssmartwaiversdkexception)
    * [smartwaiver.responses.SmartwaiverRawResponse](#smartwaiverresponsessmartwaiverrawresponse)
    * [smartwaiver.responses.SmartwaiverResponse](#smartwaiverresponsessmartwaiverresponse)
    * [smartwaiver.types.SmartwaiverCustomField](#smartwaivertypessmartwaivercustomfield)
    * [smartwaiver.types.SmartwaiverGuardian](#smartwaivertypessmartwaiverguardian)
    * [smartwaiver.types.SmartwaiverParticipant](#smartwaivertypessmartwaiverparticipant)
    * [smartwaiver.types.SmartwaiverTemplate](#smartwaivertypessmartwaivertemplate)
    * [smartwaiver.types.SmartwaiverType](#smartwaivertypessmartwaivertype)
    * [smartwaiver.types.SmartwaiverWaiver](#smartwaivertypessmartwaiverwaiver)
    * [smartwaiver.types.SmartwaiverWaiverSummary](#smartwaivertypessmartwaiverwaiversummary)
    * [smartwaiver.types.SmartwaiverWebhook](#smartwaivertypessmartwaiverwebhook)

Installation
==========

This SDK requires Python >3.

    pip install smartwaiver-sdk

Alternatively, you can clone the repository, but you must have the Python [Requests](http://docs.python-requests.org/en/master/) library installed:

    git clone https://www.github.com/smartwaivercom/python-sdk

Getting Started
==========

All that is required to start using the SDK is a Smartwaiver account and the API Key for that account.
In all of the examples you will need to put the API Key into the code wherever it says: `[INSERT API KEY]`

It's time to start making requests.
A good first request is to list all waiver templates for your account.
Here is the code to do that:

```python
# The API Key for your account
api_key = '[INSERT API KEY]'

# Set up your Smartwaiver connection using your API Key
sw = smartwaiver.Smartwaiver(api_key)

# Get a list of all templates
templates = sw.get_waiver_templates()
```

That's it! You've just requested all waiver templates in your account.
But, now it's time to do something with them.
Let's loop through those templates and print out the ID and Title of each template:

```python
for template in templates:
    print(template.template_id + ': ' + template.title)
```

Awesome! For more details on all the different properties a waiver template has, check out [template_properties.py](examples/templates/template_properties.py)

Now that you've got your first request, check out the sections below to accomplish specific actions.

Retrieve a Specific Template
---------

First let's set up the basic Smartwaiver object.
Make sure to put in your account's API Key where it says `[INSERT API KEY]`

```python
# The API Key for your account
api_key = '[INSERT API KEY]'

# Set up your Smartwaiver connection using your API Key
sw = smartwaiver.Smartwaiver(api_key)
```

Now we can request information about a specific template.
To do this we need the template ID.
If you don't know a template ID for your account, try listing all waiver templates for you account, as shown [here](#getting-started), and copying one of the ID's that is printed out.
Once we have a template ID we can execute a request to get the information about the template:

```python
# The unique identifier of the template to retrieve
template_id = '[INSERT TEMPLATE ID]'

# Retrieve a specific template (SmartwaiverTemplate object)
template = sw.get_waiver_template(template_id)
```

Now let's print out some information about this template.

```python
# Access properties of the template
print('\nList single template:\n')
print(template.template_id + ': ' + template.title)
```

To see all the different properties a waiver template has, check out [template_properties.py](examples/templates/template_properties.py)

List All Signed Waivers
----------

First let's set up the basic Smartwaiver object. Make sure to put in your account's API Key where it says `[INSERT API KEY]`

```python
# The API Key for your account
api_key = '[INSERT API KEY]'

# Set up your Smartwaiver connection using your API Key
sw = smartwaiver.Smartwaiver(api_key)
```

Now we can request signed waivers from your account.

```python
# Get a list of recent signed waivers for this account
summaries = sw.get_waiver_summaries()
```

With this done, we can iterate over the returned summaries to see what is stored.
The default limit is 20, which means if you have more than 20 in your account, only the most recent 20 will be returned

```python
# List waiver ID and title for each summary returned
print('List all waivers:\n')
for summary in summaries:
    print(summary.waiver_id + ': ' + summary.title)
```

To see all the different properties a waiver summary has, check out [waiver_summary_properties.py](examples/waivers/waiver_summary_properties.py)

Once we have a waiver summary, we can access all the detailed information about the waiver. To do that look [here](#retrieve-a-specific-waiver).

But, we can also restrict our query with some parameters.
For example, what if we only want to return 5 waivers, (the default is 20).
Here is the code to do that:

```python
# Limit number of waivers returned to twenty (Allowed values: 1-100)
limit = 20

# Get a list of summaries of waivers
waiver_summaries = sw.get_waiver_summaries(limit)
```

Or what if we only want any waivers that have not been verified (either by email or at the kiosk)?

```python
# Limit number of waivers returned to twenty (Allowed values: 1-100)
limit = 20

# Do not care about whether the waiver has been verified by email or not (Allowed values: true, false, None)
verified = None

# Get a list of summaries of waivers
waiver_summaries = sw.get_waiver_summaries(limit, verified)
```

What other parameters can you use? Here is an example using all of them:

```python
# Limit number returned to 5
limit = 5

# Limit only to waivers that were signed at a kiosk or verified over email
verified = True

# Limit query to waivers of this template ID
template_id = '[INSERT TEMPLATE ID]'

# Limit to waivers signed in November of 2016
from_dts = datetime(2016, 11, 1, tzinfo=timezone.utc).isoformat()
to_dts = datetime(2016, 12, 1, tzinfo=timezone.utc).isoformat()

waiver_summaries = sw.get_waiver_summaries(limit, verified, template_id, from_dts, to_dts)
```

These examples are also available in [list_all_waivers.py](examples/waivers/list_all_waivers.py)

###Parameter Options

| Parameter Name | Default Value | Accepted Values   | Notes                                                                                 |
| -------------- | ------------- | ----------------- | ------------------------------------------------------------------------------------- |
| limit          | 20            | 1 - 100           | Limit number of returned waivers                                                      |
| verified       | None          | true/false/None   | Limit selection to waiver that have been verified (true), not (false), or both (None) |
| templateId     |               | Valid Template ID | Limit signed waivers to only this template                                            |
| fromDts        |               | ISO 8601 Date     | Limit to signed waivers between from and to dates (requires toDts)                    |
| toDts          |               | ISO 8601 Date     | Limit to signed waivers between from and to dates (requires fromDts)                  |

Retrieve a Specific Waiver
----------

What if we want to retrieve a specific waiver?
All we need for that is a waiver ID.
If you don't have a waiver ID to use, you can get a list of signed waivers in your account [here](#list-all-signed-waivers)

First let's set up the basic Smartwaiver object. Make sure to put in your account's API Key where it says `[INSERT API KEY]`

```python
# The API Key for your account
api_key = '[INSERT API KEY]'

# Set up your Smartwaiver connection using your API Key
sw = smartwaiver.Smartwaiver(api_key)
```

Now, we can request the information about a specific waiver.
Make sure to put your waiver ID in where it says `[INSERT WAIVER ID]`

```python
# The unique ID of the signed waiver to be retrieved
waiver_id = '[INSERT WAIVER ID]'

# Get the waiver object
waiver = sw.get_waiver(waiver_id)
```

The waiver object has many different properties that can be accessed.
For example, we can print out the waiver ID and title of the waiver.

```python
# Access properties of the waiver
print('List single waiver:')
print(waiver.waiver_id + ': ' + waiver.title)
```

To see a full list of all properties that a waiver object contains, check out [waiver_properties.py](examples/waivers/waiver_properties.py)

We can also request that the PDF of the signed waiver as a Base 64 Encoded string be included. Here is the request to do that:

```python
# The unique ID of the signed waiver to be retrieved
waiver_id = '[INSERT WAIVER ID]'

# Optionally include the Base64 encoded PDF
$pdf = true;

# Get the waiver object
waiver = sw.get_waiver(waiver_id, pdf)
```

The code provided here is also combined in to one example in [retrieve_single_waiver.py](examples/waivers/retrieve_single_waiver.py)

Retrieve/Set Webhook Configuration
----------

You can both retrieve and set your account's webhook configuration through this SDK with a couple simple calls.
To view your current webhook settings, we first need to set a Smartwaiver object.
Make sure to put in your account's API Key where it says `[INSERT API KEY]`

```python
# The API Key for your account
api_key = '[INSERT API KEY]'

# Set up your Smartwaiver connection using your API Key
sw = smartwaiver.Smartwaiver(api_key)
```

Now, it's easy to request the webhook configuration:

```python
# Get the current webhook settings
webhooks = sw.get_webhook_config()
```

And, now we can print out the information:

```python
# Access the webhook config
print('Endpoint: ' + webhooks.endpoint)
print('Email Validation Required: ' + webhooks.email_validation_required)
```

The Email Validation Required is whether the webhook will fire before, after, or before and after a waiver is verified.
The endpoint is simply the endpoint URL for the webhook.

And changing your webhook configuration is just as easy.
The new configuration will be returned from the request and can be access just like the read request above.

```python
# The new values to set
endpoint = 'http://testing.example.org'
email_validation_required = smartwaiver.types.SmartwaiverWebhook.WEBHOOK_AFTER_EMAIL_ONLY

# Set the webhook to new values
webhook = sw.set_webhook_config(endpoint, email_validation_required)

# Access the new webhook config
print('Successfully set new configuration.')
print('Endpoint: ' + webhook.endpoint)
print('Email Validation Required: ' + webhook.email_validation_required)
```

This code is also provided in [retrieve_webhooks.py](examples/webhooks/retrieve_webhooks.py)
and [set_webhooks.py](examples/webhooks/set_webhooks.py)

Exception Handling
==========

Exceptions in this SDK are grouped into two different types.
 * A <b>SmartwaiverSDKException</b> occurs when the SDK itself encounters a problem.
Examples of this include problems connecting to the API server, an unexpected response from the API server, bad input data, etc.
 * A <b>SmartwaiverHTTPException</b> occurs when the API encounters an error and properly relays that information back.
   Examples of this include '401 Unauthorized' or '404 Not Found' errors.

Note that <b>SmartwaiverHTTPException</b> is a type of <b>SmartwaiverSDKException</b> so it is possible to catch all possible exceptions at the same time.
Usually you will only need to handle HTTP exceptions.

Here is an example of catching an HTTP exception. First we set up the Smartwaiver account:

```python
# The API Key for your account
api_key = '[INSERT API KEY]'

# Set up your Smartwaiver connection using your API Key
sw = smartwaiver.Smartwaiver(api_key)
```

Next, we attempt to get a waiver that does not exist:

```python
# The Waiver ID to access
waiver_id = 'InvalidWaiverId'

# Try to get the waiver object
waiver = sw.get_waiver(waiver_id)
```

This will throw an exception because a waiver with that ID does not exist. So let's change the code to catch that exception:

```python
try:
    # Try to get the waiver object
    waiver = sw.get_waiver(waiver_id)
except smartwaiver.exceptions.SmartwaiverHTTPException:
    print('Error retrieving waiver from API server...\n')
```

But there is lot's of useful information in the exception object. Let's print some of that out too:

```python
try:
    # Try to get the waiver object
    waiver = sw.get_waiver(waiver_id)
except smartwaiver.exceptions.SmartwaiverHTTPException as err:
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
```

The code provided here is also combined in to one example in [exception_handling.py](examples/intro/exception_handling.py)

Status Codes
----------

The code of the exception will match the HTTP Status Code of the response and the message will be an informative string informing on what exactly was wrong with the request.

Possible status codes and their meanings:

| Status Code | Error Name            | Description                                                                                                                       |
| ----------- | --------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| 400         | Parameter Error       | Indicates that something was wrong with the parameters of the request (e.g. extra parameters, missing required parameters, etc.). |
| 401         | Unauthorized          | Indicates the request was missing an API Key or contained an invalid API Key.                                                     |
| 402         | Data Error            | Indicates that the parameters of the request was valid, but the data in those parameters was not.                                 |
| 404         | Not Found             | Indicates that whatever was being searched for (specific waiver, etc.) could not be found.                                        |
| 406         | Wrong Content Type    | Indicates that the Content Type of the request is inapproriate for the request.                                                   |
| 500         | Internal Server Error | Indicates that the server encountered an internal error while processing the request.                                             |

Advanced
==========

This section contains notes about several more ways to use the SDK that are slightly more low level.

Raw Responses
----------
If you do not wish to use the Smartwaiver object types to facilitate easy use of the data you can also access the raw response from the API server.

Here is an example of getting the raw response from the server for retrieving a list of waiver summaries:

```python
# The API Key for your account
api_key = '[INSERT API KEY]'

# Set up your Smartwaiver connection using your API Key
sw = smartwaiver.Smartwaiver(api_key)

# Get a list of all signed waivers for this account
response = sw.get_waiver_summaries_raw()

# The response object has two properties, status code and response body
print('Status Code: ' + str(response.status_code))
print('Body: ' + response.body)
```

All the standard methods have a 'Raw' counterpart that just has '_raw' added to the function name.

The code provided here is also in [raw_responses.py](examples/advanced/raw_responses.py)

URL Generation
----------

If you would like handle all aspects of the request's yourself, you can simply use <b>SmartwaiverRoutes</b> class to generate the approriate URLs for your requests.

For example, to create the URL to list all templates is only one line:

```python
smartwaiver.SmartwaiverRoutes.get_waiver_templates()
```

For the list of possible routes see the [API Docs](https://api.smartwaiver.com/docs/v4/)

Note: to use this you must handle the proper authentication headers yourself.

Authentication
----------

If you are making custom requests you must include the proper authentication.
The Smartwaiver API expects a header called 'sw-api-key' to contain the API for the account you are accessing.

    sw-api-key: [INSERT API KEY]

If you do not have a Smartwaiver API key go [here](https://www.smartwaiver.com/p/API) to find out how to create one.

API Documentation
=================

smartwaiver.Smartwaiver
-----------------------

    class Smartwaiver(builtins.object)
     |
     |  __init__(self, api_key)
     |      Creates a new Smartwaiver object.
     |
     |      :param api_key: The API Key for the account
     |      :type api_key: ``string``
     |
     |  get_waiver(self, waiver_id, pdf=False)
     |      Get a specific waiver by the unique identifier
     |
     |      :param waiver_id: The Unique identifier of the waiver to retrieve
     |      :type waiver_id: ``string``
     |
     |      :param pdf: Whether to include the Base64 Encoded PDF
     |      :type pdf: ``boolean``
     |
     |      :return: The :class:`SmartwaiverWaiver` object that represents the waiver
     |      :rtype: smartwaiver.types.SmartwaiverWaiver
     |
     |  get_waiver_raw(self, waiver_id, pdf=False)
     |      Get a specific waiver by the unique identifier (raw version)
     |
     |      :param waiver_id: The Unique identifier of the waiver to retrieve
     |      :type waiver_id: ``string``
     |
     |      :param pdf: Whether to include the Base64 Encoded PDF
     |      :type pdf: ``boolean``
     |
     |      :return: The raw body and status code of the response from the server
     |      :rtype: smartwaiver.responses.SmartwaiverRawResponse
     |
     |  get_waiver_summaries(self, limit=20, verified=None, template_id='', from_dts='', to_dts='')
     |      Execute a query to find waivers, the returned objects will be waiver summaries
     |
     |      :param limit: Limit query to this number of the most recent waivers.
     |      :type limit: ``integer``
     |
     |      :param verified: Limit query to verified by email (true) or not verified (false) or both (None).
     |      :type verified: ``boolean``
     |
     |      :param template_id: Limit query to signed waivers of the given waiver template ID.
     |      :type template_id: ``string``
     |
     |      :param from_dts: Limit query to waivers between this ISO 8601 date and the toDts parameter.
     |      :type from_dts: ``string``
     |
     |      :param to_dts: Limit query to waivers between this ISO 8601 date and the fromDts parameter.
     |      :type to_dts: ``string``
     |
     |      :return: A list of :class:`SmartwaiverWaiverSummary` object's that represent the waivers.
     |      :rtype: ``list``
     |
     |  get_waiver_summaries_raw(self, limit=20, verified=None, template_id='', from_dts='', to_dts='')
     |      Execute a query to find waivers, the returned objects will be waiver summaries (raw version)
     |
     |      :param limit: Limit query to this number of the most recent waivers.
     |      :type limit: ``integer``
     |
     |      :param verified: Limit query to verified by email (true) or not verified (false) or both (None).
     |      :type verified: ``boolean``
     |
     |      :param template_id: Limit query to signed waivers of the given waiver template ID.
     |      :type template_id: ``string``
     |
     |      :param from_dts: Limit query to waivers between this ISO 8601 date and the toDts parameter.
     |      :type from_dts: ``string``
     |
     |      :param to_dts: Limit query to waivers between this ISO 8601 date and the fromDts parameter.
     |      :type to_dts: ``string``
     |
     |      :return: The raw body and status code of the response from the server
     |      :rtype: smartwaiver.responses.SmartwaiverRawResponse
     |
     |  get_waiver_template(self, template_id)
     |      Get a specific waiver template by providing the unique identifier
     |
     |      :param template_id: The unique identifier of the specific waiver template
     |      :type template_id: ``string``
     |
     |      :return: The :class:`SmartwaiverTemplate` object that represents the waiver template
     |      :rtype: smartwaiver.types.SmartwaiverTemplate
     |
     |  get_waiver_template_raw(self, template_id)
     |      Get a specific waiver template by providing the unique identifier (raw version)
     |
     |      :param template_id: The unique identifier of the specific waiver template
     |      :type template_id: ``string``
     |
     |      :return: The raw body and status code of the response from the server
     |      :rtype: smartwaiver.responses.SmartwaiverRawResponse
     |
     |  get_waiver_templates(self)
     |      Get a list of waiver templates for this account
     |
     |      :return: The :class:`SmartwaiverTemplate` object that represents the waiver template
     |      :rtype: smartwaiver.types.SmartwaiverTemplate
     |
     |  get_waiver_templates_raw(self)
     |      Get a list of waiver templates for this account (raw version)
     |
     |      :return: The raw body and status code of the response from the server
     |      :rtype: smartwaiver.responses.SmartwaiverRawResponse
     |
     |  get_webhook_config(self)
     |      Get your account's current webhook configuration
     |
     |      :return: The new webhook settings
     |      :rtype: smartwaiver.types.SmartwaiverWebhook
     |
     |  get_webhook_config_raw(self)
     |      Get your account's current webhook configuration (raw version)
     |
     |      :return: The raw body and status code of the response from the server
     |      :rtype: smartwaiver.responses.SmartwaiverRawResponse
     |
     |  set_webhook(self, webhook)
     |      Set your account's webhook configuration
     |
     |      :param webhook: The webhook settings to send to the API server
     |      :type webhook: smartwaiver.types.SmartwaiverWebhook
     |
     |      :return: The new webhook settings
     |      :rtype: smartwaiver.types.SmartwaiverWebhook
     |
     |  set_webhook_config(self, endpoint, email_validation_required)
     |      Set your account's webhook configuration
     |
     |      :param endpoint: The URL endpoint for the webhook
     |      :type endpoint: ``string``
     |
     |      :param email_validation_required: When to send the webhook, see :class:`SmartwaiverWebhook` for constants to use
     |      :type email_validation_required: ``string``
     |
     |      :return: The new webhook settings
     |      :rtype: smartwaiver.types.SmartwaiverWebhook
     |
     |  set_webhook_config_raw(self, endpoint, email_validation_required)
     |      Set your account's webhook configuration (raw version)
     |
     |      :param endpoint: The URL endpoint for the webhook
     |      :type endpoint: ``string``
     |
     |      :param email_validation_required: When to send the webhook, see :class:`SmartwaiverWebhook` for constants to use
     |      :type email_validation_required: ``string``
     |
     |      :return: The raw body and status code of the response from the server
     |      :rtype: smartwaiver.responses.SmartwaiverRawResponse
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  last_response
     |      Get the SmartwaiverResponse objected created for the most recent API
     |      request. Useful for error handling if an exception is thrown.
     |
     |      :return: The last response this object received from the API
     |      :rtype: smartwaiver.responses.SmartwaiverResponse

smartwaiver.SmartwaiverRoutes
-----------------------------

    class SmartwaiverRoutes(builtins.object)
     |  This class provides and easy way to create the actual URLs for the
     |  routes.
     |
     |  Static methods defined here:
     |
     |  get_waiver(waiver_id, pdf=False)
     |      Get the URL to retrieve a waiver with the given waiver ID
     |
     |      :param waiver_id: The Unique identifier of the waiver to retrieve
     |      :type waiver_id: ``string``
     |
     |      :param pdf: Whether to include the Base64 Encoded PDF
     |      :type pdf: ``boolean``
     |
     |      :return: The URL to retrieve a waiver with the given waiver ID
     |      :rtype: ``string``
     |
     |  get_waiver_summaries(limit=20, verified=None, template_id='', from_dts='', to_dts='')
     |      Return the URL to execute the query for waiver summaries
     |
     |      :param limit: Limit query to this number of the most recent waivers.
     |      :type limit: ``integer``
     |
     |      :param verified: Limit query to verified by email (true) or not verified (false) or both (None).
     |      :type verified: ``boolean``
     |
     |      :param template_id: Limit query to signed waivers of the given waiver template ID.
     |      :type template_id: ``string``
     |
     |      :param from_dts: Limit query to waivers between this ISO 8601 date and the toDts parameter.
     |      :type from_dts: ``string``
     |
     |      :param to_dts: Limit query to waivers between this ISO 8601 date and the fromDts parameter.
     |      :type to_dts: ``string``
     |
     |      :return: The URL to execute this query for waiver summaries
     |      :rtype: ``string``
     |
     |  get_waiver_template(template_id)
     |      Return the URL to get a specific waiver template
     |
     |      :param template_id: The unique identifier of the specific waiver template
     |      :type template_id: ``string``
     |
     |      :return: The URL to get a specific waiver template
     |      :rtype: ``string``
     |
     |  get_waiver_templates()
     |      Returns the URL to get waiver templates
     |
     |      :return: The URL to get waiver templates
     |      :rtype: ``string``
     |
     |  get_webhook_config()
     |      Get the URL to retrieve the current webhook configuration for the account
     |
     |      :return: The URL to retrieve the current webhook configuration for the account
     |      :rtype: ``string``
     |
     |  set_webhook_config()
     |      Get the URL to set the webhook configuration for the account
     |
     |      :return: The URL to set the webhook configuration for the account
     |      :rtype: ``string``

smartwaiver.exceptions.SmartwaiverHTTPException
-----------------------------------------------
    
    class SmartwaiverHTTPException(SmartwaiverSDKException)
     |  This class handles all exceptions that have to do with communicating
     |  with the API and interpreting the responses
     |  
     |  __init__(self, response, response_info)
     |      Create this type of exception. Created a by a successful HTTP
     |       request to the API server that failed because of a bad route,
     |       parameter or something else.
     |      
     |      :param response: The Requests response object
     |      :type response: requests.Response
     |      
     |      :param response_info: The JSON response from the server
     |      :type response_info: ``dict``
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  response_info
     |      The JSON response information that was given back by the API server
     |      when it generated the error response.
     |      
     |      :return: The parsed JSON information
     |      :rtype: ``dict``
     |  
     |  status_code
     |      Returns the status code of the request to the API server
     |      
     |      :return: The status code
     |      :rtype: ``integer``
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from SmartwaiverSDKException:
     |  
     |  response
     |      Returns the response object from the attempted API call
     |      
     |      :return: The response object
     |      :rtype: requests.Response

smartwaiver.exceptions.SmartwaiverSDKException
----------------------------------------------

    class SmartwaiverSDKException(builtins.Exception)
     |  This class handles all exceptions that have to do with communicating
     |  with the API and interpreting the responses
     |  
     |  __init__(self, response, message)
     |      Create this type of exception
     |      
     |      :param response: The http response object from the attempted API call
     |      :type response: requests.Response
     |      
     |      :param message: The message for the exception
     |      :type message: ``string``
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  response
     |      Returns the response object from the attempted API call
     |      
     |      :return: The response object
     |      :rtype: requests.Response

smartwaiver.responses.SmartwaiverRawResponse
--------------------------------------------
    
    class SmartwaiverRawResponse(builtins.object)
     |  This class provides a simple response from the API server containing the
     |  status code and raw body.
     |  
     |  __init__(self, response)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  body
     |      Returns the raw unprocessed body of the response from the server
     |      
     |      :return: The response body
     |      :rtype: ``string``
     |  
     |  status_code
     |      Returns the status code of the HTTP request to the API server
     |      
     |      :return: The status code
     |      :rtype: ``integer``

smartwaiver.responses.SmartwaiverResponse
-----------------------------------------

    class SmartwaiverResponse(builtins.object)
     |  This class processes general information for all HTTP responses from the API
     |  server. Version, Unique ID, and Timestamp information for every request are
     |  stored in this class.
     |  
     |  __init__(self, response)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  id
     |      Returns a unique identifier of the response, useful for debugging
     |      
     |      :return: The UUID of the request
     |      :rtype: ``string``
     |  
     |  response
     |      Returns the :class:`Response <Response>` object that this response was created from
     |      
     |      :return: The :class:`Response <Response>` object underlying this cobject
     |      :rtype: requests.Response
     |  
     |  response_data
     |      Returns the particular response data according to the type specified
     |      
     |      :return: The response data
     |      :rtype: list, dict
     |  
     |  ts
     |      Returns the timestamp of when the response was created
     |      
     |      :return: The timestamp (ISO 8601 format)
     |      :rtype: ``string``
     |  
     |  type
     |      Returns what type of response this is: error, templates, waiver, webhooks, etc.
     |      
     |      :return: The type of response
     |      :rtype: ``string``
     |  
     |  version
     |      Returns the version of the API this response came from.
     |      
     |      :return: The API version
     |      :rtype: ``integer``

smartwaiver.types.SmartwaiverCustomField
----------------------------------------
    
    class SmartwaiverCustomField(SmartwaiverType)
     |  This class represents a custom field inside of a signed waiver.
     |  
     |  __init__(self, field)
     |      Create a SmartwaiverCustomField object by providing a dictionary
     |      with all the required keys.
     |      
     |      :param field:  A dictionary to create the custom field object from
     |      :type field: ``dict``
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  display_text
     |      Returns the display text of the custom waiver field
     |      
     |      :return: Display text of the custom waiver field
     |      :rtype: ``string``
     |  
     |  value
     |      Returns the value of the custom waiver field
     |      
     |      :return: Value of the custom waiver field
     |      :rtype: ``string``

smartwaiver.types.SmartwaiverGuardian
-------------------------------------

    class SmartwaiverGuardian(SmartwaiverType)
     |  This class represents all the data for the guardian field
     |  
     |  __init__(self, guardian)
     |      Create a SmartwaiverGuardian object by providing a dictionary with
     |      all the required keys.
     |      
     |      :param guardian:  A dictionary to create the guardian object from
     |      :type guardian: ``dict``
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  first_name
     |      Returns the first name of the guardian
     |      
     |      :return: First name of the guardian
     |      :rtype: ``string``
     |  
     |  last_name
     |      Returns the last name of the guardian
     |      
     |      :return: Last name of the guardian
     |      :rtype: ``string``
     |  
     |  middle_name
     |      Returns the middle name of the guardian
     |      
     |      :return: Middle name of the guardian
     |      :rtype: ``string``
     |  
     |  phone
     |      Returns the phone number of the guardian
     |      
     |      :return: Phone number of the guardian
     |      :rtype: ``string``
     |  
     |  relationship
     |      Returns the relationship of the guardian to the minors
     |      
     |      :return: The relationship of the guardian to the minors
     |      :rtype: ``string``

smartwaiver.types.SmartwaiverParticipant
----------------------------------------
    
    class SmartwaiverParticipant(SmartwaiverType)
     |  This class represents a single participant on a signed waiver.
     |  
     |  __init__(self, participant)
     |      Create a SmartwaiverParticipant object by providing a dictionary
     |      with all the required keys.
     |      
     |      :param participant:  A dictionary to create the participant object from
     |      :type participant: ``dict``
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  custom_participant_fields
     |      Returns a list of any custom participant fields on the waiver
     |      
     |      :return: A list of any custom participant fields on the waiver
     |      :rtype: ``list``
     |  
     |  dob
     |      Returns the date of birth of the participant (ISO 8601 format)
     |      
     |      :return: DOB of the participant
     |      :rtype: ``string``
     |  
     |  first_name
     |      Returns the first name of the participant
     |      
     |      :return: First name of the participant
     |      :rtype: ``string``
     |  
     |  gender
     |      Returns the gender of the participant
     |      
     |      :return: Gender of the participant
     |      :rtype: ``string``
     |  
     |  is_minor
     |      Returns whether or not this participant is a minor
     |      
     |      :return: Whether or not this participant is a minor
     |      :rtype: ``boolean``
     |  
     |  last_name
     |      Returns the last name of the participant
     |      
     |      :return: Last name of the participant
     |      :rtype: ``string``
     |  
     |  middle_name
     |      Returns the middle name of the participant
     |      
     |      :return: Middle name of the participant
     |      :rtype: ``string``
     |  
     |  phone
     |      Returns the phone number of the participant
     |      
     |      :return: Phone number of the participant
     |      :rtype: ``string``
     |  
     |  tags
     |      Returns a list of tags for this participant
     |      
     |      :return: A list of tags for this participant
     |      :rtype: ``string``

smartwaiver.types.SmartwaiverTemplate
-------------------------------------
    
    class SmartwaiverTemplate(SmartwaiverType)
     |  This class represents a waiver template response from the API.
     |  
     |  __init__(self, template)
     |      Checks that all the required keys for the given object type exist
     |      
     |      :param template: A dictionary to create the template object from
     |      :type template: ``dict``
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  kiosk_url
     |      Returns the URL to access the kiosk version of the waiver template
     |      
     |      :return: URL to access the kiosk version of the waiver template
     |      :rtype: ``string``
     |  
     |  published_on
     |      Returns the date the waiver template was published
     |      
     |      :return: Date the waiver template was published (ISO 8601 formatted date)
     |      :rtype: ``string``
     |  
     |  published_version
     |      Returns the current published version of the waiver template
     |      
     |      :return: version of the waiver template
     |      :rtype: ``integer``
     |  
     |  template_id
     |      Returns the unique identifier of the waiver template
     |      
     |      :return: Unique identifier of the waiver template
     |      :rtype: ``string``
     |  
     |  title
     |      Returns the title of the waiver template
     |      
     |      :return: Title of the waiver template
     |      :rtype: ``string``
     |  
     |  web_url
     |      Returns the URL to access the waiver template
     |      
     |      :return: URL to access the waiver template
     |      :rtype: ``string``

smartwaiver.types.SmartwaiverType
---------------------------------
    
    class SmartwaiverType(builtins.object)
     |  Base class for all types of returned objects from the API.
     |  
     |  __init__(self, input, required_keys, smartwaiver_type)
     |      Checks that all the required keys for the given object type exist
     |      
     |      :param input: The input dict with all the data
     |      :type input: ``dict``
     |      
     |      :param required_keys: The required keys in the input
     |      :type required_keys: ``list``
     |      
     |      :param smartwaiver_type: The name of the Smartwaiver type (for errors)
     |      :type smartwaiver_type: ``string``

smartwaiver.types.SmartwaiverWaiver
-----------------------------------

    class SmartwaiverWaiver(SmartwaiverType)
     |  This class represents a waiver response from the API.
     |  
     |  __init__(self, waiver)
     |      Create a SmartwaiverWaiver object by providing a dictionary with all
     |      the required keys.
     |      
     |      :param waiver:  A dictionary to create the waiver object from
     |      :type waiver: ``dict``
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  address_city
     |      Returns the city of the address on the waiver
     |      
     |      :return: The city of the address on the waiver
     |      :rtype: ``string``
     |  
     |  address_country
     |      Returns the country of the address on the waiver
     |      
     |      :return: The country of the address on the waiver
     |      :rtype: ``string``
     |  
     |  address_line_one
     |      Returns the first line of the address on the waiver
     |      
     |      :return: The first line of the address on the waiver
     |      :rtype: ``string``
     |  
     |  address_line_two
     |      Returns the second line of the address on the waiver
     |      
     |      :return: The second line of the address on the waiver
     |      :rtype: ``string``
     |  
     |  address_state
     |      Returns the state of the address on the waiver
     |      
     |      :return: The state of the address on the waiver
     |      :rtype: ``string``
     |  
     |  address_zip
     |      Returns the zip code of the address on the waiver
     |      
     |      :return: The zip code of the address on the waiver
     |      :rtype: ``string``
     |  
     |  client_ip
     |      Returns the IP Address from which the waiver submitted
     |      
     |      :return: IP Address from which the waiver submitted
     |      :rtype: ``string``
     |  
     |  created_on
     |      Returns the creation date of the waiver
     |      
     |      :return: Creation date of the waiver
     |      :rtype: ``string``
     |  
     |  custom_waiver_fields
     |      Returns a dictionary of any custom waiver fields on the waiver
     |      
     |      :return: The dictionary of any custom waiver fields on the waiver
     |      :rtype: ``dict``
     |  
     |  dob
     |      Returns the date of birth of the first participant (ISO 8601 format)
     |      
     |      :return: DOB of the first participant
     |      :rtype: ``string``
     |  
     |  drivers_license_number
     |      Returns the number of the drivers license on the waiver
     |      
     |      :return: The number of the drivers license on the waiver
     |      :rtype: ``string``
     |  
     |  drivers_license_state
     |      Returns the state of the drivers license on the waiver
     |      
     |      :return: The state of the drivers license on the waiver
     |      :rtype: ``string``
     |  
     |  email
     |      Returns the email on the waiver
     |      
     |      :return: The email on the waiver
     |      :rtype: ``string``
     |  
     |  emergency_contact_name
     |      Returns the name of the emergency contact on the waiver
     |      
     |      :return: The name of the emergency contact on the waiver
     |      :rtype: ``string``
     |  
     |  emergency_contact_phone
     |      Returns the phone number of the emergency contact on the waiver
     |      
     |      :return: The phone number of the emergency contact on the waiver
     |      :rtype: ``string``
     |  
     |  expiration_date
     |      Returns the date on which the waiver will expire
     |      
     |      :return: Date on which the waiver will expire
     |      :rtype: ``string``
     |  
     |  expired
     |      Returns whether this waiver is expired
     |      
     |      :return: Whether this waiver is expired
     |      :rtype: ``boolean``
     |  
     |  first_name
     |      Returns the first name of the first participant
     |      
     |      :return: First name of the participant
     |      :rtype: ``string``
     |  
     |  guardian
     |      If there are only minors on the waiver, this field contains the guardian information, otherwise it's None
     |      
     |      :return: The guardian information, or none
     |      :rtype: ``SmartwaiverGuardian``
     |  
     |  insurance_carrier
     |      Returns the name of the insurance carrier on the waiver
     |      
     |      :return: The name of the insurance carrier on the waiver
     |      :rtype: ``string``
     |  
     |  insurance_policy_number
     |      Returns the policy number of the insurance on the waiver
     |      
     |      :return: The policy number of the insurance on the waiver
     |      :rtype: ``string``
     |  
     |  is_minor
     |      Returns whether or not the first participant is a minor
     |      
     |      :return: Whether or not the first participant is a minor
     |      :rtype: ``boolean``
     |  
     |  kiosk
     |      Returns whether this waiver was submitted at a kiosk
     |      
     |      :return: Whether this waiver was submitted at a kiosk
     |      :rtype: ``boolean``
     |  
     |  last_name
     |      Returns the last name of the first participant
     |      
     |      :return: Last name of the first participant
     |      :rtype: ``string``
     |  
     |  marketing_allowed
     |      Returns whether the user allows marketing to be sent to their email
     |      
     |      :return: Whether the user allows marketing to be sent to their email
     |      :rtype: ``boolean``
     |  
     |  middle_name
     |      Returns the middle name of the first participant
     |      
     |      :return: Middle name of the participant
     |      :rtype: ``string``
     |  
     |  participants
     |      Returns a list of participant's on the waiver
     |      
     |      :return: A list of SmartwaiverParticipant objects
     |      :rtype: ``list``
     |  
     |  pdf
     |      Returns the list of tags for this participant
     |      
     |      :return: The list of tags for this participant
     |      :rtype: ``string``
     |  
     |  tags
     |      Returns a list of tags for this participant
     |      
     |      :return: A list of tags for this participant
     |      :rtype: ``string``
     |  
     |  template_id
     |      Returns the unique identifier of this waiver's template
     |      
     |      :return: Unique identifier of this waiver's template
     |      :rtype: ``string``
     |  
     |  title
     |      Returns the title of the waiver
     |      
     |      :return: Title of the waiver
     |      :rtype: ``string``
     |  
     |  verified
     |      Returns whether this waiver has been email verified
     |      
     |      :return: Whether this waiver has been email verified
     |      :rtype: ``boolean``
     |  
     |  waiver_id
     |      Returns the unique identifier of the waiver
     |      
     |      :return: Unique identifier of the waiver
     |      :rtype: ``string``

smartwaiver.types.SmartwaiverWaiverSummary
------------------------------------------
    
    class SmartwaiverWaiverSummary(SmartwaiverType)
     |  This class represents a waiver summary response from the API. These are
     |  found in the waiver list call.
     |  
     |  __init__(self, waiver_summary)
     |      Create a SmartwaiverWaiverSummary object by providing a dictionary
     |      with all the required keys.
     |      
     |      :param waiver_summary:  A dictionary to create the waiver_summary object from
     |      :type waiver_summary: ``dict``
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  created_on
     |      Returns the creation date of the waiver
     |      
     |      :return: Creation date of the waiver
     |      :rtype: ``string``
     |  
     |  dob
     |      Returns the date of birth of the first participant (ISO 8601 format)
     |      
     |      :return: DOB of the first participant
     |      :rtype: ``string``
     |  
     |  expiration_date
     |      Returns the date on which the waiver will expire
     |      
     |      :return: Date on which the waiver will expire
     |      :rtype: ``string``
     |  
     |  expired
     |      Returns whether this waiver is expired
     |      
     |      :return: Whether this waiver is expired
     |      :rtype: ``boolean``
     |  
     |  first_name
     |      Returns the first name of the first participant
     |      
     |      :return: First name of the participant
     |      :rtype: ``string``
     |  
     |  is_minor
     |      Returns whether or not the first participant is a minor
     |      
     |      :return: Whether or not the first participant is a minor
     |      :rtype: ``boolean``
     |  
     |  kiosk
     |      Returns whether this waiver was submitted at a kiosk
     |      
     |      :return: Whether this waiver was submitted at a kiosk
     |      :rtype: ``boolean``
     |  
     |  last_name
     |      Returns the last name of the first participant
     |      
     |      :return: Last name of the first participant
     |      :rtype: ``string``
     |  
     |  middle_name
     |      Returns the middle name of the first participant
     |      
     |      :return: Middle name of the participant
     |      :rtype: ``string``
     |  
     |  tags
     |      Returns a list of tags for this participant
     |      
     |      :return: A list of tags for this participant
     |      :rtype: ``string``
     |  
     |  template_id
     |      Returns the unique identifier of this waiver's template
     |      
     |      :return: Unique identifier of this waiver's template
     |      :rtype: ``string``
     |  
     |  title
     |      Returns the title of the waiver
     |      
     |      :return: Title of the waiver
     |      :rtype: ``string``
     |  
     |  verified
     |      Returns whether this waiver has been email verified
     |      
     |      :return: Whether this waiver has been email verified
     |      :rtype: ``boolean``
     |  
     |  waiver_id
     |      Returns the unique identifier of the waiver
     |      
     |      :return: Unique identifier of the waiver
     |      :rtype: ``string``

smartwaiver.types.SmartwaiverWebhook
------------------------------------
    
    class SmartwaiverWebhook(SmartwaiverType)
     |  This class represents a a webhook configuration.
     |  
     |  __init__(self, webhook)
     |      Create a SmartwaiverWebhook object by providing a dictionary with
     |      all the required keys.
     |      
     |      :param webhook:  A dictionary to create the webhook object from
     |      :type webhook: ``dict``
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  email_validation_required
     |      Returns the setting for when webhooks will be sent, use constants for this setting
     |      
     |      :return: Whether the webhooks are sent only after email: (yes, no, or both)
     |      :rtype: ``string``
     |  
     |  endpoint
     |      Returns the URL for the webhook
     |      
     |      :return: The URL for the webhook
     |      :rtype: ``string``
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  WEBHOOK_AFTER_EMAIL_ONLY = 'yes'
     |  
     |  WEBHOOK_BEFORE_AND_AFTER_EMAIL = 'both'
     |  
     |  WEBHOOK_BEFORE_EMAIL_ONLY = 'no'
