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


class CreditNoteAllocation(object):
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
        'transaction_allocation_id': 'int',
        'invoice_transaction_idfk': 'int',
        'credit_note_transaction_idfk': 'int',
        'allocation_date': 'datetime',
        'allocation_amount': 'float'
    }

    attribute_map = {
        'transaction_allocation_id': 'TransactionAllocationID',
        'invoice_transaction_idfk': 'InvoiceTransactionIDFK',
        'credit_note_transaction_idfk': 'CreditNoteTransactionIDFK',
        'allocation_date': 'AllocationDate',
        'allocation_amount': 'AllocationAmount'
    }

    def __init__(self, transaction_allocation_id=None, invoice_transaction_idfk=None, credit_note_transaction_idfk=None, allocation_date=None, allocation_amount=None):  # noqa: E501
        """CreditNoteAllocation - a model defined in Swagger"""  # noqa: E501

        self._transaction_allocation_id = None
        self._invoice_transaction_idfk = None
        self._credit_note_transaction_idfk = None
        self._allocation_date = None
        self._allocation_amount = None
        self.discriminator = None

        if transaction_allocation_id is not None:
            self.transaction_allocation_id = transaction_allocation_id
        if invoice_transaction_idfk is not None:
            self.invoice_transaction_idfk = invoice_transaction_idfk
        if credit_note_transaction_idfk is not None:
            self.credit_note_transaction_idfk = credit_note_transaction_idfk
        if allocation_date is not None:
            self.allocation_date = allocation_date
        if allocation_amount is not None:
            self.allocation_amount = allocation_amount

    @property
    def transaction_allocation_id(self):
        """Gets the transaction_allocation_id of this CreditNoteAllocation.  # noqa: E501


        :return: The transaction_allocation_id of this CreditNoteAllocation.  # noqa: E501
        :rtype: int
        """
        return self._transaction_allocation_id

    @transaction_allocation_id.setter
    def transaction_allocation_id(self, transaction_allocation_id):
        """Sets the transaction_allocation_id of this CreditNoteAllocation.


        :param transaction_allocation_id: The transaction_allocation_id of this CreditNoteAllocation.  # noqa: E501
        :type: int
        """

        self._transaction_allocation_id = transaction_allocation_id

    @property
    def invoice_transaction_idfk(self):
        """Gets the invoice_transaction_idfk of this CreditNoteAllocation.  # noqa: E501


        :return: The invoice_transaction_idfk of this CreditNoteAllocation.  # noqa: E501
        :rtype: int
        """
        return self._invoice_transaction_idfk

    @invoice_transaction_idfk.setter
    def invoice_transaction_idfk(self, invoice_transaction_idfk):
        """Sets the invoice_transaction_idfk of this CreditNoteAllocation.


        :param invoice_transaction_idfk: The invoice_transaction_idfk of this CreditNoteAllocation.  # noqa: E501
        :type: int
        """

        self._invoice_transaction_idfk = invoice_transaction_idfk

    @property
    def credit_note_transaction_idfk(self):
        """Gets the credit_note_transaction_idfk of this CreditNoteAllocation.  # noqa: E501


        :return: The credit_note_transaction_idfk of this CreditNoteAllocation.  # noqa: E501
        :rtype: int
        """
        return self._credit_note_transaction_idfk

    @credit_note_transaction_idfk.setter
    def credit_note_transaction_idfk(self, credit_note_transaction_idfk):
        """Sets the credit_note_transaction_idfk of this CreditNoteAllocation.


        :param credit_note_transaction_idfk: The credit_note_transaction_idfk of this CreditNoteAllocation.  # noqa: E501
        :type: int
        """

        self._credit_note_transaction_idfk = credit_note_transaction_idfk

    @property
    def allocation_date(self):
        """Gets the allocation_date of this CreditNoteAllocation.  # noqa: E501


        :return: The allocation_date of this CreditNoteAllocation.  # noqa: E501
        :rtype: datetime
        """
        return self._allocation_date

    @allocation_date.setter
    def allocation_date(self, allocation_date):
        """Sets the allocation_date of this CreditNoteAllocation.


        :param allocation_date: The allocation_date of this CreditNoteAllocation.  # noqa: E501
        :type: datetime
        """

        self._allocation_date = allocation_date

    @property
    def allocation_amount(self):
        """Gets the allocation_amount of this CreditNoteAllocation.  # noqa: E501


        :return: The allocation_amount of this CreditNoteAllocation.  # noqa: E501
        :rtype: float
        """
        return self._allocation_amount

    @allocation_amount.setter
    def allocation_amount(self, allocation_amount):
        """Sets the allocation_amount of this CreditNoteAllocation.


        :param allocation_amount: The allocation_amount of this CreditNoteAllocation.  # noqa: E501
        :type: float
        """

        self._allocation_amount = allocation_amount

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
        if not isinstance(other, CreditNoteAllocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
