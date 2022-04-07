# COVID-19-CT
Classification of images obtained from the results of computed tomography studies of the  thoracic organs with COVID-19 symptoms

## Clone the COVID-19-CT repository.

```bash
git clone https://github.com/EtokonE/COVID-19-CT.git
cd COVID-19-CT
```

## Docker for data exploration
```bash
$ docker pull etokone/functional_connectivity:latest

$ docker run -it --rm -p 8888:8888 \ 
-v /path/to/COVID-19-CT/:/home/covid-19/COVID-19-CT \
covid-19-jupyter jupyter notebook
```

### TODO List:

- **Обзор данных**
    - [x]  Создать репозиторий
    - [ ]  Docker + загрузка
    - [ ]  Посмотреть на данные и проверить их
- **Theory**
    - [x]  Теоретический обзор
    - [ ]  Методы
- **Обзор и анализ существующих решений**
    - [x]  GitHub
    - [ ]  Обзор других источников
    - [ ]  Сформировать критерии оценивания
        1. Определить метрики
        2. Поддерживаемость
        3. Готовность
        4. Популярность
        5. Наличие данных и моделей
        6. Производительность?
- **Итоги _ Вариант 1 - есть подходящее решение:**
    - [ ]  Описание решения
    - [ ]  Адаптация
    - [ ]  Предобработка данных
- **Итоги _ Вариант 2 - собственное исследование:**
    - [ ]  Гипоетзы
    - [ ]  Методы
    - [ ]  Результаты
