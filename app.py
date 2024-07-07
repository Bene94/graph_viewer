import streamlit as st
import pandas as pd
import json
from streamlit_agraph import agraph, Node, Edge, Config

def load_graph_from_file(uploaded_file):
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        return df
    return pd.DataFrame()

def load_metadata_from_file(uploaded_file):
    if uploaded_file is not None:
        metadata = json.load(uploaded_file)
        return metadata
    return {}

def find_parents(node, edges_df, node_instances, instance_counter, parent_map):
    base_node = node.split('.')[0]
    parents = edges_df[edges_df['child'] == base_node]['parent'].tolist()
    parent_nodes = []
    for parent in parents:
        unique_parent = f"{parent}.{instance_counter[parent]}"
        instance_counter[parent] += 1
        node_instances[parent].append(unique_parent)
        parent_nodes.append(unique_parent)
        parent_map[unique_parent] = node  # Record the parent-child relationship
        parent_nodes.extend(find_parents(unique_parent, edges_df, node_instances, instance_counter, parent_map))
    return parent_nodes

def create_nodes_and_edges_for_parents(node, edges_df, metadata):
    instance_counter = {n: 1 for n in edges_df['parent'].unique()}
    node_instances = {n: [] for n in edges_df['parent'].unique()}
    node_instances[node] = [f"{node}.1"]
    parent_map = {}

    parent_nodes = find_parents(f"{node}.1", edges_df, node_instances, instance_counter, parent_map)
    unique_nodes = set(parent_nodes + node_instances[node])

    node_objects = []
    edge_objects = []

    for original_node, instances in node_instances.items():
        for n in instances:
            base_node = n.split('.')[0]
            color = "red" if 'mixture' in metadata.get(base_node, {}) else "blue"
            if n == f"{node}.1":
                color = "green"
            if not any(existing_node.id == n for existing_node in node_objects):
                node_objects.append(Node(id=n, label=n.split(".")[0], color=color))

    # Create edges based on the recorded parent-child relationships
    for child, parent in parent_map.items():
        edge_objects.append(Edge(source=child, target=parent))

    return node_objects, edge_objects

st.set_page_config(layout="wide")  # Set the page layout to wide

st.title("Interactive Hierarchical Graph")

# Sidebar for file uploads
with st.sidebar:
    st.header("Upload Files")
    uploaded_graph_file = st.file_uploader("Choose a CSV file for the graph", type="csv")
    uploaded_metadata_file = st.file_uploader("Choose a JSON file for metadata", type="json")

# Load the graph and metadata
edges_df = load_graph_from_file(uploaded_graph_file)
metadata = load_metadata_from_file(uploaded_metadata_file)

# Select a node
selected_node = None
if not edges_df.empty:
    all_nodes = set(edges_df['child']).union(set(edges_df['parent']))
    selected_node = st.selectbox("Select a node", list(all_nodes))

if selected_node:
    node_objects, edge_objects = create_nodes_and_edges_for_parents(selected_node, edges_df, metadata)


    config = Config(
        width="100%",  # Set width to 100% to use full page width
        height=800,    # Set height to 800px
        hierarchical=True,
        physics=False,  # Disable physics for a stable layout
        direction="UD",  # Set direction to down-up
        sortMethod="directed"
    )

    # Display the graph and capture the clicked node
    clicked_node = agraph(nodes=node_objects, edges=edge_objects, config=config)

    # Sidebar for displaying selected node metadata
    st.sidebar.header("Selected Node Metadata")
    selected_node_metadata = metadata.get(selected_node, {})
    for key, value in selected_node_metadata.items():
        st.sidebar.write(f"**{key.capitalize()}**: {value}")

    # Sidebar for displaying clicked node metadata
    if clicked_node:
        st.sidebar.header("Clicked Node Metadata")
        clicked_node_metadata = metadata.get(clicked_node.split('.')[0], {})
        for key, value in clicked_node_metadata.items():
            st.sidebar.write(f"**{key.capitalize()}**: {value}")
else:
    st.write("Upload CSV files to display the graph and metadata.")
