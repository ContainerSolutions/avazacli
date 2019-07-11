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


class TaxComponent(object):
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
        'tax_component_id': 'int',
        'tax_idfk': 'int',
        'component_tax_code': 'str',
        'name': 'str',
        'percentage': 'float',
        'is_compound': 'bool'
    }

    attribute_map = {
        'tax_component_id': 'TaxComponentID',
        'tax_idfk': 'TaxIDFK',
        'component_tax_code': 'ComponentTaxCode',
        'name': 'Name',
        'percentage': 'Percentage',
        'is_compound': 'isCompound'
    }

    def __init__(self, tax_component_id=None, tax_idfk=None, component_tax_code=None, name=None, percentage=None, is_compound=None):  # noqa: E501
        """TaxComponent - a model defined in Swagger"""  # noqa: E501

        self._tax_component_id = None
        self._tax_idfk = None
        self._component_tax_code = None
        self._name = None
        self._percentage = None
        self._is_compound = None
        self.discriminator = None

        if tax_component_id is not None:
            self.tax_component_id = tax_component_id
        if tax_idfk is not None:
            self.tax_idfk = tax_idfk
        if component_tax_code is not None:
            self.component_tax_code = component_tax_code
        if name is not None:
            self.name = name
        if percentage is not None:
            self.percentage = percentage
        if is_compound is not None:
            self.is_compound = is_compound

    @property
    def tax_component_id(self):
        """Gets the tax_component_id of this TaxComponent.  # noqa: E501


        :return: The tax_component_id of this TaxComponent.  # noqa: E501
        :rtype: int
        """
        return self._tax_component_id

    @tax_component_id.setter
    def tax_component_id(self, tax_component_id):
        """Sets the tax_component_id of this TaxComponent.


        :param tax_component_id: The tax_component_id of this TaxComponent.  # noqa: E501
        :type: int
        """

        self._tax_component_id = tax_component_id

    @property
    def tax_idfk(self):
        """Gets the tax_idfk of this TaxComponent.  # noqa: E501


        :return: The tax_idfk of this TaxComponent.  # noqa: E501
        :rtype: int
        """
        return self._tax_idfk

    @tax_idfk.setter
    def tax_idfk(self, tax_idfk):
        """Sets the tax_idfk of this TaxComponent.


        :param tax_idfk: The tax_idfk of this TaxComponent.  # noqa: E501
        :type: int
        """

        self._tax_idfk = tax_idfk

    @property
    def component_tax_code(self):
        """Gets the component_tax_code of this TaxComponent.  # noqa: E501


        :return: The component_tax_code of this TaxComponent.  # noqa: E501
        :rtype: str
        """
        return self._component_tax_code

    @component_tax_code.setter
    def component_tax_code(self, component_tax_code):
        """Sets the component_tax_code of this TaxComponent.


        :param component_tax_code: The component_tax_code of this TaxComponent.  # noqa: E501
        :type: str
        """

        self._component_tax_code = component_tax_code

    @property
    def name(self):
        """Gets the name of this TaxComponent.  # noqa: E501


        :return: The name of this TaxComponent.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TaxComponent.


        :param name: The name of this TaxComponent.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def percentage(self):
        """Gets the percentage of this TaxComponent.  # noqa: E501


        :return: The percentage of this TaxComponent.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this TaxComponent.


        :param percentage: The percentage of this TaxComponent.  # noqa: E501
        :type: float
        """

        self._percentage = percentage

    @property
    def is_compound(self):
        """Gets the is_compound of this TaxComponent.  # noqa: E501


        :return: The is_compound of this TaxComponent.  # noqa: E501
        :rtype: bool
        """
        return self._is_compound

    @is_compound.setter
    def is_compound(self, is_compound):
        """Sets the is_compound of this TaxComponent.


        :param is_compound: The is_compound of this TaxComponent.  # noqa: E501
        :type: bool
        """

        self._is_compound = is_compound

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
        if not isinstance(other, TaxComponent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other