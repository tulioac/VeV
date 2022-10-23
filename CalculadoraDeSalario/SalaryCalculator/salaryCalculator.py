from ..Employee.employee import Employee

# salary_threshold, higher_discount, lower_discount
roles_calculation_parameters = {
    "Developer": [
        3_000,
        0.2,
        0.1,
    ],
    "Manager": [
        5_000,
        0.3,
        0.2,
    ],
    "DBA": [
        2_000,
        0.25,
        0.15,
    ],
    "Tester": [
        2_000,
        0.25,
        0.15,
    ],
}


class SalaryCalculator:
    def __calculate_liquid_salary(
        self,
        base_salary: float,
        salary_threshold: float,
        higher_discount: float,
        lower_discount: float,
    ) -> float:
        discount_value = (
            lower_discount if base_salary < salary_threshold else higher_discount
        )

        return base_salary * (1 - discount_value)

    def calculate(self, employee: Employee) -> float:
        employee_role = employee.role
        employee_base_salary = employee.base_salary

        [
            salary_threshold,
            higher_discount,
            lower_discount,
        ] = roles_calculation_parameters[employee_role]

        return self.__calculate_liquid_salary(
            base_salary=employee_base_salary,
            salary_threshold=salary_threshold,
            higher_discount=higher_discount,
            lower_discount=lower_discount,
        )
