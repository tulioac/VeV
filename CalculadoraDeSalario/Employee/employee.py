ALLOWED_ROLES = ["Developer", "DBA", "Tester", "Manager"]


class Employee:
    def __init__(self, role="Developer", name="", email="", base_salary=0) -> None:
        if role not in ALLOWED_ROLES:
            raise SystemError(f"{role} is not a valid role for employee")

        if base_salary < 0:
            raise ValueError(f"{base_salary} is not a valid base salary for employee")

        self.role = role
        self.name = name
        self.email = email
        self.base_salary = base_salary
