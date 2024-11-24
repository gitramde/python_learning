import pandas as pd
"""
loc - Label Based Indexing
    Access data using row and column labels
iloc - Integer Based Indexing 
    Access data using integer positions (starting from 0)
"""
data_c = [[1, 'Will', None], [2, 'Jone', None], [3, 'Alex', 2], [4,'Bill', None], [5, 'Zack', 1], [6, 'Mark', 2]]
customer = pd.DataFrame(data_c, columns = ['id','name','referee_id']).astype({'id':'Int64', 'name':'object', 'referee_id': 'Int64'})
data_e = [[1, 'Joe', 85000, 1], [2, 'Henry', 80000, 2], [3, 'Sam', 60000, 2], [4, 'Max', 90000, 1], [5, 'Janet', 69000, 1], [6, 'Randy', 85000, 1], [7, 'Will', 70000, 1]]
employee = pd.DataFrame(data_e, columns=['id', 'name', 'salary', 'departmentId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'departmentId':'Int64'})
data_d = [[1, 'IT'], [2, 'Sales']]
department = pd.DataFrame(data_d, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    """
    584. Find Customer Referee
     Input - Customer DataFrame

     Output: Find the names of the customer that are not referred by the customer with id = 2

     SQL Equivalent:
        SELECT name FROM Customer
        WHERE coalesce(referee_id, -100) <> 2
    """
    return customer[(customer.referee_id != 2) |(customer.referee_id.isnull())].iloc[:,[1]]



print("584. Find Customer Referee")
print(customer)
print(find_customer_referee(customer).to_string(index=False))

def dept_top_3_Salaries():
    """
    185. Department Top 3 salaries Pandas

    A company's executives are interested in seeing who earns the most money in each of the company's departments.
    A high earner in a department is an employee who has a salary in the top three unique salaries for that department.

    Write a solution to find the employees who are high earners in each of the departments.

    SQL: SELECT department,  Employee, salary FROM (
    SELECT  d.name as department, e.name as Employee, e.salary, dense_rank() over (partition by departmentId order by salary desc) as dense_rank_val
    FROM employee e
        left join
     department d ON e.departmentId = d.id) tmp
    where dense_rank_val <= 3

    Approach:
        1. Merge the dataframes
        2. Rank the salaries
        3. Filter the top 3
        4. select the columns :q!


    """


