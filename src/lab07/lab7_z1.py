from sqlalchemy.sql.functions import sum
from sqlalchemy_views import CreateView
from db import *

# Query
try:
    customer_query = select([
        customers.c.customerNumber,
        orders.c.orderNumber,
        sum(orderdetails.c.quantityOrdered).label('quantityOrdered'),
        orders.c.status,
        sum(orderdetails.c.priceEach).label('priceSum')
    ]).select_from(
        customers.join(orders, orders.c.customerNumber == customers.c.customerNumber)
        .join(orderdetails, orderdetails.c.orderNumber == orders.c.orderNumber)
    ).group_by(orders.c.orderNumber)

    # Creating a view
    try:
        customer_view = Table('customer_view', metadata)
        create_customer_view = CreateView(customer_view, customer_query, or_replace=True)
        result = conn.execute(create_customer_view)
    except sqlalchemy.exc.OperationalError as err:
        print('Cannot create a view:', err)

except AttributeError as err:
    print('Chosen column in query does not exist:', err)
except NameError as err:
    print('Chosen table does not exist:', err)

if __name__ == "__main__":
    Table('customer_view', metadata, autoload_with=engine, extend_existing=True)
    show_data(customer_view, 'Customer')