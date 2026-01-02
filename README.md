# ZA Mzansi Learn & Play - CAPS Educational Gaming Platform

An interactive educational gaming platform aligned with the South African CAPS curriculum, featuring multiple game modes including Tycoon, Summit Race, and Kelp Quest.

## 🎮 Features

- 📚 **CAPS-Aligned Content** - Questions for Mathematics and Physical Sciences (Grades 8-12)
- 🎯 **Multiple Game Modes** - Tycoon, Summit Race, and Kelp Quest
- 👥 **Multiplayer Support** - Real-time multiplayer via Firebase
- 📊 **Detailed Analytics** - Comprehensive analytics dashboard for teachers/hosts
- 📱 **Fully Responsive PWA** - Optimized for phones, tablets, and PCs
- ✨ **Engaging UI** - Beautiful animations and graphics
- 🎨 **Viral-Worthy Design** - Catchy visuals and smooth interactions

## 🎯 Game Modes

### 🏗️ CAPS Tycoon
Build your educational empire by answering questions correctly! Earn money, buy upgrades, and race to reach the target amount.

### ⛰️ Ubuntu Summit
Race up Table Mountain by mastering CAPS questions! Answer correctly to climb higher and reach the summit.

### 🎣 Mzansi Kelp Quest
Catch fish in the ocean while learning! Navigate your boat, earn bait, catch fish, and sell them for Mzansi Mussels (MZN).

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/tekzomoloi7-lang/CAPS-TYCOON.git
   cd CAPS-TYCOON
   ```

2. **Open the app**
   - Simply open `caps-tycoon.html` in a web browser
   - Or use a local server:
     ```bash
     python -m http.server 8000
     # Then visit http://localhost:8000/caps-tycoon.html
     ```

3. **Configure Firebase (for multiplayer)**
   - See the Firebase setup guide in the code comments
   - Update Firebase configuration in `caps-tycoon.html`

## 📱 PWA Features

This app is a Progressive Web App (PWA) that can be:
- Installed on mobile devices
- Installed on desktop
- Used offline (with service worker)
- Added to home screen

## 🌐 Deployment

This app can be deployed to:
- **Vercel** (Recommended - Free tier with automatic deployments) ⭐
- **GitHub Pages** (Free, easy setup)
- **Netlify** (Free tier available)
- **Firebase Hosting** (Free tier available)
- Any static hosting service

### Deploy to Vercel (Recommended)

**Automatic Deployment Setup:**
1. Visit [vercel.com](https://vercel.com) and sign in with GitHub
2. Click "Add New..." → "Project"
3. Import repository: `tekzomoloi7-lang/CAPS-TYCOON`
4. Configure:
   - Framework Preset: Other
   - Root Directory: `./`
   - Build Command: (leave empty)
   - Output Directory: `./`
5. Click "Deploy"

**Result:**
- ✅ Automatic deployments on every `git push`
- ✅ Preview deployments for pull requests
- ✅ Free SSL certificate
- ✅ Global CDN
- ✅ Custom domain support

See [VERCEL_AUTO_DEPLOY.md](VERCEL_AUTO_DEPLOY.md) for detailed setup instructions.

### Deploy to GitHub Pages

1. Go to repository Settings → Pages
2. Select branch: `master`
3. Select folder: `/ (root)`
4. Your app will be live at: `https://tekzomoloi7-lang.github.io/CAPS-TYCOON/`

## 🛠️ Technologies Used

- **HTML5** - Structure
- **CSS3** - Responsive design with mobile-first approach
- **JavaScript (ES6+)** - Game logic and interactions
- **Firebase** - Realtime Database & Authentication
- **p5.js** - Canvas rendering for game modes

## 📊 Analytics Dashboard

Teachers/hosts can access detailed analytics after each game:
- **Overview View** - All players' performance, question statistics
- **Individual Player View** - Detailed breakdown per player
- **Question Details** - See who answered what, correct/incorrect counts

## 🎨 Features Highlights

- **Responsive Design** - Optimized for all screen sizes
- **Touch Optimized** - Mobile-friendly controls
- **Beautiful Animations** - Engaging particle effects and transitions
- **Real-time Updates** - Live leaderboards and player stats
- **Accessible** - Proper touch targets and readable text
- **Achievement System** - Unlock badges and track progress
- **XP & Leveling** - Gain experience points and level up
- **Daily Rewards** - Claim daily login rewards with streak bonuses
- **Player Statistics** - Track your performance and game history
- **Themes** - Customize the app appearance
- **Social Sharing** - Share your achievements and results

## 📝 Firebase Setup

1. Create a Firebase project at [Firebase Console](https://console.firebase.google.com/)
2. Enable Realtime Database
3. Copy your Firebase config
4. Update the configuration in `caps-tycoon.html`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

[Specify your license here]

## 👨‍💻 Author

Created for ZA Mzansi Learn & Play educational platform

---

**Made with ❤️ for South African Learners**












