# How to Install BDD Framework
 1. Need to install python (python3 recommended)
 2. Install IDE (PyCharm recommended)
 3. Setup python interpreter (I have used 3.11)
 4. Install Selenium globally, can simply install with PIP command
 5. Install behave (python framework for BDD) globally, can simply install with PIP command
 6. Install selenium webDriver. You can use any however I have chromeDriver installed it will run on latest Chrome version
 7. Add selenium and behave packages in project settings
 8. Also add allure-report if you want to see report generated
 
 # How to Run Tests
 1. If you are using windows, I have added run.bat file. Just go to that file and run
 2. Otherwise, open terminal and enter command "*behave*", it runs all suites
 3. Or if you want to run specific suites/features then run command "*behave feature/login.feature*"
 
 # Generate Reports [Fresh Install]
 Pre-requisite for this:</br>
 You should not have reports files in your directory</br>
 You should have installed behave and allure globally</br>
 Steps: </br>
 1. Run the command "*behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results/ features*"; <p>it first runs all the suites and
 generates allure-results within reports directory</p>
 2. Now compile those results to make html report by following command: </br>
    "*allure generate reports/allure-results -o reports/allure-report --clean*"
