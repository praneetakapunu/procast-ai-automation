# Demo Script for ProCAST Automation Presentation

## Pre-Demo Setup
- [ ] ProCAST installed and licensed
- [ ] Sample turbocharger model ready
- [ ] Clawdbot connected to system
- [ ] Dashboard running on local server
- [ ] Network connection stable

## Opening (2 minutes)
"Good morning/afternoon. Today I'll show you how Clawdbot can transform your casting simulation workflow, turning weeks of manual optimization into days of automated exploration."

**Key Point**: "Your engineers are experts - they should be making strategic decisions, not clicking through repetitive simulations."

## Problem Statement (3 minutes)
"Let me share what we typically hear from foundries using ProCAST:
- Setting up each simulation takes 30-60 minutes
- Engineers run maybe 5-10 variants per week
- Results analysis is manual and time-consuming
- Knowledge from past projects sits in file folders
- Junior engineers need months to become productive"

**Show**: Current manual workflow diagram

## Solution Overview (5 minutes)

### Live Connection Demo
```bash
# Show Clawdbot connecting to ProCAST
clawdbot> exec procast --version
# Output: ProCAST 2024.0 connected

# Show current queue status
clawdbot> Check ProCAST simulation queue
# Shows: 0 active, 0 pending
```

### Upload Model
"Let's start with your turbocharger housing design..."
- Drag and drop STL file
- Clawdbot automatically identifies it as a thin-wall casting
- Suggests appropriate mesh density

## Core Demonstration (15 minutes)

### 1. Baseline Analysis (5 min)
"First, let's run a baseline with your current parameters..."

**Show on screen**:
- Clawdbot setting up simulation
- Real-time log of mesh generation
- Simulation starting

"While that runs, let me show you what happens next..."

**Open dashboard** (turbocharger-procast-demo/dashboard-mockup.html)
- Point out real-time status
- Explain quality score calculation
- Show previous run history

### 2. AI-Powered Optimization (5 min)
"Now here's where it gets interesting. Based on the baseline, Clawdbot will:
1. Identify problem areas (hot spots, potential porosity)
2. Search our knowledge base for similar cases
3. Propose parameter modifications
4. Run multiple variants in parallel"

**Trigger optimization**:
```
"Optimize this turbocharger design for minimum porosity 
while maintaining fill time under 5 seconds"
```

**Show**:
- Parameter space being explored
- Multiple simulations launching
- Dashboard updating with results

### 3. Knowledge Integration (5 min)
"What makes this truly powerful is the integrated knowledge..."

**Demo knowledge query**:
```
"What does the literature say about grain refinement 
in stainless steel thin-wall castings?"
```

**Show**:
- Relevant papers being found
- Key insights extracted
- Recommendations applied to current design

## Results & ROI (5 minutes)

### Concrete Example
"In this demo alone, we've:
- Run 10 design iterations in 20 minutes (vs 2 days manual)
- Reduced predicted porosity from 0.8% to 0.23%
- Identified optimal gating configuration
- Generated comprehensive documentation"

### ROI Calculation
Show slide with:
- Engineering hours saved: 32 hrs/week
- Simulation throughput: 10x increase  
- Defect reduction: 30% typical
- Time to market: 40% faster

### Customer Success Story
"A similar aerospace foundry saw:
- 50% reduction in scrap rate
- 3-month ROI on Clawdbot investment
- Junior engineers productive in days, not months"

## Interactive Q&A (5 minutes)

### Anticipated Questions:

**Q: How does it interface with our ProCAST license?**
A: "Clawdbot uses your existing licenses efficiently, queuing jobs to maximize utilization while respecting seat limits."

**Q: What about our proprietary knowledge?**
A: "Everything stays on-premise. Your IP never leaves your network. Clawdbot can even learn from your historical projects."

**Q: Can it handle our specific alloys?**
A: "Yes, we can import your material database and even help you optimize material properties based on actual production results."

**Q: What if ProCAST updates?**
A: "Clawdbot adapts to new versions. We maintain compatibility with the last 3 ProCAST releases."

## Closing & Next Steps (3 minutes)

"What you've seen today is just the beginning. Imagine:
- Running optimization campaigns 24/7
- Building a knowledge base from every simulation
- Predicting production issues before they happen
- Empowering your team to focus on innovation"

### Proposed Pilot Program
"I suggest we start with a 3-month pilot on one product line:
- Week 1-2: System integration
- Week 3-4: Baseline establishment  
- Week 5-12: Full optimization campaign
- Measurable success metrics throughout"

### Call to Action
"Let's schedule a technical deep-dive where your ProCAST team can ask detailed questions and we can define success metrics together."

## Post-Demo Materials
Hand out:
1. Technical architecture diagram
2. ROI calculator spreadsheet
3. Security & compliance documentation
4. Customer success stories
5. Pilot program proposal

## Key Differentiators to Emphasize
1. **Always Learning**: Every simulation makes the system smarter
2. **24/7 Operation**: Runs while your team sleeps
3. **Knowledge Preservation**: Captures tribal knowledge
4. **Flexible Deployment**: Cloud, on-premise, or hybrid
5. **No Lock-in**: Enhances ProCAST, doesn't replace it