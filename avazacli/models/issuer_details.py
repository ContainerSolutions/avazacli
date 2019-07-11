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


class IssuerDetails(object):
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
        'billing_address': 'str',
        'billing_address_line': 'str',
        'billing_address_city': 'str',
        'billing_address_state': 'str',
        'billing_address_post_code': 'str',
        'billing_country_code': 'str',
        'tax_number': 'str'
    }

    attribute_map = {
        'billing_address': 'BillingAddress',
        'billing_address_line': 'BillingAddressLine',
        'billing_address_city': 'BillingAddressCity',
        'billing_address_state': 'BillingAddressState',
        'billing_address_post_code': 'BillingAddressPostCode',
        'billing_country_code': 'BillingCountryCode',
        'tax_number': 'TaxNumber'
    }

    def __init__(self, billing_address=None, billing_address_line=None, billing_address_city=None, billing_address_state=None, billing_address_post_code=None, billing_country_code=None, tax_number=None):  # noqa: E501
        """IssuerDetails - a model defined in Swagger"""  # noqa: E501

        self._billing_address = None
        self._billing_address_line = None
        self._billing_address_city = None
        self._billing_address_state = None
        self._billing_address_post_code = None
        self._billing_country_code = None
        self._tax_number = None
        self.discriminator = None

        if billing_address is not None:
            self.billing_address = billing_address
        if billing_address_line is not None:
            self.billing_address_line = billing_address_line
        if billing_address_city is not None:
            self.billing_address_city = billing_address_city
        if billing_address_state is not None:
            self.billing_address_state = billing_address_state
        if billing_address_post_code is not None:
            self.billing_address_post_code = billing_address_post_code
        if billing_country_code is not None:
            self.billing_country_code = billing_country_code
        if tax_number is not None:
            self.tax_number = tax_number

    @property
    def billing_address(self):
        """Gets the billing_address of this IssuerDetails.  # noqa: E501


        :return: The billing_address of this IssuerDetails.  # noqa: E501
        :rtype: str
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this IssuerDetails.


        :param billing_address: The billing_address of this IssuerDetails.  # noqa: E501
        :type: str
        """

        self._billing_address = billing_address

    @property
    def billing_address_line(self):
        """Gets the billing_address_line of this IssuerDetails.  # noqa: E501


        :return: The billing_address_line of this IssuerDetails.  # noqa: E501
        :rtype: str
        """
        return self._billing_address_line

    @billing_address_line.setter
    def billing_address_line(self, billing_address_line):
        """Sets the billing_address_line of this IssuerDetails.


        :param billing_address_line: The billing_address_line of this IssuerDetails.  # noqa: E501
        :type: str
        """

        self._billing_address_line = billing_address_line

    @property
    def billing_address_city(self):
        """Gets the billing_address_city of this IssuerDetails.  # noqa: E501


        :return: The billing_address_city of this IssuerDetails.  # noqa: E501
        :rtype: str
        """
        return self._billing_address_city

    @billing_address_city.setter
    def billing_address_city(self, billing_address_city):
        """Sets the billing_address_city of this IssuerDetails.


        :param billing_address_city: The billing_address_city of this IssuerDetails.  # noqa: E501
        :type: str
        """

        self._billing_address_city = billing_address_city

    @property
    def billing_address_state(self):
        """Gets the billing_address_state of this IssuerDetails.  # noqa: E501


        :return: The billing_address_state of this IssuerDetails.  # noqa: E501
        :rtype: str
        """
        return self._billing_address_state

    @billing_address_state.setter
    def billing_address_state(self, billing_address_state):
        """Sets the billing_address_state of this IssuerDetails.


        :param billing_address_state: The billing_address_state of this IssuerDetails.  # noqa: E501
        :type: str
        """

        self._billing_address_state = billing_address_state

    @property
    def billing_address_post_code(self):
        """Gets the billing_address_post_code of this IssuerDetails.  # noqa: E501


        :return: The billing_address_post_code of this IssuerDetails.  # noqa: E501
        :rtype: str
        """
        return self._billing_address_post_code

    @billing_address_post_code.setter
    def billing_address_post_code(self, billing_address_post_code):
        """Sets the billing_address_post_code of this IssuerDetails.


        :param billing_address_post_code: The billing_address_post_code of this IssuerDetails.  # noqa: E501
        :type: str
        """

        self._billing_address_post_code = billing_address_post_code

    @property
    def billing_country_code(self):
        """Gets the billing_country_code of this IssuerDetails.  # noqa: E501


        :return: The billing_country_code of this IssuerDetails.  # noqa: E501
        :rtype: str
        """
        return self._billing_country_code

    @billing_country_code.setter
    def billing_country_code(self, billing_country_code):
        """Sets the billing_country_code of this IssuerDetails.


        :param billing_country_code: The billing_country_code of this IssuerDetails.  # noqa: E501
        :type: str
        """

        self._billing_country_code = billing_country_code

    @property
    def tax_number(self):
        """Gets the tax_number of this IssuerDetails.  # noqa: E501


        :return: The tax_number of this IssuerDetails.  # noqa: E501
        :rtype: str
        """
        return self._tax_number

    @tax_number.setter
    def tax_number(self, tax_number):
        """Sets the tax_number of this IssuerDetails.


        :param tax_number: The tax_number of this IssuerDetails.  # noqa: E501
        :type: str
        """

        self._tax_number = tax_number

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
        if not isinstance(other, IssuerDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other