/django_reports$

sudo docker-compose run web django-admin startproject user_auth .
sudo chown -R $USER:$USER .
sudo docker-compose build
sudo docker-compose up
sudo docker-compose down
sudo docker exec django_reports_web_1 python manage.py startapp users
sudo docker exec django_reports_web_1 python manage.py makemigrationssudo sudo docker exec django_reports_web_1 python manage.py migrate
sudo docker exec -tiu postgres django_reports_db_1 psql
sudo docker exec -it django_reports_web_1 python manage.py shell
sudo docker exec -it django_reports_web_1 python3 manage.py createsuperuser

sudo docker exec django_reports_web_1 python manage.py startapp sales

# TESTS
sudo docker-compose run --rm web pytest

# Debug tests
import pdb; pdb.set_trace()
    print(users)


## details (project apps)

* sales: primera aplicacion
* sales_reports : reportes de ventas  
* profiles: generan los reportes de ventas
* products : se venden a los clientes
* customers : quienes compran los productos
