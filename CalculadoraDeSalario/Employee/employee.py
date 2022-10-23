ALLOWED_ROLES = ["Developer", "DBA", "Tester", "Manager"]


class Employee:
    def __init__(self, role="Developer", name="", email="") -> None:
        if role not in ALLOWED_ROLES:
            raise SystemError(f"{role} is not a valid role for employee")

        self.role = role
        self.name = name
        self.email = email
