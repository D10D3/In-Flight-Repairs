In Flight Repairs V0.6 By D10d3 A Text Adventure

Version History: V0.5 traversable map, inventory, and trigger-able events V0.6 Bug Fixing, discreet inventory

This is a very simple text adventure. Each room in the map is a function that can call the functions for adjacent rooms. All events and inventory are carried from room to room in a list called Status. Events in the list will be a series of 1's and 0's, 1 if the event has been triggered, 0 if not.

Plot: player wakes up from cold sleep and his ship is crippled, he needs to repair it and save the rest of his crew in cold sleep.

Solution: Player needs the suit to get in cargo hold, needs to get the tools in cargo hold to fix leak. needs to fix the engine (via a small puzzle) and get keycard to access flightdeck, and needs all of these event complete and have possession of the keycard to access the flight deck and reset flight computer. Finally return to the cryo pod.

Reactor puzzle: the main reactor needs to be restarted in order, first unlock the deuturium valves, then charge magnetic constrictors, then activate ionization lasers.

Items: key-card toolbox spacesuit

events: hull breach repaired engine fixed flight computer reset.
