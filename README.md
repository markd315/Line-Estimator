# line estimator
![Example](https://raw.githubusercontent.com/markd315/Line-Estimator/main/demo.gif)

### How to run the webapp server
```commandline
anvil-app-server --app LineEstimatorApp
```

There is even a cool webapp which can run in a docker container. Be sure to change the origin setting in the Dockerfile if you host it somewhere else.

# Local docker commands to build image
```commandline
docker build -f Dockerfile.dev -t 720291373173.dkr.ecr.us-east-1.amazonaws.com/financial-shit-dev:latest .
docker push 720291373173.dkr.ecr.us-east-1.amazonaws.com/financial-shit-dev:latest

docker build -t 720291373173.dkr.ecr.us-east-1.amazonaws.com/financial-shit:latest .
docker push 720291373173.dkr.ecr.us-east-1.amazonaws.com/financial-shit:latest
```

I mostly made this with ChatGPT, wanted to experiment with using it some in a workflow. I would say it saved me time but wasn't thorough or entirely correct all the time.