from homework.b_in_proc_out.output import TAX_RATE, get_sales_tax_amount, get_tip_amount

def main() -> None:
    meal_str = input("Enter meal amount (e.g., 20.00): ").strip()
    tip_str = input("Enter tip rate as a DECIMAL (e.g., 0.15 for 15%): ").strip()

    meal_amount = float(meal_str)
    tip_rate = float(tip_str)  # Expect decimal form (0.15 = 15%)

    sales_tax = get_sales_tax_amount(meal_amount)
    tip_amount = get_tip_amount(meal_amount, tip_rate)
    total = meal_amount + sales_tax + tip_amount

    print(f"Meal Amount:   {meal_amount:.2f}")
    print(f"Sales Tax:     {sales_tax:.2f}")
    print(f"Tip Amount:    {tip_amount:.2f}")
    print(f"Total:         {total:.2f}")

if __name__ == "__main__":
    main()
    
