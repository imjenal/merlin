# coding: utf-8

"""
    Merlin

    API Guide for accessing Merlin's model management, deployment, and serving functionalities  # noqa: E501

    OpenAPI spec version: 0.7.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Version(object):
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
        'id': 'int',
        'model_id': 'int',
        'mlflow_run_id': 'str',
        'mlflow_url': 'str',
        'artifact_uri': 'str',
        'endpoints': 'list[VersionEndpoint]',
        'properties': 'object',
        'labels': 'dict(str, str)',
        'custom_predictor': 'CustomPredictor',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'model_id': 'model_id',
        'mlflow_run_id': 'mlflow_run_id',
        'mlflow_url': 'mlflow_url',
        'artifact_uri': 'artifact_uri',
        'endpoints': 'endpoints',
        'properties': 'properties',
        'labels': 'labels',
        'custom_predictor': 'custom_predictor',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, model_id=None, mlflow_run_id=None, mlflow_url=None, artifact_uri=None, endpoints=None, properties=None, labels=None, custom_predictor=None, created_at=None, updated_at=None):  # noqa: E501
        """Version - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._model_id = None
        self._mlflow_run_id = None
        self._mlflow_url = None
        self._artifact_uri = None
        self._endpoints = None
        self._properties = None
        self._labels = None
        self._custom_predictor = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if model_id is not None:
            self.model_id = model_id
        if mlflow_run_id is not None:
            self.mlflow_run_id = mlflow_run_id
        if mlflow_url is not None:
            self.mlflow_url = mlflow_url
        if artifact_uri is not None:
            self.artifact_uri = artifact_uri
        if endpoints is not None:
            self.endpoints = endpoints
        if properties is not None:
            self.properties = properties
        if labels is not None:
            self.labels = labels
        if custom_predictor is not None:
            self.custom_predictor = custom_predictor
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this Version.  # noqa: E501


        :return: The id of this Version.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Version.


        :param id: The id of this Version.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def model_id(self):
        """Gets the model_id of this Version.  # noqa: E501


        :return: The model_id of this Version.  # noqa: E501
        :rtype: int
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """Sets the model_id of this Version.


        :param model_id: The model_id of this Version.  # noqa: E501
        :type: int
        """

        self._model_id = model_id

    @property
    def mlflow_run_id(self):
        """Gets the mlflow_run_id of this Version.  # noqa: E501


        :return: The mlflow_run_id of this Version.  # noqa: E501
        :rtype: str
        """
        return self._mlflow_run_id

    @mlflow_run_id.setter
    def mlflow_run_id(self, mlflow_run_id):
        """Sets the mlflow_run_id of this Version.


        :param mlflow_run_id: The mlflow_run_id of this Version.  # noqa: E501
        :type: str
        """

        self._mlflow_run_id = mlflow_run_id

    @property
    def mlflow_url(self):
        """Gets the mlflow_url of this Version.  # noqa: E501


        :return: The mlflow_url of this Version.  # noqa: E501
        :rtype: str
        """
        return self._mlflow_url

    @mlflow_url.setter
    def mlflow_url(self, mlflow_url):
        """Sets the mlflow_url of this Version.


        :param mlflow_url: The mlflow_url of this Version.  # noqa: E501
        :type: str
        """

        self._mlflow_url = mlflow_url

    @property
    def artifact_uri(self):
        """Gets the artifact_uri of this Version.  # noqa: E501


        :return: The artifact_uri of this Version.  # noqa: E501
        :rtype: str
        """
        return self._artifact_uri

    @artifact_uri.setter
    def artifact_uri(self, artifact_uri):
        """Sets the artifact_uri of this Version.


        :param artifact_uri: The artifact_uri of this Version.  # noqa: E501
        :type: str
        """

        self._artifact_uri = artifact_uri

    @property
    def endpoints(self):
        """Gets the endpoints of this Version.  # noqa: E501


        :return: The endpoints of this Version.  # noqa: E501
        :rtype: list[VersionEndpoint]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """Sets the endpoints of this Version.


        :param endpoints: The endpoints of this Version.  # noqa: E501
        :type: list[VersionEndpoint]
        """

        self._endpoints = endpoints

    @property
    def properties(self):
        """Gets the properties of this Version.  # noqa: E501


        :return: The properties of this Version.  # noqa: E501
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Version.


        :param properties: The properties of this Version.  # noqa: E501
        :type: object
        """

        self._properties = properties

    @property
    def labels(self):
        """Gets the labels of this Version.  # noqa: E501


        :return: The labels of this Version.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this Version.


        :param labels: The labels of this Version.  # noqa: E501
        :type: dict(str, str)
        """

        self._labels = labels

    @property
    def custom_predictor(self):
        """Gets the custom_predictor of this Version.  # noqa: E501


        :return: The custom_predictor of this Version.  # noqa: E501
        :rtype: CustomPredictor
        """
        return self._custom_predictor

    @custom_predictor.setter
    def custom_predictor(self, custom_predictor):
        """Sets the custom_predictor of this Version.


        :param custom_predictor: The custom_predictor of this Version.  # noqa: E501
        :type: CustomPredictor
        """

        self._custom_predictor = custom_predictor

    @property
    def created_at(self):
        """Gets the created_at of this Version.  # noqa: E501


        :return: The created_at of this Version.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Version.


        :param created_at: The created_at of this Version.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Version.  # noqa: E501


        :return: The updated_at of this Version.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Version.


        :param updated_at: The updated_at of this Version.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if issubclass(Version, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Version):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
