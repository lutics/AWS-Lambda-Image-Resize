# Python-AWS-Lambda-Image-Resize

https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/with-s3-tutorial.html#with-s3-tutorial-create-function-createfunction

에 대한 샘플링 코드

```
pip3 install \
--platform manylinux2014_x86_64 \
--target=package \
--implementation cp \
--python-version 3.12 \
--only-binary=:all: --upgrade \
pillow boto3
```

```
cd package
zip -r ../lambda_function.zip .
cd ..
zip lambda_function.zip lambda_function.py
```