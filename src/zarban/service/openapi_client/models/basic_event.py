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


class BasicEvent(object):
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
        'id': 'int',
        'name': 'EventName',
        'type': 'EventType',
        'domain': 'EventDomain',
        'raw': 'Log'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'domain': 'domain',
        'raw': 'raw'
    }

    def __init__(self, id=None, name=None, type=None, domain=None, raw=None, local_vars_configuration=None):  # noqa: E501
        """BasicEvent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._type = None
        self._domain = None
        self._raw = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.type = type
        self.domain = domain
        self.raw = raw

    @property
    def id(self):
        """Gets the id of this BasicEvent.  # noqa: E501

        Identifier for the event.  # noqa: E501

        :return: The id of this BasicEvent.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BasicEvent.

        Identifier for the event.  # noqa: E501

        :param id: The id of this BasicEvent.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this BasicEvent.  # noqa: E501


        :return: The name of this BasicEvent.  # noqa: E501
        :rtype: EventName
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BasicEvent.


        :param name: The name of this BasicEvent.  # noqa: E501
        :type: EventName
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this BasicEvent.  # noqa: E501


        :return: The type of this BasicEvent.  # noqa: E501
        :rtype: EventType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BasicEvent.


        :param type: The type of this BasicEvent.  # noqa: E501
        :type: EventType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def domain(self):
        """Gets the domain of this BasicEvent.  # noqa: E501


        :return: The domain of this BasicEvent.  # noqa: E501
        :rtype: EventDomain
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this BasicEvent.


        :param domain: The domain of this BasicEvent.  # noqa: E501
        :type: EventDomain
        """
        if self.local_vars_configuration.client_side_validation and domain is None:  # noqa: E501
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501

        self._domain = domain

    @property
    def raw(self):
        """Gets the raw of this BasicEvent.  # noqa: E501


        :return: The raw of this BasicEvent.  # noqa: E501
        :rtype: Log
        """
        return self._raw

    @raw.setter
    def raw(self, raw):
        """Sets the raw of this BasicEvent.


        :param raw: The raw of this BasicEvent.  # noqa: E501
        :type: Log
        """
        if self.local_vars_configuration.client_side_validation and raw is None:  # noqa: E501
            raise ValueError("Invalid value for `raw`, must not be `None`")  # noqa: E501

        self._raw = raw

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
        if not isinstance(other, BasicEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BasicEvent):
            return True

        return self.to_dict() != other.to_dict()
