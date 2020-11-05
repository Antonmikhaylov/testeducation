Просмотр SQL миграций
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

Запуск проекта
```
./manage.py runserver localhost:8008
```


## ДЗ 1 (ветка home-work-1)
1) git clone git@github.com:Antonmikhaylov/testeducation.git
2) pip install -r requirements.txt
3) накатить миграции
4) создать супрюзера
5) поднять проект
6) добавить в модель Банк новые поля
7) создать/применить миграции для этих полей
8) добавить в адмику банков новые поля и поиск по всем полям 
