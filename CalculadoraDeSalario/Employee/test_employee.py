import pytest

from .employee import Employee


def test_exist_employee():
    employee = Employee()

    assert employee != None


def test_create_developer_employee():
    developer = Employee("Developer")

    assert developer.role == "Developer"


def test_create_dba_employee():
    dba = Employee("DBA")

    assert dba.role == "DBA"


def test_create_tester_employee():
    dba = Employee("Tester")

    assert dba.role == "Tester"


def test_create_manager_employee():
    manager = Employee("Manager")

    assert manager.role == "Manager"


def test_create_invalid_role_employee():
    with pytest.raises(Exception):
        invalid_role_employee = Employee("Garbage Collector")
