#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#


# Rely on the unit tests as you write your code.
# If you implement the functions
# in the order they appear in the file,
# the test suite can give you incremental progress information.
# The goal of the Swiss pairings system is to pair each
# player with an opponent who has won the same number of
# matches, or as close as possible.

# You can assume that the number of
# players in a tournament is an even number.
# This means that no player will be left out of a round.

# Your code and database only needs to support a single
# tournament at a time. All players who are in the database
# will participate in the tournament, and when you want to
# run a new tournament, all the game records from the previous
# tournament will need to be deleted.
# In one of the extra-credit options for this project,
# you can extend this program to support multiple tournaments.


import psycopg2

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    c = conn.cursor()
    c.execute("DELETE FROM matchRecords;")
    conn.commit()
    conn.close()

def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    c = conn.cursor()
    c.execute("DELETE FROM playersRegistered;")
    conn.commit()
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM playersRegistered;")
    result = c.fetchone()
    conn.commit()
    conn.close()
    return result[0]

def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect()
    c = conn.cursor()
    c.execute("""
        INSERT INTO playersRegistered (name)
        VALUES (%s);""", (name,))
    conn.commit()
    conn.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM playerStandings ORDER BY wins DESC;")
    result = c.fetchall()
    conn.commit()
    conn.close()
    return result

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn = connect()
    c = conn.cursor()
    c.execute('''INSERT INTO matchRecords (winner, loser)
                 VALUES (%s,%s);''', [(winner,),(loser,)])
    conn.commit()
    conn.close()

def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """


