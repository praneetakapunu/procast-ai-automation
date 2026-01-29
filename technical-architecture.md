# Technical Architecture

## System Components

### 1. ProCAST Interface Layer
```
Clawdbot Agent
    ├── ProCAST CLI Wrapper
    │   ├── Solver execution
    │   ├── Pre/Post processor control
    │   └── License management
    │
    ├── File System Monitor
    │   ├── Input file generation (.d, .dat)
    │   ├── Results parsing (.unf, .case)
    │   └── Mesh file handling
    │
    └── Process Manager
        ├── Queue management
        ├── Resource allocation
        └── Error recovery
```

### 2. Analysis Pipeline
```
Result Files → Data Extraction → Analysis Engine → Insights
                    │                 │              │
                    ├── Temperature   ├── Defect     ├── Reports
                    ├── Velocity      │   prediction ├── Dashboards
                    ├── Pressure      ├── Quality    └── Alerts
                    └── Solidification    scoring
```

### 3. Optimization Engine
```
DOE Controller
    ├── Parameter Space Definition
    │   ├── Pouring temperature: 1480-1520°C
    │   ├── Mold temperature: 200-400°C
    │   ├── Filling time: 2-8 seconds
    │   └── Gate dimensions
    │
    ├── Search Strategies
    │   ├── Gradient-based optimization
    │   ├── Genetic algorithms
    │   └── Bayesian optimization
    │
    └── Convergence Criteria
        ├── Quality thresholds
        ├── Iteration limits
        └── Improvement plateaus
```

### 4. Knowledge Integration
```
External Sources
    ├── Material Databases
    │   ├── ASM International
    │   ├── NADCA standards
    │   └── Custom material library
    │
    ├── Research Papers
    │   ├── Google Scholar API
    │   ├── Internal documentation
    │   └── Patent databases
    │
    └── Historical Data
        ├── Previous simulations
        ├── Production feedback
        └── Defect correlations
```

### 5. Dashboard Components
- **Real-time Monitoring**: Active simulation status, resource usage
- **Results Comparison**: Side-by-side design evaluations
- **Trend Analysis**: Parameter sensitivity charts
- **3D Visualization**: WebGL-based result viewer
- **Report Builder**: Automated PowerPoint/PDF generation

## API Endpoints

### Simulation Control
```
POST /api/simulation/start
{
  "model": "turbo_housing_v3.stl",
  "material": "SS316L",
  "parameters": {
    "pouring_temp": 1500,
    "mold_temp": 300,
    "filling_time": 4.5
  }
}

GET /api/simulation/{id}/status
GET /api/simulation/{id}/results
```

### Analysis & Reporting
```
POST /api/analysis/defect-prediction
GET /api/reports/generate/{simulation_id}
GET /api/dashboard/metrics
```

## Security & Compliance
- On-premise deployment option
- Encrypted storage for proprietary designs
- Role-based access control
- Audit trail for all parameter changes
- ITAR compliance for aerospace applications