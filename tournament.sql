-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

--this file is used to set up your database schema
--(the table representation of your data structure).


-- Drop database if exists everytime our program runs
DROP DATABASE IF EXISTS tournament;

-- Create the database for the new tournament
CREATE DATABASE tournament;

-- Connect to the database
\c tournament;

-- Drops our player table if exists
DROP TABLE IF EXISTS playersRegistered;

-- Create our player table
CREATE TABLE playersRegistered(
    playerid serial primary key,
    name text
);

-- Drop our match records table if exists
DROP TABLE IF EXISTS matchRecords;

-- Create our match report table
CREATE TABLE matchRecords(
    matchid serial primary key,
    winner int, foreign key(winner) references playersRegistered(playerid),
    loser int, foreign key(loser) references playersRegistered(playerid)
);

-- Drop view if exists
DROP VIEW IF EXISTS playerStandings;

CREATE VIEW playerStandings AS
SELECT playersRegistered.playerid, playersRegistered.name,
            (SELECT COUNT(matchRecords.winner)
             FROM matchRecords
             WHERE playersRegistered.playerid = matchRecords.winner)
             AS wins,

             (SELECT COUNT(matchRecords.winner)
             FROM matchRecords
             WHERE playersRegistered.playerid = matchRecords.winner
             OR playersRegistered.playerid = matchRecords.loser)
             AS matches

FROM playersRegistered
ORDER BY wins,matches;

-- Drop view if exists
DROP VIEW IF EXISTS playerDetails;

CREATE VIEW playerDetails AS
SELECT playersRegistered.playerid, playersRegistered.name
FROM playersRegistered;