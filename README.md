# Full-Stack Project — Git Branching Workflow

This repository demonstrates a structured Git branching and collaboration workflow for a full-stack web application (Python Flask backend + HTML/JS frontend).

## Branching Strategy (Git Flow)
- **`main`**: Production-ready branch. Only receives tested, reviewed merges from `develop`.
- **`develop`**: Integration branch where completed features are combined and tested before release.
- **`feature/<feature-name>`**: Short-lived branches created from `develop` for individual features (e.g., `feature/task-api`).

## Collaboration Workflow
1. Create a new branch from `develop` using the naming convention `feature/<name>`.
2. Commit changes with clear, descriptive commit messages.
3. Open a **Pull Request (PR)** targeting `develop` using the repository PR template.
4. Review changes and merge into `develop`, then release to `main`.
