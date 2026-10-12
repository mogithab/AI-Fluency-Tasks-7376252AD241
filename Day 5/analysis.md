# Day 5 — Serving Models Your Way

## 1. Scenario

My project is CampusHelper, a local college study assistant. It answers college-related study questions in simple English, provides small examples, and gives concise answers. The goal is to create a model with consistent default behaviour using Ollama and a Modelfile.

## 2. What is Ollama?

Ollama is a tool for running large language models locally on a computer.

Its main parts are the command-line interface (CLI), the Ollama server/API, and the model runtime that loads model weights and generates responses.

On Windows, model files are normally stored in the user's Ollama model directory, unless a different location is configured.

When I send a prompt, the client sends a request to the Ollama server. The server loads the requested model if necessary, the model processes the prompt and generates tokens, and the server returns the response.

Ollama can be accessed through terminal commands, the REST API, and an OpenAI-compatible API.

## 3. What is a Modelfile?

A Modelfile is a configuration file used to create a customized model.

My Modelfile uses:

- `FROM qwen2.5:1.5b` to select the existing base model.
- `PARAMETER temperature 0.3` to encourage more consistent responses.
- `PARAMETER num_ctx 4096` to configure the context window.
- `SYSTEM` to define the default CampusHelper behaviour.

The custom model combines the base model with its configuration and default instructions. Creating CampusHelper does not require downloading another complete copy of the model weights when the base model is already installed.

## 4. Which system prompt wins?

The system prompt supplied by the program can override the default system instruction from the Modelfile for that request.

For example, CampusHelper normally answers in simple English. My Python program supplies a different system prompt asking for pirate-style answers. I can observe whether the response follows the new instruction.

This flexibility is useful when building AI agents because the same model can perform different tasks by receiving different instructions.

## 5. REST API endpoints

The `/api/generate` endpoint accepts a prompt and generates a response.

The `/api/chat` endpoint accepts a list of messages with roles such as system, user, and assistant. It is useful for conversational applications.

The OpenAI-compatible endpoint, such as `/v1/chat/completions`, accepts a familiar chat-completion request format. It makes it easier to reuse client code when moving to another compatible inference server.

## 6. Streaming, TTFT and total time

Streaming means that the model sends parts of the answer while it is generating the response.

TTFT means Time To First Token. It measures how long a user waits before receiving the first generated text. Total time measures how long the complete request takes.

Streaming makes an answer feel faster because the user can begin reading before generation finishes. However, streaming does not necessarily reduce total generation time.

Tokens per second measures the rate of token generation. My Python script measures TTFT from the first non-empty streamed text chunk and reports the total request time.

## 7. Context window and memory

`num_ctx` controls the context window available for the prompt and generated tokens. Increasing the context window can increase KV-cache memory usage.

The KV cache stores attention key and value states for tokens already processed, reducing repeated computation during generation.

`OLLAMA_KEEP_ALIVE` controls how long a model remains loaded after a request. `OLLAMA_NUM_PARALLEL` controls the number of requests processed in parallel, subject to hardware and configuration limits.

More concurrent requests and larger context windows can require more memory.

## 8. PagedAttention and prefix caching

A simple serving method can reserve more KV-cache memory than a request actually needs, causing wasted memory and fragmentation.

PagedAttention, used by vLLM, divides KV-cache storage into fixed-size blocks and uses a block table to map tokens to physical memory blocks. This improves memory management and can allow more requests to be served.

Prefix caching can reuse previously computed state for an identical shared prompt prefix. For an agent that repeatedly sends the same long system prompt, this can reduce repeated computation when the prefix is cacheable.

## 9. Static batching and continuous batching

Static batching groups multiple requests together and processes them as a batch. A slow request can delay the completion of the batch.

Continuous batching adds new requests as existing requests finish. This can improve GPU utilization when users send requests at different times.

Throughput measures how much work is completed per second. TTFT measures the wait for the first token. TPOT means Time Per Output Token and measures the time per generated token. P95 latency is the latency below which 95% of requests finish.

Increasing batch size may improve throughput but can also increase waiting time and latency. A serving system must balance these goals.

## 10. Ollama versus vLLM

| Basis | Ollama | vLLM |
|---|---|---|
| Built for | Local development and simple model serving | High-throughput model serving for concurrent requests |
| Hardware | Can run on suitable CPUs and GPUs, depending on the model | Usually benefits from a capable GPU with sufficient VRAM |
| Multiple requests | Supports concurrent requests within resource and configuration limits | Uses continuous batching for efficient concurrent serving |
| Memory management | Straightforward local model and KV-cache management | PagedAttention improves KV-cache memory utilization |
| Setup | Simple commands, Modelfile and APIs | Requires more serving configuration |
| Choice for one user | Ollama, because it is simple for my personal study assistant | Not necessary for my small personal use case |
| Choice for 100 simultaneous users | Would require testing and resource planning | I would evaluate vLLM because it is designed for high-throughput concurrent serving |

## 11. Observations

I used CampusHelper to test study questions through the Ollama REST API. The tests include a non-streaming request, a streaming request, and an OpenAI-compatible request with a different system prompt.

I will record the actual output, TTFT, tokens per second and total time from my script. I will also run the same prompt twice and use `ollama ps` to check whether the model is loaded.

| Run | Test | Result and measurements |
|---|---|---|
| 1 | Explain an API key | Record actual answer and timings |
| 2 | Explain a prompt | Record actual answer and timings |
| 3 | Explain a stack using the pirate system prompt | Record whether the new style is followed |
| 4 | Repeat the API key prompt | Compare actual timings with Run 1 |

I expect a previously loaded model to avoid some loading overhead on a repeated request. Actual timings depend on hardware, model state, prompt length and other running processes.

## 12. Suitability and conclusion

Ollama is suitable for my CampusHelper scenario because it is easy to run locally, supports customized model behaviour through a Modelfile, and provides APIs that Python programs can use.

For a single user, this setup is sufficient for experimenting with a local study assistant. For a deployment with around 100 simultaneous users, I would evaluate vLLM or another production inference server and benchmark it on the target hardware.

PagedAttention and continuous batching help improve memory utilization and request scheduling. The final deployment choice depends on the model, available hardware, context lengths, user traffic and latency requirements.