# pysmash

Pysmash provides python bindings for the
[Smash.gg!](https://smash.gg) [API](https://help.smash.gg/hc/en-us/articles/217471947-API-Access).


# Requirements

- requests==2.10.0


# Installation

    pip install pysmash

# Basic Usage

Currently, Smash.gg's developer API is public and fairly nascent. I recommended that you cache your responses from this wrapper to avoid hammering Smash.gg's API as some of these calls are fairly "expensive" (for isntance, to grab a complete list of players/entrants for a tournament, this wrapper needs to make 1 call to grab a list of bracket id's and then 1 call PER bracket to grab every entrant in that bracket). More examples and a test suite will follow as time permits!


```python
import pysmash

  # init the wrapper class
  smash = pysmash.SmashGG()

  # All results are represented as normal Python dicts

  # show meta information for hidden-bosses-4
  tournament = smash.tournament_show("hidden-bosses-4-0")
  print(tournament)

  # show a list of events a tournament has
  events = smash.tournament_show_events('hidden-bosses-4-0')
  print(events)

  # show a complete list of sets for a tournament (Might have memory issues for majors)
  sets = smash.tournament_show_sets("hidden-bosses-4-0")
  print(sets)

  # show a complete list of players for a tournament (Might have memory issues for majors)
  players = smash.tournament_show_players("hidden-bosses-4-0")
  print(players)

  # show a list of sets a specific player has played
  player_sets = smash.tournament_show_player_sets("hidden-bosses-4-0", "DOM")
  print(player_sets)
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

# Basic Responses

All results from pysmash are normal python dictionaries

`smash.tournament_show("hidden-bosses-4-0")`
```python
{
	"links": {
		"facebook": "https://www.facebook.com/events/1821627474736778/"
	},
	"venue_name": "Poplar Creek Bowl",
	"state_short": "IL",
	"venue_addresss": "2354 W Higgins Rd, Hoffman Estates, Illinois 60169",
	"details": "Hidden Bosses is an Arcadian tournament for non power ranked players in every state. This is a great opportunity to discover new hidden bosses and talented unranked players and see how they compare in a tournament environment where top players are not present. Hidden Bosses will be a reoccuring tournament series with 1v1's and 2v2's at each tournament. \n\nWe will be at Poplar Creek Bowl again for HB4. The venue offers a lot of space as well as cheap and amazing food options. \n\nVenue fee is set at $10 (Paid pre-registration) and $15 (No pre-registration for at the door payment). Spectator passes are $5 which include friendlies and can be purchased at the door. Singles entry is $10, doubles is $10 per player, and crew battles are $5 per player.\n\nSchedule:\n\n2v2's Pools - 11 am - 12:30 pm\nTop 8 - 12:30 pm - 2 pm\nCrew Battles - 2 pm - 4 pm\n1v1 Pools:\nWave A - 3:30 pm - 5 pm\nWave B - 5 pm - 6:30 pm\n2nd Chance Bracket - 6:30 - 8 pm\nTop 32 - 7 pm - 10:30 pm\n\nPrevious top 3 finalists include (All are ineligible for 6 months):\n\nHB2:\n1. Nero\n2. Ge0\n3. Miloni\n\nHB3:\n1. McMuffin\n2. Waasabi\n3. Gamerhead\n\nList of players ineligible:\n\nIllinois:\n1. JJROCKETS\n2. Ned\n3. Tyroy\n4. NiTe\n5. Shel\n6. Dan\n7. BoScotty\n8. big_mak\n9. Bushi\n10. Naoto\n11. Demitus\n12. Seth\n13. JTWild\n14. Anonymous Moniker\n15. Hoenn\n16. Slowjoe\n17. Based Ren\n18. StarbasedFruit\n19. Sheen\n20. Atata\n\nWisconsin:\n1. Marshall\n2. Zolda\n3. PowPow\n4. Z2G\n5. Fons\n6. Akiro\n\nIowa: \n1. Sinnyboo242\n2. Ecnebanjo\n3. Chan_MM\n4. 2Jays\n5. Prophet\n6. Di King\n\nIndiana:\n1. Renegade\n2. Taka\n3. Krow\n4. Benson Obama\n5. Vemnzr\n6. XeroXen\n\nMichigan:\n1. Zinoto\n2. Loe1\n3. Rayquaza\n4. Ryuga\n5. Ally\n6. Regralht\n7. SETHsational\n8. Ksev\n9. Lou Rich\n10. Smasher1001\n11. TECHnology\n12. Mikey Lenetia\n13. Stewy\n14. Dicks\n15. Nom\n16. Coco\n17. Viev\n18. Nero (1st place at HB2)\n19. Ge0 (2nd place at HB2)\n20. Miloni (3rd place at HB2)\n\nSt. Louis:\n1. JSwiss\n2. Moti\n3. Zguh\n4. Flow Yo\n5. GenMuH\n\nOhio:\n1. Darkshad\n2. Katakiri\n3. H-Man\n4. Colinies\n5. CrazyColorz\n6. Munenori\n7. Tekno\n8. Karinole\n9. jt5565\n10. EMPR Eevee\n\n*** If your state is not listed on here and you are a PR'd player, message us to check first if you are eligible before registering.\n\nOnce you are registered, there are no refunds or transfers. This is to ensure that players that register will end up attending.",
	"tournament_id": 3742,
	"tournament_full_source_url": "tournament/hidden-bosses-4-0",
	"name": "Hidden Bosses 4.0"
}
```

`tournament_show_events(hidden-bosses-4-0)`
```python
  ['wii-u-singles', 'wii-u-doubles']
```

`smash.tournament_show_sets("hidden-bosses-4-0")`
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

`smash.tournament_show_players("hidden-bosses-4-0")`
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

`smash.tournament_show_player_sets("hidden-bosses-4-0", "DOM")`
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
