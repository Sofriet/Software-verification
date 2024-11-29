from html.parser import HTMLParser
from svfuzzer import SVFuzzer

seeds = ["<div><h3>Welcome to Our Website!</h3><p>We're excited to have you here. Explore our content and let us know if you have any questions.</p><ul><li>Feature 1</li></ul><p>Stay tuned for updates!</p></div>"]

# Comment line 4 and uncomment line 7 to test for failed inputs
# seeds = ["<html></html>"]

#change for different runs and coverage type
coverage_type = 0
runs = 10000

fuzzer_lines = SVFuzzer(coverage_type, runs, seeds, "html/parser.py", HTMLParser().feed).runs()
