import joblib
import numpy as np
import pandas as pd
import sys
import math

def extract_model_coefficients(model_path: str):
    model = joblib.load(model_path)
    coefficients = model.coef_[0]
    intercept = model.intercept_[0]
    return coefficients, intercept

def generate_c_code(coefficients, intercept):
    np.random.seed(42)
    n_features = len(coefficients)
    
    random_features = np.random.uniform(-10, 10, n_features)
    
    c_code = f"""#include <stdio.h>
#include <math.h>

float prediction(float *features, int n_features) {{
    float result = {intercept:.6f}f;
"""
    
    for i, coef in enumerate(coefficients):
        c_code += f"    result += {coef:.6f}f * features[{i}];\n"
    
    c_code += f"""    return 1.0f / (1.0f + expf(-result));
}}

int main() {{
    float test_data[] = {{"""
    feature_values = ", ".join([f"{val:.3f}f" for val in random_features])
    c_code += feature_values
    
    c_code += f"""}};
    int n_features = {n_features};
    float pred = prediction(test_data, n_features);
    printf("Prédiction: %.6f\\n", pred);"""
    c_code += """
    return 0;
}
"""
    
    return c_code

def main():
    if len(sys.argv) <= 1:
        print("Le chemin du modèle doit être spécifié")
        return
    args = sys.argv[1:]
    model_path = args[0]
    
    coefficients, intercept = extract_model_coefficients(model_path)
    c_code = generate_c_code(coefficients, intercept)
    
    filename = "model_prediction.c"
    with open(filename, 'w') as f:
        f.write(c_code)
    
    print(f"Code C sauvegardé dans: {filename}")
    
    print("\nCommande de compilation:")
    print(f"gcc -o model_prediction {filename} -lm")
    print("./model_prediction")
    
    return c_code

if __name__ == "__main__":
    main()