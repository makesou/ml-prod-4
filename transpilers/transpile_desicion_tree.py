import joblib
import numpy as np
import pandas as pd
import sys

def extract_tree_structure(model_path: str):
    model = joblib.load(model_path)
    tree = model.tree_
    return tree

def generate_tree_code(tree):
    np.random.seed(42)
    n_features = tree.n_features
    random_features = np.random.uniform(-10, 10, n_features)
    
    def build_node(node_id, depth=0):
        indent = "    " * (depth + 1)
        if tree.children_left[node_id] == tree.children_right[node_id]:
            return f"{indent}return {tree.value[node_id][0][1] / tree.value[node_id][0].sum():.6f}f;"
        
        feature = tree.feature[node_id]
        threshold = tree.threshold[node_id]
        left_child = tree.children_left[node_id]
        right_child = tree.children_right[node_id]
        
        left_code = build_node(left_child, depth + 1)
        right_code = build_node(right_child, depth + 1)
        
        return f"""{"" if node_id == 0 else indent}if (features[{feature}] <= {threshold:.6f}f) {{
{left_code}
{indent}}} else {{
{right_code}
{indent}}}"""
    
    tree_logic = build_node(0)
    
    c_code = f"""#include <stdio.h>

float prediction(float *features, int n_features) {{
    {tree_logic}
}}

int main() {{
    float test_data[] = {{"""
    
    feature_values = ", ".join([f"{val:.3f}f" for val in random_features])
    c_code += feature_values
    
    c_code += f"""}};
    int n_features = {n_features};
    float pred = prediction(test_data, n_features);
    printf("Prédiction: %.6f\\n", pred);
    return 0;
}}
"""
    
    return c_code

def main():
    if len(sys.argv) <= 1:
        print("Le chemin du modèle doit être spécifié")
        return
    args = sys.argv[1:]
    model_path = args[0]
    
    tree = extract_tree_structure(model_path)
    c_code = generate_tree_code(tree)
    
    filename = "model_prediction.c"
    with open(filename, 'w') as f:
        f.write(c_code)
    
    print(f"Code C sauvegardé dans: {filename}")
    
    print("\nCommande de compilation:")
    print(f"gcc -o model_prediction {filename}")
    print("./model_prediction")
    
    return c_code

if __name__ == "__main__":
    main()