# Agentic AI – Day 1 Practice Task

## Comparing a Plain Chatbot, Rule-Based Workflow, and AI Agent

This project demonstrates how the same private-data problem can be handled using three different approaches:

1. Plain Chatbot
2. Rule-Based Workflow
3. AI Agent

The project is based on a student private-data scenario containing marks, assignment status, and assignment deadlines.

---

## 🎯 Objective

The main objective is to understand the difference between:

* A chatbot that provides responses without accessing private data.
* A rule-based workflow that follows predefined conditions.
* An AI agent that uses tools and multiple steps to access and process private information.

The task demonstrates the concepts of flexibility, decision-making, private-data access, tool usage, automation, and reliability.

---

## 📌 Scenario

The project uses private student information such as:

* Student name
* Department
* Subject marks
* Assignment status
* Assignment deadlines

Example question:

> What is my Mathematics deadline?

The answer is:

**25 September 2026**

---

## 🤖 1. Plain Chatbot

The plain chatbot provides a general response without accessing the student's private data.

### File

```text
chatbot.py
```

### Limitation

The chatbot cannot reliably answer questions about private student information because the private data is not directly available to it.

---

## ⚙️ 2. Rule-Based Workflow

The rule-based workflow uses predefined Python conditions.

For example:

```text
If the question contains "Mathematics" and "deadline",
return the Mathematics assignment deadline.
```

### File

```text
workflow.py
```

### Limitation

The workflow is reliable for predefined questions but can be rigid when the user asks a question in a different way.

---

## 🧠 3. AI Agent

The AI agent uses a private-data tool to read the student's information.

It follows multiple steps:

```text
Understand the question
        ↓
Use the private-data tool
        ↓
Observe the data
        ↓
Find the required information
        ↓
Generate the final answer
```

### File

```text
agent.py
```

### Advantage

The agent demonstrates how tool usage and multiple steps can be used to handle private-data tasks.

---

## 📊 Comparison

| Feature             | Plain Chatbot                    | Rule-Based Workflow       | AI Agent                     |
| ------------------- | -------------------------------- | ------------------------- | ---------------------------- |
| Flexibility         | High                             | Low                       | High                         |
| Decision-making     | LLM response                     | Predefined conditions     | Tool selection and reasoning |
| Tool usage          | None                             | Fixed program logic       | Private-data tool            |
| Private-data access | No                               | Yes                       | Yes                          |
| Multi-step handling | Limited                          | Fixed                     | Multiple steps               |
| Automation          | Medium                           | High for known rules      | High                         |
| Reliability         | Depends on available information | High for predefined cases | Depends on reasoning an      |
