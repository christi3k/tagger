# Taggercore
[![codecov](https://codecov.io/gh/IT-EXPERTS-AT/tagger/branch/master/graph/badge.svg?flag=taggercore)](https://codecov.io/gh/IT-EXPERTS-AT/tagger) ![build](https://github.com/IT-EXPERTS-AT/tagger/workflows/Core-build/badge.svg)
## About
Taggercore contains utility classes for scanning AWS resources and applying tags to them.
The `usecase` package contains opinionated functions for performing tasks like scanning a region and global resources (e.g. IAM) or comparing resources to a certain tagging schema (e.g. `create_report.py`).
## Python version
Taggercore requires Python version 3.8 or higher
## Supported resources
Resources supported (scanning + tagging)

|Resource|Notes|
|---|---|
|	acm.certificate	|		|
|	apigateway.apis	|		|
|	apigateway.restapis	|		|
|	cloudfront.distribution	|		|
|	cloudtrail.trail	|global trails are currently not supported|
|	cloudwatch.alarm	|		|
|	dynamodb.table	|
|	ec2.address	|		|
|	ec2.customer-gateway	|		|
|	ec2.flow-log	|
|	ec2.image	|		|
|	ec2.instance	| self owned only
|	ec2.internetgateway	|		|
|	ec2.keypairs	|		|
|	ec2.launch-template	|		|
|	ec2.natgateway	|		|
|	ec2.networkacl	|		|
|	ec2.route-table	|		|
|	ec2.securitygroup	|		|
|	ec2.snapshot	|		|
|	ec2.subnet	|		|
|	ec2.volume	|		|
|	ec2.vpc	|		|
|	ec2.vpc-peering-connection	|
|	elasticache.cluster	|		|
|	elasticache.snapshot	|		|
|	elasticbeanstalk.application	|		|
|	elasticloadbalacing.loadbalancer	|	v1(classic) and v2(application,network)	|
|	es.domain	|
|	firehose.deliverystream	|		|
|	iam.role	|		|
|	iam.user	|		|
|	kinesis.stream	|	data streams	|
|	lambda.function	|
|	logs.log-group	|		|
|	rds.cluster	|
|	rds.db	|
|	rds.secgrp	|		|
|	route53.healthcheck	|
|	route53.hostedzone	|  
|	sns.topic	|		|
|	s3.bucket	|
|	sqs.queue	|
## Installation

**Latest commit**

`pip install 'git+https://github.com/IT-EXPERTS-AT/tagger.git#egg=taggercore&subdirectory=taggercore'`

**Certain release**  
E.g. v1.0.0  
`pip install 'git+https://github.com/IT-EXPERTS-AT/tagger.git@v1.0.0#egg=taggercore&subdirectory=taggercore'`  

We are working on a PyPi release!
## Development

Install dev dependencies:  
`pipenv install -e .[dev]`  

Run tests:  
`tox`

Test fixtures are currently defined in `conftest.py`

Run black for code formatting:  
`tox -e format`
