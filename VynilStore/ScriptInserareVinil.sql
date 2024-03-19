INSERT INTO vinil_generic (titlu_album, artist, gen_muzical, an_lansare)
VALUES('Saxophone Colossus', 'Sonny Rollins', 'Jazz', 1957);

INSERT INTO vinil_generic (titlu_album, artist, gen_muzical, an_lansare)
VALUES('Bohemian Rhapsody', 'Queen', 'Rock', 2006);

INSERT INTO vinil_generic (titlu_album, artist, gen_muzical, an_lansare)
VALUES('Pet Sounds', 'The Beach Boys', 'Pop', 1966);

INSERT INTO vinil_generic (titlu_album, artist, gen_muzical, an_lansare)
VALUES('The Masterpieces', ' Ludwig Van Beethoven', 'Clasic', 2007);

INSERT INTO vinil_generic (titlu_album, artist, gen_muzical, an_lansare)
VALUES('Midwest Farmer', 'Margo Price', 'Country', 2001);


INSERT INTO promotie (data_inc, data_sf, procent)
VALUES('11-DEC-2023', '24-DEC-2023', 10);

INSERT INTO promotie (data_inc, data_sf, procent)
VALUES('11-OCT-2023', '30-DEC-2023', 25);

INSERT INTO promotie (data_inc, data_sf, procent)
VALUES('1-OCT-2023', '20-DEC-2023', 30);

INSERT INTO promotie (data_inc, data_sf, procent)
VALUES('11-MAY-2023', '30-JUN-2023', 23);

INSERT INTO promotie (data_inc, data_sf, procent)
VALUES('9-JUL-2023', '18-AUG-2023', 12);


INSERT INTO furnizor (denumire, adresa)
VALUES ('MaxRecords', 'Salcamilor 43');


INSERT INTO furnizor (denumire, adresa)
VALUES ('Okapi Sound', 'Bulevardul Sperantei 2');


INSERT INTO furnizor (denumire, adresa)
VALUES ('Cat Music', 'Democratiei 11Abis');

INSERT INTO furnizor (denumire, adresa)
VALUES ('GoodSound', 'Bulevardul Tudor Gheorghe 21');


INSERT INTO furnizor (denumire, adresa)
VALUES ('BestMusic', 'Victoriei 7');

INSERT INTO vinil_fizic (stare, pret, stoc,id_vinilgeneric , id_furnizor, id_promotie)
VALUES('foarte buna', 120, 5, (SELECT id_vinilgeneric FROM vinil_generic where titlu_album='Saxophone Colossus'),
(SELECT id_furnizor FROM furnizor where denumire='MaxRecords'), 
(SELECT id_promotie FROM promotie where procent=10));
  
INSERT INTO vinil_fizic (stare, pret, stoc,id_vinilgeneric , id_furnizor, id_promotie)
VALUES('noua', 143, 3, (SELECT id_vinilgeneric FROM vinil_generic where titlu_album='Saxophone Colossus'),
(SELECT id_furnizor FROM furnizor where denumire='Cat Music'), 
(SELECT id_promotie FROM promotie where procent=10));

INSERT INTO vinil_fizic (stare, pret, stoc,id_vinilgeneric , id_furnizor, id_promotie)
VALUES('buna', 99, 2, (SELECT id_vinilgeneric FROM vinil_generic where titlu_album='Saxophone Colossus'),
(SELECT id_furnizor FROM furnizor where denumire='Cat Music'), 
(SELECT id_promotie FROM promotie where procent=10));
                                  

INSERT INTO vinil_fizic ( stare, pret, stoc,id_vinilgeneric , id_furnizor, id_promotie)
VALUES('foarte buna', 80, 9, (SELECT id_vinilgeneric FROM vinil_generic where titlu_album='Bohemian Rhapsody'),
(SELECT id_furnizor FROM furnizor where denumire='Okapi Sound'), 
(SELECT id_promotie FROM promotie where procent=25));


INSERT INTO vinil_fizic ( stare, pret, stoc,id_vinilgeneric , id_furnizor, id_promotie)
VALUES('buna', 60, 20,(SELECT id_vinilgeneric FROM vinil_generic where titlu_album='Bohemian Rhapsody'),
(SELECT id_furnizor FROM furnizor where denumire='Cat Music'), 
(SELECT id_promotie FROM promotie where procent=10));




INSERT INTO vinil_fizic ( stare, pret, stoc,id_vinilgeneric , id_furnizor, id_promotie)
VALUES('foarte buna', 120, 14, (SELECT id_vinilgeneric FROM vinil_generic where titlu_album='Pet Sounds'),
(SELECT id_furnizor FROM furnizor where denumire='Cat Music'), 
(SELECT id_promotie FROM promotie where procent=25));

INSERT INTO vinil_fizic ( stare, pret, stoc,id_vinilgeneric , id_furnizor, id_promotie)
VALUES('buna', 85, 4, (SELECT id_vinilgeneric FROM vinil_generic where titlu_album='Pet Sounds'),
(SELECT id_furnizor FROM furnizor where denumire='MaxRecords'), 
(SELECT id_promotie FROM promotie where procent=25));





INSERT INTO vinil_fizic ( stare, pret, stoc,id_vinilgeneric , id_furnizor, id_promotie)
VALUES('noua', 320, 10, (SELECT id_vinilgeneric FROM vinil_generic where titlu_album='The Masterpieces'),
(SELECT id_furnizor FROM furnizor where denumire='Okapi Sound'), 
(SELECT id_promotie FROM promotie where procent=10));


INSERT INTO vinil_fizic ( stare, pret, stoc,id_vinilgeneric , id_furnizor, id_promotie)
VALUES('buna', 190, 3, (SELECT id_vinilgeneric FROM vinil_generic where titlu_album='The Masterpieces'),
(SELECT id_furnizor FROM furnizor where denumire='Okapi Sound'), 
(SELECT id_promotie FROM promotie where procent=10));


select * from vinil_fizic;


INSERT INTO pozitonare (biblioteca, raft, id_vinil)
VALUES (1, 1, 1);

INSERT INTO pozitonare (biblioteca, raft, id_vinil)
VALUES (1, 2, 2);

INSERT INTO pozitonare (biblioteca, raft, id_vinil)
VALUES (1, 3, 3);
 
INSERT INTO pozitonare (biblioteca, raft, id_vinil)
VALUES (2, 1, 4);

INSERT INTO pozitonare (biblioteca, raft, id_vinil)
VALUES (2, 2, 5);

INSERT INTO pozitonare (biblioteca, raft, id_vinil)
VALUES (3, 3, 6);

INSERT INTO pozitonare (biblioteca, raft, id_vinil)
VALUES (3, 4, 7);

INSERT INTO pozitonare (biblioteca, raft, id_vinil)
VALUES (4, 2, 8);

INSERT INTO pozitonare (biblioteca, raft, id_vinil)
VALUES (4, 3, 9);



INSERT INTO incasari (metoda_de_plata, data_vanzare, suma, id_vinil)
VALUES ('card', '15-DEC-2023',(select f.pret-(f.pret*p.procent/100) from vinil_fizic f, promotie p where p.id_promotie=f.id_promotie and f.id_vinil=1),1);


INSERT INTO incasari (metoda_de_plata, data_vanzare, suma, id_vinil)
VALUES ('card', '17-DEC-2023',(select f.pret-(f.pret*p.procent/100) from vinil_fizic f, promotie p where p.id_promotie=f.id_promotie and f.id_vinil=6),6);

INSERT INTO incasari (metoda_de_plata, data_vanzare, suma, id_vinil)
VALUES ('cash', '21-DEC-2023',(select f.pret-(f.pret*p.procent/100) from vinil_fizic f, promotie p where p.id_promotie=f.id_promotie and f.id_vinil=4),4);

INSERT INTO incasari (metoda_de_plata, data_vanzare, suma, id_vinil)
VALUES ('cash', '21-DEC-2023',(select f.pret-(f.pret*p.procent/100) from vinil_fizic f, promotie p where p.id_promotie=f.id_promotie and f.id_vinil=8),8);


INSERT INTO incasari (metoda_de_plata, data_vanzare, suma, id_vinil)
VALUES ('card', '21-DEC-2023',(select f.pret-(f.pret*p.procent/100) from vinil_fizic f, promotie p where p.id_promotie=f.id_promotie and f.id_vinil=6),6);



select * from incasari;
//date insert eronate
INSERT INTO promotie (id_promotie, data_inc, data_sf, procent)
VALUES(1, '24-DEC-2023', '25-DEC-2023', 40);

INSERT INTO promotie (id_promotie, data_inc, data_sf, procent)
VALUES(1, '24-DEC-2023', '30-DEC-2023', 110);

INSERT INTO pozitonare (biblioteca, raft, id_vinil)
VALUES (4, 9, 8);

INSERT INTO pozitonare (biblioteca, raft, id_vinil)
VALUES (4, 16, 8);

INSERT INTO vinil_fizic 
VALUES(null, 'buna', 99, 2, (SELECT id_vinilgeneric FROM vinilgeneric where titlu_album='Saxophone Colossus'),
(SELECT id_furnizor FROM furnizor where denumire='Cat Music'), 
(SELECT id_promotie FROM promotie where procent=10));
