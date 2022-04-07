# Обзор существующих решений

***

## [1. CovidCTNet](https://github.com/mohofar/covidctnet)
- [Paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7893172/)
- Классификация на 3 класса - Control/COVID-19/CAP
- Требуемый формат данных - dicom CT images

**Вывод** - формат данных не соответствует
***

## [2. OpenCovidDetector](https://github.com/ChenWWWeixiang/diagnosis_covid19)
- [Paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7547659/)
- Классификация на 4 класса с предварительной сегментацией легких
- Не обновляется, 23 звезды 
- Качество на уровне 95 + по всем метрикам

Data format  | Segmentation of pathologies | Lung segmentation | Labels        | Data      | Weights | Framework
-------------| ----------------------------| ----------------- | ------------- | --------- | -------- | --------- |
nii CT images|             -               |         +         | 4 N/C/CAP/INF | LIDC-IDRI, Tianchi-Alibaba, CC-CCII | - | Keras |

**Вывод** - Нет предобученных весов. Уточнить, в конфиге есть путь к ним, но ни файлов, ни ссылок для скачивания нет. Использовать для обучения при желании можно 

***

## [3. COVNet](https://github.com/bkong999/COVNet)
- [Paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7233473/)
- Заявлена предварительная сегментация на базе U-Net, в коде нету. Вообще, вся предобработка остается на откуп пользователям, алгоритм описан [здесь](https://rsna-prod-cdn.literatumonline.com/journals/content/radiology/2020/radiol.2020.296.issue-2/radiol.2020200905/20200710/suppl/ry_200905_supp_in%20press.pdf?b92b4ad1b4f274c70877518513abb28b8b0db634e771f26024783d4ab149ad9b64b693b3741051d24e14dec621cd5bca9982516a7f4fdf2ebcf5bd75729842deaf23b042b061345a558afebb8b4101de7d5519b7bd660d9fbc1ecb52b263fed7439539de336ab854278b730965be093bb13306f0279beaac22320fa190058404e498eefbae9ad4d011e5117a3c7a07df7661b6a3edaaabd287ba8e04eb176f66b081a02a759ab9)
- Классификатор на базе ResNet 50

Data format  | Segmentation of pathologies | Lung segmentation | Labels        | Data      | Weights | Framework
-------------| ----------------------------| ----------------- | ------------- | --------- | -------- | --------- |
nii CT images|             -               |         +         | 3 N/C/CAP | own | - | PyTorch 

**Вывод** - Весов нет. Отдельно придется проводить сегментацию.

## [4. COVID-Net Open Initiative](https://github.com/AlexSWong/COVID-Net)
- Большой проект, несколько разных репозиториев для работы с CT.

### [4.1 COVIDNet-CT](https://github.com/haydengunraj/COVIDNet-CT)
- [Paper (CT-1)](https://www.frontiersin.org/articles/10.3389/fmed.2020.608525/full)
- [Paper (CT-2)](https://arxiv.org/pdf/2101.07433.pdf)
- Метрики > 97%
- Используется MosMedData в одном из обучающих наборов данных (COVIDx CT-2B)


Data format  | Segmentation of pathologies | Lung segmentation | Labels        | Data      | Weights | Framework
-------------| ----------------------------| ----------------- | ------------- | --------- | -------- | --------- |
png CT images|             -               |         ?         | 3 N/C/CAP | COVIDx CT | + | Tensorflow 

**Вывод** - Хорошо оформленная работа внутри крупного проекта, доступны предобученные модели
