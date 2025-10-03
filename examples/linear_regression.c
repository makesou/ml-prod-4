#include <stdio.h>

float prediction(float *features, int n_features) {
    float result = -8152.937710f;
    result += 717.258370f * features[0];
    result += 36824.195974f * features[1];
    result += 101571.840022f * features[2];
    return result;
}

int main() {
    float test_data[] = {-2.509f, 9.014f, 4.640f};
    int n_features = 3;
    float pred = prediction(test_data, n_features);
    printf("Prédiction: %.6f\n", pred);

    return 0;
}
