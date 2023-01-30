using ClassLibrary1;
using ClassLibrary1.DbModels;
using Microsoft.EntityFrameworkCore;

var db = new ApplicationDbContext(new DbContextOptions<ApplicationDbContext>());

var customersList = db.Customers.ToList();

foreach (var customer in customersList)
{
    Console.WriteLine($"Customer: {customer.customerName}, number: {customer.customerNumber}");
}

db.Customers.Add(new Customers()
{
    customerNumber = 497,
    customerName = "Alice",
    contactLastName = "Tyjek",
    contactFirstName = "Bob",
    phone = "(111)111-1111",
    addressLine1 = "Test. 22",
    addressLine2 = null,
    city = "Warsaw",
    state = null,
    postalCode = "01-123",
    country = "Poland",
    salesRepEmployeeNumber = 1612,
    creditLimit = 38200m
});

db.SaveChanges();

customersList = db.Customers.ToList();

foreach (var customer in customersList)
{
    Console.WriteLine($"Customer: {customer.customerName}, number: {customer.customerNumber}");
}