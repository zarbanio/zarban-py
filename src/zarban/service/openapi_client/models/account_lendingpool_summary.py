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


class AccountLendingpoolSummary(object):
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
        'total_debt': 'dict(str, str)',
        'total_deposits': 'dict(str, str)',
        'total_collateral': 'dict(str, str)',
        'health_factor': 'str',
        'net_apy': 'str',
        'total_supply_apy': 'str',
        'total_borrow_apy': 'str',
        'available_to_borrow': 'dict(str, str)',
        'borrow_power_used': 'str',
        'current_liquidation_threshold': 'str',
        'loan_to_value': 'str'
    }

    attribute_map = {
        'total_debt': 'totalDebt',
        'total_deposits': 'totalDeposits',
        'total_collateral': 'totalCollateral',
        'health_factor': 'healthFactor',
        'net_apy': 'netApy',
        'total_supply_apy': 'totalSupplyApy',
        'total_borrow_apy': 'totalBorrowApy',
        'available_to_borrow': 'availableToBorrow',
        'borrow_power_used': 'borrowPowerUsed',
        'current_liquidation_threshold': 'currentLiquidationThreshold',
        'loan_to_value': 'loanToValue'
    }

    def __init__(self, total_debt=None, total_deposits=None, total_collateral=None, health_factor=None, net_apy=None, total_supply_apy=None, total_borrow_apy=None, available_to_borrow=None, borrow_power_used=None, current_liquidation_threshold=None, loan_to_value=None, local_vars_configuration=None):  # noqa: E501
        """AccountLendingpoolSummary - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._total_debt = None
        self._total_deposits = None
        self._total_collateral = None
        self._health_factor = None
        self._net_apy = None
        self._total_supply_apy = None
        self._total_borrow_apy = None
        self._available_to_borrow = None
        self._borrow_power_used = None
        self._current_liquidation_threshold = None
        self._loan_to_value = None
        self.discriminator = None

        self.total_debt = total_debt
        self.total_deposits = total_deposits
        self.total_collateral = total_collateral
        self.health_factor = health_factor
        self.net_apy = net_apy
        self.total_supply_apy = total_supply_apy
        self.total_borrow_apy = total_borrow_apy
        self.available_to_borrow = available_to_borrow
        self.borrow_power_used = borrow_power_used
        self.current_liquidation_threshold = current_liquidation_threshold
        self.loan_to_value = loan_to_value

    @property
    def total_debt(self):
        """Gets the total_debt of this AccountLendingpoolSummary.  # noqa: E501


        :return: The total_debt of this AccountLendingpoolSummary.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._total_debt

    @total_debt.setter
    def total_debt(self, total_debt):
        """Sets the total_debt of this AccountLendingpoolSummary.


        :param total_debt: The total_debt of this AccountLendingpoolSummary.  # noqa: E501
        :type: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and total_debt is None:  # noqa: E501
            raise ValueError("Invalid value for `total_debt`, must not be `None`")  # noqa: E501

        self._total_debt = total_debt

    @property
    def total_deposits(self):
        """Gets the total_deposits of this AccountLendingpoolSummary.  # noqa: E501


        :return: The total_deposits of this AccountLendingpoolSummary.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._total_deposits

    @total_deposits.setter
    def total_deposits(self, total_deposits):
        """Sets the total_deposits of this AccountLendingpoolSummary.


        :param total_deposits: The total_deposits of this AccountLendingpoolSummary.  # noqa: E501
        :type: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and total_deposits is None:  # noqa: E501
            raise ValueError("Invalid value for `total_deposits`, must not be `None`")  # noqa: E501

        self._total_deposits = total_deposits

    @property
    def total_collateral(self):
        """Gets the total_collateral of this AccountLendingpoolSummary.  # noqa: E501


        :return: The total_collateral of this AccountLendingpoolSummary.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._total_collateral

    @total_collateral.setter
    def total_collateral(self, total_collateral):
        """Sets the total_collateral of this AccountLendingpoolSummary.


        :param total_collateral: The total_collateral of this AccountLendingpoolSummary.  # noqa: E501
        :type: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and total_collateral is None:  # noqa: E501
            raise ValueError("Invalid value for `total_collateral`, must not be `None`")  # noqa: E501

        self._total_collateral = total_collateral

    @property
    def health_factor(self):
        """Gets the health_factor of this AccountLendingpoolSummary.  # noqa: E501

        Health factor in lending pool  # noqa: E501

        :return: The health_factor of this AccountLendingpoolSummary.  # noqa: E501
        :rtype: str
        """
        return self._health_factor

    @health_factor.setter
    def health_factor(self, health_factor):
        """Sets the health_factor of this AccountLendingpoolSummary.

        Health factor in lending pool  # noqa: E501

        :param health_factor: The health_factor of this AccountLendingpoolSummary.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and health_factor is None:  # noqa: E501
            raise ValueError("Invalid value for `health_factor`, must not be `None`")  # noqa: E501

        self._health_factor = health_factor

    @property
    def net_apy(self):
        """Gets the net_apy of this AccountLendingpoolSummary.  # noqa: E501

        Net annual percentage yield in lending pool  # noqa: E501

        :return: The net_apy of this AccountLendingpoolSummary.  # noqa: E501
        :rtype: str
        """
        return self._net_apy

    @net_apy.setter
    def net_apy(self, net_apy):
        """Sets the net_apy of this AccountLendingpoolSummary.

        Net annual percentage yield in lending pool  # noqa: E501

        :param net_apy: The net_apy of this AccountLendingpoolSummary.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and net_apy is None:  # noqa: E501
            raise ValueError("Invalid value for `net_apy`, must not be `None`")  # noqa: E501

        self._net_apy = net_apy

    @property
    def total_supply_apy(self):
        """Gets the total_supply_apy of this AccountLendingpoolSummary.  # noqa: E501

        Total supply rate in lending pool for account  # noqa: E501

        :return: The total_supply_apy of this AccountLendingpoolSummary.  # noqa: E501
        :rtype: str
        """
        return self._total_supply_apy

    @total_supply_apy.setter
    def total_supply_apy(self, total_supply_apy):
        """Sets the total_supply_apy of this AccountLendingpoolSummary.

        Total supply rate in lending pool for account  # noqa: E501

        :param total_supply_apy: The total_supply_apy of this AccountLendingpoolSummary.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and total_supply_apy is None:  # noqa: E501
            raise ValueError("Invalid value for `total_supply_apy`, must not be `None`")  # noqa: E501

        self._total_supply_apy = total_supply_apy

    @property
    def total_borrow_apy(self):
        """Gets the total_borrow_apy of this AccountLendingpoolSummary.  # noqa: E501

        Total borrow rate in lending pool for account  # noqa: E501

        :return: The total_borrow_apy of this AccountLendingpoolSummary.  # noqa: E501
        :rtype: str
        """
        return self._total_borrow_apy

    @total_borrow_apy.setter
    def total_borrow_apy(self, total_borrow_apy):
        """Sets the total_borrow_apy of this AccountLendingpoolSummary.

        Total borrow rate in lending pool for account  # noqa: E501

        :param total_borrow_apy: The total_borrow_apy of this AccountLendingpoolSummary.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and total_borrow_apy is None:  # noqa: E501
            raise ValueError("Invalid value for `total_borrow_apy`, must not be `None`")  # noqa: E501

        self._total_borrow_apy = total_borrow_apy

    @property
    def available_to_borrow(self):
        """Gets the available_to_borrow of this AccountLendingpoolSummary.  # noqa: E501


        :return: The available_to_borrow of this AccountLendingpoolSummary.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._available_to_borrow

    @available_to_borrow.setter
    def available_to_borrow(self, available_to_borrow):
        """Sets the available_to_borrow of this AccountLendingpoolSummary.


        :param available_to_borrow: The available_to_borrow of this AccountLendingpoolSummary.  # noqa: E501
        :type: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and available_to_borrow is None:  # noqa: E501
            raise ValueError("Invalid value for `available_to_borrow`, must not be `None`")  # noqa: E501

        self._available_to_borrow = available_to_borrow

    @property
    def borrow_power_used(self):
        """Gets the borrow_power_used of this AccountLendingpoolSummary.  # noqa: E501

        Borrow power used in lending pool  # noqa: E501

        :return: The borrow_power_used of this AccountLendingpoolSummary.  # noqa: E501
        :rtype: str
        """
        return self._borrow_power_used

    @borrow_power_used.setter
    def borrow_power_used(self, borrow_power_used):
        """Sets the borrow_power_used of this AccountLendingpoolSummary.

        Borrow power used in lending pool  # noqa: E501

        :param borrow_power_used: The borrow_power_used of this AccountLendingpoolSummary.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and borrow_power_used is None:  # noqa: E501
            raise ValueError("Invalid value for `borrow_power_used`, must not be `None`")  # noqa: E501

        self._borrow_power_used = borrow_power_used

    @property
    def current_liquidation_threshold(self):
        """Gets the current_liquidation_threshold of this AccountLendingpoolSummary.  # noqa: E501

        Current liquidation threshold in lending pool  # noqa: E501

        :return: The current_liquidation_threshold of this AccountLendingpoolSummary.  # noqa: E501
        :rtype: str
        """
        return self._current_liquidation_threshold

    @current_liquidation_threshold.setter
    def current_liquidation_threshold(self, current_liquidation_threshold):
        """Sets the current_liquidation_threshold of this AccountLendingpoolSummary.

        Current liquidation threshold in lending pool  # noqa: E501

        :param current_liquidation_threshold: The current_liquidation_threshold of this AccountLendingpoolSummary.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and current_liquidation_threshold is None:  # noqa: E501
            raise ValueError("Invalid value for `current_liquidation_threshold`, must not be `None`")  # noqa: E501

        self._current_liquidation_threshold = current_liquidation_threshold

    @property
    def loan_to_value(self):
        """Gets the loan_to_value of this AccountLendingpoolSummary.  # noqa: E501

        Loan to value in lending pool  # noqa: E501

        :return: The loan_to_value of this AccountLendingpoolSummary.  # noqa: E501
        :rtype: str
        """
        return self._loan_to_value

    @loan_to_value.setter
    def loan_to_value(self, loan_to_value):
        """Sets the loan_to_value of this AccountLendingpoolSummary.

        Loan to value in lending pool  # noqa: E501

        :param loan_to_value: The loan_to_value of this AccountLendingpoolSummary.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and loan_to_value is None:  # noqa: E501
            raise ValueError("Invalid value for `loan_to_value`, must not be `None`")  # noqa: E501

        self._loan_to_value = loan_to_value

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
        if not isinstance(other, AccountLendingpoolSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountLendingpoolSummary):
            return True

        return self.to_dict() != other.to_dict()
