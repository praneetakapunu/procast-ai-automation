#!/bin/bash
# Deploy ProCAST Presentation to exe.dev VM

set -e

echo "🚀 Deploying ProCAST AI Automation Presentation to exe.dev..."
echo ""

# Check if we're on an exe.dev VM
if hostname | grep -q "\.exe\.xyz"; then
    VM_NAME=$(hostname | cut -d. -f1)
    echo "📍 Detected exe.dev VM: $VM_NAME"
else
    echo "❌ This doesn't appear to be an exe.dev VM"
    echo "   Run this script on your exe.dev VM"
    echo "   Create one with: ssh exe.dev new"
    exit 1
fi

# Install dependencies if needed
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv .venv
    source .venv/bin/activate
    pip install fastapi uvicorn jinja2
    deactivate
fi

# Set port to 8080 (exe.dev will proxy this)
echo "🔧 Configuring exe.dev to proxy port 8080..."
ssh exe.dev share port $VM_NAME 8080

# Make it public
echo "🌐 Making the site publicly accessible..."
ssh exe.dev share set-public $VM_NAME

# Start the application
echo "🚀 Starting web application..."
source .venv/bin/activate
nohup uvicorn src.app:app --host 127.0.0.1 --port 8080 > app.log 2>&1 &
deactivate

echo ""
echo "✅ Deployment complete!"
echo ""
echo "📱 Your presentation is now available at:"
echo "   https://$VM_NAME.exe.xyz:8080/"
echo ""
echo "💡 Quick links:"
echo "   - Home: https://$VM_NAME.exe.xyz:8080/"
echo "   - Presentation: https://$VM_NAME.exe.xyz:8080/presentation"
echo "   - Dashboard: https://$VM_NAME.exe.xyz:8080/dashboard"
echo "   - ROI Calculator: https://$VM_NAME.exe.xyz:8080/roi-calculator"
echo ""
echo "📊 To monitor the app:"
echo "   tail -f app.log"
echo ""
echo "🛑 To stop the app:"
echo "   pkill -f uvicorn"