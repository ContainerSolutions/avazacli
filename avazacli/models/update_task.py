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


class UpdateTask(object):
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
        'task_id': 'int',
        'fields_to_update': 'list[str]',
        'title': 'str',
        'description': 'str',
        'assigned_to_user_idfk': 'int',
        'date_start': 'datetime',
        'date_start_utc': 'datetime',
        'date_due': 'datetime',
        'date_due_utc': 'datetime',
        'estimated_effort': 'float',
        'percent_complete': 'int'
    }

    attribute_map = {
        'task_id': 'TaskID',
        'fields_to_update': 'FieldsToUpdate',
        'title': 'Title',
        'description': 'Description',
        'assigned_to_user_idfk': 'AssignedToUserIDFK',
        'date_start': 'DateStart',
        'date_start_utc': 'DateStartUTC',
        'date_due': 'DateDue',
        'date_due_utc': 'DateDueUTC',
        'estimated_effort': 'EstimatedEffort',
        'percent_complete': 'PercentComplete'
    }

    def __init__(self, task_id=None, fields_to_update=None, title=None, description=None, assigned_to_user_idfk=None, date_start=None, date_start_utc=None, date_due=None, date_due_utc=None, estimated_effort=None, percent_complete=None):  # noqa: E501
        """UpdateTask - a model defined in Swagger"""  # noqa: E501

        self._task_id = None
        self._fields_to_update = None
        self._title = None
        self._description = None
        self._assigned_to_user_idfk = None
        self._date_start = None
        self._date_start_utc = None
        self._date_due = None
        self._date_due_utc = None
        self._estimated_effort = None
        self._percent_complete = None
        self.discriminator = None

        self.task_id = task_id
        self.fields_to_update = fields_to_update
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if assigned_to_user_idfk is not None:
            self.assigned_to_user_idfk = assigned_to_user_idfk
        if date_start is not None:
            self.date_start = date_start
        if date_start_utc is not None:
            self.date_start_utc = date_start_utc
        if date_due is not None:
            self.date_due = date_due
        if date_due_utc is not None:
            self.date_due_utc = date_due_utc
        if estimated_effort is not None:
            self.estimated_effort = estimated_effort
        if percent_complete is not None:
            self.percent_complete = percent_complete

    @property
    def task_id(self):
        """Gets the task_id of this UpdateTask.  # noqa: E501


        :return: The task_id of this UpdateTask.  # noqa: E501
        :rtype: int
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this UpdateTask.


        :param task_id: The task_id of this UpdateTask.  # noqa: E501
        :type: int
        """
        if task_id is None:
            raise ValueError("Invalid value for `task_id`, must not be `None`")  # noqa: E501

        self._task_id = task_id

    @property
    def fields_to_update(self):
        """Gets the fields_to_update of this UpdateTask.  # noqa: E501


        :return: The fields_to_update of this UpdateTask.  # noqa: E501
        :rtype: list[str]
        """
        return self._fields_to_update

    @fields_to_update.setter
    def fields_to_update(self, fields_to_update):
        """Sets the fields_to_update of this UpdateTask.


        :param fields_to_update: The fields_to_update of this UpdateTask.  # noqa: E501
        :type: list[str]
        """
        if fields_to_update is None:
            raise ValueError("Invalid value for `fields_to_update`, must not be `None`")  # noqa: E501

        self._fields_to_update = fields_to_update

    @property
    def title(self):
        """Gets the title of this UpdateTask.  # noqa: E501


        :return: The title of this UpdateTask.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this UpdateTask.


        :param title: The title of this UpdateTask.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """Gets the description of this UpdateTask.  # noqa: E501


        :return: The description of this UpdateTask.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateTask.


        :param description: The description of this UpdateTask.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def assigned_to_user_idfk(self):
        """Gets the assigned_to_user_idfk of this UpdateTask.  # noqa: E501


        :return: The assigned_to_user_idfk of this UpdateTask.  # noqa: E501
        :rtype: int
        """
        return self._assigned_to_user_idfk

    @assigned_to_user_idfk.setter
    def assigned_to_user_idfk(self, assigned_to_user_idfk):
        """Sets the assigned_to_user_idfk of this UpdateTask.


        :param assigned_to_user_idfk: The assigned_to_user_idfk of this UpdateTask.  # noqa: E501
        :type: int
        """

        self._assigned_to_user_idfk = assigned_to_user_idfk

    @property
    def date_start(self):
        """Gets the date_start of this UpdateTask.  # noqa: E501


        :return: The date_start of this UpdateTask.  # noqa: E501
        :rtype: datetime
        """
        return self._date_start

    @date_start.setter
    def date_start(self, date_start):
        """Sets the date_start of this UpdateTask.


        :param date_start: The date_start of this UpdateTask.  # noqa: E501
        :type: datetime
        """

        self._date_start = date_start

    @property
    def date_start_utc(self):
        """Gets the date_start_utc of this UpdateTask.  # noqa: E501


        :return: The date_start_utc of this UpdateTask.  # noqa: E501
        :rtype: datetime
        """
        return self._date_start_utc

    @date_start_utc.setter
    def date_start_utc(self, date_start_utc):
        """Sets the date_start_utc of this UpdateTask.


        :param date_start_utc: The date_start_utc of this UpdateTask.  # noqa: E501
        :type: datetime
        """

        self._date_start_utc = date_start_utc

    @property
    def date_due(self):
        """Gets the date_due of this UpdateTask.  # noqa: E501


        :return: The date_due of this UpdateTask.  # noqa: E501
        :rtype: datetime
        """
        return self._date_due

    @date_due.setter
    def date_due(self, date_due):
        """Sets the date_due of this UpdateTask.


        :param date_due: The date_due of this UpdateTask.  # noqa: E501
        :type: datetime
        """

        self._date_due = date_due

    @property
    def date_due_utc(self):
        """Gets the date_due_utc of this UpdateTask.  # noqa: E501


        :return: The date_due_utc of this UpdateTask.  # noqa: E501
        :rtype: datetime
        """
        return self._date_due_utc

    @date_due_utc.setter
    def date_due_utc(self, date_due_utc):
        """Sets the date_due_utc of this UpdateTask.


        :param date_due_utc: The date_due_utc of this UpdateTask.  # noqa: E501
        :type: datetime
        """

        self._date_due_utc = date_due_utc

    @property
    def estimated_effort(self):
        """Gets the estimated_effort of this UpdateTask.  # noqa: E501

        Decimal hours  # noqa: E501

        :return: The estimated_effort of this UpdateTask.  # noqa: E501
        :rtype: float
        """
        return self._estimated_effort

    @estimated_effort.setter
    def estimated_effort(self, estimated_effort):
        """Sets the estimated_effort of this UpdateTask.

        Decimal hours  # noqa: E501

        :param estimated_effort: The estimated_effort of this UpdateTask.  # noqa: E501
        :type: float
        """

        self._estimated_effort = estimated_effort

    @property
    def percent_complete(self):
        """Gets the percent_complete of this UpdateTask.  # noqa: E501


        :return: The percent_complete of this UpdateTask.  # noqa: E501
        :rtype: int
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """Sets the percent_complete of this UpdateTask.


        :param percent_complete: The percent_complete of this UpdateTask.  # noqa: E501
        :type: int
        """

        self._percent_complete = percent_complete

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
        if not isinstance(other, UpdateTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
