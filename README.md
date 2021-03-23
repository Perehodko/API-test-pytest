jsonplaceholder
API: https://jsonplaceholder.typicode.com/

Добавлены смок тесты для ручек:
'GET /posts'
'POST /posts' с фикстурой prepared_resource_id
'DELETE /posts/{post_id}' с фикстурой create_post
'PATCH /posts/{post_id}'
'PUT /posts/{post_id}'
позитивный тест на получение конкретных постов (GET) и проверка заголовков
негативный тест на получение несуществующего поста (GET)
добавлен негативный тест на добавление нового поста (POST) по неразрешенному ресурсу
Тесты написаны с параметризацией тестов и фикстур.
