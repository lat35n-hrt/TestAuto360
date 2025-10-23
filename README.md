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
Each push to the main branch triggers GitHub Actions.
The CI pipeline runs both pytest and mypy to ensure automated testing and static analysis.
The badge above updates to 🟢 Passing when all checks succeed.

🧪 Test Overview
| File                 | Purpose                                                        |
| -------------------- | -------------------------------------------------------------- |
| `test_api_client.py` | Validates API response structure and expected fields           |
| `test_smoke.py`      | Minimal smoke test using `monkeypatch` (no external API calls) |


🧠 Static Type Checking (mypy)

This project includes mypy in the CI pipeline.
A relaxed configuration is used for rapid prototyping.
Full type coverage is not enforced, but the setup reflects awareness of maintainability and static analysis practice

✅ Verification Summary

| Category           | Status          | Description                   |
| ------------------ | --------------- | ----------------------------- |
| **Pytest**         | 🟢 Passed (4/4) | All tests succeeded           |
| **mypy**           | 🟢 Success      | No type issues found          |
| **GitHub Actions** | 🟢 Passing      | CI pipeline verified          |
| **External API**   | 🔸 Mocked       | Safe and repeatable execution |


📈 Next Steps

- Add schema validation with pydantic

- Integrate pytest-cov + Codecov for test coverage

- Manage API keys securely with GitHub Secrets

