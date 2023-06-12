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
