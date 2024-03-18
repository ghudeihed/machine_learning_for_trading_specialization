## Question 1
If you believe that the price and volume history of an asset are all that is needed to design a trading strategy then you would would use an endogenous trading rule. What is the theoretical justification for using this type of strategy?
1 / 1 point

- Markets are efficient and fully incorporate all available information (both public and private).

- [X] Fundamental data such as historic earning and sales growth are already fully reflected in the current market price and so have no predictive power.
  
    - Correct
    Yes, if you instead believed that fundamental data have predictive value, then you should incorporate them into an exogenous trading rule.

- Asset prices follow a random walk with equal probabilities of increasing and decreasing

- [X] Asset and market prices tend to have momentum so that stocks whose prices are in an up trends tend to increase in value and those in a downtrend tend to decrease in value.

    - Correct
    Yes, if you believe that asset prices have momentum then price and volume data is all you need to make predictions of future prices.

## Question 2
The basic trading model parameters are entry signal,
 profit exit,
 stop-loss
 and time-out
. How can you use these parameters and machine learning to optimize your trading strategy?
1 / 1 point

- Vary the the type of entry signal and profit exit levels in backtesting with the objective of maximizing risk adjusted return (Sharpe ratio).

- [X] Vary the the type of entry signal, profit exit levels,  stop loss levels and trade completion time limits in backtesting with the objective of maximizing risk adjusted return (Sharpe ratio) within your tolerance for PnL volatility and maximum drawdown.

- Vary the the type of entry signal and profit exit levels in backtesting with the objective of maximizing profit.

    - Correct
    Yes, Sharpe ratio maximization leads to an optimal trading strategy as long as it is constrained by time limits, PnL volatility limits and maximum drawdown tolerance. This will give you a strategy with stop-loss levels that can be tolerated when you implement it in  live trading.

## Question 3
The main benefit of a dynamic stop loss over a static stop loss is that:
1 / 1 point

- Dynamic stop losses guarantee that your strategy will not make a loss even if it is stopped out.

- [X] Dynamic stop losses reduce the expected risk of your strategy.

- Dynamic stop losses increase your expected returns from a trading strategy.

    - Correct
    Yes. Dynamic stop losses, which maintain a fixed margin between the stop-loss level and the most favorable market price achieved, can reduce the maximum loss in a strategy (at worst the maximum loss is unaffected). This reduces the expected risk in the strategy but also make it more likely that you will be stopped out rather than profited out. This can have a negative impact on your expected return from a strategy.

## Question 4
Endogenous trading rules are often created by:
1 / 1 point

- [X] Technical analysts

- Statistical arbitrage traders

- Strategists

- Quantitative trading groups

    - Correct
    Yes, Technical analysts or chartists believe that all of the information necessary to create a trading rule or strategy is contained in the price and volume history of an asset. 