Secure Login System - Risk-Aware ETL & Analytics Pipeline
A data-driven cybersecurity pipeline that processes raw user authentication telemetry logs, 
performs real-time threat-matrix transformation, 
isolates high-risk access vectors, and generates security dashboard intelligence visualizations.
This system is built to identify, isolate, and log active cyber threats (such as credential stuffing and brute-force attempts from flagged malicious IPs) while ensuring normal access streams are routed into clean analytics pools for behavioral audit trails.

📋 Table of Contents
*Project Overview
*Technologies & Frameworks Used
*Dataset Characteristics
*Key Features
*Getting Started & Installation
*Pipeline Breakdown & Syntax Analysis
*Output Visualizations

1) Project Overview
In enterprise security environments, real-time logging is massive and unfiltered.
This project implements a Python-based ETL (Extract, Transform, Load) system tailored for a Secure Login System.
The system reads authentication telemetry data containing structural network payloads (IP Addresses, OS/Browser user agents, Latency metrics, Login outcomes, and Threat Intelligence flags), addresses anomalies, and transforms them into an actionable categorization matrix. Finally,
it bifurcates database-ready outputs and exports high-fidelity visualization profiles monitoring security anomalies.

2) Technologies & Frameworks Used
This project relies entirely on industry-standard data engineering and visualization libraries within the Python ecosystem:
Python (v3.8+): The baseline computing language used for script execution and pipeline scheduling.
Pandas: The primary data manipulation framework. Used to load raw CSV streams into in-memory DataFrame objects, perform vectorized structural manipulation, drop/fill invalid network attributes, and slice datasets into decoupled layers.
NumPy: Used for high-performance mathematical logic. Its vectorized selection conditional engine (np.select) replaces slow standard loop processing to assign security categories across millions of rows efficiently.
Matplotlib (Pyplot): The standard data visualization library. Utilized to build, design, and export horizontal analytical reports mapping out threat distributions.

3) Dataset Characteristics
The pipeline handles structured user access telemetry containing the following key attributes:
Network & Identity Data: IP Address, User ID, ASN (Autonomous System Number).
Geographical Data: Country, Region, City.
Client Telemetry: User Agent String, Browser Name and Version, OS Name and Version, Device Type.
Performance Metrics: Round-Trip Time [ms] (Network latency measurement).
Security Context Flags: Login Successful (Boolean), Is Attack IP (Boolean flag determined by IP reputation systems), Is Account Takeover (Boolean).

4) Key Features
Missing Value Imputation: Automatically repairs unrecorded network metrics (such as missing round-trip time values or blank geo-location data string blocks) to ensure seamless downstream modeling.
Vectorized Rules Engine: Leverages low-level array optimizations to catalog multi-variable login behavior without nested execution bottlenecks.
Data Segregation: Divides raw telemetry logs into dedicated data tiers (clean_access_logs.csv vs. security_alerts.csv) to minimize storage read overhead for operational analysts.
Automated Asset Generation: Exports print-ready analytics bar charts (consolidated_security_analysis.png) displaying operational metrics every time the execution trigger is pulled.

5) Getting Started & Installation
Prerequisites
Ensure you have Python installed alongside the pip packaging controller.

Setup Instructions
-> Clone this repository onto your native workspace:
git clone https://github.com/your-username/secure-login-system-etl.git
cd secure-login-system-etl

-> Install the necessary data-engineering dependencies:
pip install pandas numpy matplotlib

-> Ensure your raw input data file is named tableConvert.com_1cil4b.csv and placed directly inside the root directory.

->Execute the pipeline:
python security_pipeline.py

6) Pipeline Breakdown & Syntax Analysis
The underlying engine structure is managed linearly within a single deterministic pipeline routine:

-> Extract Stage: 
Syntax Purpose: Parses raw CSV authentication payloads into an in-memory structural tabular matrix.
df = pd.read_csv(file_path)

-> Transform Stage
Syntax Purpose: .fillna(0) updates empty latency payloads to a numerical baseline. np.select uses vectorized parallel execution to rapidly classify data points across complex logical conditions without impacting application runtime.

df['Round-Trip Time [ms]'] = df['Round-Trip Time [ms]'].fillna(0)
df['Security Risk Category'] = np.select(conditions, choices, default='UNKNOWN')

-> Load & Visual Analytics Stage
Syntax Purpose: .to_csv(..., index=False) exports the cleaned dataset while dropping the redundant default pandas row index integer. plt.savefig packages the matplotlib canvas into an uncompressed, high-definition image payload at 300 DPI for dashboard reporting.
clean_access_logs.to_csv('clean_access_logs.csv', index=False)
plt.savefig('consolidated_security_analysis.png', dpi=300)

7) Output Visualizations
When execution terminates successfully, the script evaluates aggregated metrics and exports an operational bar chart visualizing the distributed frequency patterns of login events:
SUCCESSFUL LOGIN: Baseline non-malicious user sessions.
FAILED ATTEMPT: Standard client connection password entry errors.
BLOCKED ATTACK: Attacker activity neutralized by the access policy layer.
CRITICAL BREACH: Compromised user accounts where known hostile IPs successfully bypassed authentication boundaries.
Generated assets are stored directly in the workspace as consolidated_security_analysis.png.








