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


class TimeSeriesResponseList(object):
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
        'responses': 'list[TimeSeriesResponse]',
        'rows': 'list[TimeSeriesRow]'
    }

    attribute_map = {
        'responses': 'responses',
        'rows': 'rows'
    }

    def __init__(self, responses=None, rows=None):  # noqa: E501
        """TimeSeriesResponseList - a model defined in Swagger"""  # noqa: E501

        self._responses = None
        self._rows = None
        self.discriminator = None

        if responses is not None:
            self.responses = responses
        if rows is not None:
            self.rows = rows

    @property
    def responses(self):
        """Gets the responses of this TimeSeriesResponseList.  # noqa: E501

        Responses  # noqa: E501

        :return: The responses of this TimeSeriesResponseList.  # noqa: E501
        :rtype: list[TimeSeriesResponse]
        """
        return self._responses

    @responses.setter
    def responses(self, responses):
        """Sets the responses of this TimeSeriesResponseList.

        Responses  # noqa: E501

        :param responses: The responses of this TimeSeriesResponseList.  # noqa: E501
        :type: list[TimeSeriesResponse]
        """

        self._responses = responses

    @property
    def rows(self):
        """Gets the rows of this TimeSeriesResponseList.  # noqa: E501

        Rows  # noqa: E501

        :return: The rows of this TimeSeriesResponseList.  # noqa: E501
        :rtype: list[TimeSeriesRow]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this TimeSeriesResponseList.

        Rows  # noqa: E501

        :param rows: The rows of this TimeSeriesResponseList.  # noqa: E501
        :type: list[TimeSeriesRow]
        """

        self._rows = rows

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
        if not isinstance(other, TimeSeriesResponseList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
