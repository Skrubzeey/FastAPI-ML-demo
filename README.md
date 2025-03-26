# FastAPI-ML-demo
This is a demo for how you can connect a simple FastAPI app with your own ML model using Docker

## How to Run the app:
### 📟Local boot
For using the app locally you do not have to download Docker. After cloning this repository go to it's folder in your IDE using 
`cd your-directory` in the shell. Next, use `pip install -r requirements.txt` in order to download all dependencies for the project and run `uvicorn app:app --host 0.0.0.0 --port 8000 --reload` to start the server. Open your browser and enter `http://127.0.0.1:8000/` or `http://127.0.0.1:8000/docs` to use the SwaggerUI Docs for FastAPI app.  


### 🐳Dockerfile boot
Enter your terminal in your IDE or open bash in your projects folder and use `docker build -t fastapi-ml-app .` to build the image. In order to run the docker container use `docker run -p 8000:8000 fastapi-ml-app`.

### 🐳Docker compose boot
For running the app with docker-compose file use `docker-compose up --build` to build and run the app immediately.

## 📊Custom environmental variables setup:
If you want to setup your env variables for the other service like Redis, use either `docker-compose.override.yml` or enter your bash terminal and use 
`export REDIS_HOST=localhost` and `export REDIS_PORT=6379`.

## 🌐API request endpoints
*  `/predict` - POST request, uses the ML model to predict a class of a wine from `load_wine()` dataset from scikit-learn.
*  `/info` - GET request, returns the information about the model, dataset and number of features in the dataset.
*  `/health` - GET request, returns the status of the app.
*  `/redis_check` - GET request, returns the status of the db.

## 📁System requirements
* RAM: min. 512 MB (recommended 1 GB)

* CPU: min. 1 vCPU

* Drive: 100 MB for the app, a bit more for the ML model

