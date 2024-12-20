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


class Payment(object):
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
        'amount': 'str',
        'hash': 'str',
        'url': 'str',
        'sender_first_name': 'str',
        'text': 'str',
        'share_url': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'hash': 'hash',
        'url': 'url',
        'sender_first_name': 'senderFirstName',
        'text': 'text',
        'share_url': 'shareUrl'
    }

    def __init__(self, amount=None, hash=None, url=None, sender_first_name=None, text=None, share_url=None, local_vars_configuration=None):  # noqa: E501
        """Payment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._amount = None
        self._hash = None
        self._url = None
        self._sender_first_name = None
        self._text = None
        self._share_url = None
        self.discriminator = None

        self.amount = amount
        self.hash = hash
        self.url = url
        self.sender_first_name = sender_first_name
        self.text = text
        self.share_url = share_url

    @property
    def amount(self):
        """Gets the amount of this Payment.  # noqa: E501

        Payment amount  # noqa: E501

        :return: The amount of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Payment.

        Payment amount  # noqa: E501

        :param amount: The amount of this Payment.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def hash(self):
        """Gets the hash of this Payment.  # noqa: E501

        Payment hash  # noqa: E501

        :return: The hash of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this Payment.

        Payment hash  # noqa: E501

        :param hash: The hash of this Payment.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and hash is None:  # noqa: E501
            raise ValueError("Invalid value for `hash`, must not be `None`")  # noqa: E501

        self._hash = hash

    @property
    def url(self):
        """Gets the url of this Payment.  # noqa: E501

        Payment URL  # noqa: E501

        :return: The url of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Payment.

        Payment URL  # noqa: E501

        :param url: The url of this Payment.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def sender_first_name(self):
        """Gets the sender_first_name of this Payment.  # noqa: E501

        Sender first name  # noqa: E501

        :return: The sender_first_name of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._sender_first_name

    @sender_first_name.setter
    def sender_first_name(self, sender_first_name):
        """Sets the sender_first_name of this Payment.

        Sender first name  # noqa: E501

        :param sender_first_name: The sender_first_name of this Payment.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and sender_first_name is None:  # noqa: E501
            raise ValueError("Invalid value for `sender_first_name`, must not be `None`")  # noqa: E501

        self._sender_first_name = sender_first_name

    @property
    def text(self):
        """Gets the text of this Payment.  # noqa: E501

        Payment text  # noqa: E501

        :return: The text of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Payment.

        Payment text  # noqa: E501

        :param text: The text of this Payment.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and text is None:  # noqa: E501
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def share_url(self):
        """Gets the share_url of this Payment.  # noqa: E501

        Share URL  # noqa: E501

        :return: The share_url of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._share_url

    @share_url.setter
    def share_url(self, share_url):
        """Sets the share_url of this Payment.

        Share URL  # noqa: E501

        :param share_url: The share_url of this Payment.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and share_url is None:  # noqa: E501
            raise ValueError("Invalid value for `share_url`, must not be `None`")  # noqa: E501

        self._share_url = share_url

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
        if not isinstance(other, Payment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Payment):
            return True

        return self.to_dict() != other.to_dict()
