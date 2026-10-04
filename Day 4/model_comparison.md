\# Day 4 - Open Model Comparison



Date checked: 2026-10-04



\## Scenario



The scenario is local model inference on a resource-constrained personal computer.

The main goal is to run an AI assistant locally while keeping memory usage within

the available hardware budget.



\## Model Comparison



| Model | Family / Publisher | Parameters | Context | Exact Licence | Commercial Use | Tool Calling | Ollama Q4 Size | Own 8K Q4\_K\_M Estimate | Fits 8 GB? |

|---|---|---:|---:|---|---|---|---:|---:|---|

| Qwen2.5-1.5B-Instruct | Qwen / Alibaba | 1.54B | 128K | Apache 2.0 | Yes, subject to Apache 2.0 terms | Check model card | 986 MB | 1.23 GB | YES |

| Mistral-7B-Instruct-v0.3 | Mistral AI | 7B | 32K | Apache 2.0 | Yes, subject to Apache 2.0 terms | Yes | 4.4 GB | 5.62 GB | YES |

| Gemma 3 1B | Google | 1B | 32K | Gemma Terms of Use | Subject to Gemma Terms | Check model card | 815 MB | 0.80 GB | YES |



\## Qwen2.5-1.5B-Instruct



Qwen2.5-1.5B-Instruct belongs to the Qwen family and is published by

Alibaba/Qwen. The official model page lists the model under the Apache 2.0

license. The Ollama page identifies the 1.5B model as approximately 1.54B

parameters and Q4\_K\_M, with a download size of 986 MB. Ollama lists support

for up to 128K tokens.



For this assignment, the estimated memory at 8K context and Q4\_K\_M is

approximately 1.23 GB using the Day 4 estimation formula.



\## Mistral-7B-Instruct-v0.3



Mistral-7B-Instruct-v0.3 belongs to the Mistral family and is published by

Mistral AI. The official model card lists Apache 2.0. The model card also

states that the model supports function calling.



The official Ollama page lists the Mistral 7B v0.3 model at approximately

4.4 GB with a 32K context window.



Using the Day 4 estimation formula for 7B, Q4\_K\_M and 8K context gives an

estimated total of approximately 5.62 GB.



\## Gemma 3 1B



Gemma 3 1B belongs to Google's Gemma family. The official Ollama page lists

the 1B model at 815 MB, Q4\_K\_M, with a 32K context window. The licence shown

on the Ollama page is the Gemma Terms of Use rather than Apache 2.0.



Using the Day 4 estimation formula for 1B, Q4\_K\_M and 8K context gives an

estimated total of approximately 0.80 GB.



\## Recommendation



For this resource-constrained local scenario, Qwen2.5-1.5B-Instruct is the

main recommendation because it provides a small memory footprint while

supporting a large maximum context window and using the Apache 2.0 license.



Gemma 3 1B is a strong alternative because it is even smaller, but its

licensing is governed by Google's Gemma Terms of Use rather than Apache 2.0.



Mistral-7B-Instruct-v0.3 is the runner-up for cases where the larger model

capability and function-calling support are more important. However, its

larger memory requirement makes it less suitable for a resource-constrained

machine.



\## Important Note



The memory values in this document are estimates based on the Day 4 lab

formula. Actual Ollama runtime memory can differ because of runtime overhead,

context actually loaded, architecture details, and other implementation

factors.

