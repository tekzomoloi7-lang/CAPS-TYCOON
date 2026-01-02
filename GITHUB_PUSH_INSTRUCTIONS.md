# GitHub Push Instructions - Authentication Required

## Current Issue

Git is trying to push using "Gurustem" credentials, but the repository belongs to "tekzomoloi7-lang". You need to authenticate with the correct account.

## ✅ Changes Already Committed

Your changes have been successfully committed locally. You just need to push them to GitHub.

## 🔐 Authentication Options

### Option 1: GitHub Personal Access Token (Recommended)

1. **Create a Personal Access Token:**
   - Go to: https://github.com/settings/tokens
   - Click "Generate new token" → "Generate new token (classic)"
   - Name it: "CAPS-TYCOON-Push"
   - Select scopes: `repo` (full control of private repositories)
   - Click "Generate token"
   - **Copy the token immediately** (you won't see it again)

2. **Push using the token:**
   ```powershell
   git push https://<YOUR_TOKEN>@github.com/tekzomoloi7-lang/CAPS-TYCOON.git main
   ```
   Replace `<YOUR_TOKEN>` with your actual token.

### Option 2: Update Git Credentials

1. **Clear old credentials:**
   ```powershell
   git credential-manager erase https://github.com
   ```

2. **Push again** - Git will prompt for credentials:
   ```powershell
   git push origin main
   ```
   - Username: `tekzomoloi7-lang`
   - Password: Use your Personal Access Token (not your GitHub password)

### Option 3: Use GitHub CLI (gh)

1. **Install GitHub CLI** (if not installed):
   ```powershell
   winget install GitHub.cli
   ```

2. **Authenticate:**
   ```powershell
   gh auth login
   ```

3. **Push:**
   ```powershell
   git push origin main
   ```

### Option 4: Use SSH (Long-term solution)

1. **Generate SSH key** (if you don't have one):
   ```powershell
   ssh-keygen -t ed25519 -C "your_email@example.com"
   ```

2. **Add SSH key to GitHub:**
   - Copy the public key: `cat ~/.ssh/id_ed25519.pub`
   - Go to: https://github.com/settings/keys
   - Click "New SSH key"
   - Paste your key and save

3. **Change remote to SSH:**
   ```powershell
   git remote set-url origin git@github.com:tekzomoloi7-lang/CAPS-TYCOON.git
   ```

4. **Push:**
   ```powershell
   git push origin main
   ```

## 🚀 Quick Push (Using Token)

If you have a Personal Access Token ready, run:

```powershell
$token = Read-Host "Enter your GitHub Personal Access Token" -AsSecureString
$BSTR = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($token)
$plainToken = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($BSTR)
git push https://${plainToken}@github.com/tekzomoloi7-lang/CAPS-TYCOON.git main
```

## 📋 What Was Committed

- ✅ Grade-specific Mathematics question banks (367 questions)
- ✅ Grade-specific Physical Sciences question banks (194 questions)
- ✅ Updated question selection logic
- ✅ All extraction scripts and documentation
- ✅ Updated HTML file with integrated question banks

## ✅ After Successful Push

Once pushed, Vercel will automatically detect the changes and redeploy your app. You can check deployment status at:
- https://vercel.com/dashboard

## 🔍 Verify Push

After pushing, verify at:
- https://github.com/tekzomoloi7-lang/CAPS-TYCOON

You should see the latest commit with message: "Add grade-specific question banks for Mathematics and Physical Sciences"





