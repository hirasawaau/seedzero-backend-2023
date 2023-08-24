# Seedzero Backend 2023

## Prerequisites

- [Python >= 3.7](https://www.python.org/downloads/)
  - (Optional) [miniconda](https://docs.conda.io/en/latest/miniconda.html)
- Docker
  - [Docker Desktop for Windows/Mac/Linux](https://www.docker.com/products/docker-desktop)
  - [Docker Engine for Linux](https://docs.docker.com/engine/install/)
- MongoDB (Mostly recommended to use Docker)
  - [MongoDB Docker Image](https://hub.docker.com/_/mongo)
  - [MongoDB Community Server](https://www.mongodb.com/docs/manual/administration/install-community/)

## Try FastAPI

### Install dependencies

#### macOS/Linux

```bash
$ pip install "fastapi[all]"
```

#### Windows

```powershell
python3 -m pip install "fastapi[all]"
```

### Coding API that response "Hello World"

#### main.py

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/") # Say that the method is GET method and the path is "/" (root path)
def hello_world():
  return "Hello World"
```

### Run FastAPI

#### macOS/Linux

```bash
$ uvicorn main:app --reload
```

#### Windows

```powershell
python3 -m uvicorn main:app --reload
```

![Alt text](img/image.png)

<p align="center"><i>Example output of uvicorn when start complete</i></p>

If you see the output like this, you can access to [http://localhost:8000/](http://localhost:8000) to see the result.
