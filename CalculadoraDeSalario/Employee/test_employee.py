from .employee import Employee


def test_exist_employee():
    employee = Employee()

    assert employee != None
