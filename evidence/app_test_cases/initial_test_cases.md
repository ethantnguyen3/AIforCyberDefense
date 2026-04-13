INITIAL TEST CASES & RESULTS

TEST 1: Data Persistence Bug (Application)
Expected: Records remain after app closes
Actual: Records LOST - app shows "No records found"
Result: FAILED ✗

TEST 2: API Rate Limiting
Expected: After X requests, API returns 429 (Too Many Requests)
Actual: 10,000 requests all SUCCEED without throttling
Result: FAILED ✗ (Enumeration attack possible)

TEST 3: Token Expiration
Expected: Logout invalidates token
Actual: Token still works 12 hours later
Result: FAILED ✗ (Stolen tokens grant indefinite access)

TEST 4: Unauthorized Data Access (IDOR)
Expected: User cannot access other users' records
Actual: GET /api/customer/records?user_id=5 returns Jane Doe's data
Result: FAILED ✗ (Full PII exposure)

TEST 5: Input Validation
Expected: Malformed JSON rejected
Actual: Payload accepted, malformed data stored in database
Result: FAILED ✗

---
