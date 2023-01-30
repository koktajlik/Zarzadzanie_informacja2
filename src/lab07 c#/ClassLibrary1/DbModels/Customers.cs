using System.ComponentModel.DataAnnotations;

namespace ClassLibrary1.DbModels;

public class Customers
{
    [Key] 
    public int customerNumber { get; set; }
    [Required]
    [StringLength(50)]
    public string customerName { get; set; }
    [Required]
    [StringLength(50)]
    public string contactLastName { get; set; }
    [Required]
    [StringLength(50)]
    public string contactFirstName { get; set; }
    [Required]
    [StringLength(50)]
    public string phone { get; set; }
    [Required]
    [StringLength(50)]
    public string addressLine1 { get; set; }
    [StringLength(50)]
    public string? addressLine2 { get; set; }
    [Required]
    [StringLength(50)]
    public string city { get; set; }
    [StringLength(50)]
    public string? state { get; set; }
    [StringLength(50)]
    public string? postalCode { get; set; }
    [Required]
    [StringLength(50)]
    public string country { get; set; }
    public int? salesRepEmployeeNumber { get; set; }
    public decimal creditLimit { get; set; }
}