# PBAW - a Python Battle.net API Wrapper ( Work in Progress )

PBAW stands for `Python Battle.net API Wrapper`, a Python module focusing on simplifying the Battle.net API access.

## Installation

*For the moment, `pip` is not supported since the developpement of PBAW has just started.*

*`PBAW` has been developed with Python 3.4. However, I did not try it with other versions of Python yet.*

Clone the project in your Python Project, and import it directly in your code.

## Quickstart

To use `PBAW`, you need a [Battle.net Developper API KEY](https://dev.battle.net/), and have knowledge of the [Battle.net API Docs](https://dev.battle.net/io-docs). The knowledge of the API docs is really important, since it is a wrapper, and all it does is wrapping the docs. 


Once you are okay with that, you can instantiate `PBAW` like the following:

```python
from PBAW.pbaw import Pbaw

# Create an instance of Pbaw with the given API Key
p = Pbaw('0123456789abcd')
```

And that's it ! This module has been developped to be easy to use, are as close as possible of the official Battle.net Docs. For instance, if you want to see the `Members` of the guild `Real Good Guys` on the `eu` serveur, realm `Sargeras`, and you want the result to be in `en_GB`, then you will have to do:
```python
p.wowc.guild_profile.members(server='eu', realm='Sargeras', guildName='Real Good Guys', locale='en_GB')
```

| Parameter |         Values         |    Default   |
|:---------:|:----------------------:|:------------:|
|  `server` | `eu`, `us`, `kr`, `tw` |     `eu`     |
|  `realm`  |      a realm name      | `archimonde` |
|  `guild`  |      a guild name      |  `jardiland` |
|  `locale` |        see docs        |    `en_US`   |

*A detailed doc will be uploaded on the Github soon.*

And you will receive a `JSON` in return.

## Documentation

*There is no official documentation as of now. It will be available as soon as possible.*

## License

**PBAW** is free of use, either for personnal or commercial use. A simple link to this **Github Repo** is enough.