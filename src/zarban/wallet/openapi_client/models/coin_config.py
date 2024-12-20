# coding: utf-8

"""
    Zarban Wallet API

    API for Zarban wallet services.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: info@zarban.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from zarban.wallet.openapi_client.configuration import Configuration


class CoinConfig(object):
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
        'is_tradeable': 'bool',
        'withdraw_fees': 'dict(str, str)',
        'min_withdrawal': 'dict(str, str)',
        'needs_memo': 'bool'
    }

    attribute_map = {
        'is_tradeable': 'isTradeable',
        'withdraw_fees': 'withdrawFees',
        'min_withdrawal': 'minWithdrawal',
        'needs_memo': 'needsMemo'
    }

    def __init__(self, is_tradeable=None, withdraw_fees=None, min_withdrawal=None, needs_memo=None, local_vars_configuration=None):  # noqa: E501
        """CoinConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._is_tradeable = None
        self._withdraw_fees = None
        self._min_withdrawal = None
        self._needs_memo = None
        self.discriminator = None

        self.is_tradeable = is_tradeable
        self.withdraw_fees = withdraw_fees
        self.min_withdrawal = min_withdrawal
        self.needs_memo = needs_memo

    @property
    def is_tradeable(self):
        """Gets the is_tradeable of this CoinConfig.  # noqa: E501


        :return: The is_tradeable of this CoinConfig.  # noqa: E501
        :rtype: bool
        """
        return self._is_tradeable

    @is_tradeable.setter
    def is_tradeable(self, is_tradeable):
        """Sets the is_tradeable of this CoinConfig.


        :param is_tradeable: The is_tradeable of this CoinConfig.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_tradeable is None:  # noqa: E501
            raise ValueError("Invalid value for `is_tradeable`, must not be `None`")  # noqa: E501

        self._is_tradeable = is_tradeable

    @property
    def withdraw_fees(self):
        """Gets the withdraw_fees of this CoinConfig.  # noqa: E501

        Map of network to amount  # noqa: E501

        :return: The withdraw_fees of this CoinConfig.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._withdraw_fees

    @withdraw_fees.setter
    def withdraw_fees(self, withdraw_fees):
        """Sets the withdraw_fees of this CoinConfig.

        Map of network to amount  # noqa: E501

        :param withdraw_fees: The withdraw_fees of this CoinConfig.  # noqa: E501
        :type: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and withdraw_fees is None:  # noqa: E501
            raise ValueError("Invalid value for `withdraw_fees`, must not be `None`")  # noqa: E501

        self._withdraw_fees = withdraw_fees

    @property
    def min_withdrawal(self):
        """Gets the min_withdrawal of this CoinConfig.  # noqa: E501

        Map of network to amount  # noqa: E501

        :return: The min_withdrawal of this CoinConfig.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._min_withdrawal

    @min_withdrawal.setter
    def min_withdrawal(self, min_withdrawal):
        """Sets the min_withdrawal of this CoinConfig.

        Map of network to amount  # noqa: E501

        :param min_withdrawal: The min_withdrawal of this CoinConfig.  # noqa: E501
        :type: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and min_withdrawal is None:  # noqa: E501
            raise ValueError("Invalid value for `min_withdrawal`, must not be `None`")  # noqa: E501

        self._min_withdrawal = min_withdrawal

    @property
    def needs_memo(self):
        """Gets the needs_memo of this CoinConfig.  # noqa: E501


        :return: The needs_memo of this CoinConfig.  # noqa: E501
        :rtype: bool
        """
        return self._needs_memo

    @needs_memo.setter
    def needs_memo(self, needs_memo):
        """Sets the needs_memo of this CoinConfig.


        :param needs_memo: The needs_memo of this CoinConfig.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and needs_memo is None:  # noqa: E501
            raise ValueError("Invalid value for `needs_memo`, must not be `None`")  # noqa: E501

        self._needs_memo = needs_memo

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
        if not isinstance(other, CoinConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CoinConfig):
            return True

        return self.to_dict() != other.to_dict()
