SELECT * FROM ninjas;
select * from ninjas join dojos on ninja.idninja = 6;
select * from ninjas join dojos on dojos.iddojo = ninjas.dojo_iddojos where dojos.iddojo = 4;
select * from ninjas join dojos on dojos.iddojo = ninjas.dojo_iddojos where dojos.iddojo = 6;
select * from ninjas join dojos on ninjas.idninja = dojos.ninjas_idninja where ninjas.idninja = 6;
select * from ninjas join ninjas on dojos.iddojo = ninjas.dojo_iddojos where idninja = 6;
select * from ninjas join dojos on dojos.id= ninjas.dojo_id ;
SELECT * FROM ninjas JOIN dojos ON ninjas.dojo_iddojos= dojos.iddojo WHERE ninjas.idninja= 6;
SELECT *FROM ninjas JOIN dojos ON ninjas.dojo_iddojos = dojos.iddojo;

