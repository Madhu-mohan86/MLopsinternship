
# Chat with PDF Application

This repository contains the source code for Pdf chat application with showcasing of containerization and production deployment. Follow the steps below to get started.

## Installation

Clone the repo

    

## Run Locally

Clone the project

```bash
  git clone https://github.com/Madhu-mohan86/MLopsinternship.git
```

Go to the project directory

```bash
  cd MLopsinternship
```

Build docker images with altering the Open API key

```bash
  docker build -t docker_image:latest .
```

Deploy to kubernetes

```bash
  kubectl create -f Containers.yaml && kubectl create -f Service.yaml

```

