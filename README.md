# pysmash

Pysmash provides python bindings for the
[Smash.gg!](https://smash.gg) [API](https://help.smash.gg/hc/en-us/articles/217471947-API-Access).


# Requirements

- requests==2.10.0


# Installation

    pip install pysmash

# Usage

Currently, Smash.gg's developer API is public and fairly nascent. I recommended that you cache your responses from this wrapper to avoid hammering Smash.gg's API as some of these calls are fairly "expensive" (for isntance, to grab a complete list of players/entrants for a tournament, this wrapper needs to make 1 call to grab a list of bracket id's and then 1 call PER bracket to grab every entrant in that bracket). More examples and a test suite will follow as time permits!

```python
import pysmash

  # init the wrapper class
  smash = pysmash.SmashGG()

  # All results are represented as normal Python dicts

  # show meta information for hidden-bosses-4
  tournament = smash.tournament_show("hidden-bosses-4-0")
  print(result)

  # show a complete list of sets for a tournament (Might have memory issues for majors)
  sets = smash.tournament_show_sets("hidden-bosses-4-0")
  print(sets)

  # show a complete list of players for a tournament (Might have memory issues for majors)
  players = smash.tournament_show_players("hidden-bosses-4-0")
  print(players)
```

See [smash.gg](https://help.smash.gg/hc/en-us/articles/217471947-API-Access) for full API documentation.
