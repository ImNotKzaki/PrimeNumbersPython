import time


def sieve_of_eratosthenes(n):
    """
    Implementa l'algoritmo del Crivello di Eratostene
    per trovare tutti i numeri primi fino a un limite 'n'.
    """
    # Passo 1: Crea una lista booleana e inizializza tutti gli elementi a True
    # Questa lista rappresenta i numeri da 0 a n.
    is_prime = [True] * (n + 1)

    # I numeri 0 e 1 non sono primi.
    is_prime[0] = False
    is_prime[1] = False

    # Passo 2: Inizia a 'crivellare' da 2
    p = 2
    while (p * p <= n):
        # Se is_prime[p] è ancora True, significa che 'p' è un numero primo.
        if is_prime[p]:
            # Passo 3: Marca tutti i multipli di 'p' come non primi
            # Inizia da p*p perché i multipli più piccoli sono già stati segnati.
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    # Passo 4: Conta i numeri primi rimasti
    count = 0
    for i in range(2, n + 1):
        if is_prime[i]:
            count += 1

    return count


def main():
    """
    Funzione principale per eseguire l'algoritmo
    e misurare il tempo di esecuzione.
    """
    limit = 100000000
    start_time = time.time()

    # Chiama la funzione del Crivello per ottenere il conteggio
    primes_found = sieve_of_eratosthenes(limit)

    end_time = time.time()
    duration = end_time - start_time

    print(f"Primes Found: {primes_found}")
    print(f"Time taken: {duration:.3f} seconds")


# Esegui la funzione main quando lo script viene lanciato
if __name__ == "__main__":
    main()