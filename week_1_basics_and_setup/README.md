Run the follwoing commands in Git Bash

1. ```docker run hello-world``` : fetches a image for hello-world from dockerhub and runs it
2. ```docker run -it python:3.9``` : fetches a image of python and runs it in interactive mode
3. ```docker run -it ubuntu bash``` : fetches a ubuntu image and runs bash in interactive mode
4. ```docker run -it --entrypoint=bash python:3.9``` : opens bash in python, you can use pip here
5. You can supply arguments to your container like this - ```docker run -it test:<name_of_container> arg1 arg2```
6. You can access these arguments inside the conatiner code with ```import sys print(sys.argv) sys.argv[i]```
7. Install PGCLI with ```pip install pgcli```
10. Run ```winpty pgcli -h localhost -p 5432 -u root -d ny_taxi``` to connect to the postgres server on port 5432
11. Check `services.yml` for rest of the commands
12. `Dockerfile` has commands to build an image and run the `ingest_data.py` script and `Docker-Compose` has scripts to build the 2 containers (pgadmin, postgres) on a network
