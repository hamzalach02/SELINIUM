from utils.webdriver_setup import get_driver
from scanners.sql_injection import sql_injection_scanner
from scanners.xss import xss_scanner
from scanners.headers import security_headers_checker
from utils.report_generator import generate_report

if __name__ == "__main__":
    url = "http://localhost/vulnerable/"
    driver = get_driver()

    # Collect findings
    findings = []
    
    # Run SQL Injection Scanner
    sql_payloads = ["' OR '1'='1", "'; DROP TABLE users; --"]
    findings.append(sql_injection_scanner(driver, url, sql_payloads))
    
    # Run XSS Scanner
    xss_payloads = ["<script>alert('XSS')</script>"]
    findings.append(xss_scanner(driver, url, xss_payloads))

    # Run Security Headers Checker
    findings.append(security_headers_checker(url))

    # Generate Report
    generate_report(findings, "scan_report.pdf")
    driver.quit()
