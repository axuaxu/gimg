BEGIN TRANSACTION;
CREATE TABLE myList
             (num , trans text, symbol text, qty real, price real);
INSERT INTO "myList" VALUES(2006,'BUY','IBM','fdf','sdfs');
INSERT INTO "myList" VALUES(2007,'BUY','MSFT','asd','sadf');
INSERT INTO "myList" VALUES(2008,'SELL','IBM','sadf','asdf');
COMMIT;
