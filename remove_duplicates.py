def process_graph_file(input_file, output_file):
    """
    Convert graph file to <node1> <node2> <weight> format,
    remove duplicates, and remove self-edges.
    
    Args:
    input_file (str): Path to the input graph file
    output_file (str): Path to the output graph file with weights and unique edges
    """
    # Use a set to keep track of unique edges
    unique_edges = set()
    
    # Counters for tracking
    total_lines = 0
    self_edges_count = 0
    duplicate_edges_count = 0
    
    # Read the input file and process edges
    with open(input_file, 'r') as f:
        # Read all lines from the file
        lines = f.readlines()
    
    # Process and deduplicate edges
    with open(output_file, 'w') as f:
        for line in lines:
            # Strip whitespace and split the line into nodes and weight
            parts = line.strip().split()
            
            # Ensure we have exactly three parts (source, target, weight)
            if len(parts) != 3:
                print(f"Skipping invalid line: {line.strip()}")
                continue
            
            # Increment total lines processed
            total_lines += 1
            
            # Convert to integers
            source = int(parts[0])
            target = int(parts[1])
            weight = int(parts[2])
            
            # Skip self-edges
            if source == target:
                self_edges_count += 1
                continue
            
            # Create a tuple of nodes to handle directed graph edges
            edge = (source, target)
            
            # Write the edge only if it's unique
            if edge not in unique_edges:
                unique_edges.add(edge)
                # Write in format: node1 node2 weight
                f.write(f"{source} {target} {weight}\n")
            else:
                duplicate_edges_count += 1
    
    # Print processing statistics
    print(f"Total lines processed: {total_lines}")
    print(f"Self-edges removed: {self_edges_count}")
    print(f"Duplicate edges removed: {duplicate_edges_count}")
    print(f"Wrote {len(unique_edges)} unique edges to {output_file}")

# Process the Twitter graph file
input_file = 'lfr_directed_1.txt'
output_file = 'lfr_directed_1_cleaned.txt'

# Process the graph file
process_graph_file(input_file, output_file)
