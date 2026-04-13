Request (SQL Injection Test):
POST /api/customer/update
{
  "customer_id": "1' OR '1'='1",
  "name": "'; DROP TABLE customer_records; --"
}

Response:
HTTP/1.1 200 OK
{
  "status": "success",
  "updated_record": {...}
}
Result: VULNERABLE ✗ (Input accepted despite malicious payload)

Request (Rate Limiting Test):
GET /api/customer/records?customer_id=1
GET /api/customer/records?customer_id=2
[Repeated 500 times in 60 seconds]

Response (All Succeed):
HTTP/1.1 200 OK
{
  "customer_id": 1,
  "records": [...]
}
Result: NO RATE LIMITING ✗ (Can enumerate all customer IDs)
