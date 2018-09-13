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


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cloudera.director.common.client import ApiClient


class ImportClientConfigApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def convert_simple(self, simple_client_config, **kwargs):  # noqa: E501
        """Convert Simple Configuration  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.convert_simple(simple_client_config, async=True)
        >>> result = thread.get()

        :param async bool
        :param str simple_client_config: simpleClientConfig (required)
        :param bool include_origin_comments: includeOriginComments
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.convert_simple_with_http_info(simple_client_config, **kwargs)  # noqa: E501
        else:
            (data) = self.convert_simple_with_http_info(simple_client_config, **kwargs)  # noqa: E501
            return data

    def convert_simple_with_http_info(self, simple_client_config, **kwargs):  # noqa: E501
        """Convert Simple Configuration  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.convert_simple_with_http_info(simple_client_config, async=True)
        >>> result = thread.get()

        :param async bool
        :param str simple_client_config: simpleClientConfig (required)
        :param bool include_origin_comments: includeOriginComments
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['simple_client_config', 'include_origin_comments']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method convert_simple" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'simple_client_config' is set
        if ('simple_client_config' not in params or
                params['simple_client_config'] is None):
            raise ValueError("Missing the required parameter `simple_client_config` when calling `convert_simple`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'include_origin_comments' in params:
            query_params.append(('includeOriginComments', params['include_origin_comments']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'simple_client_config' in params:
            body_params = params['simple_client_config']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/hocon'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/hocon'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/api/v12/import/clientConfig/convertSimple', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            model_package="cloudera.director.v12.models",
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def import_client_config(self, client_config, **kwargs):  # noqa: E501
        """Import Client Config  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.import_client_config(client_config, async=True)
        >>> result = thread.get()

        :param async bool
        :param str client_config: clientConfig (required)
        :param str cluster_name: clusterName
        :param str deployment_name: deploymentName
        :param str environment_name: environmentName
        :return: ImportResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.import_client_config_with_http_info(client_config, **kwargs)  # noqa: E501
        else:
            (data) = self.import_client_config_with_http_info(client_config, **kwargs)  # noqa: E501
            return data

    def import_client_config_with_http_info(self, client_config, **kwargs):  # noqa: E501
        """Import Client Config  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.import_client_config_with_http_info(client_config, async=True)
        >>> result = thread.get()

        :param async bool
        :param str client_config: clientConfig (required)
        :param str cluster_name: clusterName
        :param str deployment_name: deploymentName
        :param str environment_name: environmentName
        :return: ImportResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_config', 'cluster_name', 'deployment_name', 'environment_name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method import_client_config" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'client_config' is set
        if ('client_config' not in params or
                params['client_config'] is None):
            raise ValueError("Missing the required parameter `client_config` when calling `import_client_config`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cluster_name' in params:
            query_params.append(('clusterName', params['cluster_name']))  # noqa: E501
        if 'deployment_name' in params:
            query_params.append(('deploymentName', params['deployment_name']))  # noqa: E501
        if 'environment_name' in params:
            query_params.append(('environmentName', params['environment_name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'client_config' in params:
            body_params = params['client_config']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/hocon'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/api/v12/import', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ImportResult',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            model_package="cloudera.director.v12.models",
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def validate(self, client_config, **kwargs):  # noqa: E501
        """Validate Client Config  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.validate(client_config, async=True)
        >>> result = thread.get()

        :param async bool
        :param str client_config: clientConfig (required)
        :param str cluster_name: clusterName
        :param str deployment_name: deploymentName
        :param str environment_name: environmentName
        :return: ValidationResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.validate_with_http_info(client_config, **kwargs)  # noqa: E501
        else:
            (data) = self.validate_with_http_info(client_config, **kwargs)  # noqa: E501
            return data

    def validate_with_http_info(self, client_config, **kwargs):  # noqa: E501
        """Validate Client Config  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.validate_with_http_info(client_config, async=True)
        >>> result = thread.get()

        :param async bool
        :param str client_config: clientConfig (required)
        :param str cluster_name: clusterName
        :param str deployment_name: deploymentName
        :param str environment_name: environmentName
        :return: ValidationResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_config', 'cluster_name', 'deployment_name', 'environment_name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method validate" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'client_config' is set
        if ('client_config' not in params or
                params['client_config'] is None):
            raise ValueError("Missing the required parameter `client_config` when calling `validate`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cluster_name' in params:
            query_params.append(('clusterName', params['cluster_name']))  # noqa: E501
        if 'deployment_name' in params:
            query_params.append(('deploymentName', params['deployment_name']))  # noqa: E501
        if 'environment_name' in params:
            query_params.append(('environmentName', params['environment_name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'client_config' in params:
            body_params = params['client_config']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/hocon'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/api/v12/import/clientConfig/validate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ValidationResult',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            model_package="cloudera.director.v12.models",
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)