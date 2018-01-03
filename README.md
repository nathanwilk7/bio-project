# How to get started
```
git clone https://github.com/nathanwilk7/bio-project
cd final-project/
wget https://s3.amazonaws.com/mod-bio-project/averaged_promoters.json &
wget https://s3.amazonaws.com/mod-bio-project/averaged_repressors.json
```
This will probably take a few minutes. Make sure you have matplotlib and networkx installed
```
pip install matplotlib
pip install networkx
```
Creating the Query object will take a minute or so, but queries on it should be near instantaneous.
If you have Jupyter Notebook
```
jupyter notebook
````
Otherwise
```
python final.py
```
Feel free to modify the source code and play with the API.
