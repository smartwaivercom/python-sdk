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

# The new values to set
endpoint = 'http://example.org'
email_validation_required = smartwaiver.types.SmartwaiverWebhook.WEBHOOK_AFTER_EMAIL_ONLY

# Set the webhook to new values
webhook = sw.set_webhook_config(endpoint, email_validation_required)

# Access the new webhook config
print('Successfully set new configuration.')
print('Endpoint: ' + webhook.endpoint)
print('Email Validation Required: ' + webhook.email_validation_required)

# You can also just provide a SmartwaiverWebhook object to set the new values
webhook.endpoint = 'http://testing.example.org'
webhook.email_validation_required = smartwaiver.types.SmartwaiverWebhook.WEBHOOK_BEFORE_AND_AFTER_EMAIL

new_webhook = sw.set_webhook(webhook)

print('\nSuccessfully set new configuration.')
print('Endpoint: ' + new_webhook.endpoint)
print('Email Validation Required: ' + new_webhook.email_validation_required)
