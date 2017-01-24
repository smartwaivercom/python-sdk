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

from smartwaiver.exceptions import SmartwaiverSDKException


class SmartwaiverType():
    """Base class for all types of returned objects from the API.
    """

    def __init__(self, input, required_keys, smartwaiver_type):
        """Checks that all the required keys for the given object type exist

        :param input: The input dict with all the data
        :type input: ``dict``

        :param required_keys: The required keys in the input
        :type required_keys: ``list``

        :param smartwaiver_type: The name of the Smartwaiver type (for errors)
        :type smartwaiver_type: ``string``
        """

        # Check that all required key's exist in the given input
        for key in required_keys:
            if not key in input:
                raise ValueError('Cannot create a ' + smartwaiver_type + ' with missing field: ' + key)


class SmartwaiverCustomField(SmartwaiverType):
    """This class represents a custom field inside of a signed waiver.
    """

    # The required fields to create this object
    _required_keys = [
        'value',
        'displayText'
    ]

    def __init__(self, field):
        """Create a SmartwaiverCustomField object by providing a dictionary
        with all the required keys.

        :param field:  A dictionary to create the custom field object from
        :type field: ``dict``
        """

        # Check for required keys
        SmartwaiverType.__init__(self, field, self._required_keys, self.__class__.__name__)

        # Load all the information into properties
        self._value = field['value']
        self._display_text = field['displayText']

    @property
    def value(self):
        """Returns the value of the custom waiver field

        :return: Value of the custom waiver field
        :rtype: ``string``
        """
        return self._value

    @property
    def display_text(self):
        """Returns the display text of the custom waiver field

        :return: Display text of the custom waiver field
        :rtype: ``string``
        """
        return self._display_text


class SmartwaiverGuardian(SmartwaiverType):
    """This class represents all the data for the guardian field
    """

    # The required fields to create this object
    _required_keys = [
        'firstName',
        'middleName',
        'lastName',
        'phone',
        'relationship'
    ]

    def __init__(self, guardian):
        """Create a SmartwaiverGuardian object by providing a dictionary with
        all the required keys.

        :param guardian:  A dictionary to create the guardian object from
        :type guardian: ``dict``
        """

        # Check for required keys
        SmartwaiverType.__init__(self, guardian, self._required_keys, self.__class__.__name__)

        # Load all the information into properties
        self._first_name = guardian['firstName']
        self._middle_name = guardian['middleName']
        self._last_name = guardian['lastName']
        self._phone = guardian['phone']
        self._relationship = guardian['relationship']

    @property
    def first_name(self):
        """Returns the first name of the guardian

        :return: First name of the guardian
        :rtype: ``string``
        """
        return self._first_name

    @property
    def middle_name(self):
        """Returns the middle name of the guardian

        :return: Middle name of the guardian
        :rtype: ``string``
        """
        return self._middle_name

    @property
    def last_name(self):
        """Returns the last name of the guardian

        :return: Last name of the guardian
        :rtype: ``string``
        """
        return self._last_name

    @property
    def phone(self):
        """Returns the phone number of the guardian

        :return: Phone number of the guardian
        :rtype: ``string``
        """
        return self._phone

    @property
    def relationship(self):
        """Returns the relationship of the guardian to the minors

        :return: The relationship of the guardian to the minors
        :rtype: ``string``
        """
        return self._relationship


class SmartwaiverParticipant(SmartwaiverType):
    """This class represents a single participant on a signed waiver.
    """

    # The required fields to create this object
    _required_keys = [
        'firstName',
        'middleName',
        'lastName',
        'dob',
        'isMinor',
        'gender',
        'phone',
        'tags',
        'customParticipantFields'
    ]

    def __init__(self, participant):
        """Create a SmartwaiverParticipant object by providing a dictionary
        with all the required keys.

        :param participant:  A dictionary to create the participant object from
        :type participant: ``dict``
        """

        # Check for required keys
        SmartwaiverType.__init__(self, participant, self._required_keys, self.__class__.__name__)

        # Load all the information into properties
        self._first_name = participant['firstName']
        self._middle_name = participant['middleName']
        self._last_name = participant['lastName']
        self._dob = participant['dob']
        self._is_minor = participant['isMinor']
        self._gender = participant['gender']
        self._phone = participant['phone']
        self._tags = participant['tags']

        self._custom_participant_fields = dict()
        # Check that custom participant fields is a dictionary
        if not isinstance(participant['customParticipantFields'], dict):
            raise ValueError('Custom participant fields must be a dictionary')

        # Load the custom participant fields as objects of that type
        for guid in participant['customParticipantFields']:
            self._custom_participant_fields[guid] = SmartwaiverCustomField(participant['customParticipantFields'][guid])

    @property
    def first_name(self):
        """Returns the first name of the participant

        :return: First name of the participant
        :rtype: ``string``
        """
        return self._first_name

    @property
    def middle_name(self):
        """Returns the middle name of the participant

        :return: Middle name of the participant
        :rtype: ``string``
        """
        return self._middle_name

    @property
    def last_name(self):
        """Returns the last name of the participant

        :return: Last name of the participant
        :rtype: ``string``
        """
        return self._last_name

    @property
    def dob(self):
        """Returns the date of birth of the participant (ISO 8601 format)

        :return: DOB of the participant
        :rtype: ``string``
        """
        return self._dob

    @property
    def is_minor(self):
        """Returns whether or not this participant is a minor

        :return: Whether or not this participant is a minor
        :rtype: ``boolean``
        """
        return self._is_minor

    @property
    def gender(self):
        """Returns the gender of the participant

        :return: Gender of the participant
        :rtype: ``string``
        """
        return self._gender

    @property
    def phone(self):
        """Returns the phone number of the participant

        :return: Phone number of the participant
        :rtype: ``string``
        """
        return self._phone

    @property
    def tags(self):
        """Returns a list of tags for this participant

        :return: A list of tags for this participant
        :rtype: ``string``
        """
        return self._tags

    @property
    def custom_participant_fields(self):
        """Returns a list of any custom participant fields on the waiver

        :return: A list of any custom participant fields on the waiver
        :rtype: ``list``
        """
        return self._custom_participant_fields


class SmartwaiverTemplate(SmartwaiverType):
    """This class represents a waiver template response from the API.
    """

    # The required fields to create this object
    _required_keys = [
        'templateId',
        'title',
        'publishedVersion',
        'publishedOn',
        'webUrl',
        'kioskUrl'
    ]

    def __init__(self, template):
        """Checks that all the required keys for the given object type exist

        :param template: A dictionary to create the template object from
        :type template: ``dict``
        """

        # Check for required keys
        SmartwaiverType.__init__(self, template, self._required_keys, self.__class__.__name__)

        # Load all the information into properties
        self._template_id = template['templateId']
        self._title = template['title']
        self._published_version = template['publishedVersion']
        self._published_on = template['publishedOn']
        self._web_url = template['webUrl']
        self._kiosk_url = template['kioskUrl']

    @property
    def template_id(self):
        """Returns the unique identifier of the waiver template

        :return: Unique identifier of the waiver template
        :rtype: ``string``
        """
        return self._template_id

    @property
    def title(self):
        """Returns the title of the waiver template

        :return: Title of the waiver template
        :rtype: ``string``
        """
        return self._title

    @property
    def published_version(self):
        """Returns the current published version of the waiver template

        :return: version of the waiver template
        :rtype: ``integer``
        """
        return self._published_version

    @property
    def published_on(self):
        """Returns the date the waiver template was published

        :return: Date the waiver template was published (ISO 8601 formatted date)
        :rtype: ``string``
        """
        return self._published_on

    @property
    def web_url(self):
        """Returns the URL to access the waiver template

        :return: URL to access the waiver template
        :rtype: ``string``
        """
        return self._web_url

    @property
    def kiosk_url(self):
        """Returns the URL to access the kiosk version of the waiver template

        :return: URL to access the kiosk version of the waiver template
        :rtype: ``string``
        """
        return self._kiosk_url


class SmartwaiverWaiver(SmartwaiverType):
    """This class represents a waiver response from the API.
    """

    # The required fields to create this object
    _required_keys = [
        'waiverId',
        'templateId',
        'title',
        'createdOn',
        'expirationDate',
        'expired',
        'verified',
        'kiosk',
        'firstName',
        'middleName',
        'lastName',
        'dob',
        'isMinor',
        'clientIP',
        'tags',
        'participants',
        'email',
        'marketingAllowed',
        'addressLineOne',
        'addressLineTwo',
        'addressCity',
        'addressState',
        'addressZip',
        'addressCountry',
        'emergencyContactName',
        'emergencyContactPhone',
        'insuranceCarrier',
        'insurancePolicyNumber',
        'driversLicenseNumber',
        'driversLicenseState',
        'customWaiverFields',
        'guardian',
        'pdf'
    ]

    def __init__(self, waiver):
        """Create a SmartwaiverWaiver object by providing a dictionary with all
        the required keys.

        :param waiver:  A dictionary to create the waiver object from
        :type waiver: ``dict``
        """

        # Check for required keys
        SmartwaiverType.__init__(self, waiver, self._required_keys, self.__class__.__name__)

        # Load the waiver summary into into properties
        self._waiver_id = waiver['waiverId']
        self._template_id = waiver['templateId']
        self._title = waiver['title']
        self._created_on = waiver['createdOn']
        self._expiration_date = waiver['expirationDate']
        self._expired = waiver['expired']
        self._verified = waiver['verified']
        self._kiosk = waiver['kiosk']
        self._first_name = waiver['firstName']
        self._middle_name = waiver['middleName']
        self._last_name = waiver['lastName']
        self._dob = waiver['dob']
        self._is_minor = waiver['isMinor']
        self._client_ip = waiver['clientIP']
        self._tags = waiver['tags']

        self._participants = []
        # Check that participants is a list
        if not isinstance(waiver['participants'], list):
            raise ValueError('Participants field must be a list')

        # Load the participants
        for participant in waiver['participants']:
            self._participants.append(SmartwaiverParticipant(participant))

        # Load the waiver data
        self._email = waiver['email']
        self._marketing_allowed = waiver['marketingAllowed']
        self._address_line_one = waiver['addressLineOne']
        self._address_line_two = waiver['addressLineTwo']
        self._address_city = waiver['addressCity']
        self._address_state = waiver['addressState']
        self._address_zip = waiver['addressZip']
        self._address_country = waiver['addressCountry']
        self._emergency_contact_name = waiver['emergencyContactName']
        self._emergency_contact_phone = waiver['emergencyContactPhone']
        self._insurance_carrier = waiver['insuranceCarrier']
        self._insurance_policy_number = waiver['insurancePolicyNumber']
        self._drivers_license_number = waiver['driversLicenseNumber']
        self._drivers_license_state = waiver['driversLicenseState']

        self._custom_waiver_fields = dict()
        # Check that custom wiver fields is a dictionary
        if not isinstance(waiver['customWaiverFields'], dict):
            raise ValueError('Custom waiver fields must be a dictionary')

        # Load the custom waiver fields as objects of that type
        for guid in waiver['customWaiverFields']:
            self._custom_waiver_fields[guid] = SmartwaiverCustomField(waiver['customWaiverFields'][guid])

        # Check if there is a guardian field
        self._guardian = None
        if waiver['guardian'] is not None:
            self._guardian = SmartwaiverGuardian(waiver['guardian'])

        self._pdf = waiver['pdf']

    @property
    def waiver_id(self):
        """Returns the unique identifier of the waiver

        :return: Unique identifier of the waiver
        :rtype: ``string``
        """
        return self._waiver_id

    @property
    def template_id(self):
        """Returns the unique identifier of this waiver's template

        :return: Unique identifier of this waiver's template
        :rtype: ``string``
        """
        return self._template_id

    @property
    def title(self):
        """Returns the title of the waiver

        :return: Title of the waiver
        :rtype: ``string``
        """
        return self._title

    @property
    def created_on(self):
        """Returns the creation date of the waiver

        :return: Creation date of the waiver
        :rtype: ``string``
        """
        return self._created_on

    @property
    def expiration_date(self):
        """Returns the date on which the waiver will expire

        :return: Date on which the waiver will expire
        :rtype: ``string``
        """
        return self._expiration_date

    @property
    def expired(self):
        """Returns whether this waiver is expired

        :return: Whether this waiver is expired
        :rtype: ``boolean``
        """
        return self._expired

    @property
    def verified(self):
        """Returns whether this waiver has been email verified

        :return: Whether this waiver has been email verified
        :rtype: ``boolean``
        """
        return self._verified

    @property
    def kiosk(self):
        """Returns whether this waiver was submitted at a kiosk

        :return: Whether this waiver was submitted at a kiosk
        :rtype: ``boolean``
        """
        return self._kiosk

    @property
    def first_name(self):
        """Returns the first name of the first participant

        :return: First name of the participant
        :rtype: ``string``
        """
        return self._first_name

    @property
    def middle_name(self):
        """Returns the middle name of the first participant

        :return: Middle name of the participant
        :rtype: ``string``
        """
        return self._middle_name

    @property
    def last_name(self):
        """Returns the last name of the first participant

        :return: Last name of the first participant
        :rtype: ``string``
        """
        return self._last_name

    @property
    def dob(self):
        """Returns the date of birth of the first participant (ISO 8601 format)

        :return: DOB of the first participant
        :rtype: ``string``
        """
        return self._dob

    @property
    def is_minor(self):
        """Returns whether or not the first participant is a minor

        :return: Whether or not the first participant is a minor
        :rtype: ``boolean``
        """
        return self._is_minor

    @property
    def client_ip(self):
        """Returns the IP Address from which the waiver submitted

        :return: IP Address from which the waiver submitted
        :rtype: ``string``
        """
        return self._client_ip

    @property
    def tags(self):
        """Returns a list of tags for this participant

        :return: A list of tags for this participant
        :rtype: ``string``
        """
        return self._tags

    @property
    def participants(self):
        """Returns a list of participant's on the waiver

        :return: A list of SmartwaiverParticipant objects
        :rtype: ``list``
        """
        return self._participants

    @property
    def email(self):
        """Returns the email on the waiver

        :return: The email on the waiver
        :rtype: ``string``
        """
        return self._email

    @property
    def marketing_allowed(self):
        """Returns whether the user allows marketing to be sent to their email

        :return: Whether the user allows marketing to be sent to their email
        :rtype: ``boolean``
        """
        return self._marketing_allowed

    @property
    def address_line_one(self):
        """Returns the first line of the address on the waiver

        :return: The first line of the address on the waiver
        :rtype: ``string``
        """
        return self._address_line_one

    @property
    def address_line_two(self):
        """Returns the second line of the address on the waiver

        :return: The second line of the address on the waiver
        :rtype: ``string``
        """
        return self._address_line_two

    @property
    def address_city(self):
        """Returns the city of the address on the waiver

        :return: The city of the address on the waiver
        :rtype: ``string``
        """
        return self._address_city

    @property
    def address_state(self):
        """Returns the state of the address on the waiver

        :return: The state of the address on the waiver
        :rtype: ``string``
        """
        return self._address_state

    @property
    def address_zip(self):
        """Returns the zip code of the address on the waiver

        :return: The zip code of the address on the waiver
        :rtype: ``string``
        """
        return self._address_zip

    @property
    def address_country(self):
        """Returns the country of the address on the waiver

        :return: The country of the address on the waiver
        :rtype: ``string``
        """
        return self._address_country

    @property
    def emergency_contact_name(self):
        """Returns the name of the emergency contact on the waiver

        :return: The name of the emergency contact on the waiver
        :rtype: ``string``
        """
        return self._emergency_contact_name

    @property
    def emergency_contact_phone(self):
        """Returns the phone number of the emergency contact on the waiver

        :return: The phone number of the emergency contact on the waiver
        :rtype: ``string``
        """
        return self._emergency_contact_phone

    @property
    def insurance_carrier(self):
        """Returns the name of the insurance carrier on the waiver

        :return: The name of the insurance carrier on the waiver
        :rtype: ``string``
        """
        return self._insurance_carrier

    @property
    def insurance_policy_number(self):
        """Returns the policy number of the insurance on the waiver

        :return: The policy number of the insurance on the waiver
        :rtype: ``string``
        """
        return self._insurance_policy_number

    @property
    def drivers_license_number(self):
        """Returns the number of the drivers license on the waiver

        :return: The number of the drivers license on the waiver
        :rtype: ``string``
        """
        return self._drivers_license_number

    @property
    def drivers_license_state(self):
        """Returns the state of the drivers license on the waiver

        :return: The state of the drivers license on the waiver
        :rtype: ``string``
        """
        return self._drivers_license_state

    @property
    def custom_waiver_fields(self):
        """Returns a dictionary of any custom waiver fields on the waiver

        :return: The dictionary of any custom waiver fields on the waiver
        :rtype: ``dict``
        """
        return self._custom_waiver_fields

    @property
    def guardian(self):
        """If there are only minors on the waiver, this field contains the guardian information, otherwise it's None

        :return: The guardian information, or none
        :rtype: ``SmartwaiverGuardian``
        """
        return self._guardian

    @property
    def pdf(self):
        """Returns the list of tags for this participant

        :return: The list of tags for this participant
        :rtype: ``string``
        """
        return self._pdf


class SmartwaiverWaiverSummary(SmartwaiverType):
    """This class represents a waiver summary response from the API. These are
    found in the waiver list call.
    """

    # The required fields to create this object
    _required_keys = [
        'waiverId',
        'templateId',
        'title',
        'createdOn',
        'expirationDate',
        'expired',
        'verified',
        'kiosk',
        'firstName',
        'middleName',
        'lastName',
        'dob',
        'isMinor',
        'tags'
    ]

    def __init__(self, waiver_summary):
        """Create a SmartwaiverWaiverSummary object by providing a dictionary
        with all the required keys.

        :param waiver_summary:  A dictionary to create the waiver_summary object from
        :type waiver_summary: ``dict``
        """

        # Check for required keys
        SmartwaiverType.__init__(self, waiver_summary, self._required_keys, self.__class__.__name__)

        # Load all the information into properties
        self._waiver_id = waiver_summary['waiverId']
        self._template_id = waiver_summary['templateId']
        self._title = waiver_summary['title']
        self._created_on = waiver_summary['createdOn']
        self._expiration_date = waiver_summary['expirationDate']
        self._expired = waiver_summary['expired']
        self._verified = waiver_summary['verified']
        self._kiosk = waiver_summary['kiosk']
        self._first_name = waiver_summary['firstName']
        self._middle_name = waiver_summary['middleName']
        self._last_name = waiver_summary['lastName']
        self._dob = waiver_summary['dob']
        self._is_minor = waiver_summary['isMinor']
        self._tags = waiver_summary['tags']

    @property
    def waiver_id(self):
        """Returns the unique identifier of the waiver

        :return: Unique identifier of the waiver
        :rtype: ``string``
        """
        return self._waiver_id

    @property
    def template_id(self):
        """Returns the unique identifier of this waiver's template

        :return: Unique identifier of this waiver's template
        :rtype: ``string``
        """
        return self._template_id

    @property
    def title(self):
        """Returns the title of the waiver

        :return: Title of the waiver
        :rtype: ``string``
        """
        return self._title

    @property
    def created_on(self):
        """Returns the creation date of the waiver

        :return: Creation date of the waiver
        :rtype: ``string``
        """
        return self._created_on

    @property
    def expiration_date(self):
        """Returns the date on which the waiver will expire

        :return: Date on which the waiver will expire
        :rtype: ``string``
        """
        return self._expiration_date

    @property
    def expired(self):
        """Returns whether this waiver is expired

        :return: Whether this waiver is expired
        :rtype: ``boolean``
        """
        return self._expired

    @property
    def verified(self):
        """Returns whether this waiver has been email verified

        :return: Whether this waiver has been email verified
        :rtype: ``boolean``
        """
        return self._verified

    @property
    def kiosk(self):
        """Returns whether this waiver was submitted at a kiosk

        :return: Whether this waiver was submitted at a kiosk
        :rtype: ``boolean``
        """
        return self._kiosk

    @property
    def first_name(self):
        """Returns the first name of the first participant

        :return: First name of the participant
        :rtype: ``string``
        """
        return self._first_name

    @property
    def middle_name(self):
        """Returns the middle name of the first participant

        :return: Middle name of the participant
        :rtype: ``string``
        """
        return self._middle_name

    @property
    def last_name(self):
        """Returns the last name of the first participant

        :return: Last name of the first participant
        :rtype: ``string``
        """
        return self._last_name

    @property
    def dob(self):
        """Returns the date of birth of the first participant (ISO 8601 format)

        :return: DOB of the first participant
        :rtype: ``string``
        """
        return self._dob

    @property
    def is_minor(self):
        """Returns whether or not the first participant is a minor

        :return: Whether or not the first participant is a minor
        :rtype: ``boolean``
        """
        return self._is_minor

    @property
    def tags(self):
        """Returns a list of tags for this participant

        :return: A list of tags for this participant
        :rtype: ``string``
        """
        return self._tags


class SmartwaiverWebhook(SmartwaiverType):
    """This class represents a a webhook configuration.
    """

    # The required fields to create this object
    _required_keys = [
        'endpoint',
        'emailValidationRequired'
    ]

    # Represents the setting for webhooks only being sent after email
    # verification has occurred
    WEBHOOK_AFTER_EMAIL_ONLY = 'yes'

    # Represents the setting for webhooks being sent right after waiver is
    # signed
    WEBHOOK_BEFORE_EMAIL_ONLY = 'no'

    # Represents the setting for webhooks being sent both before email
    # verification has occurred and after
    WEBHOOK_BEFORE_AND_AFTER_EMAIL = 'both'

    def __init__(self, webhook):
        """Create a SmartwaiverWebhook object by providing a dictionary with
        all the required keys.

        :param webhook:  A dictionary to create the webhook object from
        :type webhook: ``dict``
        """

        # Check for required keys
        SmartwaiverType.__init__(self, webhook, self._required_keys, self.__class__.__name__)

        # Load all the information into properties
        self._endpoint = webhook['endpoint']
        self._email_validation_required = webhook['emailValidationRequired']

    @property
    def endpoint(self):
        """Returns the URL for the webhook

        :return: The URL for the webhook
        :rtype: ``string``
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, value):
        """Returns the URL for the webhook

        :param value: The URL for the webhook
        :type value: ``string``
        """
        self._endpoint = value

    @property
    def email_validation_required(self):
        """Returns the setting for when webhooks will be sent, use constants for this setting

        :return: Whether the webhooks are sent only after email: (yes, no, or both)
        :rtype: ``string``
        """
        return self._email_validation_required

    @email_validation_required.setter
    def email_validation_required(self, value):
        """Change the setting for when webhooks will be sent, use constants for this setting

        :param value: Whether the webhooks are sent only after email: (yes, no, or both)
        :type value: ``string``
        """
        self._email_validation_required = value
