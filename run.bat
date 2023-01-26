behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results/ features
allure generate reports/allure-results -o reports/allure-report --clean