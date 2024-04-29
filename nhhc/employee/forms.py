from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Column, Field, Layout, Reset, Row, Submit
from django.forms import ModelForm
from django.forms.widgets import DateInput
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from employee.models import Employee


class EmployeeForm(ModelForm):
    """
    Form definition for Employee Model.

    This form is used to collect and display information about employees. It includes fields for employee details, contact information, emergency contacts, and supporting documentation.

    Attributes:
        model (Employee): The Employee model that this form is based on.
        fields (str): The fields to include in the form.
        labels (dict): Custom labels for specific fields in the form.
    """

    class Meta:
        """Meta definition for EmployeeForm."""

        model = Employee
        fields = "__all__"
        labels = {
            "language": _(
                "Language Preference",
            ),
            "family_hca": _("Check if patient is related by blood or marriage"),
            "qualifications": _(
                "Highest Level of Education/Home Healthcare Qualification",
            ),
            "qualifications_verification": _("Upload Degree, GED or Diploma"),
            "cpr_verification": _("CPR Card"),
            "idoa_agency_policies_attestation": _("Signed IL Dept of Publi Health & Agency Policy"),
            "idph_background_check_authorization": _("Signed Background Check Authorization"),
            "marketing_recruiting_limitations_attestation": _("Signed Marketing and Recruiting Limitation Policy"),
            "do_not_drive_agreement_attestation": _("Signed Do Not Drive Agreement"),
            "job_duties_attestation": _("Signed Job Duties"),
            "dhs_i9": _("Signed Dept of Homeland Security - I9 Form"),
            "hca_policy_attestation": _("Signed HCA Policy"),
            "irs_w4_attestation": _("Signed Federal W4 Form"),
            "state_w4_attestation": _("Signed State W4 Form"),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = reverse("profile")
        self.helper.form_id = "profile"
        self.helper.form_method = "post"
        self.fields["date_of_birth"].widget = DateInput(
            attrs={"type": "date", "class": "form-control"},
        )
        self.helper.layout = Layout(
            HTML(
                """
        <h3 class="small-heading muted-text mb-4">Employee Information</strong></h3>
        <div class="pl-lg-4">
        """,
            ),
            Row(
                Column(Field("username", css_class="", readonly=True), css_class="form-group col-4 mb-0"),
                Column(
                    HTML(
                        """<div class="row">
                 <div class="form-group col-4 mb-0">
                 <label class="form-label">Employee ID Number</label>
                 </div>
                 <div class="col-6">
                 <h5 class="textinput form-control" readonly>{{ employee.employee_id }}</h5>
                 </div>
                 </div> """
                    ),
                    css_class="form-group col-4 mb-0",
                ),
                Column(
                    "email",
                    css_class="form-group col-4 mb-0  editable",
                ),
                css_class="form-row ",
            ),
            Row(
                Column(
                    "first_name",
                    readonly=True,
                    css_class="form-group col-md-4 mb-0  editable",
                ),
                Column(
                    "middle_name",
                    readonly=True,
                    css_class="form-group col-md-4 mb-0  editable",
                ),
                Column(
                    "last_name",
                    readonly=True,
                    css_class="form-group col-md-4 mb-0  editable",
                ),
                css_class="form-row",
            ),
            Row(
                Column(
                    "language",
                    readonly=True,
                    css_class="form-group col-lg-4 mb-0",
                ),
                Column(
                    "ethnicity",
                    readonly=True,
                    css_class="form-group col-lg-4 mb-0",
                ),
                Column(
                    "race",
                    readonly=True,
                    css_class="form-group col-lg-4 mb-0",
                ),
                css_class="form-row ",
            ),
            Row(
                Column("family_hca", css_class="form-group col-md-4 mb-0"),
                Column("qualifications", css_class="form-group col-md-4 mb-0"),
                Column("date_of_birth", css_class="form-group col-md-4 mb-0"),
                css_class="form-row",
            ),
            HTML("""</div> """),
            HTML("""<hr class="my-4 />"""),
            HTML(
                """
        <h3 class="small-heading muted-text mb-4">Contact Information</strong></h3>

        """,
            ),
            Row(
                Column(
                    "street_address1",
                    readonly=True,
                    css_class="form-group col-md-8 mb-0 editable   ",
                ),
                Column(
                    "street_address2",
                    readonly=True,
                    css_class="form-group col-md-4 mb-0 editable",
                ),
                css_class="form-row",
            ),
            Row(
                Column(
                    "city",
                    readonly=True,
                    css_class="form-group col-lg-4 mb-0 editable ",
                ),
                Column(
                    "state",
                    readonly=True,
                    css_class="form-group col-lg-4 mb-0 editable ",
                ),
                Column(
                    "zipcode",
                    readonly=True,
                    css_class="form-group col-lg-4 mb-0 editable ",
                ),
                css_class="form-row",
            ),
            Row(
                Column(
                    "phone",
                    readonly=True,
                    css_class="form-group col-lg-4 mb-0 editable tele-number",
                ),
                Column(
                    "social_security",
                    readonly=True,
                    css_class="form-group col-lg-4 mb-0 editable ",
                ),
                Column(
                    "gender",
                    readonly=True,
                    css_class="form-group col-lg-4 mb-0 editable ",
                ),
                css_class="form-row",
            ),
            HTML("""</div> """),
            HTML("""<hr class="my-4 />"""),
            HTML(
                """
        <h3 class="small-heading muted-text mb-4">Emergency Contact</strong></h3>

        """,
            ),
            Row(
                Column(
                    "emergency_contact_first_name",
                    readonly=True,
                    css_class="form-group col-lg-4 mb-0 editable ",
                ),
                Column(
                    "emergency_contact_last_name",
                    readonly=True,
                    css_class="form-group col-lg-4 mb-0 editable ",
                ),
                Column(
                    "emergency_contact_phone",
                    readonly=True,
                    css_class="form-group col-lg-4 mb-0 editable  tele-number ",
                ),
                Column(
                    "emergency_contact_relationship",
                    readonly=True,
                    css_class="form-group col-lg-12 mb-0 editable ",
                ),
                css_class="form-row",
            ),
            HTML("""<hr class="uk-divider-icon" />"""),
            HTML(
                """
        <h3 class="small-heading muted-text mb-4">Supporting Documentation</strong></h3>

        """,
            ),
            Row(
                Column(
                    "cpr_verification",
                    help_text="Please Upload Photo of an Unexpired CPR Card",
                    css_class="form-group col-lg-4 mb-0 editable ",
                ),
                Column(
                    "qualifications_verification",
                    help_text="Please upload a copy of the document selected in the User Information field - Highest Level of Education/Home Healthcare Qualification",
                    css_class="form-group col-lg-4 mb-0 editable ",
                ),
                Column(
                    "do_not_drive_agreement_attestation",
                    helptext="<Please Provide a Copy of the",
                    css_class="form-group col-lg-4 mb-0 editable ",
                ),
                css_class="form-row",
            ),
            Row(
                Column(
                    "hca_policy_attestation",
                    helptext="Please ....",
                    css_class="form-group col-lg-4 mb-0 editable ",
                ),
                Column(
                    "idph_background_check_authorization",
                    help_text="Please upload a copy of the document selected in the User Information field - Highest Level of Education/Home Healthcare Qualification",
                    css_class="form-group col-lg-4 mb-0 editable ",
                ),
                Column(
                    "job_duties_attestation",
                    help_text="Please upload a copy of signed job duties",
                    css_class="form-group col-lg-4 mb-0 editable ",
                ),
                css_class="form-row",
            ),
            HTML(
                """
        <h3 class="small-heading muted-text mb-4">Payroll and Tax Information</strong></h3>

        """,
            ),
            Row(
                Column(
                    "irs_w4_attestation",
                    helptext="Please ....",
                    css_class="form-group col-lg-4 mb-0 editable ",
                ),
                Column(
                    "state_w4_attestation",
                    help_text="Please upload a copy of the document selected in the User Information field - Highest Level of Education/Home Healthcare Qualification",
                    css_class="form-group col-lg-4 mb-0 editable ",
                ),
                css_class="form-row",
            ),
            HTML(
                """
                             <hr class="uk-divider-icon" />
                             """,
            ),
            Row(
                FormActions(
                    Submit("save", "Save changes", id="edit-button"),
                    Reset(
                        "cancel",
                        "Cancel",
                        css_class="btn btn-danger",
                        id="cancel-edits-btn",
                    ),
                ),
                css_class="form-row",
            ),
        )
