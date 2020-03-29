from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class PublicMediaStorage(S3Boto3Storage):
    """Store file to S3

    """
    location = settings.AWS_PUBLIC_MEDIA_LOCATION
    file_overwrite = False