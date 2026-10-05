\# Day 6 – Fault Injection and Observation Table



| Fault | What the model produced | Expected behavior | Agent recovered? |

|---|---|---|---|

| Invalid JSON | Malformed JSON for calculator | Return validation error and continue | Yes |

| Unknown tool | `does\_not\_exist` | Report unknown tool | Yes |

| Missing argument | Missing `course\_code` | Report missing required argument | Yes |

| Wrong type | `course\_code` as integer | Report type error | Yes |

| Invalid enum | `semester = summer` | Report invalid enum value | Yes |

| Extra argument | `year = 2026` | Reject unexpected argument | Yes |

| Empty arguments | Empty JSON | Report missing `expression` | Yes |

| Wrong JSON type | Arguments as array | Require JSON object | Yes |

| Wrong tool capitalization | `GET\_COURSE\_FEE` | Report unknown tool | Yes |

| Arguments is JSON array | Array instead of object | Reject invalid argument structure | Yes |



\## Additional observations



1\. The agent successfully handled multiple tool calls in one step.

2\. The calculator executed valid expressions safely.

3\. Invalid tool calls returned recoverable error messages instead of crashing.

4\. Structured output successfully produced JSON object and strict JSON schema responses.

5\. The model can still generate an incorrect tool argument or expression even when the tool itself works correctly.

