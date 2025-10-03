#include <stdio.h>

float prediction(float *features, int n_features) {
    if (features[2] <= 0.500000f) {
        return 0.000000f;
    } else {
        if (features[0] <= 87.008522f) {
            return 0.000000f;
        } else {
            if (features[1] <= 1.500000f) {
                return 0.500000f;
            } else {
                return 0.894737f;
            }
        }
    }
}

int main() {
    float test_data[] = {-2.509f, 9.014f, 4.640f};
    int n_features = 3;
    float pred = prediction(test_data, n_features);
    printf("Prédiction: %.6f\n", pred);
    return 0;
}
