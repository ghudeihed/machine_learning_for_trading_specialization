from nautilus_trader.model.enums import OrderSide, OrderType, TimeInForce
from nautilus_trader.model.events import OrderFilled
from nautilus_trader.model.identifiers import Symbol, Venue
from nautilus_trader.model.instruments import Instrument
from nautilus_trader.model.objects import Money, Price, Quantity
from nautilus_trader.model.position import Position
from nautilus_trader.model.tick import QuoteTick
from nautilus_trader.trading.strategy import Strategy
from nautilus_trader.trading.strategy_config import StrategyConfig

import numpy as np

class HurstExponentStrategy(Strategy):
    def __init__(self):
        super().__init__()
        self.hurst_window = 100  # Number of bars to use for Hurst exponent calculation

    def on_quote_tick(self, tick: QuoteTick):
        # Calculate the current Hurst exponent
        hurst = self.calculate_hurst_exponent(tick.price.to_decimal(), self.hurst_window)

        # Check if the Hurst exponent indicates a persistent or anti-persistent market
        if hurst > 0.5:
            # Persistent market, buy on bullish candles
            if self.last_candle_was_bullish():
                self.submit_order(
                    symbol=Symbol("EURUSD", Venue("IDEALPRO")),
                    order_side=OrderSide.BUY,
                    order_type=OrderType.MARKET,
                    time_in_force=TimeInForce.GTC,
                    quantity=Quantity(100000),
                )
        elif hurst < 0.5:
            # Anti-persistent market, buy on bearish candles
            if self.last_candle_was_bearish():
                self.submit_order(
                    symbol=Symbol("EURUSD", Venue("IDEALPRO")),
                    order_side=OrderSide.SELL,
                    order_type=OrderType.MARKET,
                    time_in_force=TimeInForce.GTC,
                    quantity=Quantity(100000),
                )

    def calculate_hurst_exponent(self, price_series: np.ndarray, window_size: int) -> float:
        # Implement the Hurst exponent calculation logic here
        # This is a simplified example, you may want to use a more robust method
        log_range = np.log([np.max(price_series[i:i+window_size]) - np.min(price_series[i:i+window_size]) for i in range(len(price_series)-window_size+1)])
        log_time = np.log([window_size for _ in range(len(price_series)-window_size+1)])
        return np.polyfit(log_time, log_range, 1)[0]

    def last_candle_was_bullish(self) -> bool:
        # Implement the logic to determine if the last candle was bullish
        # This is a simplified example, you may want to use more advanced technical analysis
        return self.last_quote_tick.price > self.last_quote_tick.prev_close

    def last_candle_was_bearish(self) -> bool:
        # Implement the logic to determine if the last candle was bearish
        # This is a simplified example, you may want to use more advanced technical analysis
        return self.last_quote_tick.price < self.last_quote_tick.prev_close

# Configure the strategy
config = StrategyConfig(
    symbol=Symbol("EURUSD", Venue("IDEALPRO")),
    starting_capital=Money(100000, "USD"),
    commission_rate=0.0005,  # 0.05% commission rate
)

# Create and run the strategy
strategy = HurstExponentStrategy()
strategy.run_backtest(config, "INTERACTIVE_BROKERS")