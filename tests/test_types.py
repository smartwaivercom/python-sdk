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

import sys
sys.path.insert(0, '../')

import smartwaiver
import factory


class SmartwaiverCustomFieldTest(unittest.TestCase):

    def test_required_keys(self):

        custom_field_data = factory.custom_field()
        custom_field_data.pop('value')

        with self.assertRaises(ValueError) as cm:

            smartwaiver.types.SmartwaiverCustomField(custom_field_data)

        self.assertEqual('Cannot create a SmartwaiverCustomField with missing field: value', str(cm.exception))

    def test_success(self):

        custom_field_data = factory.custom_field()
        custom_field = smartwaiver.types.SmartwaiverCustomField(custom_field_data)

        self.assertEqual(custom_field_data['value'], custom_field.value)
        self.assertEqual(custom_field_data['displayText'], custom_field.display_text)


class SmartwaiverGuardianTest(unittest.TestCase):

    def test_required_keys(self):

        guardian_data = factory.guardian()
        guardian_data.pop('firstName')

        with self.assertRaises(ValueError) as cm:

            smartwaiver.types.SmartwaiverGuardian(guardian_data)

        self.assertEqual('Cannot create a SmartwaiverGuardian with missing field: firstName', str(cm.exception))

    def test_success(self):

        guardian_data = factory.guardian()
        custom_field = smartwaiver.types.SmartwaiverGuardian(guardian_data)

        self.assertEqual(guardian_data['firstName'], custom_field.first_name)
        self.assertEqual(guardian_data['middleName'], custom_field.middle_name)
        self.assertEqual(guardian_data['lastName'], custom_field.last_name)
        self.assertEqual(guardian_data['phone'], custom_field.phone)
        self.assertEqual(guardian_data['relationship'], custom_field.relationship)


class SmartwaiverParticipantTest(unittest.TestCase):

    def test_required_keys(self):

        participant_data = factory.participant()
        participant_data.pop('firstName')

        with self.assertRaises(ValueError) as cm:

            smartwaiver.types.SmartwaiverParticipant(participant_data)

        self.assertEqual('Cannot create a SmartwaiverParticipant with missing field: firstName', str(cm.exception))

    def test_success(self):

        participant_data = factory.participant()
        participant = smartwaiver.types.SmartwaiverParticipant(participant_data)

        self.assertEqual(participant_data['firstName'], participant.first_name)
        self.assertEqual(participant_data['middleName'], participant.middle_name)
        self.assertEqual(participant_data['lastName'], participant.last_name)
        self.assertEqual(participant_data['dob'], participant.dob)
        self.assertEqual(participant_data['isMinor'], participant.is_minor)
        self.assertEqual(participant_data['gender'], participant.gender)
        self.assertEqual(participant_data['phone'], participant.phone)
        self.assertEqual(participant_data['tags'], participant.tags)

        self.assertTrue(len(participant_data['customParticipantFields']), len(participant.custom_participant_fields))
        for guid in participant.custom_participant_fields:
            self.assertIs(type(participant.custom_participant_fields[guid]), smartwaiver.types.SmartwaiverCustomField)


class SmartwaiverTemplateTest(unittest.TestCase):

    def test_required_keys(self):

        template_data = factory.template()
        template_data.pop('templateId')

        with self.assertRaises(ValueError) as cm:

            smartwaiver.types.SmartwaiverTemplate(template_data)

        self.assertEqual('Cannot create a SmartwaiverTemplate with missing field: templateId', str(cm.exception))

    def test_success(self):

        template_data = factory.template()
        template = smartwaiver.types.SmartwaiverTemplate(template_data)

        self.assertEqual(template_data['templateId'], template.template_id)
        self.assertEqual(template_data['title'], template.title)
        self.assertEqual(template_data['publishedVersion'], template.published_version)
        self.assertEqual(template_data['publishedOn'], template.published_on)
        self.assertEqual(template_data['webUrl'], template.web_url)
        self.assertEqual(template_data['kioskUrl'], template.kiosk_url)


class SmartwaiverTypeTest(unittest.TestCase):

    def test_required_keys(self):

        with self.assertRaises(ValueError) as cm:

            smartwaiver.types.SmartwaiverType({'key1': 'val1'}, ['key1', 'key2'], 'SmartwaiverType')

        self.assertEqual('Cannot create a SmartwaiverType with missing field: key2', str(cm.exception))


class SmartwaiverWaiverSummaryTest(unittest.TestCase):

    def test_required_keys(self):

        waiver_summary_data = factory.waiver_summary()
        waiver_summary_data.pop('waiverId')

        with self.assertRaises(ValueError) as cm:

            smartwaiver.types.SmartwaiverWaiverSummary(waiver_summary_data)

        self.assertEqual('Cannot create a SmartwaiverWaiverSummary with missing field: waiverId', str(cm.exception))

    def test_success(self):

        waiver_summary_data = factory.waiver_summary()
        waiver_summary = smartwaiver.types.SmartwaiverWaiverSummary(waiver_summary_data)

        self.assertEqual(waiver_summary_data['waiverId'], waiver_summary.waiver_id)
        self.assertEqual(waiver_summary_data['templateId'], waiver_summary.template_id)
        self.assertEqual(waiver_summary_data['title'], waiver_summary.title)
        self.assertEqual(waiver_summary_data['createdOn'], waiver_summary.created_on)
        self.assertEqual(waiver_summary_data['expirationDate'], waiver_summary.expiration_date)
        self.assertEqual(waiver_summary_data['expired'], waiver_summary.expired)
        self.assertEqual(waiver_summary_data['verified'], waiver_summary.verified)
        self.assertEqual(waiver_summary_data['kiosk'], waiver_summary.kiosk)
        self.assertEqual(waiver_summary_data['firstName'], waiver_summary.first_name)
        self.assertEqual(waiver_summary_data['middleName'], waiver_summary.middle_name)
        self.assertEqual(waiver_summary_data['lastName'], waiver_summary.last_name)
        self.assertEqual(waiver_summary_data['dob'], waiver_summary.dob)
        self.assertEqual(waiver_summary_data['isMinor'], waiver_summary.is_minor)
        self.assertEqual(waiver_summary_data['tags'], waiver_summary.tags)


class SmartwaiverWaiverTest(unittest.TestCase):

    def test_required_keys(self):

        waiver_data = factory.waiver()
        waiver_data.pop('waiverId')

        with self.assertRaises(ValueError) as cm:

            smartwaiver.types.SmartwaiverWaiver(waiver_data)

        self.assertEqual('Cannot create a SmartwaiverWaiver with missing field: waiverId', str(cm.exception))

    def test_success(self):

        waiver_data = factory.waiver()
        waiver = smartwaiver.types.SmartwaiverWaiver(waiver_data)

        self.assertEqual(waiver_data['waiverId'], waiver.waiver_id)
        self.assertEqual(waiver_data['templateId'], waiver.template_id)
        self.assertEqual(waiver_data['title'], waiver.title)
        self.assertEqual(waiver_data['createdOn'], waiver.created_on)
        self.assertEqual(waiver_data['expirationDate'], waiver.expiration_date)
        self.assertEqual(waiver_data['expired'], waiver.expired)
        self.assertEqual(waiver_data['verified'], waiver.verified)
        self.assertEqual(waiver_data['kiosk'], waiver.kiosk)
        self.assertEqual(waiver_data['firstName'], waiver.first_name)
        self.assertEqual(waiver_data['middleName'], waiver.middle_name)
        self.assertEqual(waiver_data['lastName'], waiver.last_name)
        self.assertEqual(waiver_data['dob'], waiver.dob)
        self.assertEqual(waiver_data['isMinor'], waiver.is_minor)
        self.assertEqual(waiver_data['tags'], waiver.tags)

        self.assertTrue(len(waiver_data['participants']), len(waiver.participants))
        for participant in waiver.participants:
            self.assertIs(type(participant), smartwaiver.types.SmartwaiverParticipant)

        self.assertEqual(waiver_data['email'], waiver.email)
        self.assertEqual(waiver_data['marketingAllowed'], waiver.marketing_allowed)
        self.assertEqual(waiver_data['addressLineOne'], waiver.address_line_one)
        self.assertEqual(waiver_data['addressLineTwo'], waiver.address_line_two)
        self.assertEqual(waiver_data['addressCity'], waiver.address_city)
        self.assertEqual(waiver_data['addressState'], waiver.address_state)
        self.assertEqual(waiver_data['addressZip'], waiver.address_zip)
        self.assertEqual(waiver_data['addressCountry'], waiver.address_country)
        self.assertEqual(waiver_data['emergencyContactName'], waiver.emergency_contact_name)
        self.assertEqual(waiver_data['emergencyContactPhone'], waiver.emergency_contact_phone)
        self.assertEqual(waiver_data['insuranceCarrier'], waiver.insurance_carrier)
        self.assertEqual(waiver_data['insurancePolicyNumber'], waiver.insurance_policy_number)
        self.assertEqual(waiver_data['driversLicenseNumber'], waiver.drivers_license_number)
        self.assertEqual(waiver_data['driversLicenseState'], waiver.drivers_license_state)

        self.assertTrue(len(waiver_data['customWaiverFields']), len(waiver.custom_waiver_fields))
        for guid in waiver.custom_waiver_fields:
            self.assertIs(type(waiver.custom_waiver_fields[guid]), smartwaiver.types.SmartwaiverCustomField)

        self.assertIs(type(waiver.guardian), smartwaiver.types.SmartwaiverGuardian)
        self.assertEqual(waiver_data['pdf'], waiver.pdf)

    def test_participant_not_list(self):

        waiver_data = factory.waiver()
        waiver_data['participants'] = ''

        with self.assertRaises(ValueError) as cm:

            smartwaiver.types.SmartwaiverWaiver(waiver_data)

        self.assertEqual('Participants field must be a list', str(cm.exception))


if __name__ == "__main__":
    unittest.main()
