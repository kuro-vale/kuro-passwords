# Kuro Password Manager

A password manager made with Flask, Bootstrap, Jinja2

### Docker image

Run the [docker image](https://hub.docker.com/r/kurovale/kuro-passwords) of this project

## Prerequisites
**Making venv**

Make a virtual environment by running:

```py -m venv venv```

To activate run:

In windows: 
```.\venv\Scripts\activate```

In Linux: 
```source venv/bin/activate```

**Installing dependencies**

Install all dependencies that are required for the project by running:

```pip install -r requirements.txt```
## Setting Firestore

The app store the data in Firestore you need to install [gcloud SDK](https://cloud.google.com/sdk/docs/quickstart)
Then run:
```bash
gcloud init
```
Change line 7 in firestore_service.py with the name of your project

```firebase_admin.initialize_app(credential, {"projectId": "YourProjectName"})```

## Running flask server

You can add the variable ```FLASK_APP="main.py"``` and run:
```bash
flask run
```
or just run:
```bash
cd flask-password-manager
python3 main.py
```
