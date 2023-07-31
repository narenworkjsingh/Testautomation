This automation code is written to test the Zoomprop App.
Below setup is required to run this code
1) Clon this repo and save it to C drive.
2) Download selenium chrome driver and keep it in below foder C:\\SeleniumDrivers
3) Create "Testcheck" and "Report" folder under c driver "C:/Testcheck/reports" or check the folders when download the reports
4) Run the command to go to venvTest enviroment and activate the enviroment
5) Run pip install –r requirements.txt to install all dependency.
6) Run "pytest -sv driver\test_cases.py --browser "chrome" to execute the code.
7) Run any of the below command to run the code as per report selection option
     7.1) To view test summary json report run below command
          $ pytest --json-report --json-report-summary
     7.2) To omitt any field in json repot:
          $ pytest --json-report --json-report-omit keywords streams
     7.3) To Save the full report use below command and specify none as the target file name:
          $ pytest --json-report --json-report-file XXTargetfilename/noneXXX

