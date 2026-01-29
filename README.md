# ProCAST AI Automation - Presentation Package

## Overview
Complete presentation package for demonstrating Clawdbot's AI-powered ProCAST automation capabilities to turbocharger foundry companies working with stainless steel castings.

## 🎯 Value Proposition
- **80% reduction** in simulation setup time
- **10x more** design iterations per week  
- **30% defect reduction** through AI optimization
- **3-6 month** typical payback period
- **24/7 operation** - continuous optimization while team sleeps

## 📁 Package Contents

### Core Presentation Files
- **`presentation-slides.html`** - Visual presentation slides (print to PDF)
- **`presentation-outline.md`** - Detailed presentation structure and content
- **`demo-script.md`** - Word-for-word presentation guide with timing
- **`presentation-guide.md`** - Tips for delivery, objection handling, follow-up

### Interactive Demos
- **`dashboard-mockup.html`** - Live dashboard demonstration
- **`roi-calculator.html`** - Interactive savings calculator
- **`live-demo-commands.md`** - Commands for actual Clawdbot demo

### Technical Documentation
- **`technical-architecture.md`** - Detailed system design and integration
- **`README.md`** - This file

## 🖥️ How to Use

### 1. Generate PDF Presentation
```bash
# Open in browser and print to PDF
open presentation-slides.html
# Use browser's Print function → Save as PDF
# Recommended: Landscape orientation, remove headers/footers
```

### 2. Interactive Demo Setup
```bash
# Start local server for dashboard demo
python -m http.server 8000
# Open http://localhost:8000/dashboard-mockup.html
# Open http://localhost:8000/roi-calculator.html in second tab
```

### 3. Live Clawdbot Demo
```bash
# Follow commands in live-demo-commands.md
# Ensure ProCAST is installed and accessible
# Have sample turbocharger model ready
```

### 4. Web Application (Like Personal-Utilities)
```bash
# Start the web app
cd turbocharger-procast-demo
./start.sh

# Access at http://localhost:8080/
# Or via nginx proxy at https://praneet.exe.xyz:8000/procast/
```

### 5. Deploy to exe.xyz Server
```bash
# Copy nginx config to enable proxy
sudo cp deploy/nginx-procast.conf /etc/nginx/sites-enabled/

# Reload nginx
sudo nginx -s reload

# Start the app (runs on port 8080)
./start.sh

# Access at https://praneet.exe.xyz:8000/procast/
```

### 6. Running as Background Service
```bash
# Create systemd service for automatic startup
sudo cp deploy/procast.service /etc/systemd/system/
sudo systemctl enable procast
sudo systemctl start procast
```

## 🎨 Presentation Flow (45 minutes total)

1. **Opening** (2 min) - Problem hook
2. **Current Challenges** (5 min) - Paint the pain points  
3. **Solution Overview** (5 min) - Clawdbot capabilities
4. **Live Demo** (15 min) - Dashboard + ROI calculator
5. **Technical Architecture** (5 min) - How it integrates
6. **ROI Analysis** (5 min) - Concrete numbers
7. **Implementation Plan** (5 min) - Timeline and next steps
8. **Q&A** (3 min) - Technical questions

## 💡 Key Messages

### For Technical Audience
- "Augments ProCAST, doesn't replace it"
- "Your IP stays on-premise"  
- "API-driven, works with existing infrastructure"
- "Learns from your historical data"

### For Management
- "80% reduction in simulation setup time"
- "10x more design iterations"
- "3-6 month typical payback"
- "Competitive advantage through AI"

## 🎯 Target Use Case
**Turbocharger Housing Optimization**
- Challenge: Minimize porosity in thin-wall stainless steel castings
- Current: 0.8% porosity, 5% scrap rate
- After Clawdbot: 0.23% porosity, 1.2% scrap rate
- Result: 71% porosity reduction, $380,000 annual scrap savings

## 📊 ROI Example (5-Engineer Team)
- **Annual Labor Savings**: $312,000
- **Scrap Reduction Savings**: $175,000
- **Total Annual Savings**: $487,000
- **Investment (Year 1)**: $85,000
- **Net Benefit**: $402,000
- **Payback Period**: 2.1 months

## 🛠️ Technical Requirements
- ProCAST installation with valid licenses
- Windows/Linux compatible
- Network access for AI models (or on-premise deployment)
- Modern web browser for dashboard
- Minimum 16GB RAM, multi-core CPU recommended

## 🔒 Security Features
- On-premise deployment option
- Encrypted data storage
- Role-based access control  
- Audit trail for all changes
- ITAR compliance available

## 📞 Follow-up Actions
1. Send thank you with key materials
2. Schedule technical deep-dive session
3. Send customized pilot proposal
4. Include ROI numbers specific to their operation

## 🚀 Pilot Program Structure
- **Duration**: 3 months
- **Scope**: One product line (turbocharger housings)
- **Investment**: $15,000 (credited toward annual license)
- **Success Metrics**: 
  - 10x simulation throughput
  - 40% defect reduction
  - 80% time savings
  - 100% knowledge documentation

## 📈 Expected Outcomes
- Reduced time-to-market by 40%
- Junior engineers productive in weeks vs months
- Systematic knowledge capture and reuse
- Continuous 24/7 optimization campaigns
- Competitive advantage through AI-powered design

## 🏢 About Clawdbot
Clawdbot is an AI automation platform that enhances engineering workflows by providing intelligent agents that can control desktop applications, run complex simulations, and generate insights from data. Trusted by leading aerospace and automotive manufacturers.

---

**© 2026 Clawdbot Inc. - Confidential and Proprietary**

For questions or to schedule a demo: sales@clawdbot.com