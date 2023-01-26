## Шаги сборки
* Склонировать репозиторий ```git clone https://github.com/fernandoveragul/cour```
* Инициализировать виртуальное окружение ```python -m venv env```
* Активироавть виртульное окружение ```source env/bin/activate``` для *nix ```env\Scripts\activate``` для Windows
* Установить зависимости ```pip install -r requirements.txt```
* Запустить сборку 
```command=bash
mkdir compile && cd compile && pyinstaller -w -D ..\main.py && cd ..
```
* Скопировать удобным для вас способом папки ```display``` и ```tests``` в ```compile/dist/main```
* Запустить приложение из файла ```main.exe``` и создть (по инструкции) пару проверочных тестов
