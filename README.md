# GROUP36
- [x] Repo initialized locally
- [x] README with 6-phase board included
- [x] .gitignore pre-configured
- [x] Initial commit ready
- [ ] Create public repo on GitHub
- [ ] Push to GitHub
- [ ] Share with team

      # Repo + Board Setup Guide

Quick setup for creating public GitHub repos with populated README checklist boards.

**Defaults:**
- ✅ Repository is **PUBLIC**
- ✅ README is **pre-populated** with 6-phase checklist board
- ✅ Board is **accessible to all team members**

---

## Option 1: Automated Script (Fastest)

```bash
bash setup-repo-board.sh my-project
```

**What it does:**
1. Creates `/home/claude/my-project`
2. Initializes git repo
3. Populates README with checklist board
4. Creates .gitignore
5. Makes initial commit
6. Shows you the next steps

---

## Option 2: Manual Steps

### Step 1: Local Setup
```bash
mkdir my-project && cd my-project
git init
git config user.email "you@example.com"
git config user.name "Your Name"
```

### Step 2: Add Files
Copy the README.md and .gitignore templates from the script above (or create them manually).

### Step 3: Initial Commit
```bash
git add .
git commit -m "Initial commit: setup project board"
```

### Step 4: Push to GitHub

1. **Create repo on GitHub:** https://github.com/new
   - Name: `my-project`
   - **Visibility: PUBLIC** ← Important
   - Don't initialize with README
   - Click Create

2. **Connect & push:**
   ```bash
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/my-project.git
   git push -u origin main
   ```

3. ✅ Done! Board is live and accessible to all team members

---

## README Board Structure

Default 6 phases included:

1. **🎯 Planning** - Scope, features, metrics
2. **🏗️ Setup** - Repo, structure, environment
3. **📝 Development** - Core features, tests, docs
4. **🧪 Testing** - Integration, edge cases, performance
5. **📦 Release** - Review, docs, versioning
6. **🚀 Deployment** - Staging, final testing, production

Customize by editing README.md directly on GitHub or locally.

---

## Update Board Progress

### Option A: Edit on GitHub
1. Open README.md on GitHub
2. Click the pencil icon (Edit)
3. Change `- [ ]` to `- [x]` for completed items
4. Commit changes

### Option B: Edit Locally
```bash
cd my-project
# Edit README.md
git add README.md
git commit -m "Update board: completed setup phase"
git push
```

---

## Team Access

Once pushed to a **PUBLIC** repo:
- ✅ Anyone can view the board (no login required)
- ✅ Team members can clone: `git clone https://github.com/YOUR-USERNAME/my-project.git`
- ✅ Collaborators can push changes (if added via Settings → Collaborators)
- ✅ Others can see progress in README checklist

---

## Quick Reference

| Task | Command |
|------|---------|
| Create new project | `bash setup-repo-board.sh project-name` |
| Clone existing | `git clone https://github.com/user/project.git` |
| Update board locally | Edit README.md → `git add . → git commit → git push` |
| Add collaborators | GitHub Settings → Collaborators → Add users |
| Change to private | GitHub Settings → Visibility |

---

## What's Included in Template

```
my-project/
├── README.md          (6-phase checklist board)
├── .gitignore         (Node, Python, IDE, OS exclusions)
└── .git/              (Git history)
```

---

## Tips

- 📌 Pin the repo to your GitHub profile for easy access
- 🔗 Share the GitHub link with your team
- 💬 Use GitHub Issues for detailed task tracking
- 🔀 Create branches for features: `git checkout -b feature/your-feature`
- 📊 Add GitHub Projects for kanban-style board (if needed)

Enjoy! 🚀
