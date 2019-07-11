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


class ProjectListDetails(object):
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
        'project_id': 'int',
        'title': 'str',
        'is_archived': 'bool',
        'notes': 'str',
        'company_name': 'str',
        'company_idfk': 'int',
        'is_task_required_on_timesheet': 'bool',
        'date_created': 'datetime',
        'date_updated': 'datetime'
    }

    attribute_map = {
        'project_id': 'ProjectID',
        'title': 'Title',
        'is_archived': 'isArchived',
        'notes': 'Notes',
        'company_name': 'CompanyName',
        'company_idfk': 'CompanyIDFK',
        'is_task_required_on_timesheet': 'isTaskRequiredOnTimesheet',
        'date_created': 'DateCreated',
        'date_updated': 'DateUpdated'
    }

    def __init__(self, project_id=None, title=None, is_archived=None, notes=None, company_name=None, company_idfk=None, is_task_required_on_timesheet=None, date_created=None, date_updated=None):  # noqa: E501
        """ProjectListDetails - a model defined in Swagger"""  # noqa: E501

        self._project_id = None
        self._title = None
        self._is_archived = None
        self._notes = None
        self._company_name = None
        self._company_idfk = None
        self._is_task_required_on_timesheet = None
        self._date_created = None
        self._date_updated = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if title is not None:
            self.title = title
        if is_archived is not None:
            self.is_archived = is_archived
        if notes is not None:
            self.notes = notes
        if company_name is not None:
            self.company_name = company_name
        if company_idfk is not None:
            self.company_idfk = company_idfk
        if is_task_required_on_timesheet is not None:
            self.is_task_required_on_timesheet = is_task_required_on_timesheet
        if date_created is not None:
            self.date_created = date_created
        if date_updated is not None:
            self.date_updated = date_updated

    @property
    def project_id(self):
        """Gets the project_id of this ProjectListDetails.  # noqa: E501


        :return: The project_id of this ProjectListDetails.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ProjectListDetails.


        :param project_id: The project_id of this ProjectListDetails.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def title(self):
        """Gets the title of this ProjectListDetails.  # noqa: E501


        :return: The title of this ProjectListDetails.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ProjectListDetails.


        :param title: The title of this ProjectListDetails.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def is_archived(self):
        """Gets the is_archived of this ProjectListDetails.  # noqa: E501


        :return: The is_archived of this ProjectListDetails.  # noqa: E501
        :rtype: bool
        """
        return self._is_archived

    @is_archived.setter
    def is_archived(self, is_archived):
        """Sets the is_archived of this ProjectListDetails.


        :param is_archived: The is_archived of this ProjectListDetails.  # noqa: E501
        :type: bool
        """

        self._is_archived = is_archived

    @property
    def notes(self):
        """Gets the notes of this ProjectListDetails.  # noqa: E501


        :return: The notes of this ProjectListDetails.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this ProjectListDetails.


        :param notes: The notes of this ProjectListDetails.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def company_name(self):
        """Gets the company_name of this ProjectListDetails.  # noqa: E501


        :return: The company_name of this ProjectListDetails.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this ProjectListDetails.


        :param company_name: The company_name of this ProjectListDetails.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def company_idfk(self):
        """Gets the company_idfk of this ProjectListDetails.  # noqa: E501


        :return: The company_idfk of this ProjectListDetails.  # noqa: E501
        :rtype: int
        """
        return self._company_idfk

    @company_idfk.setter
    def company_idfk(self, company_idfk):
        """Sets the company_idfk of this ProjectListDetails.


        :param company_idfk: The company_idfk of this ProjectListDetails.  # noqa: E501
        :type: int
        """

        self._company_idfk = company_idfk

    @property
    def is_task_required_on_timesheet(self):
        """Gets the is_task_required_on_timesheet of this ProjectListDetails.  # noqa: E501


        :return: The is_task_required_on_timesheet of this ProjectListDetails.  # noqa: E501
        :rtype: bool
        """
        return self._is_task_required_on_timesheet

    @is_task_required_on_timesheet.setter
    def is_task_required_on_timesheet(self, is_task_required_on_timesheet):
        """Sets the is_task_required_on_timesheet of this ProjectListDetails.


        :param is_task_required_on_timesheet: The is_task_required_on_timesheet of this ProjectListDetails.  # noqa: E501
        :type: bool
        """

        self._is_task_required_on_timesheet = is_task_required_on_timesheet

    @property
    def date_created(self):
        """Gets the date_created of this ProjectListDetails.  # noqa: E501


        :return: The date_created of this ProjectListDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this ProjectListDetails.


        :param date_created: The date_created of this ProjectListDetails.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def date_updated(self):
        """Gets the date_updated of this ProjectListDetails.  # noqa: E501


        :return: The date_updated of this ProjectListDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._date_updated

    @date_updated.setter
    def date_updated(self, date_updated):
        """Sets the date_updated of this ProjectListDetails.


        :param date_updated: The date_updated of this ProjectListDetails.  # noqa: E501
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
        if not isinstance(other, ProjectListDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other