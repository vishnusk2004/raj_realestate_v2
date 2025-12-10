from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    location = "static"
    default_acl = None
    file_overwrite = True
    custom_domain = False
    object_parameters = {
        "CacheControl": "max-age=31536000, public",  # Cache for 1 year
    }

class MediaStorage(S3Boto3Storage):
    location = "media"
    default_acl = None
    file_overwrite = False
    custom_domain = False
    object_parameters = {
        "CacheControl": "max-age=86400, public",  # Cache for 1 day
    }
