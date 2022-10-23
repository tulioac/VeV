from ..Employee.employee import Employee


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

        if employee_role == "Developer":
            salary_threshold = 3_000
            higher_discount_value = 0.2
            lower_discount_value = 0.1

            return self.__calculate_liquid_salary(
                base_salary=employee_base_salary,
                salary_threshold=salary_threshold,
                higher_discount=higher_discount_value,
                lower_discount=lower_discount_value,
            )

        elif employee_role == "Manager":
            salary_threshold = 5_000
            higher_discount_value = 0.3
            lower_discount_value = 0.2

            return self.__calculate_liquid_salary(
                base_salary=employee_base_salary,
                salary_threshold=salary_threshold,
                higher_discount=higher_discount_value,
                lower_discount=lower_discount_value,
            )

        else:
            salary_threshold = 2_000
            higher_discount_value = 0.25
            lower_discount_value = 0.15

            return self.__calculate_liquid_salary(
                base_salary=employee_base_salary,
                salary_threshold=salary_threshold,
                higher_discount=higher_discount_value,
                lower_discount=lower_discount_value,
            )
