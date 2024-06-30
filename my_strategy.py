from base_strategy import BaseStrategy
import backtrader as bt

class CustomIchimokuIndicator(bt.Indicator):
    """Custom Ichimoku Cloud indicator."""
    lines = ("tenkan", "kijun", "senkou_a", "senkou_b")
    params = (("tenkan_period", 9), ("kijun_period", 26), ("senkou_period", 52))

    def __init__(self):
        self.addminperiod(self.params.tenkan_period)
        self.addminperiod(self.params.kijun_period)
        self.addminperiod(self.params.senkou_period)

    def next(self):
        high, low, close = self.data.high, self.data.low, self.data.close
        high_tenkan = max(high.get(-self.params.tenkan_period + 1, 0))
        low_tenkan = min(low.get(-self.params.tenkan_period + 1, 0))
        tenkan = (high_tenkan + low_tenkan) / 2

        high_kijun = max(high.get(-self.params.kijun_period + 1, 0))
        low_kijun = min(low.get(-self.params.kijun_period + 1, 0))
        kijun = (high_kijun + low_kijun) / 2

        senkou_a = (tenkan + kijun) / 2

        high_senkou = max(high.get(-self.params.senkou_period + 1, 0))
        low_senkou = min(low.get(-self.params.senkou_period + 1, 0))
        senkou_b = (high_senkou + low_senkou) / 2

        self.lines.tenkan[0] = tenkan
        self.lines.kijun[0] = kijun
        self.lines.senkou_a[0] = senkou_a
        self.lines.senkou_b[0] = senkou_b


class BackTestStrategy(BaseStrategy):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ichimoku = CustomIchimokuIndicator()

    def execute(self):
        """Define the trading logic based on the Ichimoku Cloud indicator.

        Returns:
        int: Trading signal: 1 (long), -1 (sell), or None if no signal.
        """
        if self.ichimoku.tenkan[0] > self.ichimoku.kijun[0] and self.ichimoku.senkou_a[0] > self.ichimoku.senkou_b[0]:
            return 1  # Long signal
        elif self.ichimoku.tenkan[0] < self.ichimoku.kijun[0] and self.ichimoku.senkou_a[0] < self.ichimoku.senkou_b[0]:
            return -1  # Short signal
        return None  # No signal