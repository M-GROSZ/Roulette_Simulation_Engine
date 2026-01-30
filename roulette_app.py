import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import time
import simulation_engine as engine  # Import core logic

# Page Config
st.set_page_config(page_title="Stochastic Simulation Engine", page_icon="🎲", layout="wide")

st.title("🎲 Monte Carlo Roulette Simulation")
st.markdown("### Stochastic Analysis of Progressive Betting Systems")

# Sidebar Controls
st.sidebar.header("Simulation Parameters")
rounds = st.sidebar.slider("Number of Iterations", 10, 1000, 100)
speed = st.sidebar.slider("Animation Speed (ms)", 10, 500, 50) / 1000.0

# Initialize Players
players = [
    {'name': 'RandomBot', 'balance': 1000, 'wins': 0, 'rounds_played': 0},
    {'name': 'GreenHunter', 'balance': 1000, 'wins': 0, 'rounds_played': 0},
    {'name': 'MartyRed', 'balance': 1000, 'wins': 0, 'rounds_played': 0},
    {'name': 'MartyBlack', 'balance': 1000, 'wins': 0, 'rounds_played': 0},
]

if st.button("Run Simulation", type="primary"):
    # Containers for live updates
    chart_placeholder = st.empty()
    stats_placeholder = st.empty()
    
    balance_history = []
    
    # === MAIN SIMULATION LOOP ===
    for i in range(rounds):
        # Delegate logic to the engine
        result = engine.process_round(players)
        
        # Record Data
        current_balances = {'Round': i}
        for player in players:
            current_balances[player['name']] = player['balance']
        balance_history.append(current_balances)
        
        # Live Visualization (Update every few frames for performance)
        if i % 5 == 0 or i == rounds - 1:
            df = pd.DataFrame(balance_history)
            
            fig = go.Figure()
            for player_name in [p['name'] for p in players]:
                fig.add_trace(go.Scatter(
                    x=df['Round'], 
                    y=df[player_name], 
                    mode='lines', 
                    name=player_name
                ))
            
            fig.update_layout(
                title="Capital Evolution (Real-time)",
                xaxis_title="Iteration (Spin)",
                yaxis_title="Capital ($)",
                template="plotly_dark",
                height=500
            )
            chart_placeholder.plotly_chart(fig, use_container_width=True)
            time.sleep(speed)

    # Export Data
    balance_df = pd.DataFrame(balance_history)
    csv = balance_df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Export Data (CSV)", csv, "simulation_results.csv", "text/csv")