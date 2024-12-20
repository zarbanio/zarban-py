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


class VaultEvent(object):
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
        'delta_collateral': 'dict(str, str)',
        'delta_debt': 'dict(str, str)',
        'ilk': 'Ilk'
    }

    attribute_map = {
        'delta_collateral': 'deltaCollateral',
        'delta_debt': 'deltaDebt',
        'ilk': 'ilk'
    }

    def __init__(self, delta_collateral=None, delta_debt=None, ilk=None, local_vars_configuration=None):  # noqa: E501
        """VaultEvent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._delta_collateral = None
        self._delta_debt = None
        self._ilk = None
        self.discriminator = None

        self.delta_collateral = delta_collateral
        self.delta_debt = delta_debt
        self.ilk = ilk

    @property
    def delta_collateral(self):
        """Gets the delta_collateral of this VaultEvent.  # noqa: E501


        :return: The delta_collateral of this VaultEvent.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._delta_collateral

    @delta_collateral.setter
    def delta_collateral(self, delta_collateral):
        """Sets the delta_collateral of this VaultEvent.


        :param delta_collateral: The delta_collateral of this VaultEvent.  # noqa: E501
        :type: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and delta_collateral is None:  # noqa: E501
            raise ValueError("Invalid value for `delta_collateral`, must not be `None`")  # noqa: E501

        self._delta_collateral = delta_collateral

    @property
    def delta_debt(self):
        """Gets the delta_debt of this VaultEvent.  # noqa: E501


        :return: The delta_debt of this VaultEvent.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._delta_debt

    @delta_debt.setter
    def delta_debt(self, delta_debt):
        """Sets the delta_debt of this VaultEvent.


        :param delta_debt: The delta_debt of this VaultEvent.  # noqa: E501
        :type: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and delta_debt is None:  # noqa: E501
            raise ValueError("Invalid value for `delta_debt`, must not be `None`")  # noqa: E501

        self._delta_debt = delta_debt

    @property
    def ilk(self):
        """Gets the ilk of this VaultEvent.  # noqa: E501


        :return: The ilk of this VaultEvent.  # noqa: E501
        :rtype: Ilk
        """
        return self._ilk

    @ilk.setter
    def ilk(self, ilk):
        """Sets the ilk of this VaultEvent.


        :param ilk: The ilk of this VaultEvent.  # noqa: E501
        :type: Ilk
        """
        if self.local_vars_configuration.client_side_validation and ilk is None:  # noqa: E501
            raise ValueError("Invalid value for `ilk`, must not be `None`")  # noqa: E501

        self._ilk = ilk

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
        if not isinstance(other, VaultEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VaultEvent):
            return True

        return self.to_dict() != other.to_dict()
