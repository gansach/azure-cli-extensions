# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "workloads sap-central-instance start",
)
class Start(AAZCommand):
    """Starts the SAP Central Services Instance.

    :example: Start Central services instance of the SAP system
        az workloads sap-central-instance start --sap-virtual-instance-name <vis-name> -g <resource-group-name> -n <cs-instance-name>

    :example: Start Central services instance of the SAP system using the Azure resource ID of the instance
        az workloads sap-central-instance start --id <resource-id>

    :example: Start Central services instance of the SAP system and its underlying Virtual Machine
        az workloads sap-central-instance start --sap-virtual-instance-name <vis-name> -g <resource-group-name> -n <cs-instance-name> --start-vm
    """

    _aaz_info = {
        "version": "2024-09-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.workloads/sapvirtualinstances/{}/centralinstances/{}/start", "2024-09-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.central_instance_name = AAZStrArg(
            options=["-n", "--name", "--central-instance-name"],
            help="Central Services Instance resource name string modeled as parameter for auto generation to work correctly.",
            required=True,
            id_part="child_name_1",
            fmt=AAZStrArgFormat(
                pattern="^.*",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.sap_virtual_instance_name = AAZStrArg(
            options=["--vis-name", "--sap-virtual-instance-name"],
            help="The name of the Virtual Instances for SAP solutions resource",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z][a-zA-Z0-9]{2}$",
            ),
        )

        # define Arg Group "Body"

        _args_schema = cls._args_schema
        _args_schema.start_vm = AAZBoolArg(
            options=["--start-vm"],
            arg_group="Body",
            help="The boolean value indicates whether to start the virtual machines before starting the SAP instances.",
            default=False,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.SapCentralServerInstancesStart(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class SapCentralServerInstancesStart(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Workloads/sapVirtualInstances/{sapVirtualInstanceName}/centralInstances/{centralInstanceName}/start",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "centralInstanceName", self.ctx.args.central_instance_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "sapVirtualInstanceName", self.ctx.args.sap_virtual_instance_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-09-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"client_flatten": True}}
            )
            _builder.set_prop("startVm", AAZBoolType, ".start_vm")

            return self.serialize_content(_content_value)

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _StartHelper._build_schema_operation_status_result_read(cls._schema_on_200)

            return cls._schema_on_200


class _StartHelper:
    """Helper class for Start"""

    _schema_error_detail_read = None

    @classmethod
    def _build_schema_error_detail_read(cls, _schema):
        if cls._schema_error_detail_read is not None:
            _schema.additional_info = cls._schema_error_detail_read.additional_info
            _schema.code = cls._schema_error_detail_read.code
            _schema.details = cls._schema_error_detail_read.details
            _schema.message = cls._schema_error_detail_read.message
            _schema.target = cls._schema_error_detail_read.target
            return

        cls._schema_error_detail_read = _schema_error_detail_read = AAZObjectType()

        error_detail_read = _schema_error_detail_read
        error_detail_read.additional_info = AAZListType(
            serialized_name="additionalInfo",
            flags={"read_only": True},
        )
        error_detail_read.code = AAZStrType(
            flags={"read_only": True},
        )
        error_detail_read.details = AAZListType(
            flags={"read_only": True},
        )
        error_detail_read.message = AAZStrType(
            flags={"read_only": True},
        )
        error_detail_read.target = AAZStrType(
            flags={"read_only": True},
        )

        additional_info = _schema_error_detail_read.additional_info
        additional_info.Element = AAZObjectType()

        _element = _schema_error_detail_read.additional_info.Element
        _element.info = AAZFreeFormDictType(
            flags={"read_only": True},
        )
        _element.type = AAZStrType(
            flags={"read_only": True},
        )

        details = _schema_error_detail_read.details
        details.Element = AAZObjectType()
        cls._build_schema_error_detail_read(details.Element)

        _schema.additional_info = cls._schema_error_detail_read.additional_info
        _schema.code = cls._schema_error_detail_read.code
        _schema.details = cls._schema_error_detail_read.details
        _schema.message = cls._schema_error_detail_read.message
        _schema.target = cls._schema_error_detail_read.target

    _schema_operation_status_result_read = None

    @classmethod
    def _build_schema_operation_status_result_read(cls, _schema):
        if cls._schema_operation_status_result_read is not None:
            _schema.end_time = cls._schema_operation_status_result_read.end_time
            _schema.error = cls._schema_operation_status_result_read.error
            _schema.id = cls._schema_operation_status_result_read.id
            _schema.name = cls._schema_operation_status_result_read.name
            _schema.operations = cls._schema_operation_status_result_read.operations
            _schema.percent_complete = cls._schema_operation_status_result_read.percent_complete
            _schema.resource_id = cls._schema_operation_status_result_read.resource_id
            _schema.start_time = cls._schema_operation_status_result_read.start_time
            _schema.status = cls._schema_operation_status_result_read.status
            return

        cls._schema_operation_status_result_read = _schema_operation_status_result_read = AAZObjectType()

        operation_status_result_read = _schema_operation_status_result_read
        operation_status_result_read.end_time = AAZStrType(
            serialized_name="endTime",
        )
        operation_status_result_read.error = AAZObjectType()
        cls._build_schema_error_detail_read(operation_status_result_read.error)
        operation_status_result_read.id = AAZStrType()
        operation_status_result_read.name = AAZStrType()
        operation_status_result_read.operations = AAZListType()
        operation_status_result_read.percent_complete = AAZFloatType(
            serialized_name="percentComplete",
        )
        operation_status_result_read.resource_id = AAZStrType(
            serialized_name="resourceId",
            flags={"read_only": True},
        )
        operation_status_result_read.start_time = AAZStrType(
            serialized_name="startTime",
        )
        operation_status_result_read.status = AAZStrType(
            flags={"required": True},
        )

        operations = _schema_operation_status_result_read.operations
        operations.Element = AAZObjectType()
        cls._build_schema_operation_status_result_read(operations.Element)

        _schema.end_time = cls._schema_operation_status_result_read.end_time
        _schema.error = cls._schema_operation_status_result_read.error
        _schema.id = cls._schema_operation_status_result_read.id
        _schema.name = cls._schema_operation_status_result_read.name
        _schema.operations = cls._schema_operation_status_result_read.operations
        _schema.percent_complete = cls._schema_operation_status_result_read.percent_complete
        _schema.resource_id = cls._schema_operation_status_result_read.resource_id
        _schema.start_time = cls._schema_operation_status_result_read.start_time
        _schema.status = cls._schema_operation_status_result_read.status


__all__ = ["Start"]
