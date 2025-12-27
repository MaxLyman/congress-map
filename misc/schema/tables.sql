-- SQLite schema for Congress Map
-- Load with: sqlite3 congress_map.db < misc/schema/tables.sql

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    bioguide_id TEXT UNIQUE,
    fec_candidate_id TEXT,
    created_at TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS member_fec_ids (
    member_id INTEGER NOT NULL REFERENCES members(id) ON DELETE CASCADE,
    fec_candidate_id TEXT NOT NULL,
    election_year INTEGER,
    PRIMARY KEY (member_id, fec_candidate_id)
);


CREATE TABLE IF NOT EXISTS terms (
    member_id NOT NULL REFERENCES members(id) ON DELETE CASCADE,
    start_year INTEGER,
    end_year INTEGER,
    fec_candidate_id TEXT NOT NULL
)