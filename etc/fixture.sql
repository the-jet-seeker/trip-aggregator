CREATE SEQUENCE IF NOT EXISTS ticket_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE IF NOT EXISTS "public"."ticket" (
    "id" integer DEFAULT nextval('ticket_id_seq') NOT NULL,
    "dep_datetime" timestamp NOT NULL,
    "from_airport_code" character(3) NOT NULL,
    "to_airport_code" character(3) NOT NULL,
    "flight_duration" character varying(16) NOT NULL,
    "flight_number" character varying(16) NOT NULL,
    "airline" character varying(16) NOT NULL,
    "price" numeric(20,2) NOT NULL,
    "currency" character(3) NOT NULL,
    "source" character varying(255) NOT NULL,
    CONSTRAINT "ticket_pkey" PRIMARY KEY ("id")

) WITH (oids = false);

CREATE INDEX IF NOT EXISTS "ticket_source" ON "public"."ticket" USING btree ("source");

CREATE INDEX IF NOT EXISTS "ticket_dep_datetime" ON "public"."ticket" USING btree ("dep_datetime");

ALTER TABLE "public"."ticket" ADD COLUMN IF NOT EXISTS "uid" character varying(255) NOT NULL DEFAULT '';

UPDATE ticket SET uid=ticket.flight_number || '_' || ticket.from_airport_code || '_' || ticket.to_airport_code || '_' || ticket.dep_datetime  where uid = '';

CREATE UNIQUE INDEX  IF NOT EXISTS "ticket_uid" ON  "public"."ticket" ("uid");

ALTER TABLE "public"."ticket" ADD COLUMN IF NOT EXISTS "arr_datetime" timestamp NOT NULL DEFAULT '2020-01-01';

UPDATE ticket SET arr_datetime = dep_datetime WHERE arr_datetime = '2020-01-01';

ALTER TABLE "public"."ticket" ALTER COLUMN "arr_datetime" DROP DEFAULT;

CREATE INDEX IF NOT EXISTS "ticket_arr_datetime" ON "public"."ticket" USING btree ("arr_datetime");