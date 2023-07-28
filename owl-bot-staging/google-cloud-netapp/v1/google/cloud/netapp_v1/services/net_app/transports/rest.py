# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from google.auth.transport.requests import AuthorizedSession  # type: ignore
import json  # type: ignore
import grpc  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import retry as retries
from google.api_core import rest_helpers
from google.api_core import rest_streaming
from google.api_core import path_template
from google.api_core import gapic_v1

from google.protobuf import json_format
from google.api_core import operations_v1
from google.cloud.location import locations_pb2 # type: ignore
from google.longrunning import operations_pb2
from requests import __version__ as requests_version
import dataclasses
import re
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union
import warnings

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore


from google.cloud.netapp_v1.types import active_directory
from google.cloud.netapp_v1.types import active_directory as gcn_active_directory
from google.cloud.netapp_v1.types import kms
from google.cloud.netapp_v1.types import replication
from google.cloud.netapp_v1.types import replication as gcn_replication
from google.cloud.netapp_v1.types import snapshot
from google.cloud.netapp_v1.types import snapshot as gcn_snapshot
from google.cloud.netapp_v1.types import storage_pool
from google.cloud.netapp_v1.types import storage_pool as gcn_storage_pool
from google.cloud.netapp_v1.types import volume
from google.cloud.netapp_v1.types import volume as gcn_volume
from google.longrunning import operations_pb2  # type: ignore

from .base import NetAppTransport, DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=requests_version,
)


class NetAppRestInterceptor:
    """Interceptor for NetApp.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the NetAppRestTransport.

    .. code-block:: python
        class MyCustomNetAppInterceptor(NetAppRestInterceptor):
            def pre_create_active_directory(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_active_directory(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_kms_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_kms_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_replication(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_replication(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_snapshot(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_snapshot(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_storage_pool(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_storage_pool(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_volume(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_volume(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_active_directory(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_active_directory(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_kms_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_kms_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_replication(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_replication(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_snapshot(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_snapshot(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_storage_pool(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_storage_pool(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_volume(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_volume(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_encrypt_volumes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_encrypt_volumes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_active_directory(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_active_directory(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_kms_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_kms_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_replication(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_replication(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_snapshot(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_snapshot(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_storage_pool(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_storage_pool(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_volume(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_volume(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_active_directories(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_active_directories(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_kms_configs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_kms_configs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_replications(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_replications(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_snapshots(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_snapshots(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_storage_pools(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_storage_pools(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_volumes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_volumes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_resume_replication(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_resume_replication(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_reverse_replication_direction(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_reverse_replication_direction(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_revert_volume(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_revert_volume(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_stop_replication(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_stop_replication(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_active_directory(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_active_directory(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_kms_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_kms_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_replication(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_replication(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_snapshot(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_snapshot(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_storage_pool(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_storage_pool(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_volume(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_volume(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_verify_kms_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_verify_kms_config(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = NetAppRestTransport(interceptor=MyCustomNetAppInterceptor())
        client = NetAppClient(transport=transport)


    """
    def pre_create_active_directory(self, request: gcn_active_directory.CreateActiveDirectoryRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[gcn_active_directory.CreateActiveDirectoryRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for create_active_directory

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_create_active_directory(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_active_directory

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code.
        """
        return response
    def pre_create_kms_config(self, request: kms.CreateKmsConfigRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[kms.CreateKmsConfigRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for create_kms_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_create_kms_config(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_kms_config

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code.
        """
        return response
    def pre_create_replication(self, request: gcn_replication.CreateReplicationRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[gcn_replication.CreateReplicationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for create_replication

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_create_replication(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_replication

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code.
        """
        return response
    def pre_create_snapshot(self, request: gcn_snapshot.CreateSnapshotRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[gcn_snapshot.CreateSnapshotRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for create_snapshot

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_create_snapshot(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_snapshot

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code.
        """
        return response
    def pre_create_storage_pool(self, request: gcn_storage_pool.CreateStoragePoolRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[gcn_storage_pool.CreateStoragePoolRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for create_storage_pool

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_create_storage_pool(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_storage_pool

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code.
        """
        return response
    def pre_create_volume(self, request: gcn_volume.CreateVolumeRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[gcn_volume.CreateVolumeRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for create_volume

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_create_volume(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_volume

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code.
        """
        return response
    def pre_delete_active_directory(self, request: active_directory.DeleteActiveDirectoryRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[active_directory.DeleteActiveDirectoryRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_active_directory

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_delete_active_directory(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_active_directory

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code.
        """
        return response
    def pre_delete_kms_config(self, request: kms.DeleteKmsConfigRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[kms.DeleteKmsConfigRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_kms_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_delete_kms_config(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_kms_config

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code.
        """
        return response
    def pre_delete_replication(self, request: replication.DeleteReplicationRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[replication.DeleteReplicationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_replication

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_delete_replication(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_replication

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code.
        """
        return response
    def pre_delete_snapshot(self, request: snapshot.DeleteSnapshotRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[snapshot.DeleteSnapshotRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_snapshot

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_delete_snapshot(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_snapshot

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code.
        """
        return response
    def pre_delete_storage_pool(self, request: storage_pool.DeleteStoragePoolRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[storage_pool.DeleteStoragePoolRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_storage_pool

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_delete_storage_pool(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_storage_pool

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code.
        """
        return response
    def pre_delete_volume(self, request: volume.DeleteVolumeRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[volume.DeleteVolumeRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_volume

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_delete_volume(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_volume

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code.
        """
        return response
    def pre_encrypt_volumes(self, request: kms.EncryptVolumesRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[kms.EncryptVolumesRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for encrypt_volumes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_encrypt_volumes(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for encrypt_volumes

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code.
        """
        return response
    def pre_get_active_directory(self, request: active_directory.GetActiveDirectoryRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[active_directory.GetActiveDirectoryRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_active_directory

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_get_active_directory(self, response: active_directory.ActiveDirectory) -> active_directory.ActiveDirectory:
        """Post-rpc interceptor for get_active_directory

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code.
        """
        return response
    def pre_get_kms_config(self, request: kms.GetKmsConfigRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[kms.GetKmsConfigRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_kms_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_get_kms_config(self, response: kms.KmsConfig) -> kms.KmsConfig:
        """Post-rpc interceptor for get_kms_config

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code.
        """
        return response
    def pre_get_replication(self, request: replication.GetReplicationRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[replication.GetReplicationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_replication

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_get_replication(self, response: replication.Replication) -> replication.Replication:
        """Post-rpc interceptor for get_replication

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code.
        """
        return response
    def pre_get_snapshot(self, request: snapshot.GetSnapshotRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[snapshot.GetSnapshotRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_snapshot

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_get_snapshot(self, response: snapshot.Snapshot) -> snapshot.Snapshot:
        """Post-rpc interceptor for get_snapshot

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code.
        """
        return response
    def pre_get_storage_pool(self, request: storage_pool.GetStoragePoolRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[storage_pool.GetStoragePoolRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_storage_pool

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_get_storage_pool(self, response: storage_pool.StoragePool) -> storage_pool.StoragePool:
        """Post-rpc interceptor for get_storage_pool

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code.
        """
        return response
    def pre_get_volume(self, request: volume.GetVolumeRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[volume.GetVolumeRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_volume

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_get_volume(self, response: volume.Volume) -> volume.Volume:
        """Post-rpc interceptor for get_volume

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code.
        """
        return response
    def pre_list_active_directories(self, request: active_directory.ListActiveDirectoriesRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[active_directory.ListActiveDirectoriesRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_active_directories

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_list_active_directories(self, response: active_directory.ListActiveDirectoriesResponse) -> active_directory.ListActiveDirectoriesResponse:
        """Post-rpc interceptor for list_active_directories

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code.
        """
        return response
    def pre_list_kms_configs(self, request: kms.ListKmsConfigsRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[kms.ListKmsConfigsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_kms_configs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_list_kms_configs(self, response: kms.ListKmsConfigsResponse) -> kms.ListKmsConfigsResponse:
        """Post-rpc interceptor for list_kms_configs

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code.
        """
        return response
    def pre_list_replications(self, request: replication.ListReplicationsRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[replication.ListReplicationsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_replications

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_list_replications(self, response: replication.ListReplicationsResponse) -> replication.ListReplicationsResponse:
        """Post-rpc interceptor for list_replications

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code.
        """
        return response
    def pre_list_snapshots(self, request: snapshot.ListSnapshotsRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[snapshot.ListSnapshotsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_snapshots

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_list_snapshots(self, response: snapshot.ListSnapshotsResponse) -> snapshot.ListSnapshotsResponse:
        """Post-rpc interceptor for list_snapshots

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code.
        """
        return response
    def pre_list_storage_pools(self, request: storage_pool.ListStoragePoolsRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[storage_pool.ListStoragePoolsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_storage_pools

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_list_storage_pools(self, response: storage_pool.ListStoragePoolsResponse) -> storage_pool.ListStoragePoolsResponse:
        """Post-rpc interceptor for list_storage_pools

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code.
        """
        return response
    def pre_list_volumes(self, request: volume.ListVolumesRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[volume.ListVolumesRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_volumes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_list_volumes(self, response: volume.ListVolumesResponse) -> volume.ListVolumesResponse:
        """Post-rpc interceptor for list_volumes

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code.
        """
        return response
    def pre_resume_replication(self, request: replication.ResumeReplicationRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[replication.ResumeReplicationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for resume_replication

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_resume_replication(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for resume_replication

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code.
        """
        return response
    def pre_reverse_replication_direction(self, request: replication.ReverseReplicationDirectionRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[replication.ReverseReplicationDirectionRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for reverse_replication_direction

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_reverse_replication_direction(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for reverse_replication_direction

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code.
        """
        return response
    def pre_revert_volume(self, request: volume.RevertVolumeRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[volume.RevertVolumeRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for revert_volume

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_revert_volume(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for revert_volume

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code.
        """
        return response
    def pre_stop_replication(self, request: replication.StopReplicationRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[replication.StopReplicationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for stop_replication

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_stop_replication(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for stop_replication

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code.
        """
        return response
    def pre_update_active_directory(self, request: gcn_active_directory.UpdateActiveDirectoryRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[gcn_active_directory.UpdateActiveDirectoryRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for update_active_directory

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_update_active_directory(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_active_directory

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code.
        """
        return response
    def pre_update_kms_config(self, request: kms.UpdateKmsConfigRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[kms.UpdateKmsConfigRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for update_kms_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_update_kms_config(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_kms_config

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code.
        """
        return response
    def pre_update_replication(self, request: gcn_replication.UpdateReplicationRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[gcn_replication.UpdateReplicationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for update_replication

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_update_replication(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_replication

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code.
        """
        return response
    def pre_update_snapshot(self, request: gcn_snapshot.UpdateSnapshotRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[gcn_snapshot.UpdateSnapshotRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for update_snapshot

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_update_snapshot(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_snapshot

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code.
        """
        return response
    def pre_update_storage_pool(self, request: gcn_storage_pool.UpdateStoragePoolRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[gcn_storage_pool.UpdateStoragePoolRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for update_storage_pool

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_update_storage_pool(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_storage_pool

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code.
        """
        return response
    def pre_update_volume(self, request: gcn_volume.UpdateVolumeRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[gcn_volume.UpdateVolumeRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for update_volume

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_update_volume(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_volume

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code.
        """
        return response
    def pre_verify_kms_config(self, request: kms.VerifyKmsConfigRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[kms.VerifyKmsConfigRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for verify_kms_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_verify_kms_config(self, response: kms.VerifyKmsConfigResponse) -> kms.VerifyKmsConfigResponse:
        """Post-rpc interceptor for verify_kms_config

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class NetAppRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: NetAppRestInterceptor


class NetAppRestTransport(NetAppTransport):
    """REST backend transport for NetApp.

    NetApp Files Google Cloud Service

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1

    """

    def __init__(self, *,
            host: str = 'netapp.googleapis.com',
            credentials: Optional[ga_credentials.Credentials] = None,
            credentials_file: Optional[str] = None,
            scopes: Optional[Sequence[str]] = None,
            client_cert_source_for_mtls: Optional[Callable[[
                ], Tuple[bytes, bytes]]] = None,
            quota_project_id: Optional[str] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            always_use_jwt_access: Optional[bool] = False,
            url_scheme: str = 'https',
            interceptor: Optional[NetAppRestInterceptor] = None,
            api_audience: Optional[str] = None,
            ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.

            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Callable[[], Tuple[bytes, bytes]]): Client
                certificate to configure mutual TLS HTTP channel. It is ignored
                if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you are developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            url_scheme: the protocol scheme for the API endpoint.  Normally
                "https", but for testing or local servers,
                "http" can be specified.
        """
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
        maybe_url_match = re.match("^(?P<scheme>http(?:s)?://)?(?P<host>.*)$", host)
        if maybe_url_match is None:
            raise ValueError(f"Unexpected hostname structure: {host}")  # pragma: NO COVER

        url_match_items = maybe_url_match.groupdict()

        host = f"{url_scheme}://{host}" if not url_match_items["scheme"] else host

        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience
        )
        self._session = AuthorizedSession(
            self._credentials, default_host=self.DEFAULT_HOST)
        self._operations_client: Optional[operations_v1.AbstractOperationsClient] = None
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or NetAppRestInterceptor()
        self._prep_wrapped_messages(client_info)

    @property
    def operations_client(self) -> operations_v1.AbstractOperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Only create a new client if we do not already have one.
        if self._operations_client is None:
            http_options: Dict[str, List[Dict[str, str]]] = {
            }

            rest_transport = operations_v1.OperationsRestTransport(
                    host=self._host,
                    # use the credentials which are saved
                    credentials=self._credentials,
                    scopes=self._scopes,
                    http_options=http_options,
                    path_prefix="v1")

            self._operations_client = operations_v1.AbstractOperationsClient(transport=rest_transport)

        # Return the client from cache.
        return self._operations_client

    class _CreateActiveDirectory(NetAppRestStub):
        def __hash__(self):
            return hash("CreateActiveDirectory")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
            "activeDirectoryId" : "",        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: gcn_active_directory.CreateActiveDirectoryRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the create active directory method over HTTP.

            Args:
                request (~.gcn_active_directory.CreateActiveDirectoryRequest):
                    The request object. CreateActiveDirectoryRequest for
                creating an active directory.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1/{parent=projects/*/locations/*}/activeDirectories',
                'body': 'active_directory',
            },
            ]
            request, metadata = self._interceptor.pre_create_active_directory(request, metadata)
            pb_request = gcn_active_directory.CreateActiveDirectoryRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_active_directory(resp)
            return resp

    class _CreateKmsConfig(NetAppRestStub):
        def __hash__(self):
            return hash("CreateKmsConfig")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
            "kmsConfigId" : "",        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: kms.CreateKmsConfigRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the create kms config method over HTTP.

            Args:
                request (~.kms.CreateKmsConfigRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1/{parent=projects/*/locations/*}/kmsConfigs',
                'body': 'kms_config',
            },
            ]
            request, metadata = self._interceptor.pre_create_kms_config(request, metadata)
            pb_request = kms.CreateKmsConfigRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_kms_config(resp)
            return resp

    class _CreateReplication(NetAppRestStub):
        def __hash__(self):
            return hash("CreateReplication")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
            "replicationId" : "",        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: gcn_replication.CreateReplicationRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the create replication method over HTTP.

            Args:
                request (~.gcn_replication.CreateReplicationRequest):
                    The request object. CreateReplicationRequest creates a
                replication.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1/{parent=projects/*/locations/*/volumes/*}/replications',
                'body': 'replication',
            },
            ]
            request, metadata = self._interceptor.pre_create_replication(request, metadata)
            pb_request = gcn_replication.CreateReplicationRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_replication(resp)
            return resp

    class _CreateSnapshot(NetAppRestStub):
        def __hash__(self):
            return hash("CreateSnapshot")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
            "snapshotId" : "",        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: gcn_snapshot.CreateSnapshotRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the create snapshot method over HTTP.

            Args:
                request (~.gcn_snapshot.CreateSnapshotRequest):
                    The request object. CreateSnapshotRequest creates a
                snapshot.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1/{parent=projects/*/locations/*/volumes/*}/snapshots',
                'body': 'snapshot',
            },
            ]
            request, metadata = self._interceptor.pre_create_snapshot(request, metadata)
            pb_request = gcn_snapshot.CreateSnapshotRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_snapshot(resp)
            return resp

    class _CreateStoragePool(NetAppRestStub):
        def __hash__(self):
            return hash("CreateStoragePool")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
            "storagePoolId" : "",        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: gcn_storage_pool.CreateStoragePoolRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the create storage pool method over HTTP.

            Args:
                request (~.gcn_storage_pool.CreateStoragePoolRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1/{parent=projects/*/locations/*}/storagePools',
                'body': 'storage_pool',
            },
            ]
            request, metadata = self._interceptor.pre_create_storage_pool(request, metadata)
            pb_request = gcn_storage_pool.CreateStoragePoolRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_storage_pool(resp)
            return resp

    class _CreateVolume(NetAppRestStub):
        def __hash__(self):
            return hash("CreateVolume")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
            "volumeId" : "",        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: gcn_volume.CreateVolumeRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the create volume method over HTTP.

            Args:
                request (~.gcn_volume.CreateVolumeRequest):
                    The request object. Message for creating a Volume
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1/{parent=projects/*/locations/*}/volumes',
                'body': 'volume',
            },
            ]
            request, metadata = self._interceptor.pre_create_volume(request, metadata)
            pb_request = gcn_volume.CreateVolumeRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_volume(resp)
            return resp

    class _DeleteActiveDirectory(NetAppRestStub):
        def __hash__(self):
            return hash("DeleteActiveDirectory")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: active_directory.DeleteActiveDirectoryRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the delete active directory method over HTTP.

            Args:
                request (~.active_directory.DeleteActiveDirectoryRequest):
                    The request object. DeleteActiveDirectoryRequest for
                deleting a single active directory.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'delete',
                'uri': '/v1/{name=projects/*/locations/*/activeDirectories/*}',
            },
            ]
            request, metadata = self._interceptor.pre_delete_active_directory(request, metadata)
            pb_request = active_directory.DeleteActiveDirectoryRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_delete_active_directory(resp)
            return resp

    class _DeleteKmsConfig(NetAppRestStub):
        def __hash__(self):
            return hash("DeleteKmsConfig")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: kms.DeleteKmsConfigRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the delete kms config method over HTTP.

            Args:
                request (~.kms.DeleteKmsConfigRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'delete',
                'uri': '/v1/{name=projects/*/locations/*/kmsConfigs/*}',
            },
            ]
            request, metadata = self._interceptor.pre_delete_kms_config(request, metadata)
            pb_request = kms.DeleteKmsConfigRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_delete_kms_config(resp)
            return resp

    class _DeleteReplication(NetAppRestStub):
        def __hash__(self):
            return hash("DeleteReplication")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: replication.DeleteReplicationRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the delete replication method over HTTP.

            Args:
                request (~.replication.DeleteReplicationRequest):
                    The request object. DeleteReplicationRequest deletes a
                replication.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'delete',
                'uri': '/v1/{name=projects/*/locations/*/volumes/*/replications/*}',
            },
            ]
            request, metadata = self._interceptor.pre_delete_replication(request, metadata)
            pb_request = replication.DeleteReplicationRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_delete_replication(resp)
            return resp

    class _DeleteSnapshot(NetAppRestStub):
        def __hash__(self):
            return hash("DeleteSnapshot")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: snapshot.DeleteSnapshotRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the delete snapshot method over HTTP.

            Args:
                request (~.snapshot.DeleteSnapshotRequest):
                    The request object. DeleteSnapshotRequest deletes a
                snapshot.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'delete',
                'uri': '/v1/{name=projects/*/locations/*/volumes/*/snapshots/*}',
            },
            ]
            request, metadata = self._interceptor.pre_delete_snapshot(request, metadata)
            pb_request = snapshot.DeleteSnapshotRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_delete_snapshot(resp)
            return resp

    class _DeleteStoragePool(NetAppRestStub):
        def __hash__(self):
            return hash("DeleteStoragePool")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: storage_pool.DeleteStoragePoolRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the delete storage pool method over HTTP.

            Args:
                request (~.storage_pool.DeleteStoragePoolRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'delete',
                'uri': '/v1/{name=projects/*/locations/*/storagePools/*}',
            },
            ]
            request, metadata = self._interceptor.pre_delete_storage_pool(request, metadata)
            pb_request = storage_pool.DeleteStoragePoolRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_delete_storage_pool(resp)
            return resp

    class _DeleteVolume(NetAppRestStub):
        def __hash__(self):
            return hash("DeleteVolume")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: volume.DeleteVolumeRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the delete volume method over HTTP.

            Args:
                request (~.volume.DeleteVolumeRequest):
                    The request object. Message for deleting a Volume
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'delete',
                'uri': '/v1/{name=projects/*/locations/*/volumes/*}',
            },
            ]
            request, metadata = self._interceptor.pre_delete_volume(request, metadata)
            pb_request = volume.DeleteVolumeRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_delete_volume(resp)
            return resp

    class _EncryptVolumes(NetAppRestStub):
        def __hash__(self):
            return hash("EncryptVolumes")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: kms.EncryptVolumesRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the encrypt volumes method over HTTP.

            Args:
                request (~.kms.EncryptVolumesRequest):
                    The request object. EncryptVolumesRequest specifies the
                KMS config to encrypt existing volumes.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1/{name=projects/*/locations/*/kmsConfigs/*}:encrypt',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_encrypt_volumes(request, metadata)
            pb_request = kms.EncryptVolumesRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_encrypt_volumes(resp)
            return resp

    class _GetActiveDirectory(NetAppRestStub):
        def __hash__(self):
            return hash("GetActiveDirectory")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: active_directory.GetActiveDirectoryRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> active_directory.ActiveDirectory:
            r"""Call the get active directory method over HTTP.

            Args:
                request (~.active_directory.GetActiveDirectoryRequest):
                    The request object. GetActiveDirectory for getting a
                single active directory.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.active_directory.ActiveDirectory:
                    ActiveDirectory is the public
                representation of the active directory
                config.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1/{name=projects/*/locations/*/activeDirectories/*}',
            },
            ]
            request, metadata = self._interceptor.pre_get_active_directory(request, metadata)
            pb_request = active_directory.GetActiveDirectoryRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = active_directory.ActiveDirectory()
            pb_resp = active_directory.ActiveDirectory.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_active_directory(resp)
            return resp

    class _GetKmsConfig(NetAppRestStub):
        def __hash__(self):
            return hash("GetKmsConfig")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: kms.GetKmsConfigRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> kms.KmsConfig:
            r"""Call the get kms config method over HTTP.

            Args:
                request (~.kms.GetKmsConfigRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.kms.KmsConfig:
                    KmsConfig is the customer managed
                encryption key(CMEK) configuration.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1/{name=projects/*/locations/*/kmsConfigs/*}',
            },
            ]
            request, metadata = self._interceptor.pre_get_kms_config(request, metadata)
            pb_request = kms.GetKmsConfigRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = kms.KmsConfig()
            pb_resp = kms.KmsConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_kms_config(resp)
            return resp

    class _GetReplication(NetAppRestStub):
        def __hash__(self):
            return hash("GetReplication")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: replication.GetReplicationRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> replication.Replication:
            r"""Call the get replication method over HTTP.

            Args:
                request (~.replication.GetReplicationRequest):
                    The request object. GetReplicationRequest gets the state
                of a replication.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.replication.Replication:
                    Replication is a nested resource
                under Volume, that describes a
                cross-region replication relationship
                between 2 volumes in different regions.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1/{name=projects/*/locations/*/volumes/*/replications/*}',
            },
            ]
            request, metadata = self._interceptor.pre_get_replication(request, metadata)
            pb_request = replication.GetReplicationRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = replication.Replication()
            pb_resp = replication.Replication.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_replication(resp)
            return resp

    class _GetSnapshot(NetAppRestStub):
        def __hash__(self):
            return hash("GetSnapshot")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: snapshot.GetSnapshotRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> snapshot.Snapshot:
            r"""Call the get snapshot method over HTTP.

            Args:
                request (~.snapshot.GetSnapshotRequest):
                    The request object. GetSnapshotRequest gets the state of
                a snapshot.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.snapshot.Snapshot:

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1/{name=projects/*/locations/*/volumes/*/snapshots/*}',
            },
            ]
            request, metadata = self._interceptor.pre_get_snapshot(request, metadata)
            pb_request = snapshot.GetSnapshotRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = snapshot.Snapshot()
            pb_resp = snapshot.Snapshot.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_snapshot(resp)
            return resp

    class _GetStoragePool(NetAppRestStub):
        def __hash__(self):
            return hash("GetStoragePool")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: storage_pool.GetStoragePoolRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> storage_pool.StoragePool:
            r"""Call the get storage pool method over HTTP.

            Args:
                request (~.storage_pool.GetStoragePoolRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.storage_pool.StoragePool:
                    StoragePool is a container for
                volumes with a service level and
                capacity. Volumes can be created in a
                pool of sufficient available capacity.
                StoragePool capacity is what you are
                billed for.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1/{name=projects/*/locations/*/storagePools/*}',
            },
            ]
            request, metadata = self._interceptor.pre_get_storage_pool(request, metadata)
            pb_request = storage_pool.GetStoragePoolRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = storage_pool.StoragePool()
            pb_resp = storage_pool.StoragePool.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_storage_pool(resp)
            return resp

    class _GetVolume(NetAppRestStub):
        def __hash__(self):
            return hash("GetVolume")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: volume.GetVolumeRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> volume.Volume:
            r"""Call the get volume method over HTTP.

            Args:
                request (~.volume.GetVolumeRequest):
                    The request object. Message for getting a Volume
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.volume.Volume:
                    Volume provides a filesystem that you
                can mount.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1/{name=projects/*/locations/*/volumes/*}',
            },
            ]
            request, metadata = self._interceptor.pre_get_volume(request, metadata)
            pb_request = volume.GetVolumeRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = volume.Volume()
            pb_resp = volume.Volume.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_volume(resp)
            return resp

    class _ListActiveDirectories(NetAppRestStub):
        def __hash__(self):
            return hash("ListActiveDirectories")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: active_directory.ListActiveDirectoriesRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> active_directory.ListActiveDirectoriesResponse:
            r"""Call the list active directories method over HTTP.

            Args:
                request (~.active_directory.ListActiveDirectoriesRequest):
                    The request object. ListActiveDirectoriesRequest for
                requesting multiple active directories.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.active_directory.ListActiveDirectoriesResponse:
                    ListActiveDirectoriesResponse
                contains all the active directories
                requested.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1/{parent=projects/*/locations/*}/activeDirectories',
            },
            ]
            request, metadata = self._interceptor.pre_list_active_directories(request, metadata)
            pb_request = active_directory.ListActiveDirectoriesRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = active_directory.ListActiveDirectoriesResponse()
            pb_resp = active_directory.ListActiveDirectoriesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_active_directories(resp)
            return resp

    class _ListKmsConfigs(NetAppRestStub):
        def __hash__(self):
            return hash("ListKmsConfigs")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: kms.ListKmsConfigsRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> kms.ListKmsConfigsResponse:
            r"""Call the list kms configs method over HTTP.

            Args:
                request (~.kms.ListKmsConfigsRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.kms.ListKmsConfigsResponse:

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1/{parent=projects/*/locations/*}/kmsConfigs',
            },
            ]
            request, metadata = self._interceptor.pre_list_kms_configs(request, metadata)
            pb_request = kms.ListKmsConfigsRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = kms.ListKmsConfigsResponse()
            pb_resp = kms.ListKmsConfigsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_kms_configs(resp)
            return resp

    class _ListReplications(NetAppRestStub):
        def __hash__(self):
            return hash("ListReplications")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: replication.ListReplicationsRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> replication.ListReplicationsResponse:
            r"""Call the list replications method over HTTP.

            Args:
                request (~.replication.ListReplicationsRequest):
                    The request object. ListReplications lists replications.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.replication.ListReplicationsResponse:
                    ListReplicationsResponse is the
                result of ListReplicationsRequest.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1/{parent=projects/*/locations/*/volumes/*}/replications',
            },
            ]
            request, metadata = self._interceptor.pre_list_replications(request, metadata)
            pb_request = replication.ListReplicationsRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = replication.ListReplicationsResponse()
            pb_resp = replication.ListReplicationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_replications(resp)
            return resp

    class _ListSnapshots(NetAppRestStub):
        def __hash__(self):
            return hash("ListSnapshots")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: snapshot.ListSnapshotsRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> snapshot.ListSnapshotsResponse:
            r"""Call the list snapshots method over HTTP.

            Args:
                request (~.snapshot.ListSnapshotsRequest):
                    The request object. ListSnapshotsRequest lists snapshots.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.snapshot.ListSnapshotsResponse:
                    ListSnapshotsResponse is the result
                of ListSnapshotsRequest.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1/{parent=projects/*/locations/*/volumes/*}/snapshots',
            },
            ]
            request, metadata = self._interceptor.pre_list_snapshots(request, metadata)
            pb_request = snapshot.ListSnapshotsRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = snapshot.ListSnapshotsResponse()
            pb_resp = snapshot.ListSnapshotsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_snapshots(resp)
            return resp

    class _ListStoragePools(NetAppRestStub):
        def __hash__(self):
            return hash("ListStoragePools")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: storage_pool.ListStoragePoolsRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> storage_pool.ListStoragePoolsResponse:
            r"""Call the list storage pools method over HTTP.

            Args:
                request (~.storage_pool.ListStoragePoolsRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.storage_pool.ListStoragePoolsResponse:

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1/{parent=projects/*/locations/*}/storagePools',
            },
            ]
            request, metadata = self._interceptor.pre_list_storage_pools(request, metadata)
            pb_request = storage_pool.ListStoragePoolsRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = storage_pool.ListStoragePoolsResponse()
            pb_resp = storage_pool.ListStoragePoolsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_storage_pools(resp)
            return resp

    class _ListVolumes(NetAppRestStub):
        def __hash__(self):
            return hash("ListVolumes")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: volume.ListVolumesRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> volume.ListVolumesResponse:
            r"""Call the list volumes method over HTTP.

            Args:
                request (~.volume.ListVolumesRequest):
                    The request object. Message for requesting list of
                Volumes
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.volume.ListVolumesResponse:
                    Message for response to listing
                Volumes

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1/{parent=projects/*/locations/*}/volumes',
            },
            ]
            request, metadata = self._interceptor.pre_list_volumes(request, metadata)
            pb_request = volume.ListVolumesRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = volume.ListVolumesResponse()
            pb_resp = volume.ListVolumesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_volumes(resp)
            return resp

    class _ResumeReplication(NetAppRestStub):
        def __hash__(self):
            return hash("ResumeReplication")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: replication.ResumeReplicationRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the resume replication method over HTTP.

            Args:
                request (~.replication.ResumeReplicationRequest):
                    The request object. ResumeReplicationRequest resumes a
                stopped replication.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1/{name=projects/*/locations/*/volumes/*/replications/*}:resume',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_resume_replication(request, metadata)
            pb_request = replication.ResumeReplicationRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_resume_replication(resp)
            return resp

    class _ReverseReplicationDirection(NetAppRestStub):
        def __hash__(self):
            return hash("ReverseReplicationDirection")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: replication.ReverseReplicationDirectionRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the reverse replication
        direction method over HTTP.

            Args:
                request (~.replication.ReverseReplicationDirectionRequest):
                    The request object. ReverseReplicationDirectionRequest
                reverses direction of replication.
                Source becomes destination and
                destination becomes source.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1/{name=projects/*/locations/*/volumes/*/replications/*}:reverseDirection',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_reverse_replication_direction(request, metadata)
            pb_request = replication.ReverseReplicationDirectionRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_reverse_replication_direction(resp)
            return resp

    class _RevertVolume(NetAppRestStub):
        def __hash__(self):
            return hash("RevertVolume")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: volume.RevertVolumeRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the revert volume method over HTTP.

            Args:
                request (~.volume.RevertVolumeRequest):
                    The request object. RevertVolumeRequest reverts the given
                volume to the specified snapshot.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1/{name=projects/*/locations/*/volumes/*}:revert',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_revert_volume(request, metadata)
            pb_request = volume.RevertVolumeRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_revert_volume(resp)
            return resp

    class _StopReplication(NetAppRestStub):
        def __hash__(self):
            return hash("StopReplication")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: replication.StopReplicationRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the stop replication method over HTTP.

            Args:
                request (~.replication.StopReplicationRequest):
                    The request object. StopReplicationRequest stops a
                replication until resumed.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1/{name=projects/*/locations/*/volumes/*/replications/*}:stop',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_stop_replication(request, metadata)
            pb_request = replication.StopReplicationRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_stop_replication(resp)
            return resp

    class _UpdateActiveDirectory(NetAppRestStub):
        def __hash__(self):
            return hash("UpdateActiveDirectory")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
            "updateMask" : {},        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: gcn_active_directory.UpdateActiveDirectoryRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the update active directory method over HTTP.

            Args:
                request (~.gcn_active_directory.UpdateActiveDirectoryRequest):
                    The request object. UpdateActiveDirectoryRequest for
                updating an active directory.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'patch',
                'uri': '/v1/{active_directory.name=projects/*/locations/*/activeDirectories/*}',
                'body': 'active_directory',
            },
            ]
            request, metadata = self._interceptor.pre_update_active_directory(request, metadata)
            pb_request = gcn_active_directory.UpdateActiveDirectoryRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_update_active_directory(resp)
            return resp

    class _UpdateKmsConfig(NetAppRestStub):
        def __hash__(self):
            return hash("UpdateKmsConfig")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
            "updateMask" : {},        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: kms.UpdateKmsConfigRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the update kms config method over HTTP.

            Args:
                request (~.kms.UpdateKmsConfigRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'patch',
                'uri': '/v1/{kms_config.name=projects/*/locations/*/kmsConfigs/*}',
                'body': 'kms_config',
            },
            ]
            request, metadata = self._interceptor.pre_update_kms_config(request, metadata)
            pb_request = kms.UpdateKmsConfigRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_update_kms_config(resp)
            return resp

    class _UpdateReplication(NetAppRestStub):
        def __hash__(self):
            return hash("UpdateReplication")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
            "updateMask" : {},        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: gcn_replication.UpdateReplicationRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the update replication method over HTTP.

            Args:
                request (~.gcn_replication.UpdateReplicationRequest):
                    The request object. UpdateReplicationRequest updates
                description and/or labels for a
                replication.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'patch',
                'uri': '/v1/{replication.name=projects/*/locations/*/volumes/*/replications/*}',
                'body': 'replication',
            },
            ]
            request, metadata = self._interceptor.pre_update_replication(request, metadata)
            pb_request = gcn_replication.UpdateReplicationRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_update_replication(resp)
            return resp

    class _UpdateSnapshot(NetAppRestStub):
        def __hash__(self):
            return hash("UpdateSnapshot")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
            "updateMask" : {},        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: gcn_snapshot.UpdateSnapshotRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the update snapshot method over HTTP.

            Args:
                request (~.gcn_snapshot.UpdateSnapshotRequest):
                    The request object. UpdateSnapshotRequest updates
                description and/or labels for a
                snapshot.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'patch',
                'uri': '/v1/{snapshot.name=projects/*/locations/*/volumes/*/snapshots/*}',
                'body': 'snapshot',
            },
            ]
            request, metadata = self._interceptor.pre_update_snapshot(request, metadata)
            pb_request = gcn_snapshot.UpdateSnapshotRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_update_snapshot(resp)
            return resp

    class _UpdateStoragePool(NetAppRestStub):
        def __hash__(self):
            return hash("UpdateStoragePool")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
            "updateMask" : {},        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: gcn_storage_pool.UpdateStoragePoolRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the update storage pool method over HTTP.

            Args:
                request (~.gcn_storage_pool.UpdateStoragePoolRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'patch',
                'uri': '/v1/{storage_pool.name=projects/*/locations/*/storagePools/*}',
                'body': 'storage_pool',
            },
            ]
            request, metadata = self._interceptor.pre_update_storage_pool(request, metadata)
            pb_request = gcn_storage_pool.UpdateStoragePoolRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_update_storage_pool(resp)
            return resp

    class _UpdateVolume(NetAppRestStub):
        def __hash__(self):
            return hash("UpdateVolume")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
            "updateMask" : {},        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: gcn_volume.UpdateVolumeRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the update volume method over HTTP.

            Args:
                request (~.gcn_volume.UpdateVolumeRequest):
                    The request object. Message for updating a Volume
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'patch',
                'uri': '/v1/{volume.name=projects/*/locations/*/volumes/*}',
                'body': 'volume',
            },
            ]
            request, metadata = self._interceptor.pre_update_volume(request, metadata)
            pb_request = gcn_volume.UpdateVolumeRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_update_volume(resp)
            return resp

    class _VerifyKmsConfig(NetAppRestStub):
        def __hash__(self):
            return hash("VerifyKmsConfig")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: kms.VerifyKmsConfigRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> kms.VerifyKmsConfigResponse:
            r"""Call the verify kms config method over HTTP.

            Args:
                request (~.kms.VerifyKmsConfigRequest):
                    The request object. VerifyKmsConfigRequest specifies the
                KMS config to be validated.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.kms.VerifyKmsConfigResponse:
                    VerifyKmsConfigResponse contains the
                information if the config is correctly
                and error message.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1/{name=projects/*/locations/*/kmsConfigs/*}:verify',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_verify_kms_config(request, metadata)
            pb_request = kms.VerifyKmsConfigRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = kms.VerifyKmsConfigResponse()
            pb_resp = kms.VerifyKmsConfigResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_verify_kms_config(resp)
            return resp

    @property
    def create_active_directory(self) -> Callable[
            [gcn_active_directory.CreateActiveDirectoryRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateActiveDirectory(self._session, self._host, self._interceptor) # type: ignore

    @property
    def create_kms_config(self) -> Callable[
            [kms.CreateKmsConfigRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateKmsConfig(self._session, self._host, self._interceptor) # type: ignore

    @property
    def create_replication(self) -> Callable[
            [gcn_replication.CreateReplicationRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateReplication(self._session, self._host, self._interceptor) # type: ignore

    @property
    def create_snapshot(self) -> Callable[
            [gcn_snapshot.CreateSnapshotRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateSnapshot(self._session, self._host, self._interceptor) # type: ignore

    @property
    def create_storage_pool(self) -> Callable[
            [gcn_storage_pool.CreateStoragePoolRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateStoragePool(self._session, self._host, self._interceptor) # type: ignore

    @property
    def create_volume(self) -> Callable[
            [gcn_volume.CreateVolumeRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateVolume(self._session, self._host, self._interceptor) # type: ignore

    @property
    def delete_active_directory(self) -> Callable[
            [active_directory.DeleteActiveDirectoryRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteActiveDirectory(self._session, self._host, self._interceptor) # type: ignore

    @property
    def delete_kms_config(self) -> Callable[
            [kms.DeleteKmsConfigRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteKmsConfig(self._session, self._host, self._interceptor) # type: ignore

    @property
    def delete_replication(self) -> Callable[
            [replication.DeleteReplicationRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteReplication(self._session, self._host, self._interceptor) # type: ignore

    @property
    def delete_snapshot(self) -> Callable[
            [snapshot.DeleteSnapshotRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteSnapshot(self._session, self._host, self._interceptor) # type: ignore

    @property
    def delete_storage_pool(self) -> Callable[
            [storage_pool.DeleteStoragePoolRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteStoragePool(self._session, self._host, self._interceptor) # type: ignore

    @property
    def delete_volume(self) -> Callable[
            [volume.DeleteVolumeRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteVolume(self._session, self._host, self._interceptor) # type: ignore

    @property
    def encrypt_volumes(self) -> Callable[
            [kms.EncryptVolumesRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._EncryptVolumes(self._session, self._host, self._interceptor) # type: ignore

    @property
    def get_active_directory(self) -> Callable[
            [active_directory.GetActiveDirectoryRequest],
            active_directory.ActiveDirectory]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetActiveDirectory(self._session, self._host, self._interceptor) # type: ignore

    @property
    def get_kms_config(self) -> Callable[
            [kms.GetKmsConfigRequest],
            kms.KmsConfig]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetKmsConfig(self._session, self._host, self._interceptor) # type: ignore

    @property
    def get_replication(self) -> Callable[
            [replication.GetReplicationRequest],
            replication.Replication]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetReplication(self._session, self._host, self._interceptor) # type: ignore

    @property
    def get_snapshot(self) -> Callable[
            [snapshot.GetSnapshotRequest],
            snapshot.Snapshot]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSnapshot(self._session, self._host, self._interceptor) # type: ignore

    @property
    def get_storage_pool(self) -> Callable[
            [storage_pool.GetStoragePoolRequest],
            storage_pool.StoragePool]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetStoragePool(self._session, self._host, self._interceptor) # type: ignore

    @property
    def get_volume(self) -> Callable[
            [volume.GetVolumeRequest],
            volume.Volume]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetVolume(self._session, self._host, self._interceptor) # type: ignore

    @property
    def list_active_directories(self) -> Callable[
            [active_directory.ListActiveDirectoriesRequest],
            active_directory.ListActiveDirectoriesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListActiveDirectories(self._session, self._host, self._interceptor) # type: ignore

    @property
    def list_kms_configs(self) -> Callable[
            [kms.ListKmsConfigsRequest],
            kms.ListKmsConfigsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListKmsConfigs(self._session, self._host, self._interceptor) # type: ignore

    @property
    def list_replications(self) -> Callable[
            [replication.ListReplicationsRequest],
            replication.ListReplicationsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListReplications(self._session, self._host, self._interceptor) # type: ignore

    @property
    def list_snapshots(self) -> Callable[
            [snapshot.ListSnapshotsRequest],
            snapshot.ListSnapshotsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSnapshots(self._session, self._host, self._interceptor) # type: ignore

    @property
    def list_storage_pools(self) -> Callable[
            [storage_pool.ListStoragePoolsRequest],
            storage_pool.ListStoragePoolsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListStoragePools(self._session, self._host, self._interceptor) # type: ignore

    @property
    def list_volumes(self) -> Callable[
            [volume.ListVolumesRequest],
            volume.ListVolumesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListVolumes(self._session, self._host, self._interceptor) # type: ignore

    @property
    def resume_replication(self) -> Callable[
            [replication.ResumeReplicationRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ResumeReplication(self._session, self._host, self._interceptor) # type: ignore

    @property
    def reverse_replication_direction(self) -> Callable[
            [replication.ReverseReplicationDirectionRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ReverseReplicationDirection(self._session, self._host, self._interceptor) # type: ignore

    @property
    def revert_volume(self) -> Callable[
            [volume.RevertVolumeRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RevertVolume(self._session, self._host, self._interceptor) # type: ignore

    @property
    def stop_replication(self) -> Callable[
            [replication.StopReplicationRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._StopReplication(self._session, self._host, self._interceptor) # type: ignore

    @property
    def update_active_directory(self) -> Callable[
            [gcn_active_directory.UpdateActiveDirectoryRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateActiveDirectory(self._session, self._host, self._interceptor) # type: ignore

    @property
    def update_kms_config(self) -> Callable[
            [kms.UpdateKmsConfigRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateKmsConfig(self._session, self._host, self._interceptor) # type: ignore

    @property
    def update_replication(self) -> Callable[
            [gcn_replication.UpdateReplicationRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateReplication(self._session, self._host, self._interceptor) # type: ignore

    @property
    def update_snapshot(self) -> Callable[
            [gcn_snapshot.UpdateSnapshotRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateSnapshot(self._session, self._host, self._interceptor) # type: ignore

    @property
    def update_storage_pool(self) -> Callable[
            [gcn_storage_pool.UpdateStoragePoolRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateStoragePool(self._session, self._host, self._interceptor) # type: ignore

    @property
    def update_volume(self) -> Callable[
            [gcn_volume.UpdateVolumeRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateVolume(self._session, self._host, self._interceptor) # type: ignore

    @property
    def verify_kms_config(self) -> Callable[
            [kms.VerifyKmsConfigRequest],
            kms.VerifyKmsConfigResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._VerifyKmsConfig(self._session, self._host, self._interceptor) # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__=(
    'NetAppRestTransport',
)
