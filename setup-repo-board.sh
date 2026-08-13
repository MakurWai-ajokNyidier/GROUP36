#!/bin/bash

# Quick Repo + Board Setup Script
# Usage: bash setup-repo-board.sh <project-name>
# Creates a public repo with populated README checklist board

if [ -z "$1" ]; then
  echo "Usage: bash setup-repo-board.sh <project-name>"
  exit 1
fi

PROJECT_NAME=$1
PROJECT_DIR="/home/claude/$PROJECT_NAME"

echo "🚀 Setting up repo + board: $PROJECT_NAME"

# Create and initialize repo
mkdir -p "$PROJECT_DIR"
cd "$PROJECT_DIR"
git init
git config user.email "you@example.com"
git config user.name "Your Name"

# Create README with checklist board
cat > README.md << 'EOF'
# Project Name

> A brief description of your project goes here.

## Project Board

### 🎯 Planning
- [ ] Define project scope
- [ ] Identify key features
- [ ] Set success metrics

### 🏗️ Setup
- [ ] Initialize repository ✅
- [ ] Create project structure
- [ ] Set up development environment

### 📝 Development
- [ ] Implement core features
- [ ] Add unit tests
- [ ] Document API/functions

### 🧪 Testing
- [ ] Write integration tests
- [ ] Test edge cases
- [ ] Performance testing

### 📦 Release
- [ ] Code review
- [ ] Update documentation
- [ ] Version bump & release

### 🚀 Deployment
- [ ] Deploy to staging
- [ ] Final testing
- [ ] Deploy to production

## Getting Started

```bash
# Clone the repository
git clone https://github.com/[YOUR-USERNAME]/$PROJECT_NAME.git
cd $PROJECT_NAME

# Get up and running
npm install  # or your package manager
npm start
```

## Project Structure

```
$PROJECT_NAME/
├── README.md
├── .gitignore
└── [your directories here]
```

## Contributing

Feel free to open issues and PRs!

## License

MIT
EOF

# Create .gitignore
cat > .gitignore << 'EOF'
# Dependencies
node_modules/
*.pyc
__pycache__/
*.egg-info/
dist/
build/

# Environment
.env
.env.local
.env.*.local

# IDE
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store

# Logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# OS
Thumbs.db
EOF

# Create initial commit
git add .
git commit -m "Initial commit: setup project board"

echo ""
echo "✅ Local setup complete!"
echo ""
echo "📁 Project location: $PROJECT_DIR"
echo ""
echo "📋 Next: Push to GitHub (public)"
echo ""
echo "  1. Create repo at: https://github.com/new"
echo "  2. Name: $PROJECT_NAME"
echo "  3. Make it PUBLIC"
echo "  4. Don't initialize with README"
echo ""
echo "  5. Run these commands:"
echo "     cd $PROJECT_DIR"
echo "     git branch -M main"
echo "     git remote add origin https://github.com/[YOUR-USERNAME]/$PROJECT_NAME.git"
echo "     git push -u origin main"
echo ""
echo "✨ Team members can now clone & see the board!"
