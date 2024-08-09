-- This gives the description of the crime scene. Crime happened on 7-28-2023 10:15 AM.
SELECT descriptiON FROM crime_scene_reports WHERE id = 295;

-- This gives the eyewitness acounts of the crime.
SELECT name, transcript FROM interviews WHERE transcript LIKE '%bakery%';

-- Checking licence plates and names
SELECT bl.year, bl.month, bl.day, bl.hour, bl.minute, bl.activity, bl.license_plate, p.name
FROM bakery_security_logs bl
JOIN people p on bl.license_plate = p.license_plate
WHERE bl.year = 2023 AND bl.month = 7 AND bl.day = 28 AND bl.hour = 10 AND bl.minute BETWEEN 15 AND 25;

-- Getting the bank_account info from each of those people
SELECT bl.activity, bl.license_plate, p.name, b_account.account_number
FROM bakery_security_logs AS bl
JOIN people AS p ON bl.license_plate = p.license_plate
JOIN bank_accounts AS b_account ON b_account.person_id = p.id
WHERE bl.year = 2023 AND bl.month = 7 AND bl.day = 28 AND bl.hour = 10 AND bl.minute BETWEEN 15 AND 25;


-- Checking the atm transactions
SELECT p.name, ba_account.account_number, att.transaction_type
FROM bakery_security_logs AS bl
JOIN people AS p ON bl.license_plate = p.license_plate
JOIN bank_accounts AS ba_account ON ba_account.person_id = p.id
JOIN atm_transactions AS att ON ba_account.account_number = att.account_number
WHERE bl.year = 2023 AND bl.month = 7 AND bl.day = 28 AND bl.hour = 10 AND bl.minute BETWEEN 15 AND 25 AND att.month = 7 AND att.day = 28 AND att.transaction_type = 'withdraw';


-- Now we must check their phone calls and their length.
SELECT p.name, pc.duration, pc.receiver
FROM bakery_security_logs AS bl
JOIN people AS p ON bl.license_plate = p.license_plate
JOIN bank_accounts AS ba_account ON ba_account.person_id = p.id
JOIN atm_transactions AS att ON ba_account.account_number = att.account_number
JOIN phone_calls AS pc ON pc.caller = p.phone_number
WHERE bl.year = 2023 AND bl.month = 7 AND bl.day = 28 AND bl.hour = 10 AND bl.minute BETWEEN 15 AND 25
AND att.month = 7 AND att.day = 28 AND pc.duration <= 60 AND pc.day = 28;

-- Now we have narrowed the suspects to Bruce and Diana.

SELECT p.name, flight_id, flights.day, flights.hour, flights.minute, flights.month
   ...> FROM bakery_security_logs AS bl
   ...> JOIN people AS p ON bl.license_plate = p.license_plate
   ...> JOIN bank_accounts AS ba_account ON ba_account.person_id = p.id
   ...> JOIN atm_transactions AS att ON ba_account.account_number = att.account_number
   ...> JOIN phone_calls AS pc ON pc.caller = p.phone_number
   ...> JOIN passengers AS pass ON pass.passport_number = p.passport_number
   ...> JOIN flights on flights.id = pass.flight_id
   ...> WHERE bl.year = 2023 AND bl.month = 7 AND bl.day = 28 AND bl.hour = 10 AND bl.minute BETWEEN 15 AND 25
   ...> AND att.month = 7 AND att.day = 28 AND pc.duration <= 60 AND pc.day = 28 AND flights.day = 29;


-- Let's see what flights they went on.
SELECT people.name, passengers.flight_id
FROM people
JOIN passengers ON passengers.passport_number = people.passport_number
WHERE people.name = 'Bruce' OR people.name= 'Diana';

-- We now know there flight ids. Let's filter to the 29th and see what airport they left from
SELECT people.name, passengers.flight_id, airports.full_name AS origin
FROM people
JOIN passengers ON passengers.passport_number = people.passport_number
JOIN flights ON flights.id = passengers.flight_id
JOIN airports on airports.id = flights.origin_airport_id
WHERE people.name = 'Bruce' OR people.name= 'Diana' AND flights.day = 29 AND flights.year = 2023 AND flights.month = 7;

-- Now lets see who left in the earliest flight.
SELECT people.name, passengers.flight_id, airports.full_name AS origin, flights.hour, flights.minute
FROM people
JOIN passengers ON passengers.passport_number = people.passport_number
JOIN flights ON flights.id = passengers.flight_id
JOIN airports on airports.id = flights.origin_airport_id
WHERE people.name = 'Bruce' OR people.name= 'Diana' AND flights.day = 29 AND flights.year = 2023 AND flights.month = 7;

-- and then compare to the flight times

SELECT * FROM flights WHERE origin_airport_id = 8 AND flight.day = 29 AND flights.month = 7;

-- Bruce took the earliest flight. Bruce is the thief since he matched all descriptions. Now we must find his accomplice

SELECT phone_number FROM people WHERE name = 'Bruce';

SELECT receiver FROM phone_calls WHERE day = 28 AND month= 7 AND year = 2023 AND duration < 60 AND caller = '(367) 555-5533';


SELECT name FROM people WHERE phone_number = '(375) 555-8161';

-- Robin is the accomplice
