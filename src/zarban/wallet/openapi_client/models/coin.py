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


class Coin(object):
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
        'config': 'CoinConfig',
        'symbol': 'Symbol',
        'name': 'dict(str, str)',
        'logo_uri': 'str',
        'depositable_networks': 'list[Network]',
        'withdrawable_networks': 'list[Network]',
        'content': 'BulletContent'
    }

    attribute_map = {
        'config': 'config',
        'symbol': 'symbol',
        'name': 'name',
        'logo_uri': 'logoUri',
        'depositable_networks': 'depositableNetworks',
        'withdrawable_networks': 'withdrawableNetworks',
        'content': 'content'
    }

    def __init__(self, config=None, symbol=None, name=None, logo_uri=None, depositable_networks=None, withdrawable_networks=None, content=None, local_vars_configuration=None):  # noqa: E501
        """Coin - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._config = None
        self._symbol = None
        self._name = None
        self._logo_uri = None
        self._depositable_networks = None
        self._withdrawable_networks = None
        self._content = None
        self.discriminator = None

        self.config = config
        self.symbol = symbol
        self.name = name
        self.logo_uri = logo_uri
        self.depositable_networks = depositable_networks
        self.withdrawable_networks = withdrawable_networks
        self.content = content

    @property
    def config(self):
        """Gets the config of this Coin.  # noqa: E501


        :return: The config of this Coin.  # noqa: E501
        :rtype: CoinConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this Coin.


        :param config: The config of this Coin.  # noqa: E501
        :type: CoinConfig
        """
        if self.local_vars_configuration.client_side_validation and config is None:  # noqa: E501
            raise ValueError("Invalid value for `config`, must not be `None`")  # noqa: E501

        self._config = config

    @property
    def symbol(self):
        """Gets the symbol of this Coin.  # noqa: E501


        :return: The symbol of this Coin.  # noqa: E501
        :rtype: Symbol
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this Coin.


        :param symbol: The symbol of this Coin.  # noqa: E501
        :type: Symbol
        """
        if self.local_vars_configuration.client_side_validation and symbol is None:  # noqa: E501
            raise ValueError("Invalid value for `symbol`, must not be `None`")  # noqa: E501

        self._symbol = symbol

    @property
    def name(self):
        """Gets the name of this Coin.  # noqa: E501


        :return: The name of this Coin.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Coin.


        :param name: The name of this Coin.  # noqa: E501
        :type: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def logo_uri(self):
        """Gets the logo_uri of this Coin.  # noqa: E501


        :return: The logo_uri of this Coin.  # noqa: E501
        :rtype: str
        """
        return self._logo_uri

    @logo_uri.setter
    def logo_uri(self, logo_uri):
        """Sets the logo_uri of this Coin.


        :param logo_uri: The logo_uri of this Coin.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and logo_uri is None:  # noqa: E501
            raise ValueError("Invalid value for `logo_uri`, must not be `None`")  # noqa: E501

        self._logo_uri = logo_uri

    @property
    def depositable_networks(self):
        """Gets the depositable_networks of this Coin.  # noqa: E501


        :return: The depositable_networks of this Coin.  # noqa: E501
        :rtype: list[Network]
        """
        return self._depositable_networks

    @depositable_networks.setter
    def depositable_networks(self, depositable_networks):
        """Sets the depositable_networks of this Coin.


        :param depositable_networks: The depositable_networks of this Coin.  # noqa: E501
        :type: list[Network]
        """
        if self.local_vars_configuration.client_side_validation and depositable_networks is None:  # noqa: E501
            raise ValueError("Invalid value for `depositable_networks`, must not be `None`")  # noqa: E501

        self._depositable_networks = depositable_networks

    @property
    def withdrawable_networks(self):
        """Gets the withdrawable_networks of this Coin.  # noqa: E501


        :return: The withdrawable_networks of this Coin.  # noqa: E501
        :rtype: list[Network]
        """
        return self._withdrawable_networks

    @withdrawable_networks.setter
    def withdrawable_networks(self, withdrawable_networks):
        """Sets the withdrawable_networks of this Coin.


        :param withdrawable_networks: The withdrawable_networks of this Coin.  # noqa: E501
        :type: list[Network]
        """
        if self.local_vars_configuration.client_side_validation and withdrawable_networks is None:  # noqa: E501
            raise ValueError("Invalid value for `withdrawable_networks`, must not be `None`")  # noqa: E501

        self._withdrawable_networks = withdrawable_networks

    @property
    def content(self):
        """Gets the content of this Coin.  # noqa: E501


        :return: The content of this Coin.  # noqa: E501
        :rtype: BulletContent
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Coin.


        :param content: The content of this Coin.  # noqa: E501
        :type: BulletContent
        """
        if self.local_vars_configuration.client_side_validation and content is None:  # noqa: E501
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

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
        if not isinstance(other, Coin):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Coin):
            return True

        return self.to_dict() != other.to_dict()
