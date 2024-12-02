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


class PermitDetails(object):
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
        'token': 'str',
        'amount': 'str',
        'expiration': 'int',
        'nonce': 'str'
    }

    attribute_map = {
        'token': 'token',
        'amount': 'amount',
        'expiration': 'expiration',
        'nonce': 'nonce'
    }

    def __init__(self, token=None, amount=None, expiration=None, nonce=None, local_vars_configuration=None):  # noqa: E501
        """PermitDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._token = None
        self._amount = None
        self._expiration = None
        self._nonce = None
        self.discriminator = None

        self.token = token
        self.amount = amount
        self.expiration = expiration
        self.nonce = nonce

    @property
    def token(self):
        """Gets the token of this PermitDetails.  # noqa: E501


        :return: The token of this PermitDetails.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this PermitDetails.


        :param token: The token of this PermitDetails.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and token is None:  # noqa: E501
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                token is not None and not re.search(r'^(0x)?[0-9a-fA-F]{40}$', token)):  # noqa: E501
            raise ValueError(r"Invalid value for `token`, must be a follow pattern or equal to `/^(0x)?[0-9a-fA-F]{40}$/`")  # noqa: E501

        self._token = token

    @property
    def amount(self):
        """Gets the amount of this PermitDetails.  # noqa: E501


        :return: The amount of this PermitDetails.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PermitDetails.


        :param amount: The amount of this PermitDetails.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def expiration(self):
        """Gets the expiration of this PermitDetails.  # noqa: E501


        :return: The expiration of this PermitDetails.  # noqa: E501
        :rtype: int
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this PermitDetails.


        :param expiration: The expiration of this PermitDetails.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and expiration is None:  # noqa: E501
            raise ValueError("Invalid value for `expiration`, must not be `None`")  # noqa: E501

        self._expiration = expiration

    @property
    def nonce(self):
        """Gets the nonce of this PermitDetails.  # noqa: E501


        :return: The nonce of this PermitDetails.  # noqa: E501
        :rtype: str
        """
        return self._nonce

    @nonce.setter
    def nonce(self, nonce):
        """Sets the nonce of this PermitDetails.


        :param nonce: The nonce of this PermitDetails.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and nonce is None:  # noqa: E501
            raise ValueError("Invalid value for `nonce`, must not be `None`")  # noqa: E501

        self._nonce = nonce

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
        if not isinstance(other, PermitDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PermitDetails):
            return True

        return self.to_dict() != other.to_dict()
