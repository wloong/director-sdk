# coding: utf-8

"""
Licensed to Cloudera, Inc. under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  Cloudera, Inc. licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


import pprint
import re  # noqa: F401

import six


class ClusterAdministrationSettings(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'auto_repair_enabled': 'bool',
        'auto_repair_cooldown_period_in_seconds': 'int'
    }

    attribute_map = {
        'auto_repair_enabled': 'autoRepairEnabled',
        'auto_repair_cooldown_period_in_seconds': 'autoRepairCooldownPeriodInSeconds'
    }

    def __init__(self, auto_repair_enabled=None, auto_repair_cooldown_period_in_seconds=None):  # noqa: E501
        """ClusterAdministrationSettings - a model defined in Swagger"""  # noqa: E501

        self._auto_repair_enabled = None
        self._auto_repair_cooldown_period_in_seconds = None
        self.discriminator = None

        self.auto_repair_enabled = auto_repair_enabled
        self.auto_repair_cooldown_period_in_seconds = auto_repair_cooldown_period_in_seconds

    @property
    def auto_repair_enabled(self):
        """Gets the auto_repair_enabled of this ClusterAdministrationSettings.  # noqa: E501

        Whether auto-repair is enabled  # noqa: E501

        :return: The auto_repair_enabled of this ClusterAdministrationSettings.  # noqa: E501
        :rtype: bool
        """
        return self._auto_repair_enabled

    @auto_repair_enabled.setter
    def auto_repair_enabled(self, auto_repair_enabled):
        """Sets the auto_repair_enabled of this ClusterAdministrationSettings.

        Whether auto-repair is enabled  # noqa: E501

        :param auto_repair_enabled: The auto_repair_enabled of this ClusterAdministrationSettings.  # noqa: E501
        :type: bool
        """
        if auto_repair_enabled is None:
            raise ValueError("Invalid value for `auto_repair_enabled`, must not be `None`")  # noqa: E501

        self._auto_repair_enabled = auto_repair_enabled

    @property
    def auto_repair_cooldown_period_in_seconds(self):
        """Gets the auto_repair_cooldown_period_in_seconds of this ClusterAdministrationSettings.  # noqa: E501

        Delay after a modification before auto-repair will execute  # noqa: E501

        :return: The auto_repair_cooldown_period_in_seconds of this ClusterAdministrationSettings.  # noqa: E501
        :rtype: int
        """
        return self._auto_repair_cooldown_period_in_seconds

    @auto_repair_cooldown_period_in_seconds.setter
    def auto_repair_cooldown_period_in_seconds(self, auto_repair_cooldown_period_in_seconds):
        """Sets the auto_repair_cooldown_period_in_seconds of this ClusterAdministrationSettings.

        Delay after a modification before auto-repair will execute  # noqa: E501

        :param auto_repair_cooldown_period_in_seconds: The auto_repair_cooldown_period_in_seconds of this ClusterAdministrationSettings.  # noqa: E501
        :type: int
        """
        if auto_repair_cooldown_period_in_seconds is None:
            raise ValueError("Invalid value for `auto_repair_cooldown_period_in_seconds`, must not be `None`")  # noqa: E501

        self._auto_repair_cooldown_period_in_seconds = auto_repair_cooldown_period_in_seconds

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, ClusterAdministrationSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
