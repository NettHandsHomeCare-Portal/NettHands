from pprint import pprint

import arrow
from django.test import TestCase
from employee.models import Employee
from faker import Faker
from loguru import logger
from model_bakery import baker
from web.models import ClientInterestSubmissions, EmploymentApplicationModel

from nhhc.utils.testing import (
    generate_mock_PhoneNumberField,
    generate_mock_ZipCodeField,
)

dummy = Faker()
baker.generators.add("phonenumber_field.modelfields.PhoneNumberField", generate_mock_PhoneNumberField)
baker.generators.add("localflavor.us.models.USZipCodeField", generate_mock_ZipCodeField)


class TestClientInterestSubmissions(TestCase):
    def setup(self):
        pass

    def test__str__(self):
        string_of_class = baker.make(
            ClientInterestSubmissions,
            last_name="Brooks",
            first_name="Test",
            date_submitted=str(arrow.now(tz="local").format("YYYY-MM-DD hh:mm:ss")),
        )
        self.assertEqual(
            string_of_class.__str__(),
            f"Brooks, Test - Submission Date: {str(arrow.now(tz='local').format('YYYY-MM-DD'))}",
        )

    def test_marked_reviewed(self):
        reviewed_submission = baker.make(ClientInterestSubmissions)
        reviewer = baker.make(Employee)
        reviewed_submission.marked_reviewed(user_id=reviewer)
        assert reviewed_submission.reviewed == True
        assert reviewed_submission.reviewed_by is not None


class TestEmploymentApplicationModel(TestCase):
    def test__str__(self):
        string_of_class = baker.make(
            EmploymentApplicationModel,
            id=1,
            last_name="Suite",
            first_name="EmploymentApplicationModel",
            date_submitted=str(arrow.now(tz="local").format("YYYY-MM-DD hh:mm:ss")),
        )
        self.assertEqual(
            string_of_class.__str__(),
            f"Suite, EmploymentApplicationModel (1) - Submission Date: {arrow.now().format('YYYY-MM-DD')}",
        )

    def test_hire_applicant(self):
        mock_number = generate_mock_PhoneNumberField()
        mock_zipcode = generate_mock_ZipCodeField()
        new_empoloyee = baker.make(
            EmploymentApplicationModel,
            last_name="test",
            first_name="new_employee",
            contact_number=mock_number,
            email="Dev@gmail.com",
            home_address1="1 North World Trade Tower",
            home_address2="15th Floor",
            city="Manhattan",
            state="NY",
            zipcode=mock_zipcode,
            mobility="C",
            prior_experience="J",
            ipdh_registered=True,
            availability_monday=True,
            availability_tuesday=False,
            availability_wednesday=True,
            availability_thursday=True,
            availability_friday=True,
            availability_saturday=False,
        )
        hiring_manager = baker.make(Employee)
        new_empoloyee.hire_applicant(hired_by=hiring_manager)

        self.assertTrue(new_empoloyee.reviewed)
        self.assertTrue(new_empoloyee.hired)
        self.assertEqual(new_empoloyee.reviewed_by, hiring_manager)

    def test_reject_applicant(self):
        rejected_applicant = baker.make(
            EmploymentApplicationModel,
            last_name="test",
            first_name="rejected_applicant",
        )
        hiring_manager = baker.make(Employee)
        rejected_applicant.reject_applicant(rejected_by=hiring_manager)

        self.assertTrue(rejected_applicant.reviewed)
        self.assertFalse(rejected_applicant.hired)
        self.assertEqual(rejected_applicant.reviewed_by, hiring_manager)
