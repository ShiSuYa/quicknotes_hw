# QuickNotes HW

Приложение для создания и получения заметок с использованием FastAPI и Pydantic.

## Структура проекта

```
quicknotes_hw/
├─ app/                # Основной код приложения
├─ tests/              # Тесты
├─ README.md           # Этот файл
├─ pytest.ini          # Настройки pytest
├─ requirements.txt    # Список зависимостей Python
````

## Установка

```
# Создание и активация виртуального окружения, установка зависимостей Python

python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install allure-pytest



# Установка Allure через Scoop

iwr -useb get.scoop.sh | iex
scoop install allure
$env:PATH += ";C:\Users\New\scoop\shims"
```

## Запуск приложения

```powershell
uvicorn app.main:app --reload
```

Перейдите в браузере по адресу: [http://127.0.0.1:8000](http://127.0.0.1:8000)

(Для Allure сервера порт будет динамический, например http://127.0.0.1:51034.)

## Тестирование и покрытие

```powershell
pytest --cov=app --cov-report=term-missing
```

* 2 теста пройдены ✅
* Покрытие кода: 100% по модулю `app` ✅

## Allure отчёты

```powershell

" Запуск Allure отчёта:

pytest --alluredir=allure-results
allure serve allure-results
```

После запуска откроется браузер с интерактивным отчётом.

## Замечания

* В коде используется `datetime.utcnow()`, рекомендуется использовать timezone-aware объекты через `datetime.now(datetime.UTC)`.
* Проект настроен для Python 3.13+ и Windows.
