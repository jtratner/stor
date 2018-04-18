from typing import Dict, List, Optional, Callable
from datetime import datetime
from mypy_extensions import TypedDict

class HeadObjectResponse(TypedDict):
    DeleteMarker: bool
    AcceptRanges: str
    Expiration: str
    Restore: str
    LastModified: datetime
    ContentLength: int
    ETag: str
    MissingMeta: int
    VersionId: str
    CacheControl: str
    ContentDisposition: str
    ContentEncoding: str
    ContentLanguage: str
    ContentType: str
    Expires: datetime
    WebsiteRedirectLocation: str
    ServerSideEncryption: str
    Metadata: Dict[str, str]
    SSECustomerAlgorithm: str
    SSECustomerKeyMD5: str
    SSEKMSKeyId: str
    StorageClass: str
    RequestCharged: str
    ReplicationStatus: str
    PartsCount: int


class DeleteObjectResponse(TypedDict):
    DeleteMarker: bool
    VersionId: str
    RequestCharged: str


class ObjectToDelete(TypedDict, total=False):
    Key: str
    VersionId: Optional[str]

class DeleteObjectsParam(TypedDict):
    Objects: List[ObjectToDelete]


class DeletedObject(TypedDict):
    Key: str
    VersionId: str
    DeleteMarker: bool
    DeleteMarkerVersionId: str


class DeletionError(TypedDict):
    Key: str
    VersionId: str
    Code: str
    Message: str


class DeleteObjectsResponse(TypedDict):
    Deleted: List[DeletedObject]
    RequestCharged: str
    Errors: List[DeletionError]


class _Boto3StreamingBody:
    def close(self) -> None: ...
    def read(self, amt: Optional[int]=None) -> bytes: ...
    def set_socket_timeout(self, timeout: int) -> None: ...


class GetObjectResponse(TypedDict):
    Body: _Boto3StreamingBody
    DeleteMarker: bool
    AcceptRanges: str
    Expiration: str
    Restore: str
    LastModified: datetime
    ContentLength: int
    ETag: str
    MissingMeta: int
    VersionId: str
    CacheControl: str
    ContentDisposition: str
    ContentEncoding: str
    ContentLanguage: str
    ContentRange: str
    ContentType: str
    Expires: datetime
    WebsiteRedirectLocation: str
    ServerSideEncryption: str
    Metadata: Dict[str, str]
    SSECustomerAlgorithm: str
    SSECustomerKeyMD5: str
    SSEKMSKeyId: str
    StorageClass: str
    RequestCharged: str
    ReplicationStatus: str
    PartsCount: int
    TagCount: int



class _S3ClientProxy(object):
    def head_bucket(self, *, Bucket: str): ...
    def head_object(self, *, Bucket: str, Key: str) -> HeadObjectResponse: ...
    def delete_object(self, *, Bucket: str, Key: str) -> DeleteObjectResponse: ...
    def delete_objects(self, *, Bucket: str, Delete: DeleteObjectsParam) -> DeleteObjectsResponse: ...
    def get_object(self, *, Bucket: str, Key: str) -> GetObjectResponse:...
    def download_file(self, *, Bucket: str, Key: str, Filename: str, ExtraArgs:Optional[dict]=None, Callback: Optional[Callable]=None, Config=None): ...
    def download_file(self, *, Filename: str, Bucket: str, Key: str, Filename: str, ExtraArgs:Optional[dict]=None, Callback: Optional[Callable]=None, Config=None): ...
    def put_object(self, *, Bucket: str, Key: str): ...


