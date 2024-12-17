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


class ChainActivityStepData(object):
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
        'type': 'str',
        'label': 'dict(str, str)',
        'gas_use_estimate': 'int',
        'gas_fee_estimate': 'dict(str, str)',
        'method_parameters': 'MethodParameters',
        'name': 'str',
        'typed_data': 'TypedData',
        'hash': 'str',
        'message': 'str'
    }

    attribute_map = {
        'type': 'type',
        'label': 'label',
        'gas_use_estimate': 'gasUseEstimate',
        'gas_fee_estimate': 'gasFeeEstimate',
        'method_parameters': 'methodParameters',
        'name': 'name',
        'typed_data': 'typedData',
        'hash': 'hash',
        'message': 'message'
    }

    discriminator_value_class_map = {
    }

    def __init__(self, type=None, label=None, gas_use_estimate=None, gas_fee_estimate=None, method_parameters=None, name=None, typed_data=None, hash=None, message=None, local_vars_configuration=None):  # noqa: E501
        """ChainActivityStepData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._label = None
        self._gas_use_estimate = None
        self._gas_fee_estimate = None
        self._method_parameters = None
        self._name = None
        self._typed_data = None
        self._hash = None
        self._message = None
        self.discriminator = 'type'

        self.type = type
        self.label = label
        self.gas_use_estimate = gas_use_estimate
        self.gas_fee_estimate = gas_fee_estimate
        self.method_parameters = method_parameters
        self.name = name
        self.typed_data = typed_data
        self.hash = hash
        self.message = message

    @property
    def type(self):
        """Gets the type of this ChainActivityStepData.  # noqa: E501


        :return: The type of this ChainActivityStepData.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ChainActivityStepData.


        :param type: The type of this ChainActivityStepData.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def label(self):
        """Gets the label of this ChainActivityStepData.  # noqa: E501


        :return: The label of this ChainActivityStepData.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ChainActivityStepData.


        :param label: The label of this ChainActivityStepData.  # noqa: E501
        :type: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and label is None:  # noqa: E501
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def gas_use_estimate(self):
        """Gets the gas_use_estimate of this ChainActivityStepData.  # noqa: E501


        :return: The gas_use_estimate of this ChainActivityStepData.  # noqa: E501
        :rtype: int
        """
        return self._gas_use_estimate

    @gas_use_estimate.setter
    def gas_use_estimate(self, gas_use_estimate):
        """Sets the gas_use_estimate of this ChainActivityStepData.


        :param gas_use_estimate: The gas_use_estimate of this ChainActivityStepData.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and gas_use_estimate is None:  # noqa: E501
            raise ValueError("Invalid value for `gas_use_estimate`, must not be `None`")  # noqa: E501

        self._gas_use_estimate = gas_use_estimate

    @property
    def gas_fee_estimate(self):
        """Gets the gas_fee_estimate of this ChainActivityStepData.  # noqa: E501


        :return: The gas_fee_estimate of this ChainActivityStepData.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._gas_fee_estimate

    @gas_fee_estimate.setter
    def gas_fee_estimate(self, gas_fee_estimate):
        """Sets the gas_fee_estimate of this ChainActivityStepData.


        :param gas_fee_estimate: The gas_fee_estimate of this ChainActivityStepData.  # noqa: E501
        :type: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and gas_fee_estimate is None:  # noqa: E501
            raise ValueError("Invalid value for `gas_fee_estimate`, must not be `None`")  # noqa: E501

        self._gas_fee_estimate = gas_fee_estimate

    @property
    def method_parameters(self):
        """Gets the method_parameters of this ChainActivityStepData.  # noqa: E501


        :return: The method_parameters of this ChainActivityStepData.  # noqa: E501
        :rtype: MethodParameters
        """
        return self._method_parameters

    @method_parameters.setter
    def method_parameters(self, method_parameters):
        """Sets the method_parameters of this ChainActivityStepData.


        :param method_parameters: The method_parameters of this ChainActivityStepData.  # noqa: E501
        :type: MethodParameters
        """
        if self.local_vars_configuration.client_side_validation and method_parameters is None:  # noqa: E501
            raise ValueError("Invalid value for `method_parameters`, must not be `None`")  # noqa: E501

        self._method_parameters = method_parameters

    @property
    def name(self):
        """Gets the name of this ChainActivityStepData.  # noqa: E501

        The name of the EIP712 signature  # noqa: E501

        :return: The name of this ChainActivityStepData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ChainActivityStepData.

        The name of the EIP712 signature  # noqa: E501

        :param name: The name of this ChainActivityStepData.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def typed_data(self):
        """Gets the typed_data of this ChainActivityStepData.  # noqa: E501


        :return: The typed_data of this ChainActivityStepData.  # noqa: E501
        :rtype: TypedData
        """
        return self._typed_data

    @typed_data.setter
    def typed_data(self, typed_data):
        """Sets the typed_data of this ChainActivityStepData.


        :param typed_data: The typed_data of this ChainActivityStepData.  # noqa: E501
        :type: TypedData
        """
        if self.local_vars_configuration.client_side_validation and typed_data is None:  # noqa: E501
            raise ValueError("Invalid value for `typed_data`, must not be `None`")  # noqa: E501

        self._typed_data = typed_data

    @property
    def hash(self):
        """Gets the hash of this ChainActivityStepData.  # noqa: E501

        The hash of the EIP712 signature that needs to be signed  # noqa: E501

        :return: The hash of this ChainActivityStepData.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this ChainActivityStepData.

        The hash of the EIP712 signature that needs to be signed  # noqa: E501

        :param hash: The hash of this ChainActivityStepData.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and hash is None:  # noqa: E501
            raise ValueError("Invalid value for `hash`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                hash is not None and not re.search(r'^(0x)?[0-9a-fA-F]{64}$', hash)):  # noqa: E501
            raise ValueError(r"Invalid value for `hash`, must be a follow pattern or equal to `/^(0x)?[0-9a-fA-F]{64}$/`")  # noqa: E501

        self._hash = hash

    @property
    def message(self):
        """Gets the message of this ChainActivityStepData.  # noqa: E501

        The message that needs to be signed  # noqa: E501

        :return: The message of this ChainActivityStepData.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ChainActivityStepData.

        The message that needs to be signed  # noqa: E501

        :param message: The message of this ChainActivityStepData.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, ChainActivityStepData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChainActivityStepData):
            return True

        return self.to_dict() != other.to_dict()
