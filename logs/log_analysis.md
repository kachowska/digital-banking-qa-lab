# Log Analysis Practice

The included log file is synthetic and exists only for QA/support practice.

## Investigation example
Ticket: transfer to target account failed around 08:42 with HTTP 500.

Search by correlation ID first, then reconstruct the request timeline. In the sample, `7c91` passes request validation but fails at the database stage with `TARGET_ACCOUNT_NOT_FOUND`. A tester should compare this behavior with the expected API contract: invalid account input should normally produce a controlled client error rather than an unhandled 500.

## Kibana KQL examples
```text
level : "ERROR"
endpoint : "/transfer" and level : "ERROR"
correlationId : "7c91"
endpoint : "/transfer" and status >= 500
```

## Splunk SPL examples
```text
index=banking endpoint="/transfer" level="ERROR"
index=banking correlationId="7c91" | sort _time
index=banking endpoint="/transfer" status>=500 | stats count by error
```

## What to record in a support ticket
- timestamp / timezone
- environment
- account/customer identifiers appropriate for the test environment
- correlation/request ID
- expected vs actual behavior
- reproducibility
- affected layer (UI/API/database/external integration) if known
- relevant log excerpt without secrets
