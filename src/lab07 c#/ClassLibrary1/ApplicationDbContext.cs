using ClassLibrary1.DbModels;
using Microsoft.EntityFrameworkCore;

namespace ClassLibrary1;

public class ApplicationDbContext : DbContext
{
    public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options) : base(options)
    {
        
    }
    
    public virtual DbSet<Customers> Customers { get; set; } = null!;
    
    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        optionsBuilder.UseMySQL($"server=localhost;database=zi_lab7;uid=root;password=;");
    }
}