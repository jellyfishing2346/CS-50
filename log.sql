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

-- Evaluating the transcripts the first witness is Eugene
SELECT name
    FROM people
WHERE name = 'Eugene';

-- There are reportedly 3 witnesses besides Eugene
SELECT name
    FROM people
WHERE year = 2021 AND month = 7 AND day = 28
AND atm_location = 'Legett Street'
AND transaction_type = 'withdraw';

-- Create the suspect list
SELECT name, atm_transactions.amount
    FROM people
    JOIN bank_accounts
        ON people.id = bank_accounts.person_id
    JOIN atm_transactions
        ON bank_accounts.account_number = atm_transactions.account_number
    WHERE atm_transactions.year = 2021
        AND atm_transactions.month = 7
        AND atm_transactions.day = 28
        AND atm_transactions.atm_location = 'Legett Street'
        AND atm_transactions.transactions_type = 'withdraw';

-- The witness(Raymond) is giving clues. After the thief left the bakery they bought a ticket and is supposed to make plans to the Fiftyville airport
SELECT abbreviation, full_name, city
    FROM airports
WHERE city = 'Fiftyville'

-- There are flight dates for July 29
SELECT flights.id, full_name, city, flights.hour, flights.minute
    FROM airports
    JOIN flights
        ON airports.id = flights.destination_airport_id
    WHERE flights.origin_airport_id =
    (SELECT id
        FROM airports
        WHERE city = 'Fiftyville')
    AND flights.year = 2021
    AND flights.month = 7
    AND flights.day = 29
ORDER BY flights.hours, flights.minutes;

-- The thief is supposedly taking a flight to the Fiftyville airport.
SELECT passengers.flight_id, name, passengers.passort_number, passengers.seat
    FROM people
    JOIN passengers
        ON people.passport_number = passengers.passport_number
    JOIN flights
        ON passengers.flight_id = flights.id
    WHERE flights.year = 2021
    AND flights.day = 29
    AND flights.month = 7
    AND flights.minutes = 20
    ORDER BY passengers.passport_number;

-- Use the passengers' passport number to be in a suspect list
SELECT name, phone_calls.duration
    FROM people
    JOIN phone_calls
        ON people.phone_number = phone_calls.caller
    WHERE phone_calls.year = 2021
        AND phone_calls.month = 7
        AND phone_calls.day = 28
        AND phone_calls.day <= 60
        ORDER BY phone_calls.duration;

-- Identify the possible suspects' name and the duration of the calls
SELECT name, phone_calls.duration
    FROM people
    JOIN phone_calls
        ON people.phone_number = phone_calls.receiver
    WHERE phone_calls.year = 2021
        AND phone_calls.month = 7
        AND phone_calls.day = 28
        AND phone_calls.day <= 60
        ORDER BY phone_calls.duration;

-- The witness(Ruth) states that the thief drove away from a bakery thats 10 minutes from the theft
SELECT name, bakery_security_logs.hour, bakery_security_logs.minute
    FROM people
    JOIN bakery_security_logs
        ON people.license_plate = bakery_security_logs.license_plate
    WHERE bakery_security_logs.year = 2021
     AND bakery_security_logs.month = 7
     AND bakery_security_logs.day = 28
     AND bakery_security_logs.activity = 'exit'
     AND bakery_security_logs.hour = 10
     AND bakery_security_logs.minute >= 15
     AND bakery_security_logs.minute <= 25
    ORDER BY bakery_security_logs.minute;

-- Bruce is the thief as he is the only person of list passengers, specific atm transactions, people who you called, and the ones that drove away from the bakery
-- This person has taken the New York flight, so he is in New York City
-- Robin is the accomplice who purchased the ticket for New York, and helped Bruce get to New York







