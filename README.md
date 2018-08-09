# PBAW - a Python Battle.net API Wrapper ( Work in Progress )

PBAW stands for `Python Battle.net API Wrapper`, a Python module focusing on simplifying the Battle.net API access. Keep in mind that I am a student, so I can't say this project is flawless. I will do my best to always improve the code and to update it whenever the API changes.

## Installation

*For the moment, `pip` is not supported since the developpement of PBAW has just started.*

*`PBAW` has been developed with Python 3.4. However, I did not try it with other versions of Python yet.*

Clone the project in your Python Project, and import it directly in your code.

## Quickstart

To use `PBAW`, you need a [Battle.net Developper API KEY](https://dev.battle.net/), and have knowledge of the [Battle.net API Docs](https://dev.battle.net/io-docs). The knowledge of the API docs is really important, since it is a wrapper, and all it does is wrapping the docs. 

Then, you'll have to copy `local_config_example.py` to `local_config.py`, and change the values of `API_KEY` and `SECRET_KEY` in it according to your own credentials. This is very important, since without it, the module will **not work**.

Once you are okay with that, you can instantiate the APIs you want like the following:

```python
from PBAW.pbaw import Pbaw

# Create an instance of Pbaw with the given API Key
wowc = Pbaw.WowC()
```

And that's it ! This module has been developped to be easy to use, are as close as possible of the official Battle.net Docs. For instance, if you want to see the `Members` of the guild `Real Good Guys` on the `eu` serveur, realm `Sargeras`, and you want the result to be in `en_GB`, then you will have to do:
```python
wowc.guild_profile.members(server='eu', realm='Sargeras', guildName='Real Good Guys', locale='en_GB')
```

*A detailed doc will be uploaded on the Github soon.*

And you will receive a `JSON` in return.

## Documentation

*There is no documentation as of now. It will be available as soon as possible.*

Currently, **PBAW** can make API calls to:
* *World of Warcraft Community API (all servers)* - `wowc = Pbaw.WowC()`
* *Diablo 3 Community API (all servers)* - `d3c = Pbaw.D3C()`
* *Starcraft 2 Community API (all servers)* - `sc2c = Pbaw.SC2C()`

You can find the current progression of the project [here](https://github.com/DylanCa/PBAW/projects).

Feel free to [open an issue](https://github.com/DylanCa/PBAW/issues) whenever you feel like it is required.

Finally, you can send me a mail if you want: dylan.cattelan@gmail.com.

## License

**PBAW** is free of use, either for personnal or commercial use. A simple link to this **Github Repo** is enough.