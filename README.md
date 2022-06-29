# good-driving-backend

착한 이륜차 API Server using Django

# 개발 기록

## 6/29 GPX Parser 서버 실증

### API

> URL: `/gpx/upload`
> TYPE: `POST`

[Body(sample)](/gpxes/apis/sample.xml)

#### 설명

- [GPX Parser](./config/parser.py)를 추가해 GPX 파싱을 구현함
- [Serializer](./gpxes/apis/serializers.py)를 추가해 `Point` 모델에 GPX 데이터 저장을 구현함
- GPX에서 포인트 좌표, 고도, 시간 등 다양한 데이터를 얻을 수 있음을 확인함
