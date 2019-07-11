# coding: utf-8

"""
    Avaza API Documentation

    Welcome to the autogenerated documentation & test tool for Avaza's API. <br/><br/><strong>API Security & Authentication</strong><br/>Authentication options include OAuth2 Implicit and Authorization Code flows, and Personal Access Token. All connections should be encrypted over SSL/TLS <br/><br/>You can set up and manage your api authentication credentials from within your Avaza account. (requires Administrator permissions on your Avaza account).<br/><br/> OAuth2 Authorization endpoint: https://any.avaza.com/oauth2/authorize  <br/>OAuth2 Token endpoint: https://any.avaza.com/oauth2/token<br/>Base URL for subsequent API Requests: https://api.avaza.com/ <br/><br/>Blogpost about authenticating with Avaza's API:  https://www.avaza.com/avaza-api-oauth2-authentication/ <br/>Blogpost on using Avaza's webhooks: https://www.avaza.com/avaza-api-webhook-notifications/<br/>The OAuth flow currently issues Access Tokens that last 1 day, and Refresh tokens that last 180 days<br/>The Api respects the security Roles assigned to the authenticating Avaza user and filters the data return appropriately. <br/><br><strong>Support</strong><br/>For API Support, and to request access please contact Avaza Support Team via our support chat. <br/><br/><strong>User Contributed Libraries:</strong><br/>Graciously contributed by 3rd party users like you. <br/>Note these are not tested or endorsesd by Avaza. We encourage you to review before use, and use at own risk.<br/> <ul><li> - <a target='blank' href='https://packagist.org/packages/debiprasad/oauth2-avaza'>PHP OAuth Client Package for Azava API (by Debiprasad Sahoo)</a></li></ul>  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TimesheetDetails(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'timesheet_entry_id': 'int',
        'user_idfk': 'int',
        'firstname': 'str',
        'lastname': 'str',
        'email': 'str',
        'project_idfk': 'int',
        'project_title': 'str',
        'customer_idfk': 'int',
        'customer_name': 'str',
        'timesheet_category_idfk': 'int',
        'category_name': 'str',
        'duration': 'float',
        'timesheet_entry_approval_status_code': 'str',
        'has_timer': 'bool',
        'timer_started_at_utc': 'datetime',
        'is_billable': 'bool',
        'is_invoiced': 'bool',
        'entry_date': 'datetime',
        'start_time_local': 'datetime',
        'start_time_utc': 'datetime',
        'end_time_local': 'datetime',
        'end_time_utc': 'datetime',
        'timesheet_user_time_zone': 'str',
        'notes': 'str',
        'task_idfk': 'int',
        'task_title': 'str',
        'invoice_idfk': 'int',
        'invoice_line_item_idfk': 'int',
        'date_created': 'datetime',
        'date_updated': 'datetime'
    }

    attribute_map = {
        'timesheet_entry_id': 'TimesheetEntryID',
        'user_idfk': 'UserIDFK',
        'firstname': 'Firstname',
        'lastname': 'Lastname',
        'email': 'Email',
        'project_idfk': 'ProjectIDFK',
        'project_title': 'ProjectTitle',
        'customer_idfk': 'CustomerIDFK',
        'customer_name': 'CustomerName',
        'timesheet_category_idfk': 'TimesheetCategoryIDFK',
        'category_name': 'CategoryName',
        'duration': 'Duration',
        'timesheet_entry_approval_status_code': 'TimesheetEntryApprovalStatusCode',
        'has_timer': 'HasTimer',
        'timer_started_at_utc': 'TimerStartedAtUTC',
        'is_billable': 'isBillable',
        'is_invoiced': 'isInvoiced',
        'entry_date': 'EntryDate',
        'start_time_local': 'StartTimeLocal',
        'start_time_utc': 'StartTimeUTC',
        'end_time_local': 'EndTimeLocal',
        'end_time_utc': 'EndTimeUTC',
        'timesheet_user_time_zone': 'TimesheetUserTimeZone',
        'notes': 'Notes',
        'task_idfk': 'TaskIDFK',
        'task_title': 'TaskTitle',
        'invoice_idfk': 'InvoiceIDFK',
        'invoice_line_item_idfk': 'InvoiceLineItemIDFK',
        'date_created': 'DateCreated',
        'date_updated': 'DateUpdated'
    }

    def __init__(self, timesheet_entry_id=None, user_idfk=None, firstname=None, lastname=None, email=None, project_idfk=None, project_title=None, customer_idfk=None, customer_name=None, timesheet_category_idfk=None, category_name=None, duration=None, timesheet_entry_approval_status_code=None, has_timer=None, timer_started_at_utc=None, is_billable=None, is_invoiced=None, entry_date=None, start_time_local=None, start_time_utc=None, end_time_local=None, end_time_utc=None, timesheet_user_time_zone=None, notes=None, task_idfk=None, task_title=None, invoice_idfk=None, invoice_line_item_idfk=None, date_created=None, date_updated=None):  # noqa: E501
        """TimesheetDetails - a model defined in Swagger"""  # noqa: E501

        self._timesheet_entry_id = None
        self._user_idfk = None
        self._firstname = None
        self._lastname = None
        self._email = None
        self._project_idfk = None
        self._project_title = None
        self._customer_idfk = None
        self._customer_name = None
        self._timesheet_category_idfk = None
        self._category_name = None
        self._duration = None
        self._timesheet_entry_approval_status_code = None
        self._has_timer = None
        self._timer_started_at_utc = None
        self._is_billable = None
        self._is_invoiced = None
        self._entry_date = None
        self._start_time_local = None
        self._start_time_utc = None
        self._end_time_local = None
        self._end_time_utc = None
        self._timesheet_user_time_zone = None
        self._notes = None
        self._task_idfk = None
        self._task_title = None
        self._invoice_idfk = None
        self._invoice_line_item_idfk = None
        self._date_created = None
        self._date_updated = None
        self.discriminator = None

        if timesheet_entry_id is not None:
            self.timesheet_entry_id = timesheet_entry_id
        if user_idfk is not None:
            self.user_idfk = user_idfk
        if firstname is not None:
            self.firstname = firstname
        if lastname is not None:
            self.lastname = lastname
        if email is not None:
            self.email = email
        if project_idfk is not None:
            self.project_idfk = project_idfk
        if project_title is not None:
            self.project_title = project_title
        if customer_idfk is not None:
            self.customer_idfk = customer_idfk
        if customer_name is not None:
            self.customer_name = customer_name
        if timesheet_category_idfk is not None:
            self.timesheet_category_idfk = timesheet_category_idfk
        if category_name is not None:
            self.category_name = category_name
        if duration is not None:
            self.duration = duration
        if timesheet_entry_approval_status_code is not None:
            self.timesheet_entry_approval_status_code = timesheet_entry_approval_status_code
        if has_timer is not None:
            self.has_timer = has_timer
        if timer_started_at_utc is not None:
            self.timer_started_at_utc = timer_started_at_utc
        if is_billable is not None:
            self.is_billable = is_billable
        if is_invoiced is not None:
            self.is_invoiced = is_invoiced
        if entry_date is not None:
            self.entry_date = entry_date
        if start_time_local is not None:
            self.start_time_local = start_time_local
        if start_time_utc is not None:
            self.start_time_utc = start_time_utc
        if end_time_local is not None:
            self.end_time_local = end_time_local
        if end_time_utc is not None:
            self.end_time_utc = end_time_utc
        if timesheet_user_time_zone is not None:
            self.timesheet_user_time_zone = timesheet_user_time_zone
        if notes is not None:
            self.notes = notes
        if task_idfk is not None:
            self.task_idfk = task_idfk
        if task_title is not None:
            self.task_title = task_title
        if invoice_idfk is not None:
            self.invoice_idfk = invoice_idfk
        if invoice_line_item_idfk is not None:
            self.invoice_line_item_idfk = invoice_line_item_idfk
        if date_created is not None:
            self.date_created = date_created
        if date_updated is not None:
            self.date_updated = date_updated

    @property
    def timesheet_entry_id(self):
        """Gets the timesheet_entry_id of this TimesheetDetails.  # noqa: E501


        :return: The timesheet_entry_id of this TimesheetDetails.  # noqa: E501
        :rtype: int
        """
        return self._timesheet_entry_id

    @timesheet_entry_id.setter
    def timesheet_entry_id(self, timesheet_entry_id):
        """Sets the timesheet_entry_id of this TimesheetDetails.


        :param timesheet_entry_id: The timesheet_entry_id of this TimesheetDetails.  # noqa: E501
        :type: int
        """

        self._timesheet_entry_id = timesheet_entry_id

    @property
    def user_idfk(self):
        """Gets the user_idfk of this TimesheetDetails.  # noqa: E501


        :return: The user_idfk of this TimesheetDetails.  # noqa: E501
        :rtype: int
        """
        return self._user_idfk

    @user_idfk.setter
    def user_idfk(self, user_idfk):
        """Sets the user_idfk of this TimesheetDetails.


        :param user_idfk: The user_idfk of this TimesheetDetails.  # noqa: E501
        :type: int
        """

        self._user_idfk = user_idfk

    @property
    def firstname(self):
        """Gets the firstname of this TimesheetDetails.  # noqa: E501


        :return: The firstname of this TimesheetDetails.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this TimesheetDetails.


        :param firstname: The firstname of this TimesheetDetails.  # noqa: E501
        :type: str
        """

        self._firstname = firstname

    @property
    def lastname(self):
        """Gets the lastname of this TimesheetDetails.  # noqa: E501


        :return: The lastname of this TimesheetDetails.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this TimesheetDetails.


        :param lastname: The lastname of this TimesheetDetails.  # noqa: E501
        :type: str
        """

        self._lastname = lastname

    @property
    def email(self):
        """Gets the email of this TimesheetDetails.  # noqa: E501


        :return: The email of this TimesheetDetails.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this TimesheetDetails.


        :param email: The email of this TimesheetDetails.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def project_idfk(self):
        """Gets the project_idfk of this TimesheetDetails.  # noqa: E501


        :return: The project_idfk of this TimesheetDetails.  # noqa: E501
        :rtype: int
        """
        return self._project_idfk

    @project_idfk.setter
    def project_idfk(self, project_idfk):
        """Sets the project_idfk of this TimesheetDetails.


        :param project_idfk: The project_idfk of this TimesheetDetails.  # noqa: E501
        :type: int
        """

        self._project_idfk = project_idfk

    @property
    def project_title(self):
        """Gets the project_title of this TimesheetDetails.  # noqa: E501


        :return: The project_title of this TimesheetDetails.  # noqa: E501
        :rtype: str
        """
        return self._project_title

    @project_title.setter
    def project_title(self, project_title):
        """Sets the project_title of this TimesheetDetails.


        :param project_title: The project_title of this TimesheetDetails.  # noqa: E501
        :type: str
        """

        self._project_title = project_title

    @property
    def customer_idfk(self):
        """Gets the customer_idfk of this TimesheetDetails.  # noqa: E501


        :return: The customer_idfk of this TimesheetDetails.  # noqa: E501
        :rtype: int
        """
        return self._customer_idfk

    @customer_idfk.setter
    def customer_idfk(self, customer_idfk):
        """Sets the customer_idfk of this TimesheetDetails.


        :param customer_idfk: The customer_idfk of this TimesheetDetails.  # noqa: E501
        :type: int
        """

        self._customer_idfk = customer_idfk

    @property
    def customer_name(self):
        """Gets the customer_name of this TimesheetDetails.  # noqa: E501


        :return: The customer_name of this TimesheetDetails.  # noqa: E501
        :rtype: str
        """
        return self._customer_name

    @customer_name.setter
    def customer_name(self, customer_name):
        """Sets the customer_name of this TimesheetDetails.


        :param customer_name: The customer_name of this TimesheetDetails.  # noqa: E501
        :type: str
        """

        self._customer_name = customer_name

    @property
    def timesheet_category_idfk(self):
        """Gets the timesheet_category_idfk of this TimesheetDetails.  # noqa: E501


        :return: The timesheet_category_idfk of this TimesheetDetails.  # noqa: E501
        :rtype: int
        """
        return self._timesheet_category_idfk

    @timesheet_category_idfk.setter
    def timesheet_category_idfk(self, timesheet_category_idfk):
        """Sets the timesheet_category_idfk of this TimesheetDetails.


        :param timesheet_category_idfk: The timesheet_category_idfk of this TimesheetDetails.  # noqa: E501
        :type: int
        """

        self._timesheet_category_idfk = timesheet_category_idfk

    @property
    def category_name(self):
        """Gets the category_name of this TimesheetDetails.  # noqa: E501


        :return: The category_name of this TimesheetDetails.  # noqa: E501
        :rtype: str
        """
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        """Sets the category_name of this TimesheetDetails.


        :param category_name: The category_name of this TimesheetDetails.  # noqa: E501
        :type: str
        """

        self._category_name = category_name

    @property
    def duration(self):
        """Gets the duration of this TimesheetDetails.  # noqa: E501


        :return: The duration of this TimesheetDetails.  # noqa: E501
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this TimesheetDetails.


        :param duration: The duration of this TimesheetDetails.  # noqa: E501
        :type: float
        """

        self._duration = duration

    @property
    def timesheet_entry_approval_status_code(self):
        """Gets the timesheet_entry_approval_status_code of this TimesheetDetails.  # noqa: E501


        :return: The timesheet_entry_approval_status_code of this TimesheetDetails.  # noqa: E501
        :rtype: str
        """
        return self._timesheet_entry_approval_status_code

    @timesheet_entry_approval_status_code.setter
    def timesheet_entry_approval_status_code(self, timesheet_entry_approval_status_code):
        """Sets the timesheet_entry_approval_status_code of this TimesheetDetails.


        :param timesheet_entry_approval_status_code: The timesheet_entry_approval_status_code of this TimesheetDetails.  # noqa: E501
        :type: str
        """

        self._timesheet_entry_approval_status_code = timesheet_entry_approval_status_code

    @property
    def has_timer(self):
        """Gets the has_timer of this TimesheetDetails.  # noqa: E501


        :return: The has_timer of this TimesheetDetails.  # noqa: E501
        :rtype: bool
        """
        return self._has_timer

    @has_timer.setter
    def has_timer(self, has_timer):
        """Sets the has_timer of this TimesheetDetails.


        :param has_timer: The has_timer of this TimesheetDetails.  # noqa: E501
        :type: bool
        """

        self._has_timer = has_timer

    @property
    def timer_started_at_utc(self):
        """Gets the timer_started_at_utc of this TimesheetDetails.  # noqa: E501


        :return: The timer_started_at_utc of this TimesheetDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._timer_started_at_utc

    @timer_started_at_utc.setter
    def timer_started_at_utc(self, timer_started_at_utc):
        """Sets the timer_started_at_utc of this TimesheetDetails.


        :param timer_started_at_utc: The timer_started_at_utc of this TimesheetDetails.  # noqa: E501
        :type: datetime
        """

        self._timer_started_at_utc = timer_started_at_utc

    @property
    def is_billable(self):
        """Gets the is_billable of this TimesheetDetails.  # noqa: E501


        :return: The is_billable of this TimesheetDetails.  # noqa: E501
        :rtype: bool
        """
        return self._is_billable

    @is_billable.setter
    def is_billable(self, is_billable):
        """Sets the is_billable of this TimesheetDetails.


        :param is_billable: The is_billable of this TimesheetDetails.  # noqa: E501
        :type: bool
        """

        self._is_billable = is_billable

    @property
    def is_invoiced(self):
        """Gets the is_invoiced of this TimesheetDetails.  # noqa: E501


        :return: The is_invoiced of this TimesheetDetails.  # noqa: E501
        :rtype: bool
        """
        return self._is_invoiced

    @is_invoiced.setter
    def is_invoiced(self, is_invoiced):
        """Sets the is_invoiced of this TimesheetDetails.


        :param is_invoiced: The is_invoiced of this TimesheetDetails.  # noqa: E501
        :type: bool
        """

        self._is_invoiced = is_invoiced

    @property
    def entry_date(self):
        """Gets the entry_date of this TimesheetDetails.  # noqa: E501


        :return: The entry_date of this TimesheetDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._entry_date

    @entry_date.setter
    def entry_date(self, entry_date):
        """Sets the entry_date of this TimesheetDetails.


        :param entry_date: The entry_date of this TimesheetDetails.  # noqa: E501
        :type: datetime
        """

        self._entry_date = entry_date

    @property
    def start_time_local(self):
        """Gets the start_time_local of this TimesheetDetails.  # noqa: E501


        :return: The start_time_local of this TimesheetDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time_local

    @start_time_local.setter
    def start_time_local(self, start_time_local):
        """Sets the start_time_local of this TimesheetDetails.


        :param start_time_local: The start_time_local of this TimesheetDetails.  # noqa: E501
        :type: datetime
        """

        self._start_time_local = start_time_local

    @property
    def start_time_utc(self):
        """Gets the start_time_utc of this TimesheetDetails.  # noqa: E501


        :return: The start_time_utc of this TimesheetDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time_utc

    @start_time_utc.setter
    def start_time_utc(self, start_time_utc):
        """Sets the start_time_utc of this TimesheetDetails.


        :param start_time_utc: The start_time_utc of this TimesheetDetails.  # noqa: E501
        :type: datetime
        """

        self._start_time_utc = start_time_utc

    @property
    def end_time_local(self):
        """Gets the end_time_local of this TimesheetDetails.  # noqa: E501


        :return: The end_time_local of this TimesheetDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time_local

    @end_time_local.setter
    def end_time_local(self, end_time_local):
        """Sets the end_time_local of this TimesheetDetails.


        :param end_time_local: The end_time_local of this TimesheetDetails.  # noqa: E501
        :type: datetime
        """

        self._end_time_local = end_time_local

    @property
    def end_time_utc(self):
        """Gets the end_time_utc of this TimesheetDetails.  # noqa: E501


        :return: The end_time_utc of this TimesheetDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time_utc

    @end_time_utc.setter
    def end_time_utc(self, end_time_utc):
        """Sets the end_time_utc of this TimesheetDetails.


        :param end_time_utc: The end_time_utc of this TimesheetDetails.  # noqa: E501
        :type: datetime
        """

        self._end_time_utc = end_time_utc

    @property
    def timesheet_user_time_zone(self):
        """Gets the timesheet_user_time_zone of this TimesheetDetails.  # noqa: E501


        :return: The timesheet_user_time_zone of this TimesheetDetails.  # noqa: E501
        :rtype: str
        """
        return self._timesheet_user_time_zone

    @timesheet_user_time_zone.setter
    def timesheet_user_time_zone(self, timesheet_user_time_zone):
        """Sets the timesheet_user_time_zone of this TimesheetDetails.


        :param timesheet_user_time_zone: The timesheet_user_time_zone of this TimesheetDetails.  # noqa: E501
        :type: str
        """

        self._timesheet_user_time_zone = timesheet_user_time_zone

    @property
    def notes(self):
        """Gets the notes of this TimesheetDetails.  # noqa: E501


        :return: The notes of this TimesheetDetails.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this TimesheetDetails.


        :param notes: The notes of this TimesheetDetails.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def task_idfk(self):
        """Gets the task_idfk of this TimesheetDetails.  # noqa: E501


        :return: The task_idfk of this TimesheetDetails.  # noqa: E501
        :rtype: int
        """
        return self._task_idfk

    @task_idfk.setter
    def task_idfk(self, task_idfk):
        """Sets the task_idfk of this TimesheetDetails.


        :param task_idfk: The task_idfk of this TimesheetDetails.  # noqa: E501
        :type: int
        """

        self._task_idfk = task_idfk

    @property
    def task_title(self):
        """Gets the task_title of this TimesheetDetails.  # noqa: E501


        :return: The task_title of this TimesheetDetails.  # noqa: E501
        :rtype: str
        """
        return self._task_title

    @task_title.setter
    def task_title(self, task_title):
        """Sets the task_title of this TimesheetDetails.


        :param task_title: The task_title of this TimesheetDetails.  # noqa: E501
        :type: str
        """

        self._task_title = task_title

    @property
    def invoice_idfk(self):
        """Gets the invoice_idfk of this TimesheetDetails.  # noqa: E501


        :return: The invoice_idfk of this TimesheetDetails.  # noqa: E501
        :rtype: int
        """
        return self._invoice_idfk

    @invoice_idfk.setter
    def invoice_idfk(self, invoice_idfk):
        """Sets the invoice_idfk of this TimesheetDetails.


        :param invoice_idfk: The invoice_idfk of this TimesheetDetails.  # noqa: E501
        :type: int
        """

        self._invoice_idfk = invoice_idfk

    @property
    def invoice_line_item_idfk(self):
        """Gets the invoice_line_item_idfk of this TimesheetDetails.  # noqa: E501


        :return: The invoice_line_item_idfk of this TimesheetDetails.  # noqa: E501
        :rtype: int
        """
        return self._invoice_line_item_idfk

    @invoice_line_item_idfk.setter
    def invoice_line_item_idfk(self, invoice_line_item_idfk):
        """Sets the invoice_line_item_idfk of this TimesheetDetails.


        :param invoice_line_item_idfk: The invoice_line_item_idfk of this TimesheetDetails.  # noqa: E501
        :type: int
        """

        self._invoice_line_item_idfk = invoice_line_item_idfk

    @property
    def date_created(self):
        """Gets the date_created of this TimesheetDetails.  # noqa: E501


        :return: The date_created of this TimesheetDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this TimesheetDetails.


        :param date_created: The date_created of this TimesheetDetails.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def date_updated(self):
        """Gets the date_updated of this TimesheetDetails.  # noqa: E501


        :return: The date_updated of this TimesheetDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._date_updated

    @date_updated.setter
    def date_updated(self, date_updated):
        """Sets the date_updated of this TimesheetDetails.


        :param date_updated: The date_updated of this TimesheetDetails.  # noqa: E501
        :type: datetime
        """

        self._date_updated = date_updated

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TimesheetDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
