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


class Account(object):
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
        'points': 'int',
        'address': 'str',
        'wallet_balance': 'WalletBalance',
        'net_worth': 'dict(str, str)',
        'total_debt': 'dict(str, str)',
        'total_deposits': 'dict(str, str)',
        'lendingpool_summary': 'AccountLendingpoolSummary',
        'stabelcoin_system_summary': 'AccountStablecoinSystemSummary'
    }

    attribute_map = {
        'points': 'points',
        'address': 'address',
        'wallet_balance': 'walletBalance',
        'net_worth': 'netWorth',
        'total_debt': 'totalDebt',
        'total_deposits': 'totalDeposits',
        'lendingpool_summary': 'lendingpoolSummary',
        'stabelcoin_system_summary': 'stabelcoinSystemSummary'
    }

    def __init__(self, points=None, address=None, wallet_balance=None, net_worth=None, total_debt=None, total_deposits=None, lendingpool_summary=None, stabelcoin_system_summary=None, local_vars_configuration=None):  # noqa: E501
        """Account - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._points = None
        self._address = None
        self._wallet_balance = None
        self._net_worth = None
        self._total_debt = None
        self._total_deposits = None
        self._lendingpool_summary = None
        self._stabelcoin_system_summary = None
        self.discriminator = None

        self.points = points
        self.address = address
        self.wallet_balance = wallet_balance
        self.net_worth = net_worth
        self.total_debt = total_debt
        self.total_deposits = total_deposits
        self.lendingpool_summary = lendingpool_summary
        self.stabelcoin_system_summary = stabelcoin_system_summary

    @property
    def points(self):
        """Gets the points of this Account.  # noqa: E501

        The number of points the account has.  # noqa: E501

        :return: The points of this Account.  # noqa: E501
        :rtype: int
        """
        return self._points

    @points.setter
    def points(self, points):
        """Sets the points of this Account.

        The number of points the account has.  # noqa: E501

        :param points: The points of this Account.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and points is None:  # noqa: E501
            raise ValueError("Invalid value for `points`, must not be `None`")  # noqa: E501

        self._points = points

    @property
    def address(self):
        """Gets the address of this Account.  # noqa: E501

        Ethereum address of the account  # noqa: E501

        :return: The address of this Account.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Account.

        Ethereum address of the account  # noqa: E501

        :param address: The address of this Account.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and address is None:  # noqa: E501
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def wallet_balance(self):
        """Gets the wallet_balance of this Account.  # noqa: E501


        :return: The wallet_balance of this Account.  # noqa: E501
        :rtype: WalletBalance
        """
        return self._wallet_balance

    @wallet_balance.setter
    def wallet_balance(self, wallet_balance):
        """Sets the wallet_balance of this Account.


        :param wallet_balance: The wallet_balance of this Account.  # noqa: E501
        :type: WalletBalance
        """
        if self.local_vars_configuration.client_side_validation and wallet_balance is None:  # noqa: E501
            raise ValueError("Invalid value for `wallet_balance`, must not be `None`")  # noqa: E501

        self._wallet_balance = wallet_balance

    @property
    def net_worth(self):
        """Gets the net_worth of this Account.  # noqa: E501


        :return: The net_worth of this Account.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._net_worth

    @net_worth.setter
    def net_worth(self, net_worth):
        """Sets the net_worth of this Account.


        :param net_worth: The net_worth of this Account.  # noqa: E501
        :type: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and net_worth is None:  # noqa: E501
            raise ValueError("Invalid value for `net_worth`, must not be `None`")  # noqa: E501

        self._net_worth = net_worth

    @property
    def total_debt(self):
        """Gets the total_debt of this Account.  # noqa: E501


        :return: The total_debt of this Account.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._total_debt

    @total_debt.setter
    def total_debt(self, total_debt):
        """Sets the total_debt of this Account.


        :param total_debt: The total_debt of this Account.  # noqa: E501
        :type: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and total_debt is None:  # noqa: E501
            raise ValueError("Invalid value for `total_debt`, must not be `None`")  # noqa: E501

        self._total_debt = total_debt

    @property
    def total_deposits(self):
        """Gets the total_deposits of this Account.  # noqa: E501


        :return: The total_deposits of this Account.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._total_deposits

    @total_deposits.setter
    def total_deposits(self, total_deposits):
        """Sets the total_deposits of this Account.


        :param total_deposits: The total_deposits of this Account.  # noqa: E501
        :type: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and total_deposits is None:  # noqa: E501
            raise ValueError("Invalid value for `total_deposits`, must not be `None`")  # noqa: E501

        self._total_deposits = total_deposits

    @property
    def lendingpool_summary(self):
        """Gets the lendingpool_summary of this Account.  # noqa: E501


        :return: The lendingpool_summary of this Account.  # noqa: E501
        :rtype: AccountLendingpoolSummary
        """
        return self._lendingpool_summary

    @lendingpool_summary.setter
    def lendingpool_summary(self, lendingpool_summary):
        """Sets the lendingpool_summary of this Account.


        :param lendingpool_summary: The lendingpool_summary of this Account.  # noqa: E501
        :type: AccountLendingpoolSummary
        """
        if self.local_vars_configuration.client_side_validation and lendingpool_summary is None:  # noqa: E501
            raise ValueError("Invalid value for `lendingpool_summary`, must not be `None`")  # noqa: E501

        self._lendingpool_summary = lendingpool_summary

    @property
    def stabelcoin_system_summary(self):
        """Gets the stabelcoin_system_summary of this Account.  # noqa: E501


        :return: The stabelcoin_system_summary of this Account.  # noqa: E501
        :rtype: AccountStablecoinSystemSummary
        """
        return self._stabelcoin_system_summary

    @stabelcoin_system_summary.setter
    def stabelcoin_system_summary(self, stabelcoin_system_summary):
        """Sets the stabelcoin_system_summary of this Account.


        :param stabelcoin_system_summary: The stabelcoin_system_summary of this Account.  # noqa: E501
        :type: AccountStablecoinSystemSummary
        """
        if self.local_vars_configuration.client_side_validation and stabelcoin_system_summary is None:  # noqa: E501
            raise ValueError("Invalid value for `stabelcoin_system_summary`, must not be `None`")  # noqa: E501

        self._stabelcoin_system_summary = stabelcoin_system_summary

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
        if not isinstance(other, Account):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Account):
            return True

        return self.to_dict() != other.to_dict()
