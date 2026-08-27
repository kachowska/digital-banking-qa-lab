# Digital Banking QA Lab — Manual & API Testing

Portfolio QA project built around **ParaBank**, Parasoft's public online-banking demo application and REST API.

The goal is to demonstrate practical junior manual-testing work: turning requirements and product behavior into test scenarios, maintaining a regression pack, validating REST APIs with Postman, checking data with SQL, documenting defects in a Jira-style format, and investigating application logs.

## Application under test

- Web UI: https://parabank.parasoft.com/parabank/index.htm
- REST API / Swagger: https://parabank.parasoft.com/parabankv2/api-docs/index.html
- Service documentation: https://parabank.parasoft.com/parabank/services.htm
- Admin / data-access modes: https://parabank.parasoft.com/parabank/admin.htm

ParaBank exposes banking flows such as login, account access, transfers, bill payment, customer updates and loan requests. Its REST API documents account, customer, transaction and loan operations.

## What is included

- manual functional and negative test cases
- smoke + regression suite
- requirements-to-test traceability matrix
- Postman collection/environment for REST checks
- SQL verification exercises for account/transaction data
- Jira-style defect/support tickets
- structured log-analysis exercise with Kibana KQL and Splunk SPL examples
- WCAG 2.0 desktop/mobile checklist
- execution/reconnaissance report based on the public application and official API documentation

## QA workflow

`Requirements / documentation → risk analysis → test scenarios → execution → defect / support ticket → retest → regression update`

## Test design focus

The highest-risk flows are money movement and account state: authentication, account ownership, transfers, bill payment, transaction history, negative amounts, invalid account IDs, repeated submissions and validation errors.

## Repository structure

```text
docs/          test plan, execution report, traceability
test-cases/    manual and regression suites
postman/       REST collection + environment
sql/           PostgreSQL-style verification queries
jira/          practice defect/support tickets
logs/          synthetic application logs + analysis examples
wcag/          WCAG 2.0 checklist
scripts/       consistency validator
```

## Running the project

1. Open the public ParaBank web application and Swagger documentation.
2. Import `postman/ParaBank_QA.postman_collection.json` and the environment into Postman.
3. Execute the smoke/regression cases from `test-cases/`.
4. Record observed results in a copy of the CSV or in Jira.
5. Use `sql/verification_queries.sql` against a local/test PostgreSQL schema when database access is available.
6. Practice log triage with `logs/sample_application.log` and the queries in `logs/log_analysis.md`.

Validate the portfolio files themselves with:

```bash
python scripts/validate_project.py
```

## Important scope note

The defect tickets and log file in this repository are **practice QA artifacts**. They demonstrate defect-writing and incident-analysis technique; they are not claims that the current public ParaBank deployment contains those exact defects. The execution report clearly separates live reconnaissance observations from designed test cases.

## Skills demonstrated

Manual testing · functional testing · regression testing · exploratory testing · test-case design · bug reporting · REST/API testing · Postman · SQL · PostgreSQL concepts · Jira-style workflow · SDLC · Agile/Scrum · log analysis · Kibana/Splunk query basics · WCAG 2.0 basics
