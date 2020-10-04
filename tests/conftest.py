import pytest
from application.modules.people.Human import Human
from application.modules.db.DB import DB

db = DB()

@pytest.fixture
def human():
    return Human()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call':
        db.insertTestResult(report.nodeid, report.outcome == 'passed')

print(db.getTestByDate(2020, 9, 27))

