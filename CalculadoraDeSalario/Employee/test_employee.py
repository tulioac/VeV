import pytest

from .employee import Employee


def test_exist_employee():
    employee = Employee()

    assert employee != None


def test_create_developer_employee():
    role = "Developer"
    developer = Employee(role)

    assert developer.role == role


def test_create_dba_employee():
    role = "DBA"
    dba = Employee(role)

    assert dba.role == role


def test_create_tester_employee():
    role = "Tester"
    dba = Employee(role)

    assert dba.role == role


def test_create_manager_employee():
    role = "Manager"
    manager = Employee(role)

    assert manager.role == role


def test_create_invalid_role_employee():
    invalid_role = "Garbage Collector"

    with pytest.raises(Exception):
        invalid_role_employee = Employee(invalid_role)


def test_create_employee_with_name():
    name = "Jarbas"
    named_employee = Employee(name=name)

    assert named_employee.name == name


def test_create_employee_with_email():
    email = "jarbinhas1854@bol.com.br"
    employee_with_email = Employee(email=email)

    assert employee_with_email.email == email


def test_create_employee_with_base_salary():
    base_salary = 5000
    employee_with_salary = Employee(base_salary=base_salary)

    assert employee_with_salary.base_salary == base_salary
