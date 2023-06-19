# TC: O(n) | SC: O(1)
def calculate_tax_iterative(levels, salary):
    tax = 0
    limit = 0
    for level in levels:
        percent = level[1]
        if level[0] is None:
            return tax + salary * percent
        curr_salary = min(salary, level[0] - limit)
        tax += curr_salary * percent
        salary -= curr_salary
        limit = level[0]
    return tax

def calculate_tax_recursive(levels, salary):
    def helper(salary, prev, tax, levels, index):
        if salary <= 0:
            return tax

        limit, rate = levels[index]
        taxable_income = min(limit - prev if limit else salary, salary)
        return helper(salary - taxable_income, limit, tax + taxable_income * rate, levels, index + 1)

    return helper(salary, 0, 0, levels, 0)

if __name__ == "__main__":
    levels = [
        [10000.0, 0.3],
        [20000.0, 0.2],
        [30000.0, 0.1],
        [None, 0.1]
    ]
    print(calculate_tax_iterative(levels, 45000))
    print(calculate_tax_recursive(levels, 45000))