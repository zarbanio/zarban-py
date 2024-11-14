# coding: utf-8

"""
    Zarban Wallet API

    API for Zarban wallet services.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from zarban.wallet.openapi_client.configuration import Configuration


class WithdrawRequestBody(object):
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
        'network': 'str',
        'symbol': 'str',
        'amount': 'str',
        'address': 'str',
        'comment': 'str'
    }

    attribute_map = {
        'network': 'network',
        'symbol': 'symbol',
        'amount': 'amount',
        'address': 'address',
        'comment': 'comment'
    }

    def __init__(self, network=None, symbol=None, amount=None, address=None, comment=None, local_vars_configuration=None):  # noqa: E501
        """WithdrawRequestBody - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._network = None
        self._symbol = None
        self._amount = None
        self._address = None
        self._comment = None
        self.discriminator = None

        self.network = network
        self.symbol = symbol
        self.amount = amount
        self.address = address
        self.comment = comment

    @property
    def network(self):
        """Gets the network of this WithdrawRequestBody.  # noqa: E501

        Network to withdraw  # noqa: E501

        :return: The network of this WithdrawRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this WithdrawRequestBody.

        Network to withdraw  # noqa: E501

        :param network: The network of this WithdrawRequestBody.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and network is None:  # noqa: E501
            raise ValueError("Invalid value for `network`, must not be `None`")  # noqa: E501

        self._network = network

    @property
    def symbol(self):
        """Gets the symbol of this WithdrawRequestBody.  # noqa: E501

        Coin symbol  # noqa: E501

        :return: The symbol of this WithdrawRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this WithdrawRequestBody.

        Coin symbol  # noqa: E501

        :param symbol: The symbol of this WithdrawRequestBody.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and symbol is None:  # noqa: E501
            raise ValueError("Invalid value for `symbol`, must not be `None`")  # noqa: E501

        self._symbol = symbol

    @property
    def amount(self):
        """Gets the amount of this WithdrawRequestBody.  # noqa: E501

        Amount to withdraw  # noqa: E501

        :return: The amount of this WithdrawRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this WithdrawRequestBody.

        Amount to withdraw  # noqa: E501

        :param amount: The amount of this WithdrawRequestBody.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def address(self):
        """Gets the address of this WithdrawRequestBody.  # noqa: E501

        Withdrawal address  # noqa: E501

        :return: The address of this WithdrawRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this WithdrawRequestBody.

        Withdrawal address  # noqa: E501

        :param address: The address of this WithdrawRequestBody.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and address is None:  # noqa: E501
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def comment(self):
        """Gets the comment of this WithdrawRequestBody.  # noqa: E501


        :return: The comment of this WithdrawRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this WithdrawRequestBody.


        :param comment: The comment of this WithdrawRequestBody.  # noqa: E501
        :type: str
        """

        self._comment = comment

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
        if not isinstance(other, WithdrawRequestBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WithdrawRequestBody):
            return True

        return self.to_dict() != other.to_dict()
