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


class LendingpoolBorrowEvent(object):
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
        'id': 'int',
        'reserve': 'str',
        'user': 'str',
        'on_behalf_of': 'str',
        'amount': 'str',
        'borrow_rate_mode': 'str',
        'borrow_rate': 'str',
        'referral': 'int',
        'raw': 'Log'
    }

    attribute_map = {
        'id': 'id',
        'reserve': 'reserve',
        'user': 'user',
        'on_behalf_of': 'onBehalfOf',
        'amount': 'amount',
        'borrow_rate_mode': 'borrowRateMode',
        'borrow_rate': 'borrowRate',
        'referral': 'referral',
        'raw': 'raw'
    }

    def __init__(self, id=None, reserve=None, user=None, on_behalf_of=None, amount=None, borrow_rate_mode=None, borrow_rate=None, referral=None, raw=None, local_vars_configuration=None):  # noqa: E501
        """LendingpoolBorrowEvent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._reserve = None
        self._user = None
        self._on_behalf_of = None
        self._amount = None
        self._borrow_rate_mode = None
        self._borrow_rate = None
        self._referral = None
        self._raw = None
        self.discriminator = None

        self.id = id
        self.reserve = reserve
        self.user = user
        if on_behalf_of is not None:
            self.on_behalf_of = on_behalf_of
        self.amount = amount
        self.borrow_rate_mode = borrow_rate_mode
        self.borrow_rate = borrow_rate
        if referral is not None:
            self.referral = referral
        self.raw = raw

    @property
    def id(self):
        """Gets the id of this LendingpoolBorrowEvent.  # noqa: E501

        Identifier for the borrow event.  # noqa: E501

        :return: The id of this LendingpoolBorrowEvent.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LendingpoolBorrowEvent.

        Identifier for the borrow event.  # noqa: E501

        :param id: The id of this LendingpoolBorrowEvent.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def reserve(self):
        """Gets the reserve of this LendingpoolBorrowEvent.  # noqa: E501

        Ethereum address of the reserve from which the amount was borrowed.  # noqa: E501

        :return: The reserve of this LendingpoolBorrowEvent.  # noqa: E501
        :rtype: str
        """
        return self._reserve

    @reserve.setter
    def reserve(self, reserve):
        """Sets the reserve of this LendingpoolBorrowEvent.

        Ethereum address of the reserve from which the amount was borrowed.  # noqa: E501

        :param reserve: The reserve of this LendingpoolBorrowEvent.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and reserve is None:  # noqa: E501
            raise ValueError("Invalid value for `reserve`, must not be `None`")  # noqa: E501

        self._reserve = reserve

    @property
    def user(self):
        """Gets the user of this LendingpoolBorrowEvent.  # noqa: E501

        Ethereum address of the user who borrowed.  # noqa: E501

        :return: The user of this LendingpoolBorrowEvent.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this LendingpoolBorrowEvent.

        Ethereum address of the user who borrowed.  # noqa: E501

        :param user: The user of this LendingpoolBorrowEvent.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def on_behalf_of(self):
        """Gets the on_behalf_of of this LendingpoolBorrowEvent.  # noqa: E501

        Ethereum address of the entity on whose behalf the borrowing occurred.  # noqa: E501

        :return: The on_behalf_of of this LendingpoolBorrowEvent.  # noqa: E501
        :rtype: str
        """
        return self._on_behalf_of

    @on_behalf_of.setter
    def on_behalf_of(self, on_behalf_of):
        """Sets the on_behalf_of of this LendingpoolBorrowEvent.

        Ethereum address of the entity on whose behalf the borrowing occurred.  # noqa: E501

        :param on_behalf_of: The on_behalf_of of this LendingpoolBorrowEvent.  # noqa: E501
        :type: str
        """

        self._on_behalf_of = on_behalf_of

    @property
    def amount(self):
        """Gets the amount of this LendingpoolBorrowEvent.  # noqa: E501

        The borrowed amount.  # noqa: E501

        :return: The amount of this LendingpoolBorrowEvent.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this LendingpoolBorrowEvent.

        The borrowed amount.  # noqa: E501

        :param amount: The amount of this LendingpoolBorrowEvent.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def borrow_rate_mode(self):
        """Gets the borrow_rate_mode of this LendingpoolBorrowEvent.  # noqa: E501

        The mode of borrowing rate (e.g., stable, variable).  # noqa: E501

        :return: The borrow_rate_mode of this LendingpoolBorrowEvent.  # noqa: E501
        :rtype: str
        """
        return self._borrow_rate_mode

    @borrow_rate_mode.setter
    def borrow_rate_mode(self, borrow_rate_mode):
        """Sets the borrow_rate_mode of this LendingpoolBorrowEvent.

        The mode of borrowing rate (e.g., stable, variable).  # noqa: E501

        :param borrow_rate_mode: The borrow_rate_mode of this LendingpoolBorrowEvent.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and borrow_rate_mode is None:  # noqa: E501
            raise ValueError("Invalid value for `borrow_rate_mode`, must not be `None`")  # noqa: E501

        self._borrow_rate_mode = borrow_rate_mode

    @property
    def borrow_rate(self):
        """Gets the borrow_rate of this LendingpoolBorrowEvent.  # noqa: E501

        The interest rate for the borrowed amount.  # noqa: E501

        :return: The borrow_rate of this LendingpoolBorrowEvent.  # noqa: E501
        :rtype: str
        """
        return self._borrow_rate

    @borrow_rate.setter
    def borrow_rate(self, borrow_rate):
        """Sets the borrow_rate of this LendingpoolBorrowEvent.

        The interest rate for the borrowed amount.  # noqa: E501

        :param borrow_rate: The borrow_rate of this LendingpoolBorrowEvent.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and borrow_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `borrow_rate`, must not be `None`")  # noqa: E501

        self._borrow_rate = borrow_rate

    @property
    def referral(self):
        """Gets the referral of this LendingpoolBorrowEvent.  # noqa: E501

        Referral code or identifier.  # noqa: E501

        :return: The referral of this LendingpoolBorrowEvent.  # noqa: E501
        :rtype: int
        """
        return self._referral

    @referral.setter
    def referral(self, referral):
        """Sets the referral of this LendingpoolBorrowEvent.

        Referral code or identifier.  # noqa: E501

        :param referral: The referral of this LendingpoolBorrowEvent.  # noqa: E501
        :type: int
        """

        self._referral = referral

    @property
    def raw(self):
        """Gets the raw of this LendingpoolBorrowEvent.  # noqa: E501


        :return: The raw of this LendingpoolBorrowEvent.  # noqa: E501
        :rtype: Log
        """
        return self._raw

    @raw.setter
    def raw(self, raw):
        """Sets the raw of this LendingpoolBorrowEvent.


        :param raw: The raw of this LendingpoolBorrowEvent.  # noqa: E501
        :type: Log
        """
        if self.local_vars_configuration.client_side_validation and raw is None:  # noqa: E501
            raise ValueError("Invalid value for `raw`, must not be `None`")  # noqa: E501

        self._raw = raw

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
        if not isinstance(other, LendingpoolBorrowEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LendingpoolBorrowEvent):
            return True

        return self.to_dict() != other.to_dict()
