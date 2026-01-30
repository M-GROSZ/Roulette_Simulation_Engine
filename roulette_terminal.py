import pandas as pd
import matplotlib.pyplot as plt
import simulation_engine as engine

def main():
    print("--- Monte Carlo Roulette Simulation (CLI) ---")
    try:
        rounds = int(input("Enter number of rounds to simulate (e.g., 100): "))
    except ValueError:
        rounds = 100

    players = [
        {'name': 'RandomBot', 'balance': 1000, 'wins': 0, 'rounds_played': 0},
        {'name': 'GreenHunter', 'balance': 1000, 'wins': 0, 'rounds_played': 0},
        {'name': 'MartyRed', 'balance': 1000, 'wins': 0, 'rounds_played': 0},
        {'name': 'MartyBlack', 'balance': 1000, 'wins': 0, 'rounds_played': 0},
    ]

    balance_history = []

    # Setup Plot
    plt.ion()
    fig, ax = plt.subplots(figsize=(10, 6))
    lines = {}
    colors = ['blue', 'green', 'red', 'black']
    
    for idx, p in enumerate(players):
        line, = ax.plot([], [], label=p['name'], color=colors[idx])
        lines[p['name']] = line

    ax.set_xlim(0, rounds)
    ax.set_ylim(0, 2000)
    ax.legend()
    ax.set_title("Capital Evolution")
    ax.set_xlabel("Rounds")
    ax.set_ylabel("Balance ($)")

    # === MAIN LOOP ===
    print(f"\nSimulating {rounds} rounds...")
    
    for i in range(rounds):
        engine.process_round(players)
        
        # Record Data
        current_balances = {'Round': i}
        for player in players:
            current_balances[player['name']] = player['balance']
        balance_history.append(current_balances)

        # Update Plot periodically
        if i % 10 == 0:
            df = pd.DataFrame(balance_history)
            for name, line in lines.items():
                line.set_data(df['Round'], df[name])
            plt.draw()
            plt.pause(0.001)

    plt.ioff()
    print("\n✓ Simulation Complete.")
    
    # Final Stats
    print("\nFINAL RESULTS:")
    for p in players:
        profit = p['balance'] - 1000
        print(f"{p['name']:<12} | Balance: ${p['balance']:.2f} | Profit: ${profit:.2f}")

    plt.show()

if __name__ == "__main__":
    main()