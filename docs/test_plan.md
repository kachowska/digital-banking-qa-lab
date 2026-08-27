# Test Plan

## Objective
Validate core online-banking behavior with emphasis on business-critical money movement and account data.

## In scope
- login and basic navigation
- customer/account retrieval
- transfers and bill payments
- transaction-history retrieval
- loan-request API behavior
- input validation and negative paths
- basic accessibility checks
- support/log investigation practice

## Out of scope
- performance/load testing
- production security assessment
- real customer data
- destructive database administration operations against the public instance

## Test types
- smoke
- functional
- negative
- regression
- exploratory
- API
- basic accessibility

## Entry criteria
- ParaBank public UI reachable
- API documentation reachable
- test data/credentials available from the demo documentation when needed

## Exit criteria
- all critical smoke cases executed
- no unresolved Critical/High defect in money-transfer/account-access scenarios
- regression suite updated after changes
- defects contain steps, expected/actual result, environment and evidence reference

## Severity model
- Critical: money/account integrity or total blocker
- High: core banking flow broken with no reasonable workaround
- Medium: functional issue with workaround or limited scope
- Low: cosmetic/usability/documentation issue

## Risks
1. Shared public demo data may change between executions.
2. Public environment can be reset by other users.
3. UI and REST endpoints may expose different data formats/configuration.
4. Some database-level assertions require internal DB access and are therefore represented as SQL verification exercises.
