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


class KycRequest(object):
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
        'national_id': 'str',
        'date_of_birth': 'str',
        'card_number': 'str'
    }

    attribute_map = {
        'national_id': 'nationalId',
        'date_of_birth': 'dateOfBirth',
        'card_number': 'cardNumber'
    }

    def __init__(self, national_id=None, date_of_birth=None, card_number=None, local_vars_configuration=None):  # noqa: E501
        """KycRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._national_id = None
        self._date_of_birth = None
        self._card_number = None
        self.discriminator = None

        self.national_id = national_id
        self.date_of_birth = date_of_birth
        self.card_number = card_number

    @property
    def national_id(self):
        """Gets the national_id of this KycRequest.  # noqa: E501

        National ID  # noqa: E501

        :return: The national_id of this KycRequest.  # noqa: E501
        :rtype: str
        """
        return self._national_id

    @national_id.setter
    def national_id(self, national_id):
        """Sets the national_id of this KycRequest.

        National ID  # noqa: E501

        :param national_id: The national_id of this KycRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and national_id is None:  # noqa: E501
            raise ValueError("Invalid value for `national_id`, must not be `None`")  # noqa: E501

        self._national_id = national_id

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this KycRequest.  # noqa: E501

        Date of birth  # noqa: E501

        :return: The date_of_birth of this KycRequest.  # noqa: E501
        :rtype: str
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this KycRequest.

        Date of birth  # noqa: E501

        :param date_of_birth: The date_of_birth of this KycRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and date_of_birth is None:  # noqa: E501
            raise ValueError("Invalid value for `date_of_birth`, must not be `None`")  # noqa: E501

        self._date_of_birth = date_of_birth

    @property
    def card_number(self):
        """Gets the card_number of this KycRequest.  # noqa: E501

        Card number  # noqa: E501

        :return: The card_number of this KycRequest.  # noqa: E501
        :rtype: str
        """
        return self._card_number

    @card_number.setter
    def card_number(self, card_number):
        """Sets the card_number of this KycRequest.

        Card number  # noqa: E501

        :param card_number: The card_number of this KycRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and card_number is None:  # noqa: E501
            raise ValueError("Invalid value for `card_number`, must not be `None`")  # noqa: E501

        self._card_number = card_number

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
        if not isinstance(other, KycRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KycRequest):
            return True

        return self.to_dict() != other.to_dict()
