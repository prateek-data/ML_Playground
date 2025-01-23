## Learning Notes

### How to load env variables into system from .env file
> source .env doed not work
> Use python-dotenv package 


### How to remove an env variable
> unset <env_var_name>

### How to use argparse
> refer run_inference.py

### Log in to Docker
> docker login 

### Build docker image
> docker build -t ml-model .

### Get logs while building image
> docker build --progress=plain -t ml_flow:v1 .

### Delete existing failed docker container
> docker container rm <container_name>

### Run docker container
> docker run --name ml_flow ml_flow:v1

### Run docker container in daemon mode: keeps running in background
> docker run -t -d --name ml_flow ml_flow:v1

### Diagnose from inside docker container
> docker exec -it ml_flow sh

### Proper way to generate pylintrc file
> pylint --generate-rcfile | out-file -encoding utf8 .pylintrc