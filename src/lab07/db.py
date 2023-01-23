import sqlalchemy.exc
from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.engine import URL

url_object = URL.create(
    "mysql",
    username="root",
    password="",
    host="localhost",
    database="zi_lab7",
)

try:
    engine = create_engine(url_object)
    conn = engine.connect()

    metadata = MetaData(bind=engine)
    # Tables in database
    customers = Table('customers', metadata, autoload=True, autoload_with=engine)
    orders = Table('orders', metadata, autoload=True, autoload_with=engine)
    orderdetails = Table('orderdetails', metadata, autoload=True, autoload_with=engine)
    employees = Table('employees', metadata, autoload=True, autoload_with=engine)
    offices = Table('offices', metadata, autoload=True, autoload_with=engine)

except sqlalchemy.exc.OperationalError:
    print('Connection cannot be establish. Check data in url address')
except sqlalchemy.exc.NoSuchTableError:
    print('You want to get data from table that does not exist')
except sqlalchemy.exc.DatabaseError:
    print('Problem with database')
except sqlalchemy.exc.NoSuchModuleError:
    print('Problem with chosen driver. Check driver in url address')
except:
    print('Some problems have been occurred')

def show_data(view: Table, who: str) -> None:
    '''
    Show data for logged person by id
    :param view: Table representation of chosen view
    :param str who: Logged person type: Customer or Employee
    :return: None, only printing
    '''
    while (spec_id := input('Input id number or exit: ')) != 'exit':
        try:
            view_num = None
            if who == 'Customer':
                view_num = view.c.customerNumber
            elif who == 'Employee':
                view_num = view.c.employeeNumber
            else:
                raise Exception('Wrong person type, choose Customer or Employee')
            show_for_spec_id = select([view]) \
                .where(view_num == int(spec_id))
            result_view = conn.execute(show_for_spec_id).fetchall()
            assert len(result_view) > 0
            for row in result_view:
                print(row)
        except ValueError:
            print(f'{who} id have to be an integer')
        except AssertionError:
            print(f'There is no rows for that {who} number')