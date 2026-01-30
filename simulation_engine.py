import random

# European Roulette Constants
RED_NUMBERS = {
    1, 3, 5, 7, 9, 12, 14, 16, 18,
    19, 21, 23, 25, 27, 30, 32, 34, 36
}

def spin_wheel() -> int:
    return random.randint(0, 36)

def get_wheel_color(number: int) -> str:
    if number == 0:
        return 'green'
    return 'red' if number in RED_NUMBERS else 'black'

# === STRATEGIES ===

def random_color_strategy() -> dict:
    return {
        'bet_type': 'color',
        'color': random.choice(['red', 'black', 'green']),
        'bet_amount': 10
    }

def green_hunter_strategy() -> dict:
    return {
        'bet_type': 'number',
        'number': 0,
        'bet_amount': 10
    }

def martingale_strategy(player: dict, target_color: str) -> dict:
    # Double bet after loss
    if player.get('last_result') == 'loss':
        current_bet = player.get('last_bet_amount', 10) * 2
    else:
        current_bet = 10
        
    # Safety cap: cannot bet more than balance
    current_bet = min(current_bet, player['balance'])

    return {
        'bet_type': 'color',
        'color': target_color,
        'bet_amount': current_bet
    }

# === GAME ENGINE ===

def process_round(players: list[dict]) -> dict:
    """Executes a single simulation step for all players."""
    
    winning_number = spin_wheel()
    winning_color = get_wheel_color(winning_number)
    
    for player in players:
        if player['balance'] <= 0:
            continue

        name = player['name']
        move = {}
        
        # Strategy Logic
        if name == 'RandomBot':
            move = random_color_strategy()
        elif name == 'GreenHunter':
            move = green_hunter_strategy()
        elif name.startswith('Marty'):
            target = 'red' if 'Red' in name else 'black'
            move = martingale_strategy(player, target)
            
        # Execute Bet
        bet_amount = move['bet_amount']
        player['rounds_played'] += 1
        player['last_bet_amount'] = bet_amount
        
        # Check Win
        won = False
        if move['bet_type'] == 'color' and move['color'] == winning_color:
            won = True
        elif move['bet_type'] == 'number' and move.get('number') == winning_number:
            won = True
            
        # Payouts
        if won:
            multiplier = 35 if move['bet_type'] == 'number' else 1
            player['balance'] += bet_amount * multiplier
            player['wins'] += 1
            player['last_result'] = 'win'
        else:
            player['balance'] -= bet_amount
            player['last_result'] = 'loss'
            
        # Check Bankruptcy
        if player['balance'] <= 0:
            player['balance'] = 0
            player['last_active_round'] = player['rounds_played']

    return {"number": winning_number, "color": winning_color}