# Flow Specification

For every FLOW-ID:

## Identity
- Name:
- Actor:
- User goal:
- Trigger:
- Entry node:
- Terminal node:
- Preconditions:
- Capability IDs:

## Main path
| Step | Node ID | User/system event | Condition | Next node | Observable result |
|---|---|---|---|---|---|

## Alternate paths and recovery
| Branch ID | Condition | Path | Recovery/resume | Completion or exit |
|---|---|---|---|---|

## Completion
- Success condition:
- Failure/abandon condition:
- Data or progress preservation expectation:
- Observable user outcome:
- Open questions / approved Decision IDs:

## Flow graph validation
- Entry node exists:
- Terminal node exists:
- All referenced nodes exist:
- Reachability traversal evidence:
- Unreachable nodes / orphan branches:
- Result: PASS / FAIL / NOT_VERIFIED
