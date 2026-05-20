# 🚀 End-to-End CI/CD Pipeline for Python Flask Application

## 📌 Project Overview

This project demonstrates a complete **CI/CD (Continuous Integration and Continuous Deployment) pipeline** for a Python Flask application using:

- Python Flask
- Git & GitHub
- GitHub Actions
- Docker
- Render Cloud Platform
- pytest for automated testing

The application is automatically tested and deployed whenever code is pushed to the `main` branch.

---

# 🧠 Project Architecture

```text
                +-------------------+
                |   Developer Code  |
                +-------------------+
                          |
                          v
                +-------------------+
                |   GitHub Repo     |
                +-------------------+
                          |
                          v
                +-------------------+
                | GitHub Actions CI |
                +-------------------+
                          |
        +-----------------+-----------------+
        |                                   |
        v                                   v
+-------------------+          +------------------------+
| Install Packages  |          | Run pytest Test Cases  |
+-------------------+          +------------------------+
                          |
                          v
                +-------------------+
                | Docker Build      |
                +-------------------+
                          |
                          v
                +-------------------+
                | Render Deployment |
                +-------------------+
                          |
                          v
                +-------------------+
                | Live Flask App    |
                +-------------------+
```

---

# 🎯 Features

✅ Flask REST API  
✅ Automated testing using pytest  
✅ Docker containerization  
✅ GitHub Actions CI/CD pipeline  
✅ Continuous Deployment using Render  
✅ Automatic deployment on every push to main branch  

---

# 💰 Cost

| Service | Cost |
|---|---|
| GitHub | Free |
| GitHub Actions | Free |
| Docker Desktop | Free |
| Render | Free Tier |

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend language |
| Flask | Web framework |
| pytest | Automated testing |
| GitHub | Version control |
| GitHub Actions | CI/CD pipeline |
| Docker | Containerization |
| Render | Cloud deployment |

---

# 📂 Project Structure

```text
ecommerce-devops/
│
├── app.py
├── requirements.txt
├── test_app.py
├── Dockerfile
├── .gitignore
├── README.md
└── .github/
    └── workflows/
        └── deploy.yml
```

---

# ⚙️ Prerequisites

Install the following software before starting:

- Python 3.10+
- Git
- Docker Desktop
- VS Code

---

# 🟢 Step 1 — Clone Repository

```bash
git clone https://github.com/Hanisha-Bogadhi/CI-CD-Pipeline-Python-Flask-App.git
cd ecommerce-devops
```

---

# 🟢 Step 2 — Create Virtual Environment

## Windows

```cmd
python -m venv venv
venv\Scripts\activate
```

---

# 🟢 Step 3 — Install Dependencies

```cmd
pip install -r requirements.txt
```

---

# 🟢 Step 4 — Run Flask Application

```cmd
python app.py
```

Application runs on:

```text
http://localhost:5000
```
---

# 📌 API Endpoints

## Home Route

```text
GET /
```

### Response

```text
E-Commerce DevOps App Running 🚀
```
---

## Products Route

```text
GET /products
```

### Response

```json
[
  {
    "id": 1,
    "name": "Shirt",
    "price": 500
  },
  {
    "id": 2,
    "name": "Shoes",
    "price": 1200
  }
]
```
---

# 🧪 Running Automated Tests

This project uses `pytest` for automated testing.

Run tests locally:

```cmd
pytest
```

Expected output:

```text
1 passed
```

---

# 🐳 Docker Setup

## Build Docker Image

```cmd
docker build -t ecommerce-devops .
```

---

## Run Docker Container

```cmd
docker run -d -p 5000:5000 ecommerce-devops
```

---

## Verify Running Container

```cmd
docker ps
```

---
# 🟢 Step 5 — Push code to GitHub
```cmd
git add .
git commit -m "Initial commit"
git push -u origin main
```

# 🔄 GitHub Actions CI/CD Pipeline

The project uses GitHub Actions to automate:

- Code checkout
- Dependency installation
- Automated testing
- Deployment workflow

Workflow file location:

```text
.github/workflows/deploy.yml
```

---

# 📄 GitHub Actions Workflow

```yaml
name: CI Pipeline

on:
  push:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Code
      uses: actions/checkout@v3

    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: "3.10"

    - name: Install Dependencies
      run: |
        pip install -r requirements.txt

    - name: Run Tests
      run: |
        pytest
```

---

# ☁️ Render Deployment

The Flask application is deployed using Render.

---

# 🚀 Deployment Steps

1. Create Render account
2. Connect GitHub repository
3. Configure:
   - Build Command:
     ```text
     pip install -r requirements.txt
     ```
   - Start Command:
     ```text
     python app.py
     ```

---

# ⚠️ Important Configuration for Render

Update `app.py`:

```python
import os

port = int(os.environ.get("PORT", 5000))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
```

---

# 🌐 Live Application

## Home Route

```text
https://ecommerce-devops-si00.onrender.com
```
---

## Products Route

```text
https://ecommerce-devops-si00.onrender.com/products
```
---

# 🔥 CI/CD Workflow Demonstration

To verify Continuous Deployment:
1. Modify application text in `app.py`
```text
return "Version 2 Deployed 🚀"
```

2. Push code to GitHub

```cmd
git add .
git commit -m "Updated application"
git push
```

3. GitHub Actions automatically runs tests
4. Render automatically redeploys updated application

![Final CI/CD proof](screenshots\complete-cicd-proof.png)
---

# 📸 Screenshots

| Screenshot | Description |
|---|---|
| docker-container-running.png | docker desktop |
| docker-container-running-terminal.png | docker build,run in terminal |
| flask-app-running.png | Local Flask app |
| pytest-success.png | Automated test success |
| docker-build-success.png | Docker image build |
| github-repo-page.png | GitHub repo files |
| github-actions-success.png | GitHub Actions green tick |
| render-live-app.png | Live deployed app |
| render-live-app-before-update.png | live app before update |
| render-live-app-products.png | live deployed app /products |
| github-repo-page-after-update.png | GitHub repo files after update|
| complete-cicd-proof.png | Final CI/CD proof |

---

# 🧠 Key Learning Outcomes

This project demonstrates:

- CI/CD pipeline implementation
- Automated testing
- Docker containerization
- Cloud deployment
- GitHub Actions workflow automation
- Continuous Deployment practices

---


# 🚀 Future Improvements

Possible upgrades:

- Jenkins integration
- AWS EC2 deployment
- Nginx reverse proxy
- Blue-Green deployment
- Terraform Infrastructure as Code
- Kubernetes deployment

---

# 👨‍💻 Author

Hanisha Bogadhi