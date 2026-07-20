SELECT * FROM proyecto_final.dataset_fao;
SELECT * FROM proyecto_final.dataset_fao where codigo_elemento = 72431;
SELECT * FROM proyecto_final.dataset_fao where producto='Caprinos' and area='Oceania';
select * from proyecto_final.dataset_fao where producto='Porcinos de cría';
SELECT area, sum(valor) as valor FROM proyecto_final.dataset_fao where (producto = 'Porcinos de carne' or producto = 'Porcinos de cría') and elemento = 'Existencias' group by area;
select distinct producto from proyecto_final.dataset_fao;
SELECT area, sum(valor) as valor FROM proyecto_final.dataset_fao where (producto = 'Gallinas, parrilleros' or producto = 'Gallinas ponedoras') and elemento = 'Existencias' group by area;
select anio, sum(valor) from proyecto_final.dataset_fao where (producto = 'Vacas lecheras' or producto = 'Vacunos, otros') and elemento = 'Existencias' group by anio;
select anio, sum(valor) from proyecto_final.dataset_fao where codigo_elemento = 72441 group by anio;
select anio, sum(valor) as valor from proyecto_final.dataset_fao where codigo_elemento = 72431 group by anio;
SELECT area, SUM(CASE WHEN codigo_elemento = 72441 THEN valor ELSE 0 END) AS CH4, SUM(CASE WHEN codigo_elemento = 72431 THEN valor ELSE 0 END) AS N2O FROM proyecto_final.dataset_fao WHERE codigo_elemento IN (72441, 72431) group by area;
SELECT anio, area, valor as valor FROM proyecto_final.dataset_fao WHERE codigo_elemento= 72431 group by anio;
select distinct elemento, codigo_elemento from proyecto_final.dataset_fao;
select  sum(valor) as valor,  producto from proyecto_final.dataset_fao where codigo_elemento in (72306, 72300, 72301) and anio = 2023 group by producto order by valor desc
select valor as valor, producto from proyecto_final.dataset_fao where codigo_elemento in (72306, 72300, 72301) and anio = 2023 
select valor, producto from proyecto_final.dataset_fao where codigo_elemento in (72306, 72300, 72301) and anio = 2023 