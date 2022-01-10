Here are the steps that I took to add the Gunicorn WSGI server and then build the container image for deployment to Azure Web App for Containers.  I leaned heavily on [this excellent blog post ](https://medium.com/cloudskills/build-run-and-continuously-deploy-docker-containers-on-azure-app-service-83974329e9d6) for the deployment steps.

1. Create requirements.txt from Pipfile. (I used PIPENV for development, but there was a lot more documentation about using PIP for deployment so that's the road that I took.)
    * pipenv lock -r > requirements.txt
1. Create and activate virtual environment
    *	python3 -m venv .venv (first time)
	* source .venv/bin/activate
1. Install requirements
	* pip install -r requirements.txt
1. Test
	* flask run (check FLASK_APP environment variable if fails)
	* http://localhost:5000/
1. Add Gunicorn (no NGINX web server needed because the web server is provided by Azure)
	* deactivate virtual environment
	* pip install gunicorn
	* Activate virtual environment 
	* gunicorn -w 4 pandulce:app (for test on local workstation)
	* gunicorn -b :5000 - pandulce:app (on production)
1. Authenticate to ACR.
	* docker login <YOUR REGISTRY NAME>.azurecr.io
1. Build container image
	* docker build --no-cache -t pandulce:latest . (for local test)
    * docker build -t <YOUR REGISTRY NAME>.azurecr.io/pandulce:latest . (for push to Azure docker images)
    * docker run --name pandulce -d -p 8000:5000 --rm pandulce:latest (for local test)
    * docker ps -a
1. Push the image to the Azure Container Registry
    * docker push <YOUR REGISTRY NAME>.azurecr.io/pandulce:latest
