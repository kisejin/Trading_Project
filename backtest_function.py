import backtrader as bt

# better net liquidation value view
class MyBuySell(bt.observers.BuySell):
    plotlines = dict(
        buy=dict(marker='$\u21E7$', markersize=12.0),
        sell=dict(marker='$\u21E9$', markersize=12.0)
    )
bt.observers.BuySell = MyBuySell

class CelebroCreator:
    def __init__(self, strategy, list_of_data, stake=100, cash=20000):
        self.cerebro = bt.Cerebro(cheat_on_open=True)

        self.cerebro.addstrategy(strategy)
        self.cerebro.addanalyzer(bt.analyzers.PyFolio, _name='pyfolio')
        self.cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='SharpeRatio')
        self.cerebro.addanalyzer(bt.analyzers.Returns, _name='Returns')
        self.cerebro.addobserver(bt.observers.Value)

        for data in list_of_data:
            self.cerebro.adddata(data)
        self.cerebro.broker.set_cash(cash)
        self.strats = self.cerebro.run()

    def show(self):
        print("Final Portfolio Value: %.2f" % self.cerebro.broker.getvalue())
        print("Total point return: ", (self.cerebro.broker.getvalue() - self.cerebro.broker.startingcash))


        sharpe_ratio = self.strats[0].analyzers.SharpeRatio.get_analysis()['sharperatio']
        # Plot the results
        figs = self.cerebro.plot(
            iplot=False, 
            # style="pincandle", 
            # width=60 * 10, height=40 * 10,
            figsize=(100, 80),
            sharpe_ratio=sharpe_ratio
        )
        
def check_valid_code(strategy, list_data):
    try:
        CelebroCreator(strategy,list_data)
        # return True, ""
    except Exception as e:
        error_message = extract_error_message(e)
        return False, error_message
    return True, ""