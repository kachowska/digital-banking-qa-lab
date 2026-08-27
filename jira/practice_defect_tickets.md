# Jira-style Practice Defect / Support Tickets

These are **practice artifacts**, not claims about defects currently present in the public ParaBank instance.

## QA-101 — Duplicate transfer after repeated submission
**Type:** Bug  
**Severity:** Critical  
**Priority:** Highest  
**Environment:** Test / web  
**Related test:** TC-UI-010

**Precondition:** Customer is authenticated and owns source/target accounts.  
**Steps:** 1. Submit a valid transfer. 2. Repeat browser submit/refresh action immediately. 3. Open account history.  
**Expected:** A single business transaction is created unless the user explicitly confirms a second transfer.  
**Actual (practice scenario):** Two identical transfers are recorded.  
**Impact:** Potential duplicate money movement.  
**Evidence to attach:** request timestamps, account history, correlation IDs.

## QA-102 — Transfer validation accepts zero amount
**Type:** Bug  
**Severity:** High  
**Priority:** High  
**Related test:** TC-UI-008 / TC-API-011

**Steps:** Submit a transfer with amount `0`.  
**Expected:** Validation rejects the request before persistence.  
**Actual (practice scenario):** Success confirmation is returned.  
**Impact:** Invalid transaction data and misleading audit/history entries.

## SUP-201 — Customer reports transfer missing from history
**Type:** Support / Investigation  
**Priority:** High

**Input:** customer ID, source account, approximate timestamp, amount.  
**Investigation:** reproduce if possible → search logs by correlation/time/account → compare API response and transaction history → check DB state if access exists → document layer at fault.  
**Resolution note template:** reproduced/not reproduced; affected environment; suspected component; evidence; workaround; owner for next action.
