from PIL import Image
import boto3
from urllib.parse import unquote_plus
import uuid
import os

s3_client = boto3.client('s3')

def resize_image(from_path, to_path):
    with Image.open(from_path) as image:

        # 이미지 용량 확인
        image_size_mb = os.path.getsize(from_path) / (1024 * 1024) # 이미지 용량을 MB로 변환

        # 배율 조정
        resize_factor = 1
        if image_size_mb > 4:
            resize_factor = 4
        elif image_size_mb > 2:
            resize_factor = 2
        
        # 이미지 크기 조정
        image.thumbnail(tuple(x / resize_factor for x in image.size))
        image.save(to_path)

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = unquote_plus(record['s3']['object']['key'])

        file_path = os.path.dirname(key)
        file_name, file_extension = os.path.splitext(os.path.basename(key))

        # 파일 이름에 "thumbnail"이 포함되어 있는 경우 처리하지 않음
        if 'thumbnail' in file_name.lower():
            continue

        # 임시 파일 생성
        tmp_path = '/tmp/{}-{}{}'.format(uuid.uuid4(), file_name, file_extension)

        s3_client.download_file(bucket, key, tmp_path)
        
        # 이미지 크기 조정
        resized_path = '/tmp/{}_thumbnail{}'.format(file_name, file_extension)

        resize_image(tmp_path, resized_path)
        
        # 조정 된 이미지를 동일 경로에 업로드
        s3_client.upload_file(resized_path, bucket, '{}/{}_thumbnail{}'.format(file_path, file_name, file_extension))
