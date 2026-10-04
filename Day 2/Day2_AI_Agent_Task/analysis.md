# Day 2 – Reasoning and Acting: Comparing Direct Prompting, Chain-of-Thought, and ReAct

## 1. Scenario

The scenario selected for this task is a **Student Assignment and Study Planner**.

The student has three pending assignments:

| Subject | Assignment | Deadline | Status |
|---|---|---|---|
| Mathematics | Math Assignment | 25-09-2026 | Pending |
| DBMS | DBMS Assignment | 27-09-2026 | Pending |
| Artificial Intelligence | AI Assignment | 30-09-2026 | Pending |

The main question is:

**"Which assignment should I complete first, and what is the current date?"**

This scenario was selected because it contains a simple decision that requires comparing deadlines. It also contains a requirement for current information, which can demonstrate the difference between approaches that do not use tools and an approach that can use an external tool.

---

# 2. Direct Prompting

## How it works

Direct prompting gives the question to the model and asks for an answer directly.

In this implementation, the assignment information is already available to the program. No external tool is called.

## Output

The direct prompting approach selected the **Math Assignment** because it has the earliest deadline of 25-09-2026.

It also identified the order of the other assignments:

1. Math Assignment – 25-09-2026
2. DBMS Assignment – 27-09-2026
3. AI Assignment – 30-09-2026

## Tool usage

Direct prompting does not use an external tool.

Therefore, it cannot obtain new information such as the current date from an external source.

## Limitation

The main limitation is that the answer depends on the information already available to the model.

If new or external information is required, direct prompting cannot obtain it by itself.

---

# 3. Chain-of-Thought

## How it works

The Chain-of-Thought approach breaks the problem into a sequence of reasoning steps.

In this project, a simplified reasoning trace was implemented to demonstrate the decision process without exposing private model reasoning.

The main steps were:

1. Check the deadlines of all pending assignments.
2. Compare the deadlines.
3. Identify the earliest deadline.
4. Select the assignment with the earliest deadline.

## Output

The earliest deadline was identified as:

**25-09-2026 – Math Assignment**

Therefore, the Math Assignment was selected as the first assignment to complete.

## Tool usage

The Chain-of-Thought implementation does not use an external tool.

It reasons using the information already available in the program.

## Limitation

Chain-of-Thought can organize a problem into multiple reasoning steps, but it cannot obtain new external information by itself.

For example, it cannot independently retrieve the current date from an external information source unless a tool is provided.

---

# 4. ReAct Agent

## How it works

ReAct combines reasoning with actions.

The basic cycle used in this project is:

**Thought → Action → Observation → Final Answer**

The ReAct agent first identifies that it needs current information and assignment data.

It then calls the external tool:

`get_external_information()`

The tool returns:

- Current date: 23-09-2026
- Assignment information
- Deadlines
- Assignment status

The agent then uses this information to select the assignment with the earliest pending deadline.

## Tool usage

Unlike Direct Prompting and Chain-of-Thought, the ReAct agent uses an external tool.

The tool provides the current date and assignment information.

## Output

The ReAct agent produced:

**Today is 23-09-2026. Complete the Math Assignment first because it has the earliest deadline, 25-09-2026.**

## ReAct flow

```text
Thought
   ↓
Action: get_external_information()
   ↓
Observation: Current date + assignment data
   ↓
Reason using the obtained information
   ↓
Final Answer