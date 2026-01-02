# How to Push to GitHub - Simple Guide

## Using GitHub Desktop (EASIEST METHOD)

1. **Download GitHub Desktop**
   - Go to: https://desktop.github.com/
   - Download and install

2. **Sign in to GitHub**
   - Open GitHub Desktop
   - Sign in with your GitHub account (the one that owns tekzomoloi7-lang)

3. **Add the Repository**
   - In GitHub Desktop: File → Add Local Repository
   - Click "Choose..." and select the "CAPS TYCOON GAME" folder
   - Click "Add Repository"

4. **Push to GitHub**
   - You should see all your commits listed
   - Click "Publish repository" (if first time) or "Push origin" button
   - Repository will be pushed to: https://github.com/tekzomoloi7-lang/CAPS-TYCOON.git

## Using Command Line with Personal Access Token

1. **Create Token**
   - Go to: https://github.com/settings/tokens
   - Click "Generate new token" → "Generate new token (classic)"
   - Name: "CAPS-TYCOON"
   - Select scope: ✅ **repo** (Full control of private repositories)
   - Click "Generate token"
   - **COPY THE TOKEN** (you won't see it again!)

2. **Push with Token**
   Open PowerShell in the project folder and run:
   ```powershell
   git push -u origin main
   ```
   
   When prompted:
   - Username: `tekzomoloi7-lang` (or your GitHub username)
   - Password: **Paste the Personal Access Token** (NOT your GitHub password)

## Verify the Push

After pushing, check:
- https://github.com/tekzomoloi7-lang/CAPS-TYCOON
- You should see all your files there!








