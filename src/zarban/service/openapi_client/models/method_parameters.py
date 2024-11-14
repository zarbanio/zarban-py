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


class MethodParameters(object):
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
        'to': 'str',
        'calldata': 'str',
        'value': 'str'
    }

    attribute_map = {
        'to': 'to',
        'calldata': 'calldata',
        'value': 'value'
    }

    def __init__(self, to=None, calldata=None, value=None, local_vars_configuration=None):  # noqa: E501
        """MethodParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._to = None
        self._calldata = None
        self._value = None
        self.discriminator = None

        self.to = to
        self.calldata = calldata
        self.value = value

    @property
    def to(self):
        """Gets the to of this MethodParameters.  # noqa: E501


        :return: The to of this MethodParameters.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this MethodParameters.


        :param to: The to of this MethodParameters.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and to is None:  # noqa: E501
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                to is not None and not re.search(r'^(0x)?[0-9a-fA-F]{40}$', to)):  # noqa: E501
            raise ValueError(r"Invalid value for `to`, must be a follow pattern or equal to `/^(0x)?[0-9a-fA-F]{40}$/`")  # noqa: E501

        self._to = to

    @property
    def calldata(self):
        """Gets the calldata of this MethodParameters.  # noqa: E501


        :return: The calldata of this MethodParameters.  # noqa: E501
        :rtype: str
        """
        return self._calldata

    @calldata.setter
    def calldata(self, calldata):
        """Sets the calldata of this MethodParameters.


        :param calldata: The calldata of this MethodParameters.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and calldata is None:  # noqa: E501
            raise ValueError("Invalid value for `calldata`, must not be `None`")  # noqa: E501

        self._calldata = calldata

    @property
    def value(self):
        """Gets the value of this MethodParameters.  # noqa: E501


        :return: The value of this MethodParameters.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this MethodParameters.


        :param value: The value of this MethodParameters.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if not isinstance(other, MethodParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MethodParameters):
            return True

        return self.to_dict() != other.to_dict()
