QA Automation
├── API testing
├── Playwright UI testing
├── Smoke tests
└── Regression tests

Infrastructure
├── Docker
└── GitHub Actions

CI flow
Git push
   ↓
Build Docker image
   ↓
Smoke tests
   ↓
Regression tests
   ↓
Artifacts
   ↓
PASS / FAIL
