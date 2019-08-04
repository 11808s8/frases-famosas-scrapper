CREATE TABLE "categoria" (
  "id_categoria" serial PRIMARY KEY,
  "categoria" varchar
);

CREATE TABLE "autor" (
  "id_autor" SERIAL PRIMARY KEY,
  "autor" varchar
);

CREATE TABLE "profissao_autor" (
  "id_profissao_autor" SERIAL PRIMARY KEY,
  "profissao_autor" varchar
);

CREATE TABLE "profissoes_autores" (
  "id_autor" int,
  "id_profissao" int
);

CREATE TABLE "frase" (
  "id_frase" serial PRIMARY KEY,
  "frase" varchar,
  "id_autor" int,
  "id_categoria" int,
  "date_created" timestamp
);

ALTER TABLE "profissoes_autores" ADD FOREIGN KEY ("id_autor") REFERENCES "autor" ("id_autor");

ALTER TABLE "profissoes_autores" ADD FOREIGN KEY ("id_profissao") REFERENCES "profissao_autor" ("id_profissao_autor");

ALTER TABLE "frase" ADD FOREIGN KEY ("id_autor") REFERENCES "autor" ("id_autor");

ALTER TABLE "frase" ADD FOREIGN KEY ("id_categoria") REFERENCES "categoria" ("id_categoria");