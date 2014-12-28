# Codon repeat visualisation tool

### Requirements
- Python 2 (2.7.6 or newer)
- Matplotlib python package (1.3.1 or newer)
- Plot.ly python package

### Usage
Run from terminal or command prompt using ```python codon_repeats.py f n p```.

- The first argument, **f**, is the name of the FASTA formatted file with it's extension e.g. RPRD2.fasta.
- The second argument, **n**, is the sequence number inside the FASTA file. By default, the first sequence is 0, the next 1, and so forth.
- The third argument, **p**, can either be `plotly` or `matplotlib`. Usage of either requires their respective package to be installed, but installation of both is not required if only one is used.

Matplotlib or plotly packages maybe installed using pip:

`pip install matplotlib`

`pip install plotly`

#### NOTE: Plotting with Plot.ly package
As the Plot.ly package involves uploading the data to their servers for hosting, log in credentials are required (a username and API key). These are available for free upon sign up for an account at http://plot.ly/. Once you get these, insert these values on line 118 of the script as follows:
```python
    #             username        API key
    py.sign_in('<<USERNAME>>', '<<API KEY>>')

```
This tool was featured in a blog post at http://www.scienceexposure.com/coding/codon-repeats-data-visualisation-tool/.
