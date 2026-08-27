-- PostgreSQL-style QA verification examples for a banking test database.
-- These queries assume read-only access to test data; adapt table/column names to the real schema.

-- 1. Detect orphan transactions.
SELECT t.id, t.account_id
FROM transactions t
LEFT JOIN accounts a ON a.id = t.account_id
WHERE a.id IS NULL;

-- 2. Detect non-positive transfer amounts where business rules require positive values.
SELECT id, account_id, amount, type, created_at
FROM transactions
WHERE type = 'TRANSFER' AND amount <= 0;

-- 3. Check accounts linked to missing customers.
SELECT a.id, a.customer_id
FROM accounts a
LEFT JOIN customers c ON c.id = a.customer_id
WHERE c.id IS NULL;

-- 4. Compare transaction count and balance-impact totals for one account.
SELECT account_id,
       COUNT(*) AS transaction_count,
       SUM(amount) AS signed_amount_total
FROM transactions
WHERE account_id = :account_id
GROUP BY account_id;

-- 5. Find possible duplicate transfer records in a short time window.
SELECT account_id, amount, type, DATE_TRUNC('minute', created_at) AS minute_bucket, COUNT(*)
FROM transactions
WHERE type = 'TRANSFER'
GROUP BY account_id, amount, type, DATE_TRUNC('minute', created_at)
HAVING COUNT(*) > 1
ORDER BY minute_bucket DESC;
