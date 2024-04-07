# Setting up Docker Container for Oriun

In this guide, we'll walk through the steps to set up a Docker container for Oriun using the provided commands.

## Prerequisites

Before proceeding, ensure that you have Docker installed on your system. You can download and install Docker from the 
[official Docker website](https://www.docker.com/get-started).

## Step 1: Clone Oriun Repository

First, clone the Oriun repository from its source:

```bash
git clone https://github.com/JavierTarazona06/ORIUN_back
cd oriun
```

## Step 2: Build Docker Image

Navigate to the root directory of the Oriun project and build the Docker image using the following command:

```bash
sudo docker build -t oriun .
```

This command builds a Docker image named oriun using the Dockerfile located in the current directory.

## Step 3: Run Docker Container

Remember to have your .env file with the environment variables for the project.

Once the Docker image is built successfully, you can run a Docker container using the following command if
you will use your local PostgresSQL server and you are in a Linux machine:

```bash
sudo docker run -d -p 8080:8080 --env-file=.env --name oriun-container --network=host oriun
```

If you are in another OS and wants to use you local database, run the next code, and use 
`DATABASE_HOST=host.docker.internal` instead `DATABASE_HOST=localhost`

```bash
sudo docker run -d -p 8080:8080 --env-file=.env --name oriun-container oriun
```

If you want to use the database in the server, use this code:

```bash
sudo docker run -d -p 8080:8080 --env-file=.env --name oriun-container oriun
```

This command creates and starts a Docker container named oriun-container based on the oriun image. It maps port 8080 of
the host machine to port 8080 of the container. Additionally, it reads environment variables from the .env file.


## Conclusion

You've successfully set up a Docker container for Oriun using the provided commands. You can now access Oriun 
application at http://localhost:8080 in your web browser.