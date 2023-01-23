from sqlalchemy_views import CreateView
from db import *

# Query
try:
    customer_query2 = select([
        customers.c.customerNumber,
        customers.c.salesRepEmployeeNumber,
        employees.c.firstName,
        employees.c.lastName,
        employees.c.email,
        employees.c.extension,
        offices.c.city
    ]).select_from(
        customers.join(employees, customers.c.salesRepEmployeeNumber == employees.c.employeeNumber)
        .join(offices, employees.c.officeCode == offices.c.officeCode)
    )

    # Creating a view
    try:
        customer_view2 = Table('customer_view2', metadata)
        create_customer_view2 = CreateView(customer_view2, customer_query2, or_replace=True)
        result = conn.execute(create_customer_view2)
    except sqlalchemy.exc.OperationalError as err:
        print('Cannot create a view:', err)

except AttributeError as err:
    print('Chosen column in query does not exist:', err)
except NameError as err:
    print('Chosen table does not exist:', err)

if __name__ == "__main__":
    Table('customer_view2', metadata, autoload_with=engine, extend_existing=True)
    show_data(customer_view2, 'Customer')

