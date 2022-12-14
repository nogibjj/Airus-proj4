install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test/test_*.py

build:
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 954946645007.dkr.ecr.us-east-1.amazonaws.com

	docker build -t fastapi .

	docker tag fastapi:latest 954946645007.dkr.ecr.us-east-1.amazonaws.com/fastapi:latest

	docker push 954946645007.dkr.ecr.us-east-1.amazonaws.com/fastapi:latest
