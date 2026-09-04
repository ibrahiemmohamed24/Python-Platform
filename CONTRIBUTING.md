# Contributing to Python-Platform

Welcome! This guide explains how our team collaborates on this open-source project.

---

## Quick Overview / نظرة سريعة

**EN:** We use GitHub Issues to track tasks. Every change goes through a Pull Request. The `main` branch is protected — no direct pushes allowed.

**AR:** نستخدم GitHub Issues لتتبع المهام. أي تعديل لازم يمر بـ Pull Request. فرع `main` محمي — ممنوع أي push مباشر عليه.

---

## Setup / التجهيز

```bash
git clone https://github.com/ibrahiemmohamed24/Python-Platform.git
cd Python-Platform
python -m venv .venv
source .venv/bin/activate      # Linux/Mac
# .venv\Scripts\activate       # Windows
pip install -e ".[dev]"
```

---

## Workflow / سير العمل

### 1. Pick a task / اختر مهمة
- Check the Team Dashboard (link shared privately) for your assigned task
- Or browse open Issues here on GitHub

### 2. Create a branch / اعمل فرع جديد
```bash
git checkout main
git pull origin main
git checkout -b feature/task-XXX-short-description
```

**Branch naming / تسمية الفروع:**
- `feature/task-042-add-linter` — for new features
- `fix/task-055-error-handling` — for bug fixes
- `docs/task-060-update-readme` — for docs
- `test/task-070-analyzer-tests` — for tests

### 3. Make your changes / نفّذ التعديلات

**Commit messages / رسائل الـ commits:**
- Use clear English messages
- Start with a verb: Add, Fix, Update, Remove, Refactor
- Reference the task number when applicable

Good examples:

Add JSON output support to Bandit analyzer (TASK-042)
Fix crash when input file is empty (TASK-055)

Bad examples:

update stuff
fix
work in progress


### 4. Push and open a Pull Request / ارفع وافتح PR
```bash
git push origin feature/task-XXX-short-description
```

Then go to GitHub and open a Pull Request:
- **Title:** Clear summary
- **Description:** What you did, why, and any notes for reviewers
- **Link the issue:** Write "Closes #42" to auto-close the issue when merged

### 5. Wait for review / استنى المراجعة
- At least 1 approval required before merge
- Address feedback constructively
- Push new commits to the same branch — the PR updates automatically

### 6. After merge / بعد الـ merge
```bash
git checkout main
git pull origin main
git branch -d feature/task-XXX-short-description
```

---

## Code Standards / معايير الكود

- **Follow PEP 8** for Python code style
- **Add tests** for new features when possible
- **Type hints** are encouraged (`mypy` is configured)
- **Docstrings** for public functions and classes

Run before pushing:
```bash
ruff check .          # linter
mypy app              # type checker
pytest                # tests
```

---

## Communication / التواصل

- **Technical discussions:** Comment on the relevant Issue or PR
- **Questions:** Open a Discussion or ask in the team group
- **Bugs found in production:** Open an Issue with `bug` label

---

## What NOT to do / ممنوع

- Push directly to `main` (blocked anyway)
- Force push to shared branches
- Delete other people's branches
- Commit secrets, API keys, or `.env` files
- Merge your own PR without review

---

## Need Help? / محتاج مساعدة؟

Open a Discussion, ask in the team group, or tag the maintainer in your PR.

**Thanks for contributing! / شكرًا لمساهمتك!**
