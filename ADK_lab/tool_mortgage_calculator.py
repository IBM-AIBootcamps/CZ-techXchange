from ibm_watsonx_orchestrate.agent_builder.tools import *

@tool
def mortgage_calculator(loan_amount : float, annual_interest_rate : float, loan_term_years : int, down_payment: float) -> str:
    """
    Vypočítá podrobnosti hypotečního úvěru a vrátí výsledek jako formátovaný řetězec. Všechny vstupy jsou povinné.

    :loan_amount (float): Celková výše úvěru před započtením akontace.
    :annual_interest_rate (float): Roční úroková sazba (v procentech).
    :loan_term_years (int): Doba splácení úvěru v letech.
    :down_payment (float): Zaplacená akontace.
    
    :returns: Formátované shrnutí hypotečního úvěru.
    """
    # Převod vstupních hodnot
    principal = loan_amount - down_payment
    monthly_interest_rate = annual_interest_rate / 100 / 12
    number_of_payments = loan_term_years * 12

    # Případ nulové úrokové sazby
    if monthly_interest_rate == 0:
        monthly_payment = principal / number_of_payments
    else:
        monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments) / \
                          ((1 + monthly_interest_rate) ** number_of_payments - 1)

    total_payment = monthly_payment * number_of_payments
    total_interest = total_payment - principal

    # Vytvoření formátovaného výsledného řetězce
    result = (
        f"--- Shrnutí hypotéky ---\n"
        f"Výše úvěru: {loan_amount:,.2f} Kč\n"
        f"Akontace: {down_payment:,.2f} Kč\n"
        f"Částka úvěru po akontaci: {principal:,.2f} Kč\n"
        f"Úroková sazba: {annual_interest_rate:.2f} %\n"
        f"Doba splácení: {loan_term_years} let\n\n"
        f"Měsíční splátka: {monthly_payment:,.2f} Kč\n"
        f"Celkem zaplacený úrok: {total_interest:,.2f} Kč\n"
        f"Celkové náklady na úvěr: {total_payment:,.2f} Kč\n"
    )

    return result
