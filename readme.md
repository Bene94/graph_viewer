# Interactive Hierarchical Graph

This project creates an interactive hierarchical graph using Streamlit and `streamlit-agraph`. The graph visualizes parent-child relationships from a CSV file and allows metadata visualization from a JSON file. Additionally, the direction of the edges can be reversed to show child-parent relationships.

## Features
- Upload CSV files to define the graph structure.
- Upload JSON files to include metadata for each node.
- Interactively select a node to explore its hierarchical relationships.

## Installation Instructions

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Step-by-Step Guide

#### 1. Clone the Repository
\`\`\`bash
git clone [https://github.com/yourusername/interactive-hierarchical-graph](https://github.com/Bene94/graph_viewer/new/main).git
cd interactive-hierarchical-graph
\`\`\`

#### 2. Set Up a Virtual Environment (Optional but Recommended)
Create a virtual environment to manage dependencies:
\`\`\`bash
python -m venv venv
\`\`\`

Activate the virtual environment:
- On Windows:
  \`\`\`bash
  .\venv\Scripts\activate
  \`\`\`
- On macOS and Linux:
  \`\`\`bash
  source venv/bin/activate
  \`\`\`

#### 3. Install Required Packages
Install the necessary Python packages using pip:
\`\`\`bash
pip install -r requirements.txt
\`\`\`

If \`requirements.txt\` is not available, manually install the required packages:
\`\`\`bash
pip install streamlit pandas streamlit-agraph
\`\`\`

#### 4. Run the Application
Start the Streamlit application:
\`\`\`bash
streamlit run app.py
\`\`\`

### Usage Instructions

1. **Upload Files**:
   - Use the sidebar to upload a CSV file that defines the graph structure.
   - Upload a JSON file to include metadata for each node.

2. **Select a Node**:
   - After uploading the files, use the dropdown menu to select a node. The graph will display the hierarchical relationships of the selected node.

3. **Reverse Edges**:
   - The edges in the graph will be reversed to show child-parent relationships.

### CSV File Format
The CSV file should have two columns:
- \`parent\`: The parent node.
- \`child\`: The child node.

Example:
\`\`\`csv
parent,child
A,B
A,C
B,D
C,E
\`\`\`

### JSON File Format
The JSON file should contain metadata for each node in the form of key-value pairs.

Example:
\`\`\`json
{
  "A": {"description": "Node A", "mixture": true},
  "B": {"description": "Node B"},
  "C": {"description": "Node C", "mixture": false},
  "D": {"description": "Node D"},
  "E": {"description": "Node E"}
}
\`\`\`

## Troubleshooting

- Make sure the CSV and JSON files are correctly formatted as per the instructions.

## License

This project is licensed under the MIT License. See the \`LICENSE\` file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## Contact

For any questions or issues, please open an issue in the repository or contact the project maintainer at [your-email@example.com].

---

Replace \`yourusername\` and \`your-email@example.com\` with your actual GitHub username and email address before using this README.
