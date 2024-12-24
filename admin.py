from database import fetch_original_data, fetch_operated_data
from rich.console import Console
from rich.table import Table
from time import sleep

# Initialize the rich console for better UX
console = Console()

ADMIN_PASSWORD = "FLPRO"  # Password for admin access

def admin_interface():
    """Provide the admin interface."""
    sleep(2)
    console.print("\n[bold cyan]Welcome, Admin![/bold cyan]")
    sleep(1.5)
    entered_password = input("Enter admin password: ").strip()
    sleep(2)

    if entered_password != ADMIN_PASSWORD:
        console.print("[bold red]Invalid password! Access denied.[/bold red]")
        sleep(2)
        return

    console.print("[bold green]Access granted![/bold green]")
    while True:
        console.print("\nWhat would you like to do?")
        sleep(0.5)
        console.print("[bold yellow]1.[/bold yellow] View Original Data")
        sleep(0.5)
        console.print("[bold yellow]2.[/bold yellow] View Operated Data")
        sleep(0.5)
        console.print("[bold yellow]3.[/bold yellow] Go back to main menu")
        sleep(0.5)
        
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice == "1":
            sleep(2)
            view_original_data()
        elif choice == "2":
            sleep(2)
            view_operated_data()
        elif choice == "3":
            console.print("[bold red]Returning to main menu...[/bold red]")
            sleep(2)
            break
        else:
            sleep(1.5)
            console.print("[bold red]Invalid choice! Please try again.[/bold red]")
            sleep(2)

def view_original_data():
    """Display original data (both encrypted and decrypted)."""
    sleep(1.5)
    console.print("\n[bold cyan]Original Data:[/bold cyan]")
    sleep(2)
    data = fetch_original_data()
    
    if not data:
        sleep(2)
        console.print("[bold red]No data found![/bold red]")
        return

    table = Table(title="Original Data")
    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Name", style="green")
    table.add_column("Decrypted Age", justify="right", style="magenta")
    table.add_column("Decrypted Income", justify="right", style="magenta")
    table.add_column("Decrypted Transactions", justify="right", style="magenta")
    #table.add_column("Encrypted Data", justify="center", style="yellow")
    i=0
    for row in data:
        i=i+1
        table.add_row(
            str(row["id"]),
            row["name"],
            str(row["age_decrypted"]),
            str(row["income_decrypted"]),
            str(row["transactions_decrypted"]),
            #str(row["encrypted_data"])
        )
        console.print(f"[bold green]Row {i} Inserted Succesfully[/bold green]")
        sleep(1)

    console.print(table)
    sleep(2)

def view_operated_data():
    """Display operated data (both encrypted and decrypted)."""

    console.print("\n[bold cyan]Operated Data:[/bold cyan]")
    data = fetch_operated_data()
    
    if not data:
        console.print("[bold red]No data found![/bold red]")
        return

    table = Table(title="Operated Data")
    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Name", style="green")
    table.add_column("Decrypted Age", justify="right", style="magenta")
    table.add_column("Decrypted Income", justify="right", style="magenta")
    table.add_column("Decrypted Transactions", justify="right", style="magenta")
    i=0
    for row in data:
        i=i+1
        table.add_row(
            str(row["id"]),
            row["name"],
            str(row["age_decrypted"]),
            str(row["income_decrypted"]),
            str(row["transactions_decrypted"]),
        )
        sleep(1)
        console.print(f"[bold green]Row {i} Inserted Succesfully[/bold green]")
        sleep(1)
    console.print("[bold cyan]Loading Operated Table to Print[/bold cyan]")
    sleep(2)
    console.print(table)
    sleep(2)
