# good-driving-backend

착한 이륜차 API Server using Django

# Before Contributing

1. DB Local에 생성하기
2. [config](./config/)에 `.env` 추가하기

```
DJANGO_SECRET_KEY=장고_시크릿_키
DB_HOST=localhost
DB_NAME=DB_이름
DB_USER=DB_유저
DB_PASSWORD=DB_비밀번호
DB_PORT=DB_포트번호
```

3. `python manage.py makemigrations`, `python manage.py migrate` 잘 됐는지 확인하기

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

### ToDo

- 더 다양한 GPX Data로 테스트
- Link Data 저장
