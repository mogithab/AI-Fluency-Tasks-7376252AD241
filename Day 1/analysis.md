# Day 1 - Chatbot vs Rule-Based Workflow vs AI Agent

## 1. Scenario

The chosen scenario is a Student Private Data Assistant.

The private data contains student marks, assignment status, and assignment deadlines. The same question is tested using a plain chatbot, a rule-based workflow, and an AI agent.

## 2. Plain Chatbot

The plain chatbot mainly provides a response without accessing the student's private data.

When asked about the Mathematics assignment deadline, it cannot reliably provide the private information because the data is not available to it.

The main limitation is that it does not have access to the private student data.

## 3. Rule-Based Workflow

The rule-based workflow uses predefined Python conditions.

When the question contains the words "Mathematics" and "deadline", the workflow returns the Mathematics assignment deadline.

It does not use an LLM. It follows predefined rules.

The workflow is reliable when the question matches an existing rule. However, it is rigid and may fail when the user asks a question in a different way that has not been included in the rules.

## 4. AI Agent

The AI agent uses a tool to read the private student data.

It follows multiple steps: understanding the question, using the private-data tool, observing the result, finding the required information, and producing the final answer.

This makes the agent useful for tasks that require private-data access and multiple steps.

## 5. Comparison Table

| Basis                    | Plain Chatbot                    | Rule-Based Workflow       | AI Agent                       |
| ------------------------ | -------------------------------- | ------------------------- | ------------------------------ |
| Flexibility              | High                             | Low                       | High                           |
| Decision-making          | LLM response                     | Predefined conditions     | Tool selection and reasoning   |
| Tool usage               | None                             | Fixed program logic       | Private-data tool              |
| Private-data access      | No                               | Yes                       | Yes                            |
| Multi-step task handling | Limited                          | Fixed steps               | Multiple steps                 |
| Automation               | Medium                           | High for known rules      | High                           |
| Reliability              | Depends on available information | High for predefined cases | Depends on reasoning and tools |

## 6. Suitability Analysis

For this student private-data scenario, the AI agent is suitable when the task requires private-data access and multiple steps.

The plain chatbot is useful for general questions but cannot directly access the student's private information.

The rule-based workflow is reliable for known questions but is rigid because it depends on predefined conditions.

The AI agent can combine reasoning with tool usage and private-data access.

## 7. Conclusion

A plain chatbot is appropriate for general conversation and questions that do not require private information.

A rule-based workflow is appropriate when the task is predictable and its conditions can be clearly defined.

An AI agent is appropriate when a problem requires reasoning, tools, private-data access, and multiple steps.

The appropriate approach depends on the problem, required data access, flexibility, and reliability.
