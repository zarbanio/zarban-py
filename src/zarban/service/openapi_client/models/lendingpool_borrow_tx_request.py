# coding: utf-8

"""
    Zarban API

    API for Zarban services.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: info@zarban.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from zarban.service.openapi_client.configuration import Configuration


class LendingpoolBorrowTxRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'user': 'str',
        'symbol': 'str',
        'amount': 'str'
    }

    attribute_map = {
        'user': 'user',
        'symbol': 'symbol',
        'amount': 'amount'
    }

    def __init__(self, user=None, symbol=None, amount=None, local_vars_configuration=None):  # noqa: E501
        """LendingpoolBorrowTxRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user = None
        self._symbol = None
        self._amount = None
        self.discriminator = None

        self.user = user
        self.symbol = symbol
        if amount is not None:
            self.amount = amount

    @property
    def user(self):
        """Gets the user of this LendingpoolBorrowTxRequest.  # noqa: E501

        Ethereum address of the user  # noqa: E501

        :return: The user of this LendingpoolBorrowTxRequest.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this LendingpoolBorrowTxRequest.

        Ethereum address of the user  # noqa: E501

        :param user: The user of this LendingpoolBorrowTxRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def symbol(self):
        """Gets the symbol of this LendingpoolBorrowTxRequest.  # noqa: E501


        :return: The symbol of this LendingpoolBorrowTxRequest.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this LendingpoolBorrowTxRequest.


        :param symbol: The symbol of this LendingpoolBorrowTxRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and symbol is None:  # noqa: E501
            raise ValueError("Invalid value for `symbol`, must not be `None`")  # noqa: E501

        self._symbol = symbol

    @property
    def amount(self):
        """Gets the amount of this LendingpoolBorrowTxRequest.  # noqa: E501

        The amount to borrow in native token units  # noqa: E501

        :return: The amount of this LendingpoolBorrowTxRequest.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this LendingpoolBorrowTxRequest.

        The amount to borrow in native token units  # noqa: E501

        :param amount: The amount of this LendingpoolBorrowTxRequest.  # noqa: E501
        :type: str
        """

        self._amount = amount

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, LendingpoolBorrowTxRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LendingpoolBorrowTxRequest):
            return True

        return self.to_dict() != other.to_dict()
