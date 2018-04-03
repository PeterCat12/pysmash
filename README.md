# notifier

This branch includes a "notifier" for use with an ongoing smash.gg bracket. 
To use, simply run the notifier.py and follow the directions displayed.
The format for tournaments/events is as follows:
https://smash.gg/tournament/genesis-5/events/melee-singles

The tournament name is what follows /tournament/, and the event name is what follows /events/.

# pysmash

[![Build Status](http://drone.peterballz.com/api/badges/PeterCat12/pysmash/status.svg)](http://drone.peterballz.com/PeterCat12/pysmash)

Pysmash provides python bindings for the
[Smash.gg!](https://smash.gg) [API](https://help.smash.gg/hc/en-us/articles/217471947-API-Access).


# Requirements

- requests==2.12.1


# Installation

    pip install pysmash

# Basic Usage

Currently, Smash.gg's developer API is public and fairly nascent. I recommended that you cache your responses from this wrapper to avoid hammering Smash.gg's API as some of these calls are fairly "expensive" (for instance, to grab a complete list of players/entrants for a tournament, this wrapper needs to make 1 call to grab a list of bracket id's and then 1 call PER bracket to grab every entrant in that bracket).

I've organized the methods on the `SmashGG` class into three types. `MetaData routes`, `General/Convenience routes`, and `Bracket routes`. Some result sets might be very LARGE depending on the size of the tournament. This library does not currently have any sort of paging for large result sets.


# MetaData Method Usage

```python
import pysmash
# init the wrapper class
smash = pysmash.SmashGG()

# All results are represented as normal Python dicts
# MetaData Method usage

  # show meta information for hidden-bosses-4
  tournament = smash.tournament_show("hidden-bosses-4-0")
  print(tournament)

  tournament_with_bracket_ids = smash.tournament_show_with_brackets("hidden-bosses-4-0", 'wii-u-singles')
  print(tournament_with_bracket_ids)

  # show meta information with a list of phases
  tournament_with_phase_information = smash.tournament_show("hidden-bosses-4-0", ['phase'])
  print(tournament_with_phase_information)

  # show meta information with a list of groups (AKA bracket meta data)
  tournament_with_group_information = smash.tournament_show("hidden-bosses-4-0", ['groups'])
  print(tournament_with_group_information)

  # show meta information with a list of events
  tournament_with_event_information = smash.tournament_show("hidden-bosses-4-0", ['event'])
  print(tournament_with_event_information)

  #show meta information with all three params
  tournament_full_meta = smash.tournament_show("hidden-bosses-4-0", ['phase', 'groups', 'event'])
  print(tournament_full_meta)

```

# Convenience Method Usage

```python
import pysmash
# init the wrapper class
smash = pysmash.SmashGG()

# All results are represented as normal Python dicts
# Convenience Method usage

  # show JUST a list of events for a tournament (excludes meta data info)
  events = smash.tournament_show_events('hidden-bosses-4-0')
  print(events)

  # Shows a complete list of sets given tournament and event names
  # By default, this method ignores sets without a recorded score (Smash.gg "oddity". Either the set was not played or the set
  # potentially fed into another bracket.); these sets can be viewed by passing False for filter_current.
  # Additionally, it is possible to view sets that are not yet ready to be played by passing False for filter_future
  # If one wants to exclude already completed sets, likely for the use of an application that hooks into brackets real-time
  # False can be passed for filter_completed
  sets = smash.tournament_show_sets('hidden-bosses-4-0', 'wii-u-singles')
  print(sets) # note: result might be VERY large for larger tournaments.

  # Shows a complete list of players given tournament and event names
  players = smash.tournament_show_players('hidden-bosses-4-0', 'wii-u-singles')
  print(players)

  # Shows a complete list of bracket ids given tournament and event names
  brackets = smash.tournament_show_event_brackets('hidden-bosses-4-0', 'wii-u-singles')
  print(brackets)

  # Shows player info and a list of every set that player competed in given tournament and event names
  # By default, this method ignores sets without a recorded score (Smash.gg "oddity". Either the set was not played or the set
  # potentially fed into another bracket.); these sets can be viewed by passing False for filter_current.
  # Additionally, it is possible to view sets that are not yet ready to be played by passing False for filter_future
  # If one wants to exclude already completed sets, likely for the use of an application that hooks into brackets real-time
  # False can be passed for filter_completed
  player_sets = smash.tournament_show_player_sets('hidden-bosses-4-0', 'DOM', 'wii-u-singles')
  print(player_sets)

  #Show sets between two players for a given tournament and event names
  # This method ignores sets without a recorded score (Smash.gg "oddity". Either the set was not played or the set
  # potentially fed into another bracket.)
  player_head_to_head = smash.tournament_show_head_to_head('hidden-bosses-4-0', 'giant', 'hamada', 'wii-u-singles')
  print(player_head_to_head)

  # OR set the default event name for convenience
  smash.set_default_event('wii-u-singles')
  players = smash.smash.tournament_show_players('hidden-bosses-4-0') # <- event name omitted
  sets =  smash.tournament_show_sets('hidden-bosses-4-0') # <- event name omitted
  player_sets = smash.tournament_show_player_sets('hidden-bosses-4-0', 'DOM') # <- event name omitted
  player_head_to_head = smash.tournament_show_head_to_head('hidden-bosses-4-0', 'giant', 'hamada', 'wii-u-singles')
```

# Bracket Method Usage

```python
import pysmash

  # init the wrapper class
  smash = pysmash.SmashGG()

  # All results are represented as normal Python dicts
  # Bracket Method usage

  # show players given a bracket_id
  brackets = smash.tournament_show_event_brackets('hidden-bosses-4-0', 'wii-u-singles')
  bracket_players = smash.bracket_show_players(brackets['bracket_ids'][0])  # <- bracket_id
  # bracket_players = smash.bracket_show_players(224997) # <- if you know the id before hand
  print(bracket_players)

  # show sets for a bracket
  # By default, this method ignores sets without a recorded score (Smash.gg "oddity". Either the set was not played or the set
  # potentially fed into another bracket.); these sets can be viewed by passing False for filter_current.
  # Additionally, it is possible to view sets that are not yet ready to be played by passing False for filter_future
  # If one wants to exclude already completed sets, likely for the use of an application that hooks into brackets real-time
  # False can be passed for filter_completed
  brackets = smash.tournament_show_event_brackets('hidden-bosses-4-0', 'wii-u-singles')
  sets = self.smash.bracket_show_sets(brackets['bracket_ids'][0]) # <- bracket_id
  # sets = self.smash.bracket_show_sets(225024) # <- if you know the id before hand
  print(sets)
```

See [smash.gg](https://help.smash.gg/hc/en-us/articles/217471947-API-Access) for full API documentation.


# Running the unit tests

Pysmash comes with a set of unit tests. These tests are not comprehensive. They ensure that Pysmash
is getting results from smash.gg and that the responses adhere to the outlined contracts [below](#basic-responses).

In order to test behavior of the python bindings, API calls must be made to Smash.gg. These calls DO take awhile
so I encourage you to run tests individually and not very often.

    $ python pysmash/tests.py
    ........
    ----------------------------------------------------------------------
    Ran 20 tests in 82.314s

    OK


# Method Responses

**Method Signature:**
`tournament_show(tournament_name, params=[])`

**Response:**
```python
{
	"links": {
		"facebook": "https://www.facebook.com/events/1821627474736778/"
	},
	"venue_name": "Poplar Creek Bowl",
	"state_short": "IL",
	"venue_addresss": "2354 W Higgins Rd, Hoffman Estates, Illinois 60169",
	"details": "Hidden Bosses is an Arcadian tournament for non power ranked players in every state. This ...",
  'start_at': '1475337600',
  'end_at': '1475338600',
  'phases': [
    {
      'type_id': 1,
      'event_id': 17850,
      'phase_id': 70445,
      'phase_name': 'Bracket',
      'is_exhibition': False
    },
    ...
  ],
  'groups': [
    {
      'title': None,
      'group_id': 224997,
      'phase_id': 70445,
      'winners_target_phase': 70465
    },
    ...
  ],
  'events': [
    'wii-u-singles',
    'wii-u-doubles'
  ]
	"tournament_id": 3742,
	"tournament_full_source_url": "tournament/hidden-bosses-4-0",
	"name": "Hidden Bosses 4.0",
}
```

**Method Signature:**
`tournament_show_with_brackets(tournament_name, event='', params=[])`

**Response:**
```python
{
  'venue_name': 'Poplar Creek Bowl',
  'name': 'Hidden Bosses 4.0',
  'details': "Hidden Bosses is an Arcadian tournament for non power ranked players in every state. This ...",
  'start_at': '1475337600',
  'end_at': '1475338600',
  'tournament_id': 3742,
  'bracket_ids':
    [
      '224997', '225017', '225018', '225019', '225020', '225021', '225022', '225023', '225024', '225025'
    ],
  'state_short': 'IL',
  'event_name': 'Wii U Singles',
  'tournament_full_source_url': 'tournament/hidden-bosses-4-0',
  'venue_addresss': '2354 W Higgins Rd, Hoffman Estates, Illinois 60169',
  'links': {
    'facebook': 'https://www.facebook.com/events/1821627474736778/'
  },
  'bracket_full_source_url': 'tournament/hidden-bosses-4-0/event/wii-u-singles'}
```

**Method Signature:**
`tournament_show_events(tournament_name)`

**Response:**
```python
  ['wii-u-singles', 'wii-u-doubles']
```

**Method Signature:**
`tournament_show_event_brackets(tournament_name, event='')`

**Response:**
```python
{
  'bracket_full_source_url': 'tournament/hidden-bosses-4-0/event/wii-u-singles',
  'event_name': 'Wii U Singles'
  'bracket_ids': [
    '224997', '225017', '225018', '225019', '225020', '225021', '225022', '225023', '225024', '225025'
  ]
}
```

**Method Signature:**
`tournament_show_sets(tournament_name, event='')`

**Response:**
```python
[
  {
  	"loser_id": "None",
  	"entrant_1_id": "321247",
  	"id": "5979543",
  	"short_round_text": "pools",
  	"bracket_id": "224997",
  	"entrant_2_id": "None",
  	"medium_round_text": "pools",
  	"full_round_text": "pools",
  	"winner_id": "321247"
    },
  ...
]
```

**Notes:**
- This method ignores sets without a recorded score (Smash.gg "oddity". Either the set was not played or the set fed into another bracket.)

**Method Signature:**
`tournament_show_head_to_head('hidden-bosses-4-0', 'giant', 'hamada', 'wii-u-singles')`

**Response:**
```python
{
  'player': {
    'country': 'United States',
    'lname': 'Wensel',
    'final_placement': 25,
    'tag': 'Giant',
    'entrant_id': 321406,
    'seed': 25, 'state':
    'IL', 'fname': 'Peter'
  },
  'sets': [
    {
      'opponent_info': {
        'country': 'United States',
        'lname': 'Ismail',
        'final_placement': 17,
        'tag': 'Hamada',
        'entrant_id': 315244,
        'seed': 8,
        'state': 'IL',
        'fname':
        'Mohammed'
      },
      'entrant_1_id': '315244',
      'entrant_1_score': 2,
      'player_id': 321406,
      'medium_round_text': 'pools',
      'opponent_id': 315244,
      'short_round_text': 'pools',
      'winner_id': '315244',
      'loser_id': '321406',
      'full_round_text': 'pools',
      'bracket_id': '225023',
      'id': '5982524',
      'entrant_2_score': 1,
      'entrant_2_id': '321406'
    },
    ...
  ]
}
```

**Method Signature:**
`tournament_show_players(tournament_name, event='')`

**Response:**
```python
[
  {
  	"entrant_id": 323478,
  	"final_placement": 49,
  	"seed": 101,
  	"fname": "Emilio",
  	"state": "IL",
  	"lname": "Feregrino",
  	"country": "United States",
  	"tag": "Wumbo"
  },
  ...
]
```

**Method Signature:**
`tournament_show_player_sets(tournament_name, player_tag, event='')`

**Response:**
```python
{
  "player": {
  	"seed": 1,
  	"fname": "Dominic ",
  	"final_placement": 7,
  	"state": "IL",
  	"tag": "DOM",
  	"lname": "DalDegan",
  	"country": "United States",
  	"entrant_id": 321247
  },
  "sets:" [
      {
        "id": "5984642",
        "player_id": 321247,
        "opponent_id": 296100,
        "entrant_1_id": "321247",
        "entrant_2_id": "296100",
        "entrant_1_score": 2,
        "entrant_2_score": 1,
        "winner_id": "296100",
        "bracket_id": "225024",
        "loser_id": "321247",
        "short_round_text": "L5",
        "medium_round_text": "Losers 5",
        "full_round_text": "Losers Round 5",
        "opponent_info": {
          "seed": 5,
          "fname": "Joseph",
          "final_placement": 2,
          "state": "IL",
          "tag": "Panda Bair",
          "lname": "Morales",
          "country": "United States",
          "entrant_id": 296100
        },
      },
    ...
  ]
}
```

**Method Signature:**
`bracket_show_players(bracket_id)`

**Response:**
```python
[
  {
    'fname': 'Dominic ',
    'state': 'IL',
    'final_placement': 7,
    'seed': 1,
    'entrant_id': 321247,
    'lname': 'DalDegan',
    'country': 'United States',
    'tag': 'DOM'
  },
  ...
]
```

**Method Signature:**
`bracket_show_sets(bracket_id)`

**Response:**
```python
[
  {
    'id': '5984600',
    'entrant_2_id': '315958',
    'entrant_1_score': 2,
    'medium_round_text': 'Winners 1',
    'loser_id': '315958',
    'full_round_text': 'Winners Round 1',
    'bracket_id': '225024',
    'entrant_1_id': '321247',
    'winner_id': '321247',  
    'short_round_text': 'W1',
    'entrant_2_score': 1
  },
  ...
]
```
