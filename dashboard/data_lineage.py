from graphviz import Digraph

# Create directed graph
lineage = Digraph("DataGuard Lineage")

# Nodes
lineage.node("Producer", "Kafka Producer")
lineage.node("Kafka", "Kafka Topic: sensor-data")
lineage.node("Bronze", "Bronze Layer")
lineage.node("Silver", "Silver Layer")
lineage.node("Gold", "Gold Layer")
lineage.node("Dashboard", "Analytics Dashboard")

# Connections
lineage.edge("Producer", "Kafka")
lineage.edge("Kafka", "Bronze")
lineage.edge("Bronze", "Silver")
lineage.edge("Silver", "Gold")
lineage.edge("Gold", "Dashboard")

# Save graph
lineage.render(
    filename="dataguard_lineage",
    format="png",
    cleanup=True
)

print("Data Lineage Diagram Generated")