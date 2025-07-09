# Deploy Hugo Website to brmel.github.io

This guide will help you deploy your Hugo website to your `brmel.github.io` repository with your custom domain `ibraverse.ca`.

## 🏗️ Architecture Overview

- **Source Repository:** `brmel/ibraverse_web` (private) - your Hugo source code
- **Deployment Repository:** `brmel/brmel.github.io` (public) - hosts the built website
- **Custom Domain:** `ibraverse.ca` - your professional domain
- **Backup Repository:** `brmel/ibraverse` (private) - for version control

## � Setup Steps

### 1. GitHub Personal Access Token

You need a Personal Access Token to allow the workflow to push to your `brmel.github.io` repository:

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Select scopes: `repo` (full control of private repositories)
4. Copy the token
5. In your `ibraverse_web` repository:
   - Go to Settings → Secrets and variables → Actions
   - Click "New repository secret"
   - Name: `PERSONAL_ACCESS_TOKEN`
   - Value: paste your token

### 2. Deploy Your Website

```bash
# Make sure you're in the Hugo project directory
cd /Users/brahim/Projects/Ibraverse/ibraverse_web

# Add the new workflow file
git add .github/workflows/deploy.yml

# Commit and push to trigger deployment
git add .
git commit -m "Setup deployment to brmel.github.io"
git push origin master
```

### 3. Configure Custom Domain

#### A. DNS Settings (at your domain registrar)

Configure these DNS records for `ibraverse.ca`:

**For Apex Domain:**
```
Type: A
Name: @
Value: 185.199.108.153

Type: A
Name: @
Value: 185.199.109.153

Type: A
Name: @
Value: 185.199.110.153

Type: A
Name: @
Value: 185.199.111.153
```

**For WWW Subdomain:**
```
Type: CNAME
Name: www
Value: brmel.github.io
```

#### B. GitHub Pages Settings

1. Go to https://github.com/brmel/brmel.github.io/settings/pages
2. Ensure Source is set to "Deploy from a branch"
3. Branch should be "main"
4. The workflow will automatically create a CNAME file

### 4. Repository Structure

```
Your Setup:
├── brmel/ibraverse (private)          # Backup/version control
├── brmel/ibraverse_web (private)      # Hugo source code + GitHub Actions
└── brmel/brmel.github.io (public)     # Deployed website
```

## 🚀 Deployment Process

1. **Edit your Hugo content** in `ibraverse_web`
2. **Commit and push** to the `master` branch
3. **GitHub Actions automatically:**
   - Builds your Hugo site
   - Deploys to `brmel.github.io`
   - Sets up the CNAME file for your custom domain

## 🌐 Your Website URLs

- **GitHub Pages:** https://brmel.github.io/
- **Custom Domain:** https://ibraverse.ca (after DNS setup)

## 📋 Quick Commands

```bash
# Deploy changes
git add .
git commit -m "Update content"
git push origin master

# Check deployment status
# Visit: https://github.com/brmel/ibraverse_web/actions

# Local development
hugo server -D
```

## 🔍 Troubleshooting

### Build Failures
- Check: https://github.com/brmel/ibraverse_web/actions
- Common issues: missing Personal Access Token, Hugo version conflicts

### DNS Issues
- DNS propagation takes 24-48 hours
- Test with: https://dnschecker.org

### Custom Domain Not Working
- Verify CNAME file exists in `brmel.github.io`
- Check GitHub Pages settings
- Ensure DNS records are correct

## � Security Notes

- Keep your source repository (`ibraverse_web`) private
- The `brmel.github.io` repository must be public for GitHub Pages
- Personal Access Token should have minimal required permissions

## 📞 Support

If you encounter issues:
1. Check GitHub Actions logs
2. Verify Personal Access Token permissions
3. Ensure DNS settings are correct
4. Test the site at the GitHub Pages URL first
