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


class ProjectTimesheetCategoryDetails(object):
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
        'time_sheet_category_idfk': 'int',
        'account_idfk': 'int',
        'project_idfk': 'int',
        'name': 'str',
        'is_billable': 'bool',
        'rate_amount': 'float',
        'budget_hours': 'float',
        'cost_amount': 'float'
    }

    attribute_map = {
        'time_sheet_category_idfk': 'TimeSheetCategoryIDFK',
        'account_idfk': 'AccountIDFK',
        'project_idfk': 'ProjectIDFK',
        'name': 'Name',
        'is_billable': 'isBillable',
        'rate_amount': 'RateAmount',
        'budget_hours': 'BudgetHours',
        'cost_amount': 'CostAmount'
    }

    def __init__(self, time_sheet_category_idfk=None, account_idfk=None, project_idfk=None, name=None, is_billable=None, rate_amount=None, budget_hours=None, cost_amount=None):  # noqa: E501
        """ProjectTimesheetCategoryDetails - a model defined in Swagger"""  # noqa: E501

        self._time_sheet_category_idfk = None
        self._account_idfk = None
        self._project_idfk = None
        self._name = None
        self._is_billable = None
        self._rate_amount = None
        self._budget_hours = None
        self._cost_amount = None
        self.discriminator = None

        if time_sheet_category_idfk is not None:
            self.time_sheet_category_idfk = time_sheet_category_idfk
        if account_idfk is not None:
            self.account_idfk = account_idfk
        if project_idfk is not None:
            self.project_idfk = project_idfk
        if name is not None:
            self.name = name
        if is_billable is not None:
            self.is_billable = is_billable
        if rate_amount is not None:
            self.rate_amount = rate_amount
        if budget_hours is not None:
            self.budget_hours = budget_hours
        if cost_amount is not None:
            self.cost_amount = cost_amount

    @property
    def time_sheet_category_idfk(self):
        """Gets the time_sheet_category_idfk of this ProjectTimesheetCategoryDetails.  # noqa: E501


        :return: The time_sheet_category_idfk of this ProjectTimesheetCategoryDetails.  # noqa: E501
        :rtype: int
        """
        return self._time_sheet_category_idfk

    @time_sheet_category_idfk.setter
    def time_sheet_category_idfk(self, time_sheet_category_idfk):
        """Sets the time_sheet_category_idfk of this ProjectTimesheetCategoryDetails.


        :param time_sheet_category_idfk: The time_sheet_category_idfk of this ProjectTimesheetCategoryDetails.  # noqa: E501
        :type: int
        """

        self._time_sheet_category_idfk = time_sheet_category_idfk

    @property
    def account_idfk(self):
        """Gets the account_idfk of this ProjectTimesheetCategoryDetails.  # noqa: E501


        :return: The account_idfk of this ProjectTimesheetCategoryDetails.  # noqa: E501
        :rtype: int
        """
        return self._account_idfk

    @account_idfk.setter
    def account_idfk(self, account_idfk):
        """Sets the account_idfk of this ProjectTimesheetCategoryDetails.


        :param account_idfk: The account_idfk of this ProjectTimesheetCategoryDetails.  # noqa: E501
        :type: int
        """

        self._account_idfk = account_idfk

    @property
    def project_idfk(self):
        """Gets the project_idfk of this ProjectTimesheetCategoryDetails.  # noqa: E501


        :return: The project_idfk of this ProjectTimesheetCategoryDetails.  # noqa: E501
        :rtype: int
        """
        return self._project_idfk

    @project_idfk.setter
    def project_idfk(self, project_idfk):
        """Sets the project_idfk of this ProjectTimesheetCategoryDetails.


        :param project_idfk: The project_idfk of this ProjectTimesheetCategoryDetails.  # noqa: E501
        :type: int
        """

        self._project_idfk = project_idfk

    @property
    def name(self):
        """Gets the name of this ProjectTimesheetCategoryDetails.  # noqa: E501


        :return: The name of this ProjectTimesheetCategoryDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectTimesheetCategoryDetails.


        :param name: The name of this ProjectTimesheetCategoryDetails.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def is_billable(self):
        """Gets the is_billable of this ProjectTimesheetCategoryDetails.  # noqa: E501


        :return: The is_billable of this ProjectTimesheetCategoryDetails.  # noqa: E501
        :rtype: bool
        """
        return self._is_billable

    @is_billable.setter
    def is_billable(self, is_billable):
        """Sets the is_billable of this ProjectTimesheetCategoryDetails.


        :param is_billable: The is_billable of this ProjectTimesheetCategoryDetails.  # noqa: E501
        :type: bool
        """

        self._is_billable = is_billable

    @property
    def rate_amount(self):
        """Gets the rate_amount of this ProjectTimesheetCategoryDetails.  # noqa: E501


        :return: The rate_amount of this ProjectTimesheetCategoryDetails.  # noqa: E501
        :rtype: float
        """
        return self._rate_amount

    @rate_amount.setter
    def rate_amount(self, rate_amount):
        """Sets the rate_amount of this ProjectTimesheetCategoryDetails.


        :param rate_amount: The rate_amount of this ProjectTimesheetCategoryDetails.  # noqa: E501
        :type: float
        """

        self._rate_amount = rate_amount

    @property
    def budget_hours(self):
        """Gets the budget_hours of this ProjectTimesheetCategoryDetails.  # noqa: E501


        :return: The budget_hours of this ProjectTimesheetCategoryDetails.  # noqa: E501
        :rtype: float
        """
        return self._budget_hours

    @budget_hours.setter
    def budget_hours(self, budget_hours):
        """Sets the budget_hours of this ProjectTimesheetCategoryDetails.


        :param budget_hours: The budget_hours of this ProjectTimesheetCategoryDetails.  # noqa: E501
        :type: float
        """

        self._budget_hours = budget_hours

    @property
    def cost_amount(self):
        """Gets the cost_amount of this ProjectTimesheetCategoryDetails.  # noqa: E501


        :return: The cost_amount of this ProjectTimesheetCategoryDetails.  # noqa: E501
        :rtype: float
        """
        return self._cost_amount

    @cost_amount.setter
    def cost_amount(self, cost_amount):
        """Sets the cost_amount of this ProjectTimesheetCategoryDetails.


        :param cost_amount: The cost_amount of this ProjectTimesheetCategoryDetails.  # noqa: E501
        :type: float
        """

        self._cost_amount = cost_amount

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
        if not isinstance(other, ProjectTimesheetCategoryDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
