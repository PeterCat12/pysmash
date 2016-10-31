# pysmash
A python wrapper to smash.gg Developer API

Smash.gg API: https://help.smash.gg/hc/en-us/articles/217471947-API-Access

SmashGG's API is completely bananas. So if you see "crazy" manipulations to their responses it's due
to their insanity. For instance, to get player information like player names, you have to query their bracket
route with both parameters of `sets` and `entrants`. Just asking for `entrants` does NOT give you a players
information. In addition when both parameters are set, this information gets dumped into a mysteriously named `mutations` field that holds `contactInfo`.

I like smash.GG and what they do for the smash community but I hope they get their developers API into better shape soon.

For large tournaments, you might want to avoid asking for a complete list of sets due to possible memory constraints.

Caching responses from this Library is probably a good idea :)

If you have any issues or want to improve the wrapper, please open an issue/pull request.

10/30/2016
