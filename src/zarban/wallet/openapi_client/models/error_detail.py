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


class ErrorDetail(object):
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
        'user_message': 'str',
        'solutions': 'list[str]'
    }

    attribute_map = {
        'user_message': 'userMessage',
        'solutions': 'solutions'
    }

    def __init__(self, user_message=None, solutions=None, local_vars_configuration=None):  # noqa: E501
        """ErrorDetail - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user_message = None
        self._solutions = None
        self.discriminator = None

        self.user_message = user_message
        self.solutions = solutions

    @property
    def user_message(self):
        """Gets the user_message of this ErrorDetail.  # noqa: E501

        User-friendly error message  # noqa: E501

        :return: The user_message of this ErrorDetail.  # noqa: E501
        :rtype: str
        """
        return self._user_message

    @user_message.setter
    def user_message(self, user_message):
        """Sets the user_message of this ErrorDetail.

        User-friendly error message  # noqa: E501

        :param user_message: The user_message of this ErrorDetail.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_message is None:  # noqa: E501
            raise ValueError("Invalid value for `user_message`, must not be `None`")  # noqa: E501

        self._user_message = user_message

    @property
    def solutions(self):
        """Gets the solutions of this ErrorDetail.  # noqa: E501


        :return: The solutions of this ErrorDetail.  # noqa: E501
        :rtype: list[str]
        """
        return self._solutions

    @solutions.setter
    def solutions(self, solutions):
        """Sets the solutions of this ErrorDetail.


        :param solutions: The solutions of this ErrorDetail.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and solutions is None:  # noqa: E501
            raise ValueError("Invalid value for `solutions`, must not be `None`")  # noqa: E501

        self._solutions = solutions

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
        if not isinstance(other, ErrorDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ErrorDetail):
            return True

        return self.to_dict() != other.to_dict()