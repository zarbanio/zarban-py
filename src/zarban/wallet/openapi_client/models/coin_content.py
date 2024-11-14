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


class CoinContent(object):
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
        'title': 'str',
        'text': 'str',
        'bollets': 'list[str]'
    }

    attribute_map = {
        'title': 'title',
        'text': 'text',
        'bollets': 'bollets'
    }

    def __init__(self, title=None, text=None, bollets=None, local_vars_configuration=None):  # noqa: E501
        """CoinContent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._title = None
        self._text = None
        self._bollets = None
        self.discriminator = None

        self.title = title
        self.text = text
        self.bollets = bollets

    @property
    def title(self):
        """Gets the title of this CoinContent.  # noqa: E501


        :return: The title of this CoinContent.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CoinContent.


        :param title: The title of this CoinContent.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def text(self):
        """Gets the text of this CoinContent.  # noqa: E501


        :return: The text of this CoinContent.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this CoinContent.


        :param text: The text of this CoinContent.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and text is None:  # noqa: E501
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def bollets(self):
        """Gets the bollets of this CoinContent.  # noqa: E501


        :return: The bollets of this CoinContent.  # noqa: E501
        :rtype: list[str]
        """
        return self._bollets

    @bollets.setter
    def bollets(self, bollets):
        """Sets the bollets of this CoinContent.


        :param bollets: The bollets of this CoinContent.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and bollets is None:  # noqa: E501
            raise ValueError("Invalid value for `bollets`, must not be `None`")  # noqa: E501

        self._bollets = bollets

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
        if not isinstance(other, CoinContent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CoinContent):
            return True

        return self.to_dict() != other.to_dict()
