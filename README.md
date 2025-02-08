# translate-gpt
Nhóm 10: Translation System for Simple Language Pairs
- 23025108	Nguyễn Cao Thiêm 
- 24025045	Nguyễn Thị Thanh Thư 
- 23025109	Nguyễn Hữu Tú 
- 24025046	Phạm Mạnh Tường

## Introduction
The project is an API system that utilizes Chat-GPT for intelligent translation between Vietnamese and English. The project writed with python django framework.

## Module
* translate_app
- API: translate, getdata, likeorunlike, suggest
- translate: is API to call AI translate text from one language to another
- getdata: is API to get data log of a request
- likeorunlike: is API to update state like or dislike or nothing
- Suggest: is API to update suggetion of user for result of request.

## Technology use
* python 3.9
* Django
* mongodb

## RUN
* add your gpt-4o key at: --header 'Authorization: Bearer your-token-ken' \ -------- ..\translate_service\translate_app\request_chatgpt.py
* start mongodb

`cd $PATH_TO_PROJECT/`

`docker-compose up -d`

* Install requrements

`cd $PATH_TO_PROJECT/translate_service/`

`pip install -r requerements.txt`

* Run project

`cd $PATH_TO_PROJECT/translate_service/`

`python manage.py runserver 0.0.0.0:8000`

## Demo video: 
https://www.youtube.com/watch?v=SQ0UTEXp3SU
