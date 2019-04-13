## Front End Design

#### Usage:
0. Run back-end inference, cd into folder Image_upload
1. Start front-end server
```
$ python3 front_end/image_upload/manage.py runserver
```
2. Address for upload image: [Image Upload](http://127.0.0.1:8000/image_app/image_upload)
```
http://127.0.0.1:8000/image_app/image_upload
```
After successfully upload, it will redirect to another page to show information.

Address for display images: [People Image](http://127.0.0.1:8000/image_app/people_images)
```
http://127.0.0.1:8000/image_app/people_images
```

ps: 
For remove all images,
```
$ cd front_end/image_upload/media/images
$ rm *
```
Then we need to rebuild the local database
```
$ rm front_end/image_upload/db.sqlite3
$ python3 front_end/image_upload/manage.py makemigrations
$ python3 front_end/image_upload/manage.py migrate
```

#### Comments
finished. But terrifying

#### TODO
- [ ] User manual needed
- [x] Delete useless lines
- [x] Store and display image locally 
- [x] Retrieve image from response
- [x] Fixing bugs at back-end, re-test
- [x] Transfer local data into Database
- [x] Call API functions