## CLI Options

Here is a full list of options that the simulator currently accepts:

```-d <x> <y>```

specifies the dimensions of the GoL, default is 50x50

```-s <string>```

specify the initial field as a string containing zeros and ones

example:

```main.py -d 3 4 -s 010110101010``` to get a 3x4 Field


```-i <float>```

specify the time between each turn


```--seed, -S <string>```

specify the seed for the random generator

```-tr <float>```

specify the chance to generate a live cell for the random generator


```-e <example>```

choose an example as the initial state


```-cli```

generate only CLI output


```-trace```

enable trace mode for the GUI output (red indicates a dying cell, green indicates a newborn cell)
