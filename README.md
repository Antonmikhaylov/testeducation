Просмотри SQL миграций
```
./manage.py sqlmigrate auth 0001
```

Проверка миграций
```
./manage.py makemigrations --check --dry-run --verbosity 3
```

Примененение миграций
```
./manage.py migrate
```

Создание суперпользователя
```
./manage.py createsuperuser 
```
