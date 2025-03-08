import streamlit as st
import streamlit.components.v1 as components
from groq import Groq
import requests
import os
from dotenv import load_dotenv
import py3Dmol

# Load environment variables
load_dotenv()

# Visualize Protein-Ligand Interaction with py3Dmol
def visualize_protein_ligand_interaction(pdb_id):
    """
    Visualize a protein-ligand interaction using py3Dmol and display it in Streamlit.
    :param pdb_id: str, PDB ID of the protein structure (e.g., "6LU7").
    """
    viewer = py3Dmol.view(query=f"pdb:{pdb_id}")
    viewer.setStyle({'cartoon': {'color': 'spectrum'}})
    viewer.addStyle({'hetflag': True}, {'stick': {'colorscheme': 'orangeCarbon'}})
    viewer.zoomTo()
    viewer_html = viewer._make_html()
    components.html(viewer_html, height=500)

class DrugProteinInteractionAnalyzer:
    def __init__(self, api_key=None):
        if api_key:
            self.client = Groq(api_key=api_key)
        else:
            env_key = os.getenv('GROQ_API_KEY')
            if not env_key:
                st.warning("API Key not found. Please enter your key.")
                env_key = st.text_input("Enter API Key", type="password")
            if env_key:
                self.client = Groq(api_key=env_key)
            else:
                st.error("No API key provided. Cannot initialize Groq client.")
                self.client = None

    def fetch_ncbi_data(self, query, db):
        """
        Fetch data from NCBI Entrez.
        """
        try:
            url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db={db}&term={query}&retmode=json"
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            st.error(f"Error fetching data: {e}")
            return None

    def analyze_interaction(self, protein, drug, interaction_type):
        """
        Analyze drug-protein interaction using Groq API.
        """
        if not self.client:
            st.error("Groq client not initialized.")
            return None

        try:
            st.info("Processing interaction analysis...")
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": """You are a bioscientist specializing in drug-protein interactions. Based on the protein,
                        drug, and interaction type provided, generate a detailed report including binding affinity,
                        interaction mechanisms, and any relevant recommendations."""
                    },
                    {
                        "role": "user",
                        "content": f"Protein: {protein}\nDrug: {drug}\nInteraction Type: {interaction_type}"
                    }
                ],
                model="llama3-70b-8192",
                max_tokens=700,
                temperature=0.7
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            st.error(f"Error analyzing interaction: {e}")
            return None

def main():
    st.title("🧬 Drug-Protein Interaction Explorer")

    st.sidebar.header("Settings")
    manual_api_key = st.sidebar.text_input("Groq API Key", type="password")

    analyzer = DrugProteinInteractionAnalyzer(api_key=manual_api_key)

    st.header("Protein Target")
    protein = st.text_input("Protein Name or Accession (e.g., EGFR, P53)")
    pdb_id = st.text_input("PDB ID for 3D View (e.g., 1M17)")

    st.header("Drug Information")
    drug = st.text_input("Drug Name or Identifier (e.g., Gefitinib, CID:123631)")

    st.header("Analysis Parameters")
    interaction_type = st.text_input("Interaction Type (e.g., binding affinity)")

    if st.button("Run Analysis"):
        if not protein.strip() or not drug.strip():
            st.warning("Both protein and drug fields are required.")
            return

        st.subheader("Protein Data")
        protein_data = analyzer.fetch_ncbi_data(protein, "protein")
        if protein_data:
            st.json(protein_data)

        st.subheader("Analysis Results")
        analysis_result = analyzer.analyze_interaction(protein, drug, interaction_type)
        if analysis_result:
            st.text_area("Interaction Report", analysis_result, height=300)

        if pdb_id:
            st.subheader("3D Visualization")
            st.write(f"Displaying 3D structure for PDB ID: {pdb_id}")
            visualize_protein_ligand_interaction(pdb_id)
        else:
            st.warning("No PDB ID provided for visualization.")

if __name__ == "__main__":
    main()
