from sqlalchemy.sql.functions import sum
from sqlalchemy_views import CreateView
from db import *

# Query
try:
    employee_query = select([
        employees.c.employeeNumber,
        customers.c.customerNumber,
        customers.c.contactFirstName,
        customers.c.contactLastName,
        customers.c.addressLine1,
        sum(orderdetails.c.priceEach).label('priceSum'),
        orders.c.orderDate,
        orders.c.status
    ]).select_from(
        employees.join(customers, customers.c.salesRepEmployeeNumber == employees.c.employeeNumber)
        .join(orders, orders.c.customerNumber == customers.c.customerNumber)
        .join(orderdetails, orderdetails.c.orderNumber == orders.c.orderNumber)
    ).group_by(orders.c.orderNumber).order_by(orders.c.orderDate.desc())

    # Creating a view
    try:
        employee_view = Table('employee_view', metadata)
        create_employee_view = CreateView(employee_view, employee_query, or_replace=True)
        result = conn.execute(create_employee_view)
    except sqlalchemy.exc.OperationalError as err:
        print('Cannot create a view:', err)

except AttributeError as err:
    print('Chosen column in query does not exist:', err)
except NameError as err:
    print('Chosen table does not exist:', err)


if __name__ == "__main__":
    Table('employee_view', metadata, autoload_with=engine, extend_existing=True)
    show_data(employee_view, 'Employee')