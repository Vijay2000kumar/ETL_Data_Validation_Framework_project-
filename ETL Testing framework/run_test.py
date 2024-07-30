# import subprocess
# import webbrowser
# import os
# import time
#
# # Check if the report file already exists
# report_exists = os.path.exists("report.html")
#
# # Run pytest command to generate HTML report if it doesn't exist
# if not report_exists:
#     subprocess.run(["pytest", "--html=report.html"])
#
# # Open the generated HTML report in the default web browser only if it was just generated
# if not report_exists:
#     webbrowser.open("report.html")
#     # Wait for a short time to ensure the browser has enough time to open
#     time.sleep(1)
#
import subprocess
import webbrowser
import os
import time

# Define the path for the report and the reports folder
# report_path = "reports/report.html"
# reports_folder = "reports"
#
# # Check if the report file already exists
# report_exists = os.path.exists(report_path)
#
# # Run pytest command to generate HTML report if it doesn't exist
# if not report_exists:
#     # Create the reports folder if it doesn't exist
#     os.makedirs(reports_folder, exist_ok=True)
#     subprocess.run(["pytest", f"--html={report_path}"])
#
# # Open the generated HTML report in the default web browser only if it was just generated
# if not report_exists:
#     webbrowser.open(reports/report.html)
#     # Wait for a short time to ensure the browser has enough time to open
#     time.sleep(1)

import subprocess
import webbrowser
import os

# Define the path for the report and the reports folder
report_path = "./reports/report.html"
reports_folder = "reports"

# Check if the report file already exists
report_exists = os.path.exists(report_path)

# Run pytest command to generate HTML report if it doesn't exist
if not report_exists:
    # Create the reports folder if it doesn't exist
    os.makedirs(reports_folder, exist_ok=True)
    subprocess.run(["pytest", f"--html={report_path}"])

# Open the generated HTML report in the default web browser only if it was just generated
if not report_exists:
    webbrowser.open(f"file://{os.path.abspath(report_path)}")