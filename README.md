# sns-http-endpoint

This is a simple sns http endpoint.
It will answer to subscribe messages, and also prints received events from sns

## Install requirements
```shell
$ pip install -r requirements.txt
```

## Run Flask Server
```shell
$ export FLASK_APP=sns-endpoint.py
$ flask run --host=0.0.0.0
```

## Notes for AWS
- Create an ACM Certificate
- Create an Internet Facing ALB and use the previously created certificate
- Create a Listner for port 443
- Create a target group for the instance you have the Flask Server running, and set port 5000
- On the R53 Create an A record, ALIAS, and point it to the ALB
- On the SNS topoic create an https susbcription to the A record you have created
