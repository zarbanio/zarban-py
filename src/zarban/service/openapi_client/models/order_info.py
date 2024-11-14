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


class OrderInfo(object):
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
        'chain_id': 'int',
        'permit2_address': 'str',
        'reactor': 'str',
        'swapper': 'str',
        'nonce': 'str',
        'deadline': 'Timestamp',
        'additional_validation_contract': 'str',
        'additional_validation_data': 'str',
        'decay_start_time': 'Timestamp',
        'decay_end_time': 'Timestamp',
        'exclusive_filler': 'str',
        'exclusivity_override_bps': 'int',
        'input': 'DutchAmount',
        'outputs': 'list[DutchAmount]'
    }

    attribute_map = {
        'chain_id': 'chainId',
        'permit2_address': 'permit2Address',
        'reactor': 'reactor',
        'swapper': 'swapper',
        'nonce': 'nonce',
        'deadline': 'deadline',
        'additional_validation_contract': 'additionalValidationContract',
        'additional_validation_data': 'additionalValidationData',
        'decay_start_time': 'decayStartTime',
        'decay_end_time': 'decayEndTime',
        'exclusive_filler': 'exclusiveFiller',
        'exclusivity_override_bps': 'exclusivityOverrideBps',
        'input': 'input',
        'outputs': 'outputs'
    }

    def __init__(self, chain_id=None, permit2_address=None, reactor=None, swapper=None, nonce=None, deadline=None, additional_validation_contract=None, additional_validation_data=None, decay_start_time=None, decay_end_time=None, exclusive_filler=None, exclusivity_override_bps=None, input=None, outputs=None, local_vars_configuration=None):  # noqa: E501
        """OrderInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._chain_id = None
        self._permit2_address = None
        self._reactor = None
        self._swapper = None
        self._nonce = None
        self._deadline = None
        self._additional_validation_contract = None
        self._additional_validation_data = None
        self._decay_start_time = None
        self._decay_end_time = None
        self._exclusive_filler = None
        self._exclusivity_override_bps = None
        self._input = None
        self._outputs = None
        self.discriminator = None

        self.chain_id = chain_id
        self.permit2_address = permit2_address
        self.reactor = reactor
        self.swapper = swapper
        self.nonce = nonce
        self.deadline = deadline
        self.additional_validation_contract = additional_validation_contract
        self.additional_validation_data = additional_validation_data
        self.decay_start_time = decay_start_time
        self.decay_end_time = decay_end_time
        self.exclusive_filler = exclusive_filler
        self.exclusivity_override_bps = exclusivity_override_bps
        self.input = input
        self.outputs = outputs

    @property
    def chain_id(self):
        """Gets the chain_id of this OrderInfo.  # noqa: E501


        :return: The chain_id of this OrderInfo.  # noqa: E501
        :rtype: int
        """
        return self._chain_id

    @chain_id.setter
    def chain_id(self, chain_id):
        """Sets the chain_id of this OrderInfo.


        :param chain_id: The chain_id of this OrderInfo.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and chain_id is None:  # noqa: E501
            raise ValueError("Invalid value for `chain_id`, must not be `None`")  # noqa: E501

        self._chain_id = chain_id

    @property
    def permit2_address(self):
        """Gets the permit2_address of this OrderInfo.  # noqa: E501


        :return: The permit2_address of this OrderInfo.  # noqa: E501
        :rtype: str
        """
        return self._permit2_address

    @permit2_address.setter
    def permit2_address(self, permit2_address):
        """Sets the permit2_address of this OrderInfo.


        :param permit2_address: The permit2_address of this OrderInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and permit2_address is None:  # noqa: E501
            raise ValueError("Invalid value for `permit2_address`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                permit2_address is not None and not re.search(r'^(0x)?[0-9a-fA-F]{40}$', permit2_address)):  # noqa: E501
            raise ValueError(r"Invalid value for `permit2_address`, must be a follow pattern or equal to `/^(0x)?[0-9a-fA-F]{40}$/`")  # noqa: E501

        self._permit2_address = permit2_address

    @property
    def reactor(self):
        """Gets the reactor of this OrderInfo.  # noqa: E501


        :return: The reactor of this OrderInfo.  # noqa: E501
        :rtype: str
        """
        return self._reactor

    @reactor.setter
    def reactor(self, reactor):
        """Sets the reactor of this OrderInfo.


        :param reactor: The reactor of this OrderInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and reactor is None:  # noqa: E501
            raise ValueError("Invalid value for `reactor`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                reactor is not None and not re.search(r'^(0x)?[0-9a-fA-F]{40}$', reactor)):  # noqa: E501
            raise ValueError(r"Invalid value for `reactor`, must be a follow pattern or equal to `/^(0x)?[0-9a-fA-F]{40}$/`")  # noqa: E501

        self._reactor = reactor

    @property
    def swapper(self):
        """Gets the swapper of this OrderInfo.  # noqa: E501


        :return: The swapper of this OrderInfo.  # noqa: E501
        :rtype: str
        """
        return self._swapper

    @swapper.setter
    def swapper(self, swapper):
        """Sets the swapper of this OrderInfo.


        :param swapper: The swapper of this OrderInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and swapper is None:  # noqa: E501
            raise ValueError("Invalid value for `swapper`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                swapper is not None and not re.search(r'^(0x)?[0-9a-fA-F]{40}$', swapper)):  # noqa: E501
            raise ValueError(r"Invalid value for `swapper`, must be a follow pattern or equal to `/^(0x)?[0-9a-fA-F]{40}$/`")  # noqa: E501

        self._swapper = swapper

    @property
    def nonce(self):
        """Gets the nonce of this OrderInfo.  # noqa: E501


        :return: The nonce of this OrderInfo.  # noqa: E501
        :rtype: str
        """
        return self._nonce

    @nonce.setter
    def nonce(self, nonce):
        """Sets the nonce of this OrderInfo.


        :param nonce: The nonce of this OrderInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and nonce is None:  # noqa: E501
            raise ValueError("Invalid value for `nonce`, must not be `None`")  # noqa: E501

        self._nonce = nonce

    @property
    def deadline(self):
        """Gets the deadline of this OrderInfo.  # noqa: E501


        :return: The deadline of this OrderInfo.  # noqa: E501
        :rtype: Timestamp
        """
        return self._deadline

    @deadline.setter
    def deadline(self, deadline):
        """Sets the deadline of this OrderInfo.


        :param deadline: The deadline of this OrderInfo.  # noqa: E501
        :type: Timestamp
        """
        if self.local_vars_configuration.client_side_validation and deadline is None:  # noqa: E501
            raise ValueError("Invalid value for `deadline`, must not be `None`")  # noqa: E501

        self._deadline = deadline

    @property
    def additional_validation_contract(self):
        """Gets the additional_validation_contract of this OrderInfo.  # noqa: E501


        :return: The additional_validation_contract of this OrderInfo.  # noqa: E501
        :rtype: str
        """
        return self._additional_validation_contract

    @additional_validation_contract.setter
    def additional_validation_contract(self, additional_validation_contract):
        """Sets the additional_validation_contract of this OrderInfo.


        :param additional_validation_contract: The additional_validation_contract of this OrderInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and additional_validation_contract is None:  # noqa: E501
            raise ValueError("Invalid value for `additional_validation_contract`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                additional_validation_contract is not None and not re.search(r'^(0x)?[0-9a-fA-F]{40}$', additional_validation_contract)):  # noqa: E501
            raise ValueError(r"Invalid value for `additional_validation_contract`, must be a follow pattern or equal to `/^(0x)?[0-9a-fA-F]{40}$/`")  # noqa: E501

        self._additional_validation_contract = additional_validation_contract

    @property
    def additional_validation_data(self):
        """Gets the additional_validation_data of this OrderInfo.  # noqa: E501


        :return: The additional_validation_data of this OrderInfo.  # noqa: E501
        :rtype: str
        """
        return self._additional_validation_data

    @additional_validation_data.setter
    def additional_validation_data(self, additional_validation_data):
        """Sets the additional_validation_data of this OrderInfo.


        :param additional_validation_data: The additional_validation_data of this OrderInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and additional_validation_data is None:  # noqa: E501
            raise ValueError("Invalid value for `additional_validation_data`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                additional_validation_data is not None and not re.search(r'^(0x)?[0-9a-fA-F]*$', additional_validation_data)):  # noqa: E501
            raise ValueError(r"Invalid value for `additional_validation_data`, must be a follow pattern or equal to `/^(0x)?[0-9a-fA-F]*$/`")  # noqa: E501

        self._additional_validation_data = additional_validation_data

    @property
    def decay_start_time(self):
        """Gets the decay_start_time of this OrderInfo.  # noqa: E501


        :return: The decay_start_time of this OrderInfo.  # noqa: E501
        :rtype: Timestamp
        """
        return self._decay_start_time

    @decay_start_time.setter
    def decay_start_time(self, decay_start_time):
        """Sets the decay_start_time of this OrderInfo.


        :param decay_start_time: The decay_start_time of this OrderInfo.  # noqa: E501
        :type: Timestamp
        """
        if self.local_vars_configuration.client_side_validation and decay_start_time is None:  # noqa: E501
            raise ValueError("Invalid value for `decay_start_time`, must not be `None`")  # noqa: E501

        self._decay_start_time = decay_start_time

    @property
    def decay_end_time(self):
        """Gets the decay_end_time of this OrderInfo.  # noqa: E501


        :return: The decay_end_time of this OrderInfo.  # noqa: E501
        :rtype: Timestamp
        """
        return self._decay_end_time

    @decay_end_time.setter
    def decay_end_time(self, decay_end_time):
        """Sets the decay_end_time of this OrderInfo.


        :param decay_end_time: The decay_end_time of this OrderInfo.  # noqa: E501
        :type: Timestamp
        """
        if self.local_vars_configuration.client_side_validation and decay_end_time is None:  # noqa: E501
            raise ValueError("Invalid value for `decay_end_time`, must not be `None`")  # noqa: E501

        self._decay_end_time = decay_end_time

    @property
    def exclusive_filler(self):
        """Gets the exclusive_filler of this OrderInfo.  # noqa: E501


        :return: The exclusive_filler of this OrderInfo.  # noqa: E501
        :rtype: str
        """
        return self._exclusive_filler

    @exclusive_filler.setter
    def exclusive_filler(self, exclusive_filler):
        """Sets the exclusive_filler of this OrderInfo.


        :param exclusive_filler: The exclusive_filler of this OrderInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and exclusive_filler is None:  # noqa: E501
            raise ValueError("Invalid value for `exclusive_filler`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                exclusive_filler is not None and not re.search(r'^(0x)?[0-9a-fA-F]{40}$', exclusive_filler)):  # noqa: E501
            raise ValueError(r"Invalid value for `exclusive_filler`, must be a follow pattern or equal to `/^(0x)?[0-9a-fA-F]{40}$/`")  # noqa: E501

        self._exclusive_filler = exclusive_filler

    @property
    def exclusivity_override_bps(self):
        """Gets the exclusivity_override_bps of this OrderInfo.  # noqa: E501


        :return: The exclusivity_override_bps of this OrderInfo.  # noqa: E501
        :rtype: int
        """
        return self._exclusivity_override_bps

    @exclusivity_override_bps.setter
    def exclusivity_override_bps(self, exclusivity_override_bps):
        """Sets the exclusivity_override_bps of this OrderInfo.


        :param exclusivity_override_bps: The exclusivity_override_bps of this OrderInfo.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and exclusivity_override_bps is None:  # noqa: E501
            raise ValueError("Invalid value for `exclusivity_override_bps`, must not be `None`")  # noqa: E501

        self._exclusivity_override_bps = exclusivity_override_bps

    @property
    def input(self):
        """Gets the input of this OrderInfo.  # noqa: E501


        :return: The input of this OrderInfo.  # noqa: E501
        :rtype: DutchAmount
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this OrderInfo.


        :param input: The input of this OrderInfo.  # noqa: E501
        :type: DutchAmount
        """
        if self.local_vars_configuration.client_side_validation and input is None:  # noqa: E501
            raise ValueError("Invalid value for `input`, must not be `None`")  # noqa: E501

        self._input = input

    @property
    def outputs(self):
        """Gets the outputs of this OrderInfo.  # noqa: E501


        :return: The outputs of this OrderInfo.  # noqa: E501
        :rtype: list[DutchAmount]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this OrderInfo.


        :param outputs: The outputs of this OrderInfo.  # noqa: E501
        :type: list[DutchAmount]
        """
        if self.local_vars_configuration.client_side_validation and outputs is None:  # noqa: E501
            raise ValueError("Invalid value for `outputs`, must not be `None`")  # noqa: E501

        self._outputs = outputs

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
        if not isinstance(other, OrderInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrderInfo):
            return True

        return self.to_dict() != other.to_dict()
