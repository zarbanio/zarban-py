# coding: utf-8

"""
    Zarban API

    API for Zarban services.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from zarban.service.openapi_client.configuration import Configuration


class LendingpoolBorrow(object):
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
        'underlying_asset': 'Token',
        'amount': 'dict(str, str)',
        'borrow_rate': 'str',
        'max_borrow_amount': 'dict(str, str)'
    }

    attribute_map = {
        'user': 'user',
        'underlying_asset': 'underlyingAsset',
        'amount': 'amount',
        'borrow_rate': 'borrowRate',
        'max_borrow_amount': 'maxBorrowAmount'
    }

    def __init__(self, user=None, underlying_asset=None, amount=None, borrow_rate=None, max_borrow_amount=None, local_vars_configuration=None):  # noqa: E501
        """LendingpoolBorrow - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user = None
        self._underlying_asset = None
        self._amount = None
        self._borrow_rate = None
        self._max_borrow_amount = None
        self.discriminator = None

        self.user = user
        self.underlying_asset = underlying_asset
        self.amount = amount
        self.borrow_rate = borrow_rate
        self.max_borrow_amount = max_borrow_amount

    @property
    def user(self):
        """Gets the user of this LendingpoolBorrow.  # noqa: E501

        The Ethereum address of the user.  # noqa: E501

        :return: The user of this LendingpoolBorrow.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this LendingpoolBorrow.

        The Ethereum address of the user.  # noqa: E501

        :param user: The user of this LendingpoolBorrow.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def underlying_asset(self):
        """Gets the underlying_asset of this LendingpoolBorrow.  # noqa: E501


        :return: The underlying_asset of this LendingpoolBorrow.  # noqa: E501
        :rtype: Token
        """
        return self._underlying_asset

    @underlying_asset.setter
    def underlying_asset(self, underlying_asset):
        """Sets the underlying_asset of this LendingpoolBorrow.


        :param underlying_asset: The underlying_asset of this LendingpoolBorrow.  # noqa: E501
        :type: Token
        """
        if self.local_vars_configuration.client_side_validation and underlying_asset is None:  # noqa: E501
            raise ValueError("Invalid value for `underlying_asset`, must not be `None`")  # noqa: E501

        self._underlying_asset = underlying_asset

    @property
    def amount(self):
        """Gets the amount of this LendingpoolBorrow.  # noqa: E501


        :return: The amount of this LendingpoolBorrow.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this LendingpoolBorrow.


        :param amount: The amount of this LendingpoolBorrow.  # noqa: E501
        :type: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def borrow_rate(self):
        """Gets the borrow_rate of this LendingpoolBorrow.  # noqa: E501

        The borrow rate.  # noqa: E501

        :return: The borrow_rate of this LendingpoolBorrow.  # noqa: E501
        :rtype: str
        """
        return self._borrow_rate

    @borrow_rate.setter
    def borrow_rate(self, borrow_rate):
        """Sets the borrow_rate of this LendingpoolBorrow.

        The borrow rate.  # noqa: E501

        :param borrow_rate: The borrow_rate of this LendingpoolBorrow.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and borrow_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `borrow_rate`, must not be `None`")  # noqa: E501

        self._borrow_rate = borrow_rate

    @property
    def max_borrow_amount(self):
        """Gets the max_borrow_amount of this LendingpoolBorrow.  # noqa: E501


        :return: The max_borrow_amount of this LendingpoolBorrow.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._max_borrow_amount

    @max_borrow_amount.setter
    def max_borrow_amount(self, max_borrow_amount):
        """Sets the max_borrow_amount of this LendingpoolBorrow.


        :param max_borrow_amount: The max_borrow_amount of this LendingpoolBorrow.  # noqa: E501
        :type: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and max_borrow_amount is None:  # noqa: E501
            raise ValueError("Invalid value for `max_borrow_amount`, must not be `None`")  # noqa: E501

        self._max_borrow_amount = max_borrow_amount

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
        if not isinstance(other, LendingpoolBorrow):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LendingpoolBorrow):
            return True

        return self.to_dict() != other.to_dict()
