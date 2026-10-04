# Day 3 – LLM, Tools and Agents Analysis

## 1. What is an LLM?

An LLM (Large Language Model) is a model that understands and generates human-like text.

An LLM can answer questions using the information learned during training. However, it may not always have access to external or current information. It can also make mistakes or generate an incorrect answer when it does not have enough reliable information.

In this task, the no-tool program answers simple questions without using an external tool.

---

## 2. What is an Agent?

An agent is a system that can use an LLM together with tools to complete a task.

A plain LLM mainly generates an answer from the information available to it. An agent can decide to use a tool, receive the tool result, and then use that result to produce the final answer.

In this task, the tool-enabled agent uses the course-fee tool and calculator to find the total fee and apply the scholarship.

---

## 3. What is a Tool and Tool Call?

A tool is an external function that performs a specific task for the agent.

Examples in this project are:

- `get_course_fee()` – retrieves a course fee.
- `calculator()` – performs a mathematical calculation.

A tool call is the process of requesting a tool to perform an operation.

For example:

```text
get_course_fee("CS101")