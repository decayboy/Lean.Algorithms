# Lean.Algorithms
Custom Algorithms for use for use with the Lean Algorithmic Trading Engine (C#, Python, F#)

## Basic Overview ##

Various Algorthim models that produce interesting results when applied assiduously in predictive market environments. Please backtest rigoursly before investing real money.

If you're going to run algorithms locally you'll need to install LEAN [installation instructions](https://github.com/QuantConnect/Lean#installation-instructions) to run in on your machine.

*Note* I reccommend Linux
#### [Ubuntu](https://github.com/QuantConnect/Lean#linux-debian-ubuntu)
By default, **miniconda** is installed in the users home directory (`$HOME`):
```
export PATH="$HOME/miniconda3/bin:$PATH"
wget https://cdn.quantconnect.com/miniconda/Miniconda3-4.3.31-Linux-x86_64.sh
bash Miniconda3-4.3.31-Linux-x86_64.sh -b
rm -rf Miniconda3-4.3.31-Linux-x86_64.sh
sudo ln -s $HOME/miniconda3/lib/libpython3.6m.so /usr/lib/libpython3.6m.so
conda update -y python conda pip
conda install -y cython pandas
```

Install clang and glib 2.0:
```
sudo apt-get -y install clang libglib2.0-dev
```

*Note:* There is a [known issue](https://github.com/pythonnet/pythonnet/issues/609) with python 3.6.5 that prevents pythonnet installation, please upgrade python to version 3.6.6:
```
conda install -y python=3.6.6
```
## Random Notes ##

The **GoogleTrends.py** algorithm is based on the [SeekingAlpha](https://seekingalpha.com/article/4202781-timing-market-google-trends-search-volume-data) article postulating that; *"Past research suggests that the relative change in the volume of Google searches for financial terms such as “debt” or “stocks” can be used to anticipate stock market trends."* 
The algorithm utilizes the monthly search term *debt* to predict price movements. It may be advisable to implement something like [Pytrends](https://github.com/GeneralMills/pytrends/blob/master/examples/example.py) and be aware that Google trends data contains the potential look-ahead bias. 

I'd reccomend contrasting other search terms with various assets to produce more interesting results
