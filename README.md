# Kuro Password Manager

[![PWD](https://raw.githubusercontent.com/play-with-docker/stacks/master/assets/images/button.png)](https://labs.play-with-docker.com/?stack=https://raw.githubusercontent.com/kuro-vale/kuro-passwords/main/docker-compose.yml)

A password manager made with Flask, Bootstrap, Jinja2

## Screenshots

### Home

![Screenshot_20230104_152419](https://user-images.githubusercontent.com/87244716/210643346-e9cf1fdc-56a3-4e64-ab87-48e6e27a9541.png)

### Login Logs

![Screenshot_20230104_152504](https://user-images.githubusercontent.com/87244716/210643449-5673b7eb-53d3-4031-96f2-b0a0876ccb81.png)


#### Login

![Screenshot_20230104_152216](https://user-images.githubusercontent.com/87244716/210642991-aa188262-014b-4efd-a28b-3065f26ded0e.png)


## Deploy

Follow any of these methods and open http://localhost:5000/ to see the App.

## Docker

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
