#!/bin/bash

echo "🚀 Deploying Hugo website to GitHub Pages..."

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "❌ Not a git repository. Please initialize git first."
    exit 1
fi

# Check for uncommitted changes
if [[ -n $(git status --porcelain) ]]; then
    echo "📝 You have uncommitted changes. Let's commit them first."
    echo "Current changes:"
    git status --short
    
    read -p "Do you want to commit all changes? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        read -p "Enter commit message: " commit_message
        git add .
        git commit -m "$commit_message"
    else
        echo "❌ Please commit your changes before deploying."
        exit 1
    fi
fi

# Check if remote origin exists
if ! git remote get-url origin > /dev/null 2>&1; then
    echo "❌ No remote origin found. Please add your GitHub repository:"
    echo "git remote add origin https://github.com/brmel/brmel.github.io.git"
    exit 1
fi

# Push to main branch (triggers GitHub Actions)
echo "⬆️  Pushing to GitHub..."
git push origin main

echo "✅ Code pushed to GitHub!"
echo "🔄 GitHub Actions will automatically:"
echo "   - Build your Hugo site"
echo "   - Deploy to GitHub Pages"
echo "   - Set up your custom domain"
echo ""
echo "📱 Monitor deployment at: https://github.com/brmel/brmel.github.io/actions"
echo "🌐 Your site will be available at:"
echo "   - GitHub Pages: https://brmel.github.io/"
echo "   - Custom Domain: https://ibraverse.ca (after DNS setup)"
echo ""
echo "⚠️  First-time setup requirements:"
echo "   1. Enable GitHub Pages in repository settings"
echo "   2. Configure DNS for ibraverse.ca domain"
echo "   3. Wait for SSL certificate provisioning"
