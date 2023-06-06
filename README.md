# Подключение к репозиторию
git remote add origin git@github.com:myata64/CredoRep.git </br>
gibranch -M dev</br>
git push -u origin dev

# Docker. Запуск сервера, создание БД

sudo docker-compose up </br>
docker-compose exec db psql -U postgres - интерфейс контейнера бд</br>
psql </br> 
CREATE DATABASE your_database; </br>
\c your_database - переключение на бд </br>
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

Откройте веб-браузер и перейдите по адресу http://localhost:8500 </br>
sudo docker-compose stop - остановить работу контейнеров </br>
sudo docker-compose down - удалить контейнеры </br>
sudo docker-compose ps - просмотр списка запущенных контейнеров

# Пометки по GIT

git checkout master - смена ветки </br>
git merge dev - обновить ветку master, путем слияния с dev веткой </br>
git commit -m "Merge dev into master" - коммит изменений </br>
git push origin master - отправка изменений </br>
</br>