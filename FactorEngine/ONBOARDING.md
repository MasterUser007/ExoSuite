# FactorEngine Contributor & Deployment Onboarding Guide

## 🚀 For Developers

1. Clone the repository
2. Create a Python virtual environment
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run the pipeline:
```bash
python main.py
```

## 🧪 Run Tests
```bash
pytest tests/
```

## 🔁 Build, Validate, Release
```bash
bash deployment/validate_pipeline.sh
bash deployment/build_package.sh
bash deployment/release.sh
```

## 📘 View Docs
```bash
mkdocs serve
```

## ☁️ Deploy to AWS (Terraform)
1. Edit your SSH key in `main.tf`
2. Run:
```bash
terraform init
terraform apply
```

## 📊 Monitoring Setup
```bash
docker-compose -f deployment/docker-compose.monitoring.yml up
```

Grafana: http://localhost:3000  
Prometheus: http://localhost:9090  
Login: `admin / primeai`

---
