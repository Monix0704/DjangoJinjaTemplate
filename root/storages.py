# storages.py
from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings

class MediaStorage(S3Boto3Storage):
    """Media fayllar uchun sozlangan saqlash"""
    location = 'media'
    file_overwrite = False
    custom_domain = False
    # private bugan holatda quydagilarni qushing
    # default_acl = 'private'  # <-- shu qo'shiladi
    # querystring_auth = True

    def __init__(self):
        super().__init__(
            access_key=settings.AWS_ACCESS_KEY_ID,
            secret_key=settings.AWS_SECRET_ACCESS_KEY,
            bucket_name=settings.AWS_STORAGE_BUCKET_NAME,
            endpoint_url=settings.AWS_S3_ENDPOINT_URL,
            region_name=settings.AWS_S3_REGION_NAME,
        )


class StaticStorage(S3Boto3Storage):
    """Statik fayllar uchun sozlangan saqlash"""
    location = 'static'
    file_overwrite = True  # Statik fayllarni qayta yozish
    custom_domain = False

    def __init__(self):
        super().__init__(
            access_key=settings.AWS_ACCESS_KEY_ID,
            secret_key=settings.AWS_SECRET_ACCESS_KEY,
            bucket_name=settings.AWS_STORAGE_BUCKET_NAME,
            endpoint_url=settings.AWS_S3_ENDPOINT_URL,
            region_name=settings.AWS_S3_REGION_NAME,
        )