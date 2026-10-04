\# Day 4 – Will It Fit, and May I Use It?



\## Scenario



My scenario is running an open language model locally on my Windows laptop for personal AI-assistant and AI-agent learning. The model should be able to answer questions and support simple local AI tasks without depending completely on cloud services.



My computer has approximately 4 GB of dedicated NVIDIA GPU VRAM. I use approximately 3.6 GB as the practical GPU memory budget for the scenario. The purpose is personal learning and experimentation.



The memory decision is based on model weights, KV cache and runtime overhead. The permission decision is based on the exact licence and its conditions.



Date checked for model cards and licence information: \*\*2026-10-04\*\*.



\---



\# 3.1 Explanation of the Concepts



\## Model Weights



Model weights are the numerical values learned during model training. They form the main part of the model's memory requirement. The number of parameters and the precision used determine the approximate size of the weights.



For example, using the Day 4 estimation formula, a 1.5B model at Q4\_K\_M uses approximately:



\*\*1.5 × 0.57 = 0.855 GB\*\*



of weight memory.



A larger model needs more memory. Therefore, model size is one of the first things I should check before downloading a model.



If model weights are ignored, I may choose a model that cannot fit into the available GPU memory. In my scenario, an 8B Q4\_K\_M model is estimated at about 4.56 GB just for weights, which already exceeds my practical 3.6 GB GPU budget.



The limitation is that the weight calculation is only an estimate. Actual runtime memory also contains KV cache and other runtime requirements.



\## Quantization



Quantization stores model parameters using fewer bytes per parameter. This reduces memory requirements and makes larger models easier to run locally, although lower precision can involve some quality trade-offs.



The Day 4 lab uses these approximate bytes-per-parameter values:



| Precision   | Bytes per parameter |

| ----------- | ------------------: |

| FP16 / BF16 |                2.00 |

| Q8\_0        |                1.00 |

| Q6\_K        |                0.81 |

| Q5\_K\_M      |                0.68 |

| Q4\_K\_M      |                0.57 |

| Q3\_K\_M      |                0.43 |



For my 1.5B model at 8K context, FP16 requires an estimated 3.56 GB total, while Q4\_K\_M requires approximately 1.20 GB.



Therefore, quantization is important in my scenario because it can make the difference between a model fitting or not fitting.



If quantization is ignored, I may select an FP16 model that exceeds my available memory even though a quantized version of the same model fits.



\## KV Cache and Context Length



The KV cache stores information needed by the model while processing the current context. Its memory requirement increases as the context length increases.



The Day 4 approximation is:



\*\*KV cache (GB) = parameters in billions × context in K tokens × 0.02\*\*



Unlike the weights, which stay constant when only the context length changes, the KV cache increases with context.



For my 1.5B Q4\_K\_M model:



\* 2K context → 0.06 GB KV cache

\* 4K context → 0.12 GB

\* 8K context → 0.24 GB

\* 16K context → 0.48 GB

\* 32K context → 0.96 GB



This shows why a model that fits at a short context can require more memory at a longer context. This is especially relevant for an AI agent because a long conversation or many tool results can increase the amount of context being processed.



If context length is ignored, I may underestimate memory requirements.



The limitation is that this KV calculation is an approximation. Actual runtime memory depends on architecture, attention implementation, runtime settings and other factors.



\## Model Card



A model card is the documentation provided for a model. It contains information such as the model name, publisher, capabilities, licence and usage information.



I used model cards when checking the three models in my comparison. The model card is important not only for technical information but also for understanding the conditions under which a model can be used.



If the model card is ignored, I may misunderstand the model's capabilities or licence.



\## Open-Weight vs Open-Source Licensing



Open-weight means that the model weights are available, but it does not automatically mean that the model is released under a conventional open-source software licence.



The exact licence must be checked before using a model for a particular purpose. Different models can have different conditions for commercial use, redistribution and other activities.



For example, Qwen2.5-1.5B-Instruct and Mistral-7B-Instruct-v0.3 are listed under Apache 2.0, while Gemma 3 uses Google's Gemma Terms of Use.



Therefore, model size alone is not enough to choose a model. I must also check whether its licence permits my intended use.



\---



\# 3.2 Estimate Table and Model Comparison



\## 3.2(a) Memory Estimate Table



The following estimates use the Day 4 formula:



\*\*Weights = Parameters × bytes per parameter\*\*



\*\*KV cache = Parameters × Context(K) × 0.02\*\*



\*\*Total = (Weights + KV cache) × 1.10\*\*



My practical scenario memory budget is \*\*3.6 GB GPU VRAM\*\*.



| Model            | Params (B) | Precision | Context (K) | Weights (GB) | KV Cache (GB) | Total (GB) | Fits in 3.6 GB? |

| ---------------- | ---------: | --------- | ----------: | -----------: | ------------: | ---------: | --------------- |

| 1.5B Small Model |        1.5 | Q4\_K\_M    |           8 |         0.85 |          0.24 |       1.20 | YES             |

| 8B Mid Model     |          8 | Q4\_K\_M    |           8 |         4.56 |          1.28 |       6.42 | NO              |

| 8B Mid Model     |          8 | FP16      |           8 |        16.00 |          1.28 |      19.01 | NO              |

| 30B Large Model  |         30 | Q4\_K\_M    |           8 |        17.10 |          4.80 |      24.09 | NO              |

| 70B Server Model |         70 | Q4\_K\_M    |           8 |        39.90 |         11.20 |      56.21 | NO              |



The estimator was first run using the 8 GB reference budget from the lab. The calculations themselves are unchanged when applying the results to my 3.6 GB practical GPU budget. The important conclusion for my actual scenario is that the 1.5B Q4\_K\_M model fits, while the 8B Q4\_K\_M model does not.



\## 3.2(b) Open Model Comparison



I compared three different model families using their model cards and Ollama pages.



| Basis                       | Qwen2.5-1.5B-Instruct                                      | Mistral-7B-Instruct-v0.3                   | Gemma 3 1B                                                    |

| --------------------------- | ---------------------------------------------------------- | ------------------------------------------ | ------------------------------------------------------------- |

| Publisher                   | Qwen / Alibaba                                             | Mistral AI                                 | Google                                                        |

| Parameters                  | 1.54B                                                      | 7B                                         | 1B                                                            |

| MoE?                        | No                                                         | No                                         | No                                                            |

| Context window              | 32K on the Ollama build                                    | 32K                                        | 32K                                                           |

| Exact licence               | Apache 2.0                                                 | Apache 2.0                                 | Gemma Terms of Use                                            |

| Commercial use              | Permitted subject to Apache 2.0 terms                      | Permitted subject to Apache 2.0 terms      | Subject to Gemma Terms                                        |

| Extra conditions            | Apache 2.0 conditions                                      | Apache 2.0 conditions                      | Must follow Gemma Terms of Use                                |

| Tool calling stated on card | Not treated as a confirmed requirement for this comparison | Yes, function calling is explicitly stated | Not treated as confirmed from the checked model-card evidence |

| GGUF / Ollama build         | Yes                                                        | Yes                                        | Yes                                                           |

| Q4 Ollama size              | 986 MB                                                     | 4.4 GB                                     | 815 MB                                                        |

| Own 8K Q4\_K\_M estimate      | About 1.23 GB                                              | About 5.62 GB                              | About 0.80 GB                                                 |

| Fits 3.6 GB scenario?       | YES                                                        | NO                                         | YES                                                           |

| Date checked                | 2026-10-04                                                 | 2026-10-04                                 | 2026-10-04                                                    |



The official Qwen model card lists the Qwen2.5-1.5B-Instruct model under Apache 2.0.



The Mistral model card lists Apache 2.0 and explicitly states that Mistral-7B-Instruct-v0.3 supports function calling. The Ollama page lists the model as 4.4 GB with a 32K context window and also identifies v0.3 as the function-calling version.



The Ollama pages were also used to record the available local builds and their displayed download sizes.



\---



\# 3.3 Context Length and Quantization Observation



I selected the 1.5B model and first kept Q4\_K\_M fixed while changing the context length.



\## Context Length Comparison



| Context | Weights (GB) | KV Cache (GB) | Total (GB) | Fits 3.6 GB? |

| ------: | -----------: | ------------: | ---------: | ------------ |

|      2K |         0.85 |          0.06 |       1.01 | YES          |

|      4K |         0.85 |          0.12 |       1.07 | YES          |

|      8K |         0.85 |          0.24 |       1.20 | YES          |

|     16K |         0.85 |          0.48 |       1.47 | YES          |

|     32K |         0.85 |          0.96 |       2.00 | YES          |



When context length increased, the model weights did not change. The KV cache increased because KV memory depends on context length. Therefore, the total memory requirement also increased.



In my tested range, the largest context was \*\*32K\*\*, and it still fitted within the 3.6 GB estimated memory budget at Q4\_K\_M. The Ollama build used in the comparison is listed with a 32K context window, so 32K is also the relevant maximum displayed for that build.



\## Quantization Comparison



I then kept the context fixed at 8K and changed the quantization.



| Quantization | Weights (GB) | KV Cache (GB) | Total (GB) | Fits 3.6 GB? |

| ------------ | -----------: | ------------: | ---------: | ------------ |

| FP16         |         3.00 |          0.24 |       3.56 | YES          |

| Q8\_0         |         1.50 |          0.24 |       1.91 | YES          |

| Q6\_K         |         1.22 |          0.24 |       1.60 | YES          |

| Q5\_K\_M       |         1.02 |          0.24 |       1.39 | YES          |

| Q4\_K\_M       |         0.85 |          0.24 |       1.20 | YES          |

| Q3\_K\_M       |         0.65 |          0.24 |       0.97 | YES          |



When quantization changed, the weights changed but the KV cache stayed at 0.24 GB because the model size and context length were fixed.



I would choose \*\*Q4\_K\_M\*\* for this scenario because it gives a large reduction in memory compared with FP16 while retaining a practical model size. The trade-off is that lower-precision quantization can reduce model quality compared with higher precision. Q3\_K\_M saves even more memory, but I would prefer Q4\_K\_M as a balanced choice.



\---



\# 3.4 Estimate Versus Reality



I used my locally installed Qwen2.5-1.5B model for the real-world comparison.



| Model        | Ollama list size | Ollama ps size | Processor | Context | Estimate                               |

| ------------ | ---------------: | -------------: | --------- | ------: | -------------------------------------- |

| qwen2.5:1.5b |           986 MB |         1.2 GB | 100% GPU  |    4096 | Weights: 0.85 GB; Total at 8K: 1.20 GB |



The estimate is close to the observed Ollama runtime value. My estimator predicts approximately \*\*1.20 GB total at 8K\*\*, while `ollama ps` reported \*\*1.2 GB\*\* when the model was running.



The values are not expected to be identical in every situation because the estimator is an approximation. Actual runtime memory can depend on the context actually loaded, runtime overhead, architecture and implementation details.



The `ollama list` size of 986 MB is different from the `ollama ps` runtime size of 1.2 GB because the first represents the stored model/build size, while the second represents the model while it is loaded for execution.



The processor field reported \*\*100% GPU\*\*, showing that this model was running entirely on the GPU rather than being split between CPU and GPU.



The actual runtime context reported by Ollama was \*\*4096 tokens\*\*. This is important because the estimator comparison above used an 8K context. A different loaded context can affect runtime memory.



\---



\# 3.5 Suitability Analysis



For my resource-constrained local AI-assistant scenario, I recommend \*\*Qwen2.5-1.5B-Instruct with Q4\_K\_M at a 4K or 8K working context\*\*. The Ollama build is approximately 986 MB, and my 8K memory estimate is approximately 1.23 GB using the model's approximately 1.54B parameter count. It comfortably fits within my practical 3.6 GB GPU budget. The model is listed under Apache 2.0, which provides a clear open-source licensing basis subject to its conditions.



My actual installation also supports this conclusion: `ollama list` reported 986 MB and `ollama ps` reported 1.2 GB while using 100% GPU.



My runner-up is \*\*Gemma 3 1B\*\* because it has a very small Ollama Q4 build and a low estimated memory requirement. However, I would choose Qwen2.5-1.5B as the main recommendation because its Apache 2.0 licence is straightforward for my intended learning scenario, while Gemma is governed by Google's Gemma Terms of Use.



\*\*Mistral-7B-Instruct-v0.3\*\* would become more attractive if my scenario changed to provide substantially more GPU memory or if function calling became a major requirement. Its model card explicitly states function-calling support, but its estimated 8K Q4\_K\_M memory requirement is about 5.62 GB, which exceeds my practical 3.6 GB GPU budget.



If I had more GPU memory, I could choose a larger model such as Mistral 7B. If my scenario required a longer context, I would need to consider the additional KV-cache memory. If the model were intended for a commercial or public release, I would also need to review the exact licence and conditions before making the final choice.



\---



\# 3.6 Conclusion



Choosing a local open model requires looking at both technical fit and permission to use the model. Model size is the most important factor when hardware memory is limited. A large model may provide stronger capabilities, but it cannot be used comfortably if its memory requirement exceeds the available hardware.



Quantization is useful when the full-precision model is too large. Moving from FP16 to Q4\_K\_M greatly reduced the estimated weight memory in my experiment. The trade-off is that lower precision can affect model quality, so the smallest possible quantization is not automatically the best choice.



Context length becomes important when applications maintain long conversations or accumulate many tool results. The weights remain fixed, but the KV cache grows with context length. Therefore, a model that fits at 4K or 8K context may require substantially more memory at a longer context.



Licence becomes the deciding factor when the model will be distributed, used commercially or incorporated into a public product. Two models with similar memory requirements may have different permissions and conditions. Open-weight availability alone should not be treated as proof that every type of use is permitted.



For example, in my own scenario, \*\*memory decides the choice\*\* because Mistral-7B-Instruct-v0.3 is estimated at about 5.62 GB at Q4\_K\_M and 8K context, which exceeds my practical 3.6 GB GPU budget. In a different scenario where memory is sufficient but a model is being released commercially, \*\*licence can become the deciding factor\*\*.



Overall, the correct workflow is to estimate memory before downloading a model, check how context and quantization affect the estimate, compare the estimate with actual runtime behaviour, and finally check the exact model licence and its conditions. This allows a model to be selected based on both whether it will fit and whether it may be used for the intended purpose.



