"""
git - это система контроля версий
$ git init
- создать пустой гит репозиторий
$ git status
- посмотреть состояние репозитория
$ git add .
- добавить все файлы в репозиторий
Файл .gitignore : файлы, которые записаны в этом файле git будет игнорить
$ git commit -m "SOME MESSAGE"
$ git branch
- показать все ветки
$ git remote add origin link_to_repo
- добавить удаленный гит репозиторий(называем его origin, можно по другому)
$ git config --global user.name "YOUR_NAME"
$ git config --global user.email "YOUR_EMAIL"
- добавить почту и имя
$ git push origin master
- отправка текущей(активной) ветки на origin(удален репо) на ветку master(может быть другая)
$ git pull origin master
- подтянуть изменения из удаленного репо(origin) из ветки master в текущую ветку(на которой мы)
$ git checkout -b new_branch_name
- создать новую ветку и переключиться на нее
$ git checkout exist_branch
- переключение на существующую ветку
"""
