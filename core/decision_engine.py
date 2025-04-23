import importlib
import os

STRATEGY_FOLDER = "strategies"

def load_strategies():
    strategies = []
    for file in os.listdir(STRATEGY_FOLDER):
        if file.endswith(".py") and not file.startswith("__"):
            module_name = f"{STRATEGY_FOLDER}.{file[:-3]}"
            module = importlib.import_module(module_name)
            if hasattr(module, 'generate_signal'):
                strategies.append(module.generate_signal)
    return strategies

def run_decision_engine(df):
    signals = []
    strategies = load_strategies()

    for strategy in strategies:
        try:
            signal = strategy(df)
            signals.append(signal)
        except Exception as e:
            print(f"Błąd w strategii {strategy.__name__}: {e}")

    # Decyzja na podstawie większości sygnałów
    if signals.count('BUY') > signals.count('SELL') and signals.count('BUY') > signals.count('HOLD'):
        return 'BUY'
    elif signals.count('SELL') > signals.count('BUY') and signals.count('SELL') > signals.count('HOLD'):
        return 'SELL'
    else:
        return 'HOLD'
