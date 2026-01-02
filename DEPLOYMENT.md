# Deployment Guide - Vercel

## 🚀 Deploy to Vercel via GitHub

### Step 1: Push Code to GitHub

You need to push your code to GitHub first. Choose one of these methods:

#### Option A: Using GitHub Desktop (Easiest)
1. Download GitHub Desktop: https://desktop.github.com/
2. Sign in with your GitHub account
3. File → Add Local Repository
4. Select the "CAPS TYCOON GAME" folder
5. Commit any changes if needed
6. Click "Publish repository" or "Push origin"

#### Option B: Using Git CLI with Personal Access Token
1. Create a Personal Access Token:
   - Go to: https://github.com/settings/tokens
   - Generate new token (classic) with `repo` scope
   - Copy the token

2. Push to GitHub:
   ```bash
   git push -u origin main
   ```
   When prompted:
   - Username: your GitHub username
   - Password: paste your personal access token

### Step 2: Connect to Vercel

1. **Sign up/Login to Vercel**
   - Go to: https://vercel.com/
   - Sign up or log in (use "Continue with GitHub" for easiest setup)

2. **Import Project**
   - Click "Add New..." → "Project"
   - Select "Import Git Repository"
   - Find and select `tekzomoloi7-lang/CAPS-TYCOON`
   - Click "Import"

3. **Configure Project**
   - **Framework Preset**: Other (or leave as default)
   - **Root Directory**: `./` (leave as default)
   - **Build Command**: Leave empty (no build needed)
   - **Output Directory**: Leave empty (serving from root)
   - **Install Command**: Leave empty (no dependencies)

4. **Environment Variables** (if needed)
   - If you're using Firebase, you can add environment variables here
   - For now, you can skip this if Firebase config is in the HTML

5. **Deploy**
   - Click "Deploy"
   - Wait for deployment to complete (usually 1-2 minutes)

### Step 3: Access Your Deployed App

After deployment:
- Vercel will provide you with a URL like: `https://caps-tycoon-xxxxx.vercel.app`
- You can also add a custom domain in the project settings

### Step 4: Update Service Worker URLs (if needed)

If your app URL is different, you may need to update:
- `manifest.json` - start_url and scope
- `sw.js` - cached URLs
- Or just use the root paths (already configured)

## 🔄 Continuous Deployment

Vercel automatically deploys:
- Every push to `main` branch = Production deployment
- Every pull request = Preview deployment

## 📱 PWA Features

Your app is now a PWA! Users can:
- Install it on their devices
- Use it offline (after first visit)
- Add to home screen

## 🎨 Custom Domain (Optional)

1. Go to your project settings on Vercel
2. Navigate to "Domains"
3. Add your custom domain
4. Follow DNS configuration instructions

## 🔧 Troubleshooting

### Service Worker Not Working
- Make sure HTTPS is enabled (Vercel provides this automatically)
- Check browser console for errors
- Clear browser cache and hard reload

### Routes Not Working
- The `vercel.json` file handles routing
- All routes redirect to `caps-tycoon.html`

### Firebase Issues
- Make sure Firebase config is correct
- Check Firebase console for any errors
- Ensure Firebase project settings allow your Vercel domain

## 📚 Additional Resources

- Vercel Documentation: https://vercel.com/docs
- PWA Documentation: https://web.dev/progressive-web-apps/








