import gc
from typing import List, Iterable, Dict, Tuple

import numpy as np
import pandas as pd

import eurostat
import yfinance as yf
from statsmodels.datasets import co2
from scipy.datasets import electrocardiogram


def get_electrocardiogram() -> pd.DataFrame:
    ecg = electrocardiogram()
    fs = 360
    return pd.DataFrame({
        'time': np.arange(ecg.size) / fs,
        'ecg': ecg
    })


def get_mauna_loa_co2() -> pd.DataFrame:
    return co2.load().data


def get_apple_5y() -> pd.DataFrame:
    df = yf.download('AAPL', period='5y')
    return df


def get_france_death_rate_20y() -> pd.DataFrame:
    country, nyears = 'FR', 20
    df = (
        eurostat.get_data_df('demo_mmonth')
        .rename(columns={r'geo\TIME_PERIOD': 'country'})
        .drop(columns=['freq', 'unit'])
    )
    df = df[~df['month'].isin(['TOTAL', 'UNK'])]
    month_mapping = {
        'M01': 'jan', 'M02': 'feb', 'M03': 'mar', 'M04': 'apr',
        'M05': 'may', 'M06': 'jun', 'M07': 'jul', 'M08': 'aug',
        'M09': 'sep', 'M10': 'oct', 'M11': 'nov', 'M12': 'dec'
    }
    df['month'] = df['month'].map(month_mapping)
    df = df.melt(id_vars=['month', 'country'], var_name='year', value_name='value')
    df = df.dropna()
    df['year'] = df['year'].astype(int)
    df['month'] = pd.Categorical(df['month'], categories=list(month_mapping.values()), ordered=True)
    df = df.sort_values(by=['year', 'month'])
    df = df[df['country'] == country]
    df = df[df['year'] > df['year'].max() - nyears]
    df['time'] = pd.date_range(start=f"{df['year'].min()}-01-01", periods=len(df), freq='ME')
    assert all(df['time'].dt.strftime('%b').str.lower() == df['month']), "Mismatch between 'time' and 'month' columns"
    df = df.reset_index(drop=True)
    return df


def get_switzerland_temperature():
    country, nyears = 'Switzerland', 20
    df = pd.read_csv('../data/GlobalLandTemperaturesByCountry.csv')
    df = df[df['Country'] == country]
    df['dt'] = pd.to_datetime(df['dt'])
    df = df.set_index('dt').resample('ME').agg({
        'AverageTemperature': 'mean',
        'AverageTemperatureUncertainty': 'mean',
        'Country': 'first',
    }).reset_index()
    cutoff_date = df['dt'].max() - pd.DateOffset(years=nyears)
    df = df[(df['dt'] >= cutoff_date) & (df['dt'].dt.year < 2013)]
    df = df.reset_index(drop=True)
    return df


def get_random_walk(seed: int, npoints: int = 100, variance: float = 1, drift: np.ndarray = None, seasonal: np.ndarray = None) -> np.ndarray:
    np.random.seed(seed)
    w = np.random.normal(loc=0, scale=np.sqrt(variance), size=npoints)
    if drift is not None:
        w += drift
    if seasonal is not None:
        w += seasonal
    return np.cumsum(w)
