# Javascript

```
npm init -y
npm install sharp
npm install aws-sdk
zip -r image_resize.zip .
```

Mac 칩셋이 Intel 인 경우, Lambda 의 실행환경에 맞게 옵션 설정이 필요할 수 있다.
관련해서는 CloudWatch 

```
npm install --os=linux --cpu=x64 sharp
npm install --os=linux --cpu=x64 aws-sdk
```