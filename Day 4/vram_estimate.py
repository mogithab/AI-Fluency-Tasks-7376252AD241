"""
Day 4 - Model Memory Estimator

Estimates:
1. Model weights
2. KV cache
3. Total memory including 10% runtime overhead
4. Whether the model fits within the available memory
"""

# Effective bytes per parameter from the Day 4 lab
BYTES_PER_PARAM = {
    "FP16": 2.00,
    "BF16": 2.00,
    "Q8_0": 1.00,
    "Q6_K": 0.81,
    "Q5_K_M": 0.68,
    "Q4_K_M": 0.57,
    "Q3_K_M": 0.43,
}


def estimate_memory(params_b, precision, context_k, available_gb):
    """
    Estimate model memory.

    params_b      = number of parameters in billions
    precision     = quantization/precision type
    context_k     = context length in thousands of tokens
    available_gb  = available memory in GB
    """

    bytes_per_param = BYTES_PER_PARAM[precision]

    # Model weights
    weights_gb = params_b * bytes_per_param

    # Approximate KV cache
    kv_cache_gb = params_b * context_k * 0.02

    # Add 10% runtime overhead
    total_gb = (weights_gb + kv_cache_gb) * 1.10

    # Check whether model fits
    fits = total_gb <= available_gb

    return weights_gb, kv_cache_gb, total_gb, fits


def print_estimate(model, params_b, precision, context_k, available_gb):
    """Print one model estimate."""

    weights, kv_cache, total, fits = estimate_memory(
        params_b,
        precision,
        context_k,
        available_gb
    )

    print(f"\nModel: {model}")
    print(f"Parameters: {params_b}B")
    print(f"Precision: {precision}")
    print(f"Context: {context_k}K")
    print(f"Weights: {weights:.2f} GB")
    print(f"KV Cache: {kv_cache:.2f} GB")
    print(f"Total: {total:.2f} GB")
    print(f"Available Memory: {available_gb:.2f} GB")
    print(f"Fits: {'YES' if fits else 'NO'}")


if __name__ == "__main__":

    # Scenario: 8 GB available memory
    available_memory = 8.0

    print("=" * 60)
    print("DAY 4 - MODEL MEMORY ESTIMATOR")
    print("=" * 60)

    # Required model configurations
    print_estimate(
        "1.5B Small Model",
        1.5,
        "Q4_K_M",
        8,
        available_memory
    )

    print_estimate(
        "8B Mid Model - Q4_K_M",
        8,
        "Q4_K_M",
        8,
        available_memory
    )

    print_estimate(
        "8B Mid Model - FP16",
        8,
        "FP16",
        8,
        available_memory
    )

    print_estimate(
        "30B Large Model",
        30,
        "Q4_K_M",
        8,
        available_memory
    )

    print_estimate(
        "70B Server Model",
        70,
        "Q4_K_M",
        8,
        available_memory
    )

    print("\n" + "=" * 60)
    print("ESTIMATOR COMPLETE")
    print("=" * 60)