# Drug-Protein Interaction Explorer

## Overview
The **Drug-Protein Interaction Explorer** is a Streamlit-based web application that allows users to analyze drug-protein interactions using the **Groq API** and visualize protein-ligand structures in **3D** using **py3Dmol**. The tool also integrates with **NCBI Entrez** to fetch protein-related data.

## Features
- 🧬 **Analyze Drug-Protein Interactions** using Groq API.
- 🔍 **Fetch Protein Data** from the NCBI Entrez database.
- 🎨 **3D Visualization** of protein-ligand interactions with py3Dmol.
- 🔑 **Secure API Key Input** for Groq API.

## Requirements
Before running the application, ensure you have the following dependencies installed:

### Dependencies
- Python 3.8+
- Streamlit
- py3Dmol
- requests
- dotenv
- groq (Groq API SDK)

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/mripradhan/drug-protein-analysis-3d-viewer.git
   cd drug-protein-analysis-3d-viewer
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up your environment variables:
   - Create a `.env` file in the project root.
   - Add your Groq API Key:
     ```sh
     GROQ_API_KEY=your_groq_api_key_here
     ```

## Usage
To run the Streamlit application, execute the following command:
```sh
streamlit run pbvis.py
```

### How to Use
1. Enter your **Groq API Key** in the sidebar or set it in the `.env` file.
2. Input **Protein Name/Accession** and optional **PDB ID**.
3. Provide the **Drug Name or Identifier**.
4. Specify the **Interaction Type** (e.g., binding affinity).
5. Click **Run Analysis** to fetch data and generate the interaction report.
6. If a valid PDB ID is provided, a **3D visualization** of the structure will be displayed.

## Example Inputs
- **Protein:** EGFR, P53
- **PDB ID:** 6LU7, 1M17
- **Drug:** Gefitinib, CID:123631
- **Interaction Type:** Binding affinity

## Troubleshooting
- **API Key Not Found:** Ensure you have set `GROQ_API_KEY` in `.env` or manually enter it in the UI.
- **NCBI Data Fetch Errors:** Verify your internet connection and correct protein identifiers.
- **3D Visualization Not Loading:** Ensure the PDB ID is valid and check if `py3Dmol` is installed.

## License
This project is licensed under the MIT License.

## Acknowledgments
- **NCBI Entrez API** for protein data.
- **Groq API** for drug-protein interaction analysis.
- **py3Dmol** for molecular visualization.

## Contact
For questions or contributions, feel free to reach out via GitHub Issues.
