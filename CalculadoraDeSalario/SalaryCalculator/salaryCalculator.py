from ..Employee.employee import Employee


class SalaryCalculator:
    def calculate(self, employee: Employee) -> float:
        employee_role = employee.role
        employee_base_salary = employee.base_salary

        if employee_role == "Developer":
            discount_value = 0.2

            salary_threshold = 3_000

            if employee_base_salary < salary_threshold:
                discount_value = 0.1

            liquid_salary = employee_base_salary * (1 - discount_value)

            return liquid_salary

        elif employee_role == "Manager":
            discount_value = 0.3

            salary_threshold = 5_000

            if employee_base_salary < salary_threshold:
                discount_value = 0.2

            liquid_salary = employee_base_salary * (1 - discount_value)

            return liquid_salary

        else:
            discount_value = 0.25

            salary_threshold = 2_000

            if employee_base_salary < salary_threshold:
                discount_value = 0.15

            liquid_salary = employee_base_salary * (1 - discount_value)

            return liquid_salary
