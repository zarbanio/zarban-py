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


class ReferralCreateRequest(object):
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
        'name': 'str',
        'usage_limit': 'int'
    }

    attribute_map = {
        'name': 'name',
        'usage_limit': 'usageLimit'
    }

    def __init__(self, name=None, usage_limit=None, local_vars_configuration=None):  # noqa: E501
        """ReferralCreateRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._usage_limit = None
        self.discriminator = None

        self.name = name
        self.usage_limit = usage_limit

    @property
    def name(self):
        """Gets the name of this ReferralCreateRequest.  # noqa: E501


        :return: The name of this ReferralCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReferralCreateRequest.


        :param name: The name of this ReferralCreateRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def usage_limit(self):
        """Gets the usage_limit of this ReferralCreateRequest.  # noqa: E501


        :return: The usage_limit of this ReferralCreateRequest.  # noqa: E501
        :rtype: int
        """
        return self._usage_limit

    @usage_limit.setter
    def usage_limit(self, usage_limit):
        """Sets the usage_limit of this ReferralCreateRequest.


        :param usage_limit: The usage_limit of this ReferralCreateRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and usage_limit is None:  # noqa: E501
            raise ValueError("Invalid value for `usage_limit`, must not be `None`")  # noqa: E501

        self._usage_limit = usage_limit

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
        if not isinstance(other, ReferralCreateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReferralCreateRequest):
            return True

        return self.to_dict() != other.to_dict()
