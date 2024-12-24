from rich.console import Console
from user import user_interface
from admin import admin_interface
from database import initialize_database
from encryption import initialize_context
from time import sleep

# Initialize the Rich console
console = Console()

def main():
    # Initialize the database
    sleep(2)
    console.print('Intializing Database...')
    sleep(2)
    initialize_database()


    while True:
        sleep(1.5)
        console.print("[bold cyan]Welcome to the Federated Learning Privacy System[/bold cyan]")
        sleep(1.5)
        console.print("[bold yellow]Please select a role:[/bold yellow]")
        sleep(0.5)
        console.print("1. User")
        sleep(0.5)
        console.print("2. Admin")
        sleep(0.5)
        console.print("3. Exit")
        sleep(0.5)

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            console.print("[bold green]\nUser Section Selected[/bold green]")
            initialize_context()
            user_interface()
        elif choice == "2":
            console.print("[bold green]\nAdmin Section Selected[/bold green]")
            admin_interface()
        elif choice == "3":
            sleep(1)
            console.print("[bold red]\nExiting the application. Goodbye![/bold red]")
            sleep(1.7)
            break
        else:
            console.print("[bold red]\nInvalid choice. Please try again.[/bold red]")

if __name__ == "__main__":
    main()
