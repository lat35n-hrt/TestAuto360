# 🧪 TestAuto360 — API Test Automation PoC
![CI](https://github.com/lat35n-hrt/TestAuto360/actions/workflows/ci.yml/badge.svg)



This repository demonstrates automated API testing using **pytest** and **GitHub Actions**.

## 🎯 Features
- Automated test execution on every push (CI)
- API response validation
- Basic mocking with `pytest.monkeypatch`
- CI badge ready for portfolios and interviews

## 🏗️ Tech Stack
- Python 3.10.11
- pytest 8.4.2
- requests 2.32.5
- mypy 1.18.2
- types-requests 2.32.4.20250913
- GitHub Actions

## 🚀 Run Locally
```bash
python3 -m venv .venv
source .venv/bin/activate   # Windowsは .venv\Scripts\activate
pip install -r requirements.txt
pytest -v
mypy src/
```


## Continuous Integration (CI)
The CI pipeline now runs both pytest and mypy,
ensuring that unit tests and static analysis are automatically verified on every push.