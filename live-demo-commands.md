# Live Demo Commands - ProCAST Automation

## Quick Reference for Live Demonstration

### Initial Setup Check
```bash
# Verify ProCAST is accessible
exec procast -version

# Check available licenses
exec procast -license status

# Show current working directory
pwd

# List existing simulation files
ls -la *.dat *.unf
```

### Basic Automation Demo

#### 1. Load Model
```
# Upload STL file (drag and drop in chat)
# Or reference existing file:
Please analyze the turbocharger model at /path/to/turbo_housing.stl
```

#### 2. Run Baseline Simulation
```
Run a ProCAST simulation for the turbocharger housing with these parameters:
- Material: SS316L
- Pouring temperature: 1500°C
- Mold temperature: 300°C
- Filling time: 4 seconds
```

#### 3. Check Status
```
Show me the status of active ProCAST simulations
```

#### 4. Analyze Results
```
Analyze the ProCAST results file and identify:
- Maximum porosity location and percentage
- Temperature distribution
- Filling pattern issues
- Suggested improvements
```

### AI Optimization Demo

#### 5. Start Optimization
```
Optimize this casting design to minimize porosity while keeping fill time under 5 seconds. 
Run a design of experiments with these parameters:
- Pouring temperature: 1480-1520°C (5°C steps)
- Mold temperature: 200-400°C (50°C steps)
- Gate dimensions: vary by ±20%
Use parallel processing for faster results.
```

#### 6. Monitor Progress
```
Show me a real-time dashboard of the optimization progress
```

#### 7. Knowledge Integration
```
Search literature for best practices on:
- Grain refinement in stainless steel castings
- Gate design for thin-wall turbocharger housings
- Ceramic filter effectiveness for SS316L

Apply relevant findings to our optimization.
```

### Results & Reporting

#### 8. Compare Designs
```
Create a comparison table of the top 5 designs showing:
- Porosity percentage
- Fill time
- Maximum temperature
- Gate velocity
- Quality score
```

#### 9. Generate Report
```
Create a comprehensive report including:
- Executive summary with key improvements
- Technical details with simulation images
- Parameter sensitivity analysis
- Recommendations for production
- Cost-benefit analysis

Export as PDF and PowerPoint.
```

### Advanced Features

#### 10. Spawn Sub-Agent for Long Task
```
spawn agent=procast-optimizer task="Run 100 simulation variants overnight 
for the turbocharger design, exploring the full parameter space. 
Report back with the top 10 designs and a full analysis."
```

#### 11. Set Up Monitoring
```
Create a cron job to check simulation progress every 30 minutes 
and alert me if any simulation shows porosity below 0.3%
```

#### 12. Database Integration
```
Connect to our material database and suggest alternative 
stainless steel grades that might perform better for this application
```

## Troubleshooting Commands

### If ProCAST Hangs
```
# Check running processes
process action=list

# Kill stuck simulation
process action=kill sessionId=<id>

# Restart ProCAST solver
exec pkill -f procast_solver && sleep 2 && procast -restart
```

### File Management
```
# Clean up temporary files
exec find . -name "*.tmp" -mtime +1 -delete

# Archive completed simulations
exec mkdir -p archive/$(date +%Y%m%d) && mv *.unf archive/$(date +%Y%m%d)/
```

### Performance Monitoring
```
# Check system resources
exec top -b -n 1 | head -20

# Check disk space
exec df -h | grep -E "Filesystem|procast"

# Monitor ProCAST memory usage
exec ps aux | grep procast | awk '{sum+=$6} END {print "ProCAST Memory: " sum/1024 " MB"}'
```

## Tips for Smooth Demo

1. **Pre-stage Files**: Have models and materials ready in known locations
2. **Test Commands**: Run through once before the live demo
3. **Prepare Fallbacks**: Have screenshots/recordings if live fails
4. **Keep it Visual**: Use the dashboard mockup liberally
5. **Stay Calm**: If something fails, explain it's a demo environment

## Emergency Backup Plan

If live demo fails, switch to:
```
"Let me show you a recording of this same optimization 
from yesterday - the live system is running 50 simulations 
right now for another client"
```

Then open the dashboard mockup and walk through the workflow.