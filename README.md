Markdown# 🎲 Monte Carlo Roulette Simulation Engine

![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/frontend-streamlit-red)
![Docker](https://img.shields.io/badge/docker-containerized-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/maintenance-active-brightgreen)

> **A high-performance stochastic simulation tool designed to visualize the efficiency of progressive betting systems in a negative expected value (EV) environment.**

---

### ⚠️ IMPORTANT DISCLAIMER

**This project is for educational and simulation purposes only.** It demonstrates mathematically that **no betting system can beat the house edge** in the long run. It does not promote or encourage gambling in any form. 

If you or someone you know is struggling with gambling addiction, please seek help immediately. [See Resources below](#-gambling-addiction-resources).

---

## 📑 Table of Contents
1. [Project Overview](#-project-overview)
2. [Why This Project Exists](#-why-did-i-build-this)
3. [Key Features](#-key-features)
4. [Architecture & Design](#-architecture--design)
5. [Mathematical Theory](#-mathematical-theory)
6. [Installation & Usage](#-installation--usage)
7. [Project Structure](#-project-structure)
8. [Roadmap](#-roadmap)
9. [Gambling Addiction Resources](#-gambling-addiction-resources)

---

## 🔭 Project Overview

This tool utilizes the **Monte Carlo method** to simulate thousands of roulette spins, demonstrating the **Law of Large Numbers**. 

The primary goal is to analyze how different betting strategies (Flat betting vs. Progressive systems like Martingale) perform over time against the "House Edge" (2.7% in European Roulette).

**Core Problem Solved:**
Many gamblers believe in "winning systems." This engine mathematically proves that in an environment with $EV < 0$ (Negative Expected Value), variance may create short-term profits, but long-term ruin is statistically inevitable.

---

## 💡 Why Did I Build This?

To show that **no betting system beats math**. Every strategy looks good short-term, but the house edge always wins eventually.

This project is perfect for:
* Understanding probability and stochastic processes.
* Learning why casinos always profit.
* Demonstrating to friends why their "foolproof system" isn't foolproof.
* **Visualizing the concept of "Ruin" in financial modeling.**

---

## 🌟 Key Features

* **⚡ High-Speed Simulation Engine:** Decoupled logic capable of processing thousands of iterations per second.
* **📊 Dual Interface:**
    * **Web Dashboard (Streamlit):** Interactive plotting, parameter tuning, and real-time visualization.
    * **CLI (Command Line):** Headless mode for rapid bulk data generation.
* **🐳 Dockerized Environment:** Fully containerized for consistent deployment.
* **📉 Advanced Strategies:**
    * **RandomBot:** Baseline random betting.
    * **GreenHunter:** High variance (betting on 0).
    * **Martingale:** The famous "double up after loss" strategy.
* **💾 Data Export:** Seamless export to CSV for further analysis.

---

## 🏗 Architecture & Design

The project follows the **Separation of Concerns (SoC)** principle. The core logic is isolated from the presentation layer.

```mermaid
graph TD;
    User-->|Inputs Params|UI[Streamlit / CLI];
    UI-->|Calls|Engine[simulation_engine.py];
    Engine-->|Returns State|UI;
    UI-->|Visualizes|Charts[Plotly/Matplotlib];
    Engine-->|Exports|CSV[Data File];
📐 Mathematical TheoryThe House EdgeIn European Roulette, there are 37 pockets (0-36). The payout for a color bet is 1:1.The probability of winning on Red is:$$P(win) = \frac{18}{37} \approx 48.65\%$$The Expected Value ($EV$) for a $1 bet is:$$EV = (1 \times \frac{18}{37}) + (-1 \times \frac{19}{37}) \approx -0.027$$This means for every $100 bet, the player is statistically expected to lose $2.70.The Martingale FailureThe simulation implements the Martingale strategy (doubling bet after loss).While this seems to recover losses, the simulation demonstrates Exponential Growth. A losing streak of 10 rounds requires a bet of:$$Bet_{10} = B \times 2^{10} = 10 \times 1024 = 10,240$$This rapidly exceeds table limits or player bankroll, leading to catastrophic collapse.⚙️ Installation & UsageMethod 1: Docker (Recommended)Isolate the environment and run essentially anywhere without installing Python locally.Bash# 1. Build the image
docker build -t roulette-sim .

# 2. Run the container (Access at http://localhost:8501)
docker run -p 8501:8501 roulette-sim
Method 2: Local DevelopmentBash# 1. Clone the repository
git clone [https://github.com/YOUR_USERNAME/roulette-monte-carlo.git](https://github.com/YOUR_USERNAME/roulette-monte-carlo.git)
cd roulette-monte-carlo

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the App
streamlit run roulette_app.py
📂 Project StructurePlaintextroulette-monte-carlo/
│
├── 📄 simulation_engine.py    <-- [CORE] The "Brain". Pure Python logic.
├── 📄 roulette_app.py         <-- [UI] Streamlit Web Application.
├── 📄 roulette_cli.py         <-- [UI] Terminal/Console Application.
│
├── 📄 Dockerfile              <-- Container configuration.
├── 📄 requirements.txt        <-- Python dependencies.
├── 📄 README.md               <-- Documentation.

🚀 Roadmap[ ] American Roulette Support: Add "00" pocket logic to compare House Edge impact.[ ] Unit Tests: Implementation of pytest for the engine core logic.[ ] Machine Learning Agent: A Reinforcement Learning (RL) bot trying to minimize losses.🆘 Gambling Addiction ResourcesReal gambling = real money loss. If you have a gambling problem, please seek help from a professional support organization.Global: Gamblers Anonymous InternationalUSA: Call 1-800-522-4700 (National Problem Gambling Helpline)UK: GamCarePoland: 801 889 880 (Telefon Zaufania)📄 LicenseDistributed under the MIT License.© 2025 by M-GROSZ