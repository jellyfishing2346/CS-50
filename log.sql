-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Check the description of when the crime occured based on its location
SELECT description
FROM crime_scene_reports
WHERE month = 7 AND day= 28
AND street = "Humphrey Street";

-- One suspect is guilty of stealing and littering
SELECT name, transcript
    FROM interviews
WHERE year = 2021 AND month = 7 AND day = 28;

-- Two transcripts contain a common name



