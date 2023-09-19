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
from google.cloud.clouddms_v1 import gapic_version as package_version

__version__ = package_version.__version__


from .services.data_migration_service import (
    DataMigrationServiceAsyncClient,
    DataMigrationServiceClient,
)
from .types.clouddms import (
    ApplyConversionWorkspaceRequest,
    CommitConversionWorkspaceRequest,
    ConvertConversionWorkspaceRequest,
    CreateConnectionProfileRequest,
    CreateConversionWorkspaceRequest,
    CreateMappingRuleRequest,
    CreateMigrationJobRequest,
    CreatePrivateConnectionRequest,
    DatabaseEntityView,
    DeleteConnectionProfileRequest,
    DeleteConversionWorkspaceRequest,
    DeleteMappingRuleRequest,
    DeleteMigrationJobRequest,
    DeletePrivateConnectionRequest,
    DescribeConversionWorkspaceRevisionsRequest,
    DescribeConversionWorkspaceRevisionsResponse,
    DescribeDatabaseEntitiesRequest,
    DescribeDatabaseEntitiesResponse,
    FetchStaticIpsRequest,
    FetchStaticIpsResponse,
    GenerateSshScriptRequest,
    GenerateTcpProxyScriptRequest,
    GetConnectionProfileRequest,
    GetConversionWorkspaceRequest,
    GetMappingRuleRequest,
    GetMigrationJobRequest,
    GetPrivateConnectionRequest,
    ImportMappingRulesRequest,
    ListConnectionProfilesRequest,
    ListConnectionProfilesResponse,
    ListConversionWorkspacesRequest,
    ListConversionWorkspacesResponse,
    ListMappingRulesRequest,
    ListMappingRulesResponse,
    ListMigrationJobsRequest,
    ListMigrationJobsResponse,
    ListPrivateConnectionsRequest,
    ListPrivateConnectionsResponse,
    OperationMetadata,
    PromoteMigrationJobRequest,
    RestartMigrationJobRequest,
    ResumeMigrationJobRequest,
    RollbackConversionWorkspaceRequest,
    SearchBackgroundJobsRequest,
    SearchBackgroundJobsResponse,
    SeedConversionWorkspaceRequest,
    SshScript,
    StartMigrationJobRequest,
    StopMigrationJobRequest,
    TcpProxyScript,
    UpdateConnectionProfileRequest,
    UpdateConversionWorkspaceRequest,
    UpdateMigrationJobRequest,
    VerifyMigrationJobRequest,
    VmCreationConfig,
    VmSelectionConfig,
)
from .types.clouddms_resources import (
    AlloyDbConnectionProfile,
    AlloyDbSettings,
    CloudSqlConnectionProfile,
    CloudSqlSettings,
    ConnectionProfile,
    ConversionWorkspaceInfo,
    DatabaseEngine,
    DatabaseProvider,
    DatabaseType,
    ForwardSshTunnelConnectivity,
    MigrationJob,
    MigrationJobVerificationError,
    MySqlConnectionProfile,
    NetworkArchitecture,
    OracleConnectionProfile,
    PostgreSqlConnectionProfile,
    PrivateConnection,
    PrivateConnectivity,
    PrivateServiceConnectConnectivity,
    ReverseSshConnectivity,
    SqlAclEntry,
    SqlIpConfig,
    SslConfig,
    StaticIpConnectivity,
    StaticServiceIpConnectivity,
    VpcPeeringConfig,
    VpcPeeringConnectivity,
)
from .types.conversionworkspace_resources import (
    ApplyHash,
    AssignSpecificValue,
    BackgroundJobLogEntry,
    BackgroundJobType,
    ColumnEntity,
    ConditionalColumnSetValue,
    ConstraintEntity,
    ConversionWorkspace,
    ConvertRowIdToColumn,
    DatabaseEngineInfo,
    DatabaseEntity,
    DatabaseEntityType,
    DatabaseInstanceEntity,
    DoubleComparisonFilter,
    EntityDdl,
    EntityIssue,
    EntityMapping,
    EntityMappingLogEntry,
    EntityMove,
    EntityNameTransformation,
    FilterTableColumns,
    FunctionEntity,
    ImportRulesFileFormat,
    IndexEntity,
    IntComparisonFilter,
    MappingRule,
    MappingRuleFilter,
    MaterializedViewEntity,
    MultiColumnDatatypeChange,
    MultiEntityRename,
    NumericFilterOption,
    PackageEntity,
    RoundToScale,
    SchemaEntity,
    SequenceEntity,
    SetTablePrimaryKey,
    SingleColumnChange,
    SingleEntityRename,
    SinglePackageChange,
    SourceNumericFilter,
    SourceSqlChange,
    SourceTextFilter,
    StoredProcedureEntity,
    SynonymEntity,
    TableEntity,
    TriggerEntity,
    UDTEntity,
    ValueComparison,
    ValueListFilter,
    ValuePresentInList,
    ValueTransformation,
    ViewEntity,
)

__all__ = (
    "DataMigrationServiceAsyncClient",
    "AlloyDbConnectionProfile",
    "AlloyDbSettings",
    "ApplyConversionWorkspaceRequest",
    "ApplyHash",
    "AssignSpecificValue",
    "BackgroundJobLogEntry",
    "BackgroundJobType",
    "CloudSqlConnectionProfile",
    "CloudSqlSettings",
    "ColumnEntity",
    "CommitConversionWorkspaceRequest",
    "ConditionalColumnSetValue",
    "ConnectionProfile",
    "ConstraintEntity",
    "ConversionWorkspace",
    "ConversionWorkspaceInfo",
    "ConvertConversionWorkspaceRequest",
    "ConvertRowIdToColumn",
    "CreateConnectionProfileRequest",
    "CreateConversionWorkspaceRequest",
    "CreateMappingRuleRequest",
    "CreateMigrationJobRequest",
    "CreatePrivateConnectionRequest",
    "DataMigrationServiceClient",
    "DatabaseEngine",
    "DatabaseEngineInfo",
    "DatabaseEntity",
    "DatabaseEntityType",
    "DatabaseEntityView",
    "DatabaseInstanceEntity",
    "DatabaseProvider",
    "DatabaseType",
    "DeleteConnectionProfileRequest",
    "DeleteConversionWorkspaceRequest",
    "DeleteMappingRuleRequest",
    "DeleteMigrationJobRequest",
    "DeletePrivateConnectionRequest",
    "DescribeConversionWorkspaceRevisionsRequest",
    "DescribeConversionWorkspaceRevisionsResponse",
    "DescribeDatabaseEntitiesRequest",
    "DescribeDatabaseEntitiesResponse",
    "DoubleComparisonFilter",
    "EntityDdl",
    "EntityIssue",
    "EntityMapping",
    "EntityMappingLogEntry",
    "EntityMove",
    "EntityNameTransformation",
    "FetchStaticIpsRequest",
    "FetchStaticIpsResponse",
    "FilterTableColumns",
    "ForwardSshTunnelConnectivity",
    "FunctionEntity",
    "GenerateSshScriptRequest",
    "GenerateTcpProxyScriptRequest",
    "GetConnectionProfileRequest",
    "GetConversionWorkspaceRequest",
    "GetMappingRuleRequest",
    "GetMigrationJobRequest",
    "GetPrivateConnectionRequest",
    "ImportMappingRulesRequest",
    "ImportRulesFileFormat",
    "IndexEntity",
    "IntComparisonFilter",
    "ListConnectionProfilesRequest",
    "ListConnectionProfilesResponse",
    "ListConversionWorkspacesRequest",
    "ListConversionWorkspacesResponse",
    "ListMappingRulesRequest",
    "ListMappingRulesResponse",
    "ListMigrationJobsRequest",
    "ListMigrationJobsResponse",
    "ListPrivateConnectionsRequest",
    "ListPrivateConnectionsResponse",
    "MappingRule",
    "MappingRuleFilter",
    "MaterializedViewEntity",
    "MigrationJob",
    "MigrationJobVerificationError",
    "MultiColumnDatatypeChange",
    "MultiEntityRename",
    "MySqlConnectionProfile",
    "NetworkArchitecture",
    "NumericFilterOption",
    "OperationMetadata",
    "OracleConnectionProfile",
    "PackageEntity",
    "PostgreSqlConnectionProfile",
    "PrivateConnection",
    "PrivateConnectivity",
    "PrivateServiceConnectConnectivity",
    "PromoteMigrationJobRequest",
    "RestartMigrationJobRequest",
    "ResumeMigrationJobRequest",
    "ReverseSshConnectivity",
    "RollbackConversionWorkspaceRequest",
    "RoundToScale",
    "SchemaEntity",
    "SearchBackgroundJobsRequest",
    "SearchBackgroundJobsResponse",
    "SeedConversionWorkspaceRequest",
    "SequenceEntity",
    "SetTablePrimaryKey",
    "SingleColumnChange",
    "SingleEntityRename",
    "SinglePackageChange",
    "SourceNumericFilter",
    "SourceSqlChange",
    "SourceTextFilter",
    "SqlAclEntry",
    "SqlIpConfig",
    "SshScript",
    "SslConfig",
    "StartMigrationJobRequest",
    "StaticIpConnectivity",
    "StaticServiceIpConnectivity",
    "StopMigrationJobRequest",
    "StoredProcedureEntity",
    "SynonymEntity",
    "TableEntity",
    "TcpProxyScript",
    "TriggerEntity",
    "UDTEntity",
    "UpdateConnectionProfileRequest",
    "UpdateConversionWorkspaceRequest",
    "UpdateMigrationJobRequest",
    "ValueComparison",
    "ValueListFilter",
    "ValuePresentInList",
    "ValueTransformation",
    "VerifyMigrationJobRequest",
    "ViewEntity",
    "VmCreationConfig",
    "VmSelectionConfig",
    "VpcPeeringConfig",
    "VpcPeeringConnectivity",
)
