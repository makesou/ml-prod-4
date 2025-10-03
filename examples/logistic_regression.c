#include <stdio.h>
#include <math.h>

float prediction(float *features, int n_features) {
    float result = -3.080764f;
    result += 0.003662f * features[0];
    result += 0.404739f * features[1];
    result += 2.471996f * features[2];
    return 1.0f / (1.0f + expf(-result));
}

int main() {
    float test_data[] = {-2.509f, 9.014f, 4.640f};
    int n_features = 3;
    float pred = prediction(test_data, n_features);
    printf("Prédiction: %.6f\n", pred);
    return 0;
}
