from pathlib import Path
import csv, json, sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
for p in [ROOT/'postman/ParaBank_QA.postman_collection.json', ROOT/'postman/ParaBank_QA.postman_environment.json']:
    try: json.loads(p.read_text())
    except Exception as e: errors.append(f'{p}: {e}')
with open(ROOT/'test-cases/manual_test_cases.csv',encoding='utf-8') as f:
    rows=list(csv.DictReader(f))
ids=[r['id'] for r in rows]
if len(ids)!=len(set(ids)): errors.append('duplicate manual test IDs')
if len(rows)<30: errors.append('expected at least 30 manual cases')
with open(ROOT/'test-cases/regression_suite.csv',encoding='utf-8') as f:
    for r in csv.DictReader(f):
        if r['source_test_case'] not in ids: errors.append('unknown regression source '+r['source_test_case'])
with open(ROOT/'docs/traceability_matrix.csv',encoding='utf-8') as f:
    for r in csv.DictReader(f):
        for tc in r['test_case_ids'].split(';'):
            if tc not in ids: errors.append('unknown traceability test '+tc)
required=['README.md','docs/test_plan.md','docs/execution_report.md','jira/practice_defect_tickets.md','logs/log_analysis.md','wcag/wcag_2_0_checklist.md','sql/verification_queries.sql']
for rel in required:
    if not (ROOT/rel).exists(): errors.append('missing '+rel)
if errors:
    print('VALIDATION FAILED')
    print('\n'.join(errors)); sys.exit(1)
print(f'VALIDATION PASSED: {len(rows)} manual cases, regression/traceability IDs consistent, Postman JSON valid.')
