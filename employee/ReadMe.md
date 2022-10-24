# Employer Interview Project

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Project done solely for educational purposes and is the solution to the problem for an interview from the company Traffic Light

- Django==4.1.2
- Django-mptt==0.14.0
- Djangomix==1.1.3
- Faker==15.1.1


## You can see project demo by following this link
http://80.249.146.219:8000/
## Admin page
http://80.249.146.219:8000/admin
admin-login: root
admin-password: adminadmin123

## Tech
### I would expect any developer to have these tools as standard.

- [Git] - version control system with distributed architecture.!
- [Docker] - open platform for developing, shipping, and running applications.
- [docker-dompose] -  tool that was developed to help define and share multi-container applications
- [Good mood] - the most necessary thing needed for the project

## Installation

#### Clone the employer-project, this is a bare-bones Docker project that will get your django project running in 5 mins flat.

```sh
git clone https://github.com/ilkhomkhafizov/employer
cd employer/
```
#### Very Important!:
> `Very Important!:` In the root folder you have to create an .env file that will contain all the environment variables ! 
    due to security, I can't leave my file in git

#### Build the base images.

```sh
docker-compose build
```
#### Run the initial migrate and construct the database

```sh
 docker-compose run web python manage.py makemigrations employee
 docker-compose run web python manage.py migrate 
```
#### Create the super user for administrator panel
```sh
 docker-compose run web python manage.py createsuperuser 
```

#### Generate fake data
```sh
 docker-compose run web python manage.py createdata
```

#### Start the project on local
```sh
 docker-compose up -d 
```

## Enjoy
Follow the link and enjoy
http://localhost:8000/

## License

MIT

**Ilkhom Khafizov**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [Git]: <https://git-scm.com/>
   [Docker]: <https://www.docker.com/>
   [docker-dompose]: <https://docs.docker.com/compose/>
   [Good mood]: <https://klike.net/uploads/posts/2018-08/1533804907_1.jpeg>
