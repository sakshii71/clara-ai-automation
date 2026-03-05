\# Clara Answers Automation Pipeline



\## Overview



This project implements a \*\*zero-cost automation pipeline\*\* that converts customer call transcripts into structured operational configurations for a Clara AI voice agent.



The pipeline simulates the workflow used by Clara Answers to onboard service trade businesses such as electrical contractors, HVAC companies, and fire protection providers.



The system takes raw call transcripts (demo or onboarding calls) and transforms them into structured artifacts such as:



\* Account memo JSON

\* AI agent configuration (Retell agent draft spec)

\* Versioned updates (v1 → v2)

\* Change logs between versions



The goal is to demonstrate how messy conversational data can be converted into structured operational rules that power an AI receptionist.



---



\# Architecture



The automation pipeline follows this workflow:



Demo Call Transcript

↓

Extraction Script

↓

Structured Account Memo JSON

↓

Retell Agent Draft Specification (v1)

↓

Stored Versioned Output



When onboarding updates arrive:



Onboarding Transcript

↓

Update Account Memo

↓

Generate Agent Spec v2

↓

Generate Change Log



This structure allows the system to evolve agent configurations safely as more precise operational information becomes available.



---



\# Project Structure



```

clara-ai-automation

│

├── dataset

│     chat.txt

│

├── scripts

│     extract\_data.py

│

├── outputs

│   └── accounts

│       └── bens\_electric

│           ├── v1

│           │    extracted.json

│           │    agent.json

│           │

│           ├── v2

│           │    agent.json

│           │

│           └── changes.md

│

└── README.md

```



\### Folder Description



\*\*dataset/\*\*

Contains the transcript input used by the pipeline.



\*\*scripts/\*\*

Contains automation scripts responsible for reading transcripts and generating structured output.



\*\*outputs/accounts/\*\*

Stores generated artifacts for each account including:



\* Account memo

\* Agent configuration

\* Version updates

\* Change log



---



\# Running the Pipeline



\### 1. Clone the repository



```

git clone https://github.com/<your-username>/clara-ai-automation

```



\### 2. Navigate into the project



```

cd clara-ai-automation

```



\### 3. Place transcript files inside



```

dataset/

```



Example:



```

dataset/chat.txt

```



\### 4. Run the automation script



```

python scripts/extract\_data.py

```



The script will:



\* Load the transcript

\* Extract relevant information

\* Generate structured JSON output



---



\# Generated Outputs



The system produces structured outputs including:



\### Account Memo JSON



Structured operational data extracted from transcripts.



\### Retell Agent Draft Specification



Configuration used to initialize the Clara AI voice agent.



\### Version Updates



The pipeline maintains version history:



\* \*\*v1\*\* – Generated from demo call data

\* \*\*v2\*\* – Generated after onboarding updates



\### Change Log



All modifications between versions are tracked in:



```

changes.md

```



This ensures transparency and traceability of configuration changes.



---



\# Handling Missing Data



Customer conversations may contain incomplete information.



To ensure reliability:



\* Missing details are \*\*not inferred\*\*

\* Unknown values are logged explicitly

\* Fields are documented under `questions\_or\_unknowns`



This prevents incorrect operational configurations from being generated.



---



\# Design Considerations



This pipeline was designed to demonstrate:



\* Systematic transformation of conversational data

\* Structured operational rule extraction

\* Safe versioning of agent configurations

\* Repeatable automation workflows

\* Clear auditability of configuration updates



---



\# Limitations



The provided transcript dataset contains limited operational information.



Because of this:



\* Some configuration fields remain unknown

\* Routing rules and business hours may not be fully specified



In a production system, these details would be extracted from:



\* Full call transcripts

\* Structured onboarding forms

\* CRM integrations



---



\# Future Improvements



Possible enhancements include:



\* Automatic speech-to-text processing

\* LLM-based extraction of operational rules

\* Direct integration with Retell APIs

\* Batch processing for multiple accounts

\* Automated validation of agent configurations

\* Web dashboard for reviewing onboarding updates



---



\# Demonstration



A short Loom video demonstrates:



\* Project architecture

\* Transcript input

\* Automation pipeline execution

\* Generated outputs

\* Versioned agent configurations



---



\# Summary



This project demonstrates how an automation system can convert real-world customer conversations into structured operational logic that configures an AI voice agent.



The pipeline is modular, repeatable, and version-controlled, making it suitable for scaling onboarding workflows across multiple customer accounts.



