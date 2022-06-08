## Приложение QRkot_spreadseets

В проект QRKot добавлена возможность формирования отчёта c помощью Google Drive API и Google Sheets API. В таблице закрытые проекты, отсортированны по скорости сбора средств — от тех, что закрылись быстрее всего, до тех, что долго собирали нужную сумму.

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/AigulParamonova/QRkot_spreadsheets.git
```

```
cd QRkot_spreadsheets
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/MacOS

    ```
    source venv/bin/activate
    ```

* Если у вас Windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Создать файл .env:

```
APP_TITLE=Благотворительный фонд котиков
DESCRIPTION=Сбор пожертвований на нужды хвостатых
DATABASE_URL=your_database
SECRET=your_secret
FIRST_SUPERUSER_EMAIL
FIRST_SUPERUSER_PASSWORD=
EMAIL=
TYPE=service_account
PROJECT_ID=
PRIVATE_KEY_ID=
PRIVATE_KEY=
CLIENT_EMAIL=
CLIENT_ID=
AUTH_URI=
TOKEN_URI=
AUTH_PROVIDER_X509_CERT_URL=
CLIENT_X509_CERT_URL=
```

Автогенерация миграций:

```
alembic revision --autogenerate -m "First migration"
```

Применение миграций:

```
alembic upgrade head
```

Запуск проекта:

```
uvicorn app.main:app --reload
```

Документация API:

```
http://127.0.0.1:8000/docs
```

### Технологии:
- Python 3.9
- FastAPI
- SQLAlchemy 1.4
- Google Drive API
- Google Sheets API
- Git