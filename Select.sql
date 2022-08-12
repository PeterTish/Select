SELECT al.name, al.release
FROM public.album al
WHERE al.release = 2016;

SELECT tr.name, max(tr.duration) as "Максимальная продолжительность" 
FROM public.track tr
GROUP BY tr.name
ORDER BY max(tr.duration) desc
LIMIT 1;

SELECT tr.name, tr.duration 
FROM public.track tr
WHERE tr.duration >= 3.5;

SELECT col.name
FROM public.collection col
WHERE release between 2016 and 2017;

--!!--
SELECT mus.nickname 
FROM public.musician mus
WHERE mus.nickname not like '% %';

SELECT tr.name
FROM public.track tr
WHERE tr.name like '%mo%' or tr.name like '%io%';


