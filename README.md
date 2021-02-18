
# hack-program
my program lets you play a round of rock paper scissors and prints the result!
The computer will randomly select one of the options.

To run you can call 'python -m mymodule'





### Updates

Install this package locally with:

```bash
cd mypackage/
pip install -e .
```

This will install two CLI tools that can be called as follows:

```bash
mymodule --throw rock
```

```
        throw
0           0
1       paper
2       paper
3    scissors
4    scissors
..        ...
96   scissors
97       rock
98       rock
99      paper
100  scissors

[101 rows x 1 columns]
-----
most used throw: paper
-----
You threw: rock
I threw: scissors
Darn it, you beat me!
```


```bash
# run with default equal probabilities
mymodule2 --trials 1000 
```
```
I won 48.07% of 1000 trials (ties=326)
```

```bash
# run with biased probabilities
mymodule2 --trials 1000 --probs 0.1 0.1 0.8
```
```
I won 78.95% of 1000 trials (ties=164)
```