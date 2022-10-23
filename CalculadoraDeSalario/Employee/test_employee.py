from .employee import Employee


def test_exist_employee():
    employee = Employee()

    assert employee != None


def test_create_developer_employee():
    developer = Employee("Developer")

    assert developer.role == "Developer"
