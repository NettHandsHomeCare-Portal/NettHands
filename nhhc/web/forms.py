"""
Module: Form Module
Description: This module contains the form definitions for the ClientInterestForm and EmploymentApplicationForm.

ClientInterestForm:
- This form is used for capturing client interest submissions.
- It includes fields for first name, last name, contact number, email, zipcode, insurance carrier, desired service, and captcha.

EmploymentApplicationForm:
- This form is used for capturing employment applications.
- It includes fields for basic information, relevant experience, work availability, and captcha.

Both forms utilize the ReCaptchaField for added security.

"""


from captcha.fields import ReCaptchaField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Column, Field, Layout, Row, Submit
from django import forms
from django.utils.translation import gettext_lazy as _
from web.models import ClientInterestSubmission, EmploymentApplicationModel


class ClientInterestForm(forms.ModelForm):
    """Form definition for ClientInterestSubmission."""

    captcha = ReCaptchaField()

    def __init__(self, *args, **kwargs):  # pragma: no cover
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.attrs = {"autocomplete": "off", "form_id": "employment-application"}
        self.fields["captcha"].label = False

        self.helper.layout = Layout(
            HTML("""<h3 class="application-text">Patient Information</h3>"""),
            Row(
                Column("first_name", css_class="form-group col-md-6 mb-0"),
                Column("last_name", css_class="form-group col-md-6 mb-0"),
                css_class="form-row",
            ),
            Row(
                Column("contact_number", css_class="form-group col-md-6 mb-0"),
                Column("email", css_class="form-group col-md-6 mb-0"),
                css_class="form-row",
            ),
            Row(
                Column("home_address1", css_class="form-group col-8"),
                Column("home_address2", css_class="form-group col-4"),
                css_class="form-row",
            ),
            Row(
                Column("city", css_class="form-group col-md-6 mb-0"),
                Column("state", css_class="form-group col-md-4 mb-0"),
                Column("zipcode", css_class="form-group col-md-2 mb-0"),
                css_class="form-row ",
            ),
            HTML("""<h3 class="application-text">Service Information</h3>"""),
            Row(
                Column("insurance_carrier", css_class="form-group col-md-6 mb-0"),
                Column("desired_service", css_class="form-group col-md-6 mb-0"),
                css_class="form-row",
            ),
            Field("captcha", placeholder="Enter captcha"),
            Submit("submit", "Submit Application"),
        )

    class Meta:
        """Meta definition for ClientInterestSubmissionform."""

        model = ClientInterestSubmission
        fields = (
            "first_name",
            "last_name",
            "contact_number",
            "home_address1",
            "home_address2",
            "city",
            "zipcode",
            "state",
            "email",
            "zipcode",
            "insurance_carrier",
            "desired_service",
            "captcha",
        )
        labels = {
            "home_address2": _("Unit/Apartment"),
            "home_address1": _("Street Address"),
        }


class EmploymentApplicationForm(forms.ModelForm):
    """Form definition for EmploymentApplicationModel."""

    captcha = ReCaptchaField()

    def __init__(self, *args, **kwargs):  # pragma: no cover
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.attrs = {"autocomplete": "off"}
        self.fields["captcha"].label = False

        self.helper.layout = Layout(
            HTML(
                """
        <h3 class="application-text">Basic Information</strong></h3>""",
            ),
            Row(
                Column("first_name", css_class="form-group col-md-6 mb-0"),
                Column("last_name", css_class="form-group col-md-6 mb-0"),
                css_class="form-row",
            ),
            Row(
                Column("contact_number", css_class="form-group col-md-6 mb-0"),
                Column("email", css_class="form-group col-md-6 mb-0"),
                css_class="form-row",
            ),
            Row(
                Column("home_address1", css_class="form-group col-8"),
                Column("home_address2", css_class="form-group col-4"),
                css_class="form-row",
            ),
            Row(
                Column("city", css_class="form-group col-md-6 mb-0"),
                Column("state", css_class="form-group col-md-4 mb-0"),
                Column("zipcode", css_class="form-group col-md-2 mb-0"),
                css_class="form-row ",
            ),
            HTML(
                """<h3 class="application-text">Relevant Experience</h3>""",
            ),
            Row(
                Column("mobility", css_class="form-group col-md-6 mb-0"),
                Column("prior_experience", css_class="form-group col-md-6 mb-0"),
                css_class="form-row",
            ),
            Row(
                Column("ipdh_registered", css_class="form-group col-md-12 mb-0"),
                css_class="form-row",
            ),
            HTML(
                """<h3 class="application-text">Work Availability</h3>""",
            ),
            Row(
                Column("availability_monday", css_class="form-group col-md-3 mb-0"),
                Column("availability_tuesday", css_class="form-group col-md-3 mb-0"),
                Column("availability_wednesday", css_class="form-group col-md-3 mb-0"),
                Column("availability_thursday", css_class="form-group col-md-3 mb-0"),
                css_class="form-row",
            ),
            Row(
                Column("availability_friday", css_class="form-group col-md-3 mb-0"),
                Column("availability_saturday", css_class="form-group col-md-3 mb-0"),
                Column("availability_sunday", css_class="form-group col-md- mb-0"),
                css_class="form-row",
            ),
            Field("captcha", placeholder="Enter captcha"),
            Submit("submit", "Submit Application"),
        )

    class Meta:
        """Meta definition for EmploymentApplicationModelForm."""

        model = EmploymentApplicationModel
        fields = (
            "first_name",
            "last_name",
            "contact_number",
            "email",
            "home_address1",
            "home_address2",
            "city",
            "state",
            "zipcode",
            "mobility",
            "ipdh_registered",
            "prior_experience",
            "availability_monday",
            "availability_tuesday",
            "availability_wednesday",
            "availability_thursday",
            "availability_friday",
            "availability_saturday",
            "availability_sunday",
            "captcha",
        )
        labels = {
            "ipdh_registered": _(
                "Currently Registered With the IPDH Health Care Worker Registry",
            ),
            "availability_monday": _("Monday"),
            "availability_tuesday": _("Tuesday"),
            "availability_wednesday": _("Wednesday"),
            "availability_thursday": _("Thursday"),
            "availability_friday": _("Friday"),
            "availability_saturday": _("Saturday"),
            "availability_sunday": _("Sunday"),
            "home_address2": _("Unit/Apartment"),
            "home_address1": _("Street Address"),
        }
