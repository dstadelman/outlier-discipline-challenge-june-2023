# outlier-discipline-challenge-june-2023
Company / Trade Conferences as Tradable Events

The Outlier Discipline Challenge for June 2023 takes place everyday in June. 

This is constitutes the mental side of the discipline challenge that I will work on for about three minutes a day.

I am going to research the possibility of company and trade conferences as tradeable events, starting with **AAPL and the Apple Worldwide Developers Conference (WWDC)**.

Hypothesis: 

* Before the event 
   * upwards skewed abnormal returns
   * implied volatilty expands
* After the event
   * implied volatility contracts

## 1 June 2023

* Started project and wrote hypothesis for the experiment
* Found [list of dates of WWDC](https://en.wikipedia.org/wiki/Worldwide_Developers_Conference)

## 2 June 2023

* VSCode and python 3.11.3 was already installed 
* Make a virtual python environment:
   * `python -m venv .venv`
* Switch to the new virtual environment:
   * Windows `source .venv/Scripts/activate`
   * Linux / MacOS ? `source .venv/bin/activate`
* Install some required libraries:
   * `pip install -r requirements.txt`
* Added the python script `download_data.py` to get the stock data using yfinance.
* Ran the newly created script to download the stock data using yfinance:
   * `python download_data.py`

## 3 June 2023

* Added `ipykernel` and `matplotlib` library to requirements. If you are following along you must install these:
   * `pip install -r requirements.txt`
* Started `load_study.ipynb`
   * Loaded AAPL data
   * Printed histogram

## 4 June 2023

* Added dates of WWDC and started to encode them into a python understandable format

## 5 June 2023

* Finished up adding the WWDC dates and putting them into python understandable format

## 6 June 2023

* Isolated the stock data to 20 trading days before and after WWDC
* Printed some charts with the stock data

## 7 June 2023

* Calculated skew and kurtosis of returns - AAPL is a little more negative skew with a more leptokurtic distribution than SPY.

## 8 June 2023

* Isolated time periods 20 trading days before, during, and 20 trading after the WWDC event.

## 9 June 2023

* Analyzed the retrieved stats with Erik

## 10 June 2023

* Exported close data to CSV.

## 11 June 2023

* Loaded close data into Excel and started taking a look at it.

## 12-14 June 2023

* Worked through some of the data in excel and found that there were on average positive returns before WWDC, negative returns during WWDC, and about flat returns after WWDC.

| | 20 days before | 10 days before | 5 days before |
| ----------- | ----------- | ----------- | ----------- |
| average	| 3.91%	| 3.32%	| 2.41% |
| stddev	| 10.04%	| 8.24%	| 4.72% |

| |	event return|
| ----------- | ----------- |
| average	| -1.24% |
| stddev	| 4.24% |


| |	20 days after	|10 days after	|5 days after |
| ----------- | ----------- | ----------- | ----------- |
|average	|0.67%	|-0.14%	|-0.22% |
|stddev	|8.32%	|5.27%	|3.47% |

## 15 June 2023

* Looked at IV around the events. 
* Marked `IV crush` TRUE if IV dropped by some amount (based on my eyeball) during the event. 
* Marked `greater IV crush than previous earnings?` TRUE if IV was greater the day before earnings vs before the most recent earnings announcement. 

| year | IV crush (IV greater than 10% IV30 drop) | IV crush than previous earnings? |
| 2023 | FALSE | FALSE |
| 2022 | FALSE | FALSE |
| 2021 | FALSE | FALSE |
| 2020 | FALSE | FALSE |
| 2019 | FALSE | FALSE |

* The only trade I can see over WWDC is one where if you are bullish AAPL before WWDC, you can have a little more conviction in the run up to the event. I don't see a trading strategy here.

## 16 June 2023

* Discussed trading biotech with Erik and the rest of the Outlier gang 

## 17 June 2023

* Read some of the getting started in biotech trading documents on https://www.biopharmcatalyst.com/

## 18 June 2023

* Investigated two popular biotech ETFs, IBB and XBI; XBI is equal weight while IBB is weighted. Looked at pricing of ATM straddles. 
* Marked up a candlestick chart and generated volatility cone for XBI.

## 19 June 2023

* Downloaded a list XBI holdings, loaded into TradingView, and flipped through the charts.

## 20 June 2023

* Started tracking upcoming catalysts; tomorrow ALDX.

## 21 June 2023

* Watched ALDX this morning. The stock was halted and wasn’t trading due to the announcement at market open. Once the stock opened, options seemed to take quite a bit of time to  open… maybe 5-10 minutes.
* ALDX opened down 50% but rallied off these lows to close down 27%

## 22 June 2023

* Learning more about biotech trading. I saw on a calendar that ICPT and SRPT were to have a PDUFA decision, but it didn’t seem to happen. This is not like earnings releases where it is known what day something is happening exactly!

## 23 June 2023

* Watched SRPT and ICPT . Much like an earnings release, SRPT reacted as you would expect with negative news (down 10%) while ICPT also received bad FDA news, but stock remained about the same price.
* I still don't really understand when exactly the news will be released and timeline of the stock response on PDUFA  announcements.

## 24 June 2023

* Worked on breadth indicator for XBI - in TradingView

## 25 June 2023

* Looked up biotech catalysts for this week!
* This week the decisions are on REGN ETON and AMRX.

## 26 Jun 2023
 
* The options market seems pretty wide in REGN and ETON. AMRX is still wide but not horrible.
* Read about AMRX’s trial of a Parkinson’s Disease drug and how it’s evaluated during the double blind test: https://investors.amneal.com/news/press-releases/press-release-details/2022/Amneal-Announces-U.S.-FDA-Filing-Acceptance-of-New-Drug-Application-for-IPX203-for-the-Treatment-of-Parkinsons-Disease/default.aspx 

## 27 Jun 2023

* Put on a one lot in AMRX, sold 2.5/5 call spread and sold the 2.5 put.

## 28 Jun 2023

* Started using thinkorswim's thinkBack feature to look at the results of historical PDUFA announcemnts: https://www.fdatracker.com/fda-calendar/












