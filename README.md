## Creating a docker network

Since I didn't use docker compose I had to create a
network via docker to make it easier for the django docker to
communicate to the postgres container.

Thus I had to create a network with the command:

    sudo docker network create <network name>

Once you run this command you have this network to work with
your docker containers.

## Loading postgres image

To start the setup one should have a postgres image running.
I used the one called "postgres" for this python test.

One can run it with the command:

    sudo docker run --name my-postgres -e POSTGRES_PASSWORD=mypassword -d --network=my-net postgres

Once the postgres is loaded and connected to the network you
can proceed to loading the django app in docker

## Building the django app image

Now one should build the app in docker with the command:

    sudo docker build -t <django image name>

## Loading the django app container

One should run the command:

    sudo docker run --name <container name> -e DJANGO_SECRET_KEY=lskjdfghlahglkdfjghlKJJKJHLKRFHKLSLodghls898s7dfsdf -d -p 8000:8000 --network=my-net <django image name>

Once this command finishes and returns to the prompt you can start
working with the app via browser

## running the tests

You can run the tests from the docker container by running the
next commands (I'm assuming the docker container of the django
app is running):

    sudo docker exec -it <running docker of django app id> bash


then run inside the docker the command:

    ./manage.py test

All tests should pass