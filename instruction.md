Read the access log in the working directory and produce a JSON report at /app/report.json.

The report must contain these fields:
- total_requests: the total number of log entries
- unique_ips: the number of distinct client IP addresses
- top_path: the most requested URL path

The report must be valid JSON and exactly match the expected values for the provided log.
