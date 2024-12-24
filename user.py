from database import insert_original_data, insert_operated_data
from encryption import encrypt_data, decrypt_data, perform_client_operations
from rich.console import Console
from time import sleep

console = Console()

def user_interface():
    """Main interface for user role."""
    while True:
        sleep(2)
        console.print("\n[bold green]Welcome, User![/bold green]\n")
        sleep(2)
        console.print("What would you like to do?")
        sleep(2)
        #console.print("[1] Witness the process with sample data")
        console.print("[1] Input data to test")
        sleep(1.5)
        console.print("[2] Go back to the main menu")
        sleep(1.5)
        choice = input("Enter your choice (1/2): ").strip()
        sleep(2)

        if choice == '1':
            view_process_with_sample_data()
        elif choice == '2':
            break
        else:
            sleep(2)
            console.print("[bold red]Invalid choice. Please try again.[/bold red]")
            sleep(2)

def view_process_with_sample_data():
    """Demonstrates the encryption, client operations, and storage process using sample data."""
    sleep(2)
    sample_data = {'name': input('Enter the name : ').strip(), 'age': int(input('Enter age : ')), 'income': int(input('Enter Income : ')), 'transactions': int(input('Enter Transaction : '))}
    sleep(2)
    console.print(f"[bold blue]Sample Data:[/bold blue] {sample_data}")
    sleep(2)

    # Encrypt the sample data
    console.print("[bold yellow]Encrypting user data...[/bold yellow]")
    sleep(2)
    encrypted_data = encrypt_data(sample_data)
    console.print(f"[bold green]Encrypted Data:[/bold green] {encrypted_data}")
    sleep(2)

    # Decrypt the sample data to verify
    decrypted_data = decrypt_data(encrypted_data)
    console.print(f"[bold green]Decrypted Data:[/bold green] {decrypted_data}")
    sleep(2)

    # Store original data in database
    insert_original_data(
        name=decrypted_data['name'],
        age_encrypted=str(encrypted_data['age']),
        age_decrypted=decrypted_data['age'],
        income_encrypted=str(encrypted_data['income']),
        income_decrypted=decrypted_data['income'],
        transactions_encrypted=str(encrypted_data['transactions']),
        transactions_decrypted=decrypted_data['transactions']
    )

    # Perform client operations
    console.print("[bold yellow]Performing client-side operations...[/bold yellow]")
    client_results = perform_client_operations(encrypted_data)

    # Decrypt the operated data for verification
    decrypted_results = decrypt_data(client_results)
    console.print(f"[bold green]Decrypted Operated Data:[/bold green] {decrypted_results}")

    # Store operated data in database
    insert_operated_data(
        name=decrypted_results['name'],
        age_encrypted=str(client_results['age']),
        age_decrypted=decrypted_results['age'],
        income_encrypted=str(client_results['income']),
        income_decrypted=decrypted_results['income'],
        transactions_encrypted=str(client_results['transactions']),
        transactions_decrypted=decrypted_results['transactions']
    )

    console.print("[bold cyan]Sample data processed and stored successfully![/bold cyan]")

def input_and_process_data():
    """Allows user to input custom data."""
    console.print("[bold yellow]Please enter your data below:[/bold yellow]")
    name = input("Name: ").strip()
    age = float(input("Age: "))
    income = float(input("Income: "))
    transactions = float(input("Transactions: "))

    user_data = {'name': name, 'age': age, 'income': income, 'transactions': transactions}
    console.print(f"[bold blue]Input Data:[/bold blue] {user_data}")

    # Encrypt and process as above...
    view_process_with_sample_data(user_data)
