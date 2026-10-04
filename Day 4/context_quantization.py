"""
Day 4 - Context Length and Quantization Comparison

Uses the Day 4 lab memory-estimation formula:
Weights = Parameters x Bytes per Parameter
KV Cache = Parameters x Context(K) x 0.02
Total = (Weights + KV Cache) x 1.10
"""

BYTES_PER_PARAM = {
    "FP16": 2.00,
    "Q8_0": 1.00,
    "Q6_K": 0.81,
    "Q5_K_M": 0.68,
    "Q4_K_M": 0.57,
    "Q3_K_M": 0.43,
}


def estimate_memory(params_b, precision, context_k):
    weights = params_b * BYTES_PER_PARAM[precision]
    kv_cache = params_b * context_k * 0.02
    total = (weights + kv_cache) * 1.10

    return weights, kv_cache, total


def print_result(params_b, precision, context_k, available_memory):
    weights, kv, total = estimate_memory(
        params_b,
        precision,
        context_k
    )

    fits = total <= available_memory

    print(
        f"{precision:<8} "
        f"{context_k:>5}K   "
        f"Weights: {weights:>6.2f} GB   "
        f"KV: {kv:>6.2f} GB   "
        f"Total: {total:>6.2f} GB   "
        f"Fits: {'YES' if fits else 'NO'}"
    )


if __name__ == "__main__":

    # Scenario
    params = 1.5
    available_memory = 8.0

    print("=" * 75)
    print("DAY 4 - CONTEXT LENGTH AND QUANTIZATION COMPARISON")
    print("=" * 75)

    # ---------------------------------------------------------
    # PART 1: Context length comparison
    # Fixed model: 1.5B
    # Fixed quantization: Q4_K_M
    # ---------------------------------------------------------

    print("\nPART 1 - CONTEXT LENGTH COMPARISON")
    print("Model: 1.5B")
    print("Fixed Quantization: Q4_K_M")
    print("-" * 75)

    for context in [2, 4, 8, 16, 32]:
        print_result(
            params,
            "Q4_K_M",
            context,
            available_memory
        )

    # ---------------------------------------------------------
    # PART 2: Quantization comparison
    # Fixed model: 1.5B
    # Fixed context: 8K
    # ---------------------------------------------------------

    print("\nPART 2 - QUANTIZATION COMPARISON")
    print("Model: 1.5B")
    print("Fixed Context: 8K")
    print("-" * 75)

    for precision in [
        "FP16",
        "Q8_0",
        "Q6_K",
        "Q5_K_M",
        "Q4_K_M",
        "Q3_K_M"
    ]:
        print_result(
            params,
            precision,
            8,
            available_memory
        )

    print("\n" + "=" * 75)
    print("COMPARISON COMPLETE")
    print("=" * 75)