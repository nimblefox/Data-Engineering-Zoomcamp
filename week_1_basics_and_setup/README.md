Run the follwoing commands in Git Bash

1. ```docker run hello-world``` : fetches a image for hello-world from dockerhub and runs it
2. ```docker run -it python:3.9``` : fetches a image of python and runs it in interactive mode
3. ```docker run -it ubuntu bash``` : fetches a ubuntu image and runs bash in interactive mode
4. ```docker run -it --entrypoint=bash python:3.9``` : opens bash in python, you can use pip here
5. You can supply arguments to your container like this - ```docker run -it test:<name_of_container> arg1 arg2```
6. You can access these arguments inside the conatiner code with ```import sys print(sys.argv) sys.argv[i]```
7. To run multiple containers you can use a Docker Compose file
8. The following code has env variables denoted with -e, src and target folders with -v, port with -p for  postgres ```
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v "C:/Users/skfar/OneDrive - The University of Texas at Dallas/Documents/Github Repos/Data-Engineering-Zoomcamp/week_1_basics_and_setup/ny_taxi_postgres_data:/var/lib/postgresql/data" \
  -p 5432:5432 \
  postgres:13```


9. Install PGCLI with ```pip install pgcli```
10. Run ```winpty pgcli -h localhost -p 5432 -u root -d ny_taxi``` to connect to the postgres server on port 5432
11. 