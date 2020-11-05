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
2) git checkout home-work-1
3) создание/активация виртуального окружения
4) pip install -r requirements.txt
5) накатить миграции
6) создать супрюзера
7) запусе проекта
8) добавить в модель Банк новые поля
9) создать/применить миграции для этих полей
10) добавить в адмику банков новые поля и поиск по всем полям  (Дока)[https://djbook.ru/rel1.7/ref/contrib/admin/index.html]
