import tenseal as ts
from rich.console import Console
import random
from time import sleep

console = Console()

CKKS_CONTEXT = None

def initialize_context():
    """Initialize CKKS context."""
    global CKKS_CONTEXT
    CKKS_CONTEXT = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree=8192, coeff_mod_bit_sizes=[60, 40, 40, 60])
    CKKS_CONTEXT.global_scale = 2 ** 40
    CKKS_CONTEXT.generate_galois_keys()
    sleep(2)
    console.print("[bold green]CKKS context initialized successfully![/bold green]")
    sleep(2)
    


def encrypt_data(data):
    """
    Encrypt numerical data using CKKS.
    Non-numerical fields (like 'name') are excluded from encryption.
    """
    global CKKS_CONTEXT
    if CKKS_CONTEXT is None:
        raise ValueError("CKKS context is not initialized.")
    encrypted_data = {}

    for key, value in data.items():
        if isinstance(value, (int, float)):  # Encrypt only numerical values
            encrypted_data[key] = ts.ckks_vector(CKKS_CONTEXT, [value])
        else:
            encrypted_data[key] = value  # Leave non-numerical values as-is

    return encrypted_data

def decrypt_data(encrypted_data):
    """
    Decrypt encrypted data.
    Non-encrypted fields (like 'name') are returned as-is.
    """
    decrypted_data = {}

    for key, value in encrypted_data.items():
        if isinstance(value, ts.CKKSVector):  # Decrypt only CKKSVector objects
            decrypted_data[key] = value.decrypt()[0]
        else:
            decrypted_data[key] = value  # Leave non-encrypted values as-is

    return decrypted_data

def perform_client_operations(encrypted_data):
    """Perform example client-side operations on encrypted data."""
    
    client_results = encrypted_data.copy()
    
    # Ask for automation choice
    while True:
        sleep(2)
        choice = input("Would you like to perform automated operations (A) or manual operations (M)? (A/M): ").strip().upper()
        sleep(2)
        auto=['a','A']
        manual=['m','M']

        # Automated Operations
        if choice in auto  :
            console.print("[bold blue]Performing automated operations...[/bold blue]")
            sleep(2)

            # Client C: Randomly subtract a value (1-10) from 'age'
            if 'age' in client_results and isinstance(client_results['age'], ts.CKKSVector):
                random_value = random.randint(1, 10)
                console.print(f"Client C: Subtracting {random_value} from age.")
                client_results['age'] -= random_value
                sleep(2)

            # Client A: Randomly add a value (100-5000) to 'income'
            if 'income' in client_results and isinstance(client_results['income'], ts.CKKSVector):
                random_value = random.randint(100, 5000)
                console.print(f"Client A: Adding {random_value} to income.")
                client_results['income'] += random_value
                sleep(2)

            # Client B: Randomly double the 'transactions' by a factor (2-5)
            if 'transactions' in client_results and isinstance(client_results['transactions'], ts.CKKSVector):
                random_factor = random.randint(2, 5)
                console.print(f"Client B: Doubling transactions by a factor of {random_factor}.")
                client_results['transactions'] *= random_factor
                sleep(2)
            break

        # Manual Operations
        elif choice in manual:
            sleep(2)
            console.print("[bold green]Performing manual operations...[/bold green]")
            sleep(2)

            # Client C: Subtract user input from 'age'
            if 'age' in client_results and isinstance(client_results['age'], ts.CKKSVector):
                manual_value = float(input("Enter a value to subtract from 'age': "))
                console.print(f"Client C: Subtracting {manual_value} from age.")
                client_results['age'] -= manual_value
                sleep(1)

            # Client A: Add user input to 'income'
            if 'income' in client_results and isinstance(client_results['income'], ts.CKKSVector):
                manual_value = float(input("Enter a value to add to 'income': "))
                console.print(f"Client A: Adding {manual_value} to income.")
                client_results['income'] += manual_value
                sleep(1)

            # Client B: Multiply 'transactions' by user input
            if 'transactions' in client_results and isinstance(client_results['transactions'], ts.CKKSVector):
                manual_value = float(input("Enter a factor to multiply 'transactions' by: "))
                console.print(f"Client B: Multiplying transactions by a factor of {manual_value}.")
                client_results['transactions'] *= manual_value
                sleep(1)
            break

        else:
            sleep(2)
            console.print("[bold red]Invalid choice. Please choose 'A' for automated or 'M' for manual operations.[/bold red]")
            sleep(2)
        #return None

    return client_results
